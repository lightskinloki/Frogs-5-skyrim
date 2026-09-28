"""Live FROGS combat advisor.

Subscribes to the existing table-ear/Antigravity transcript bridge on port 3111.
Jev performs fast typed triage; Antigravity/Gemini only generates a tactical
recommendation for transcript entries that look relevant to the current fight.

Run with:  py live_advisor.py
The session runsheet polls this service on port 3112.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TRANSCRIPT_URL = "http://127.0.0.1:3111/api/transcript"
HOST = "127.0.0.1"
PORT = 3112
AGY = Path(r"C:\Users\fbrown\AppData\Local\agy\bin\agy.exe")
JEV = Path(r"C:\Users\fbrown\Projects\ai-panels\jev.py")

LOCK = threading.Lock()
STATE = {
    "round": "1",
    "zone": "Zone 3",
    "anchors": {letter: 300 for letter in "ABCDE"},
    "jasper_hp": "2000 / 2000",
    "log": "",
    "updated": None,
}
ADVISOR = {
    "status": "waiting",
    "last_transcript": None,
    "last_triage": None,
    "latest": None,
    "history": [],
    "error": None,
}
SEEN = set()
TRANSCRIPT_HISTORY = []
PROCESSING = False
INITIALIZED = False


def json_response(handler: BaseHTTPRequestHandler, payload: dict, status: int = 200):
    raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.end_headers()
    handler.wfile.write(raw)


def read_jev():
    spec = importlib.util.spec_from_file_location("frogs_jev", JEV)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load Jev module: {JEV}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def current_state() -> dict:
    with LOCK:
        return json.loads(json.dumps(STATE))


def recent_context() -> str:
    with LOCK:
        transcript = "\n".join(
            f"[{x.get('timestamp', '')}] {x.get('speaker', 'Table')}: {x.get('text', '')}"
            for x in TRANSCRIPT_HISTORY[-8:]
        )
        state = json.dumps(STATE, ensure_ascii=False)
    return f"""FROGS 5 live combat context.
Objective once combat starts: Jasper is trying to kill the Lanterns while preventing
three anchors from being destroyed. Identify the best kill pressure without losing
track of the ritual.
Gaelen does not attack and does not defend himself. Jasper is player-controlled and is trying to kill the Lanterns.
Several Mythic Dawn allies actively support Jasper: they attack, block routes, protect stations, and create openings. Jasper must remain capable of fighting the party alone; the allies are additional pressure, not his substitute.
Five anchors each have 300 HP and DR 10. Three anchors down disrupts the working.
Orion's tonal counter-note is Hard Magic (-4), 100 damage to one anchor, ignoring DR.
Jasper's current boss sheet: 2000 HP, 24 starting FP, DR 50 from Dagon-corrupted Ebonyflesh. Hollow Heart drains 2 FP from each enemy who starts within 15 feet and adds it to Jasper's pool without a cap. His two separate Atronach negations trigger The Unmaking: the caster loses that spell for the encounter, Jasper gets one free cast, the caster takes fire damage equal to the spell's FP cost, and becomes Staggered.
Jasper is controlled by a player tonight. Never decide Jasper's dialogue or action for
that player. Surface a tactical option, the threatened anchor, and the reason; the
Jasper player and GM choose what he actually does.
The current live runsheet state is: {state}

Recent table transcript:
{transcript}
"""


def jev_triage(text: str) -> dict:
    jev = read_jev()
    state = recent_context() + f"\nNewest transcript entry:\n{text}"
    questions = {
        "combat_relevant": {
            "type": "noul",
            "instructions": "Return true only if this entry describes a player or NPC action, target, roll, damage, movement, spell, or explicit combat decision in the current Jasper encounter. Return false for table chatter, jokes, food, or unrelated conversation.",
            "criteria": {"true": "This is current combat information", "false": "This is not current combat information"},
        },
        "action": {
            "type": "choice",
            "instructions": "Choose the best description of the move or intent present in the newest entry. Use unknown when no move is stated.",
            "criteria": {
                "attack_anchor": "attacks, damages, moves against, or targets an anchor",
                "attack_jasper": "attacks or targets Jasper",
                "attack_assistant": "attacks or targets a Dawn assistant",
                "protect_or_heal": "heals, protects, rescues, or repositions an ally",
                "control_or_disable": "uses control, debuff, terrain, or a defensive action",
                "move_or_reposition": "moves without a clearly stated attack",
                "dialogue_or_refusal": "talks, refuses, agrees, or makes a tactical declaration",
                "unknown": "no actionable combat move is stated",
            },
        },
        "target": {
            "type": "choice",
            "instructions": "Choose the best target named or clearly implied by the newest entry. Use unknown when none is available.",
            "criteria": {**{f"anchor_{x.lower()}": f"anchor {x}" for x in "ABCDE"}, "jasper": "Jasper", "assistant": "a Dawn assistant", "gaelen": "Gaelen", "ally": "an ally or party member", "unknown": "no clear target"},
        },
    }
    return jev.ask(state, questions)


def unwrap_jev(result: dict) -> dict:
    # Jev's response shape is intentionally preserved in the state; this helper
    # extracts only values where the API returns the common answer/value form.
    out = {}
    for key, value in result.items():
        if isinstance(value, dict):
            out[key] = value.get("answer", value.get("value", value))
        else:
            out[key] = value
    return out


def call_agy(triage: dict) -> dict:
    prompt = f"""You are the live tactical assistant for a FROGS 5 GM and a player-controlled Jasper.
Read the current state and newest transcript below. Give one immediately usable recommendation.
Do not invent a roll, damage value, spell, stat, location, or target that is not supported by the context.
Do not make decisions for the players. Recommend what the GM should surface or track,
and phrase Jasper's recommendation as an option for Jasper's player, never as an order.
Remember: Gaelen does not attack; Jasper is player-controlled and is pursuing a TPK;
multiple Mythic Dawn allies actively support him; three anchors down disrupts the working.

Return JSON only with exactly these keys:
recommendation, target, reason, next_track, confidence
Keep recommendation to one or two sentences. If the transcript is ambiguous, say so and recommend asking the table to clarify.

CURRENT CONTEXT:
{recent_context()}

JEV TRIAGE:
{json.dumps(triage, ensure_ascii=False)}
"""
    args = [
        str(AGY), "-p", prompt, "--model", "gemini-3.7-flash-low",
        "--output-format", "json", "--print-timeout", "90s",
        "--disable-slash-commands", "--dangerously-skip-permissions",
    ]
    proc = subprocess.run(args, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "agy failed").strip()[:1000])

    response = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "response" in event:
            response = event["response"]
    if response is None:
        raise RuntimeError("AGY returned no response")
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"recommendation": response, "target": "unknown", "reason": "AGY returned non-JSON text", "next_track": "Review manually", "confidence": "unknown"}


def process_entry(entry: dict):
    global PROCESSING
    try:
        text = entry.get("text", "").strip()
        if not text:
            return
        with LOCK:
            ADVISOR["status"] = "triaging"
            ADVISOR["last_transcript"] = entry
        raw = jev_triage(text)
        triage = unwrap_jev(raw)
        with LOCK:
            ADVISOR["last_triage"] = triage
        relevant = triage.get("combat_relevant")
        if isinstance(relevant, str):
            relevant = relevant.lower() in {"true", "yes", "1"}
        if not relevant:
            with LOCK:
                ADVISOR["status"] = "waiting"
            return
        with LOCK:
            ADVISOR["status"] = "asking_gemini"
        suggestion = call_agy(triage)
        suggestion["source_transcript"] = entry
        suggestion["triage"] = triage
        suggestion["player_controlled"] = {"jasper": True, "gaelen": False}
        with LOCK:
            ADVISOR["latest"] = suggestion
            ADVISOR["history"].append(suggestion)
            ADVISOR["history"] = ADVISOR["history"][-20:]
            ADVISOR["status"] = "ready"
            ADVISOR["error"] = None
    except Exception as exc:
        with LOCK:
            ADVISOR["status"] = "error"
            ADVISOR["error"] = str(exc)
    finally:
        PROCESSING = False


def poll_transcripts():
    global PROCESSING, INITIALIZED
    try:
        req = urllib.request.Request(TRANSCRIPT_URL)
        with urllib.request.urlopen(req, timeout=2) as response:
            payload = json.loads(response.read().decode("utf-8"))
        entries = payload.get("transcripts", [])
        if not INITIALIZED:
            for entry in entries:
                SEEN.add(f"{entry.get('timestamp', '')}|{entry.get('speaker', '')}|{entry.get('text', '')}")
            INITIALIZED = True
            return
        for entry in entries:
            key = f"{entry.get('timestamp', '')}|{entry.get('speaker', '')}|{entry.get('text', '')}"
            if key in SEEN:
                continue
            SEEN.add(key)
            with LOCK:
                TRANSCRIPT_HISTORY.append(entry)
                del TRANSCRIPT_HISTORY[:-30]
            if PROCESSING:
                continue
            PROCESSING = True
            threading.Thread(target=process_entry, args=(entry,), daemon=True).start()
            break
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        pass


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

    def do_OPTIONS(self):
        json_response(self, {}, 204)

    def do_GET(self):
        if self.path == "/health":
            json_response(self, {"status": "ok", "service": "frogs-live-advisor", "transcript_source": TRANSCRIPT_URL, "port": PORT})
        elif self.path == "/api/advisor":
            with LOCK:
                payload = {"state": current_state(), "advisor": json.loads(json.dumps(ADVISOR))}
            json_response(self, payload)
        else:
            json_response(self, {"error": "Not found"}, 404)

    def do_POST(self):
        if self.path != "/api/advisor/state":
            json_response(self, {"error": "Not found"}, 404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            incoming = json.loads(self.rfile.read(length).decode("utf-8"))
            with LOCK:
                for key in ("round", "zone", "jasper_hp", "log"):
                    if key in incoming:
                        STATE[key] = str(incoming[key])
                if isinstance(incoming.get("anchors"), dict):
                    STATE["anchors"].update({k: int(v) for k, v in incoming["anchors"].items() if k in "ABCDE"})
                STATE["updated"] = time.time()
            json_response(self, {"ok": True})
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            json_response(self, {"error": str(exc)}, 400)


def main():
    def loop():
        while True:
            poll_transcripts()
            time.sleep(1.5)

    threading.Thread(target=loop, daemon=True).start()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"FROGS live advisor listening on http://{HOST}:{PORT}")
    print(f"Polling existing transcript bridge: {TRANSCRIPT_URL}")
    server.serve_forever()


if __name__ == "__main__":
    main()
