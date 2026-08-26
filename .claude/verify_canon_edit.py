#!/usr/bin/env python3
"""
PostToolUse hook: after Claude edits a canon file, four independent models --
not Claude, not each other -- each run one narrow, distinct check against the
actual edit, sequentially. Fails CLOSED: any model error, timeout, or FAIL
verdict blocks the turn.

Why different models instead of Claude subagents: a fresh Claude instance
still shares whatever structurally produces the original error. A genuinely
different model family doesn't share that correlated blind spot.

Why DIFFERENT prompts instead of the same "check everything" prompt four
times: the four passes are built from real, distinct clusters already
established in CLAUDE.md and AI_REASONING_PATTERNS.md, not invented for this
script -- see the citations inside each prompt below. Each pass is narrow on
purpose; an open-ended "audit everything" prompt was observed to run for
5+ minutes chasing its own tangents on one model.

Runtime is real: 5-15 minutes per model is normal and expected, not a bug to
optimize away. 20-40 minutes total for the four-pass sequence is the accepted
cost, deliberately traded against the alternative (a whole chapter rewritten
by hand after the fact).

Two engines are used: OpenCode (opencode-cli.exe) for the first three passes,
and the Antigravity CLI (agy.exe, Gemini models) for the fourth (lore
consistency against actual Elder Scrolls source material in Lore Books/).
agy required its "Tool Execution Policy" set to always-allow in the
Antigravity GUI's own Settings first -- headless mode cannot answer an
interactive permission prompt, and there was no config file to edit directly;
it had to be set once through the app itself before this worked at all.
"""
import json
import subprocess
import sys

OPENCODE = r"C:\Users\fbrown\AppData\Local\OpenCode\opencode-cli.exe"
AGY = r"C:\Users\fbrown\AppData\Local\agy\bin\agy.exe"
CANON_PREFIXES = ("Toryggs legacy", "web")
TIMEOUT_SECS = 1800  # 30 min ceiling per model; observed real runs can take 5-15 min

PASSES = [
    {
        "engine": "opencode",
        "model": "opencode/nemotron-3-ultra-free",
        "name": "Fabrication & Citation",
        "prompt": """A file in a tabletop campaign's canon repository was just edited: {path}

This is the FABRICATION & CITATION pass (CLAUDE.md Rule 1, G1, G10, G11; AI_REASONING_PATTERNS \
#6, #9, #14, #25, #29, #31). Read the CURRENT full content of that file yourself.

For every factual claim, mechanism, number, consequence, and attribution of an action or line \
to a named character: find and cite the actual source that supports it -- another file in this \
repo (Npcs/, Players/, The Narrative/ chapters, module/rules docs, or a scratch/design doc for \
an intentional choice). You have file tools; use them for real, don't guess from the filename.

Flag as a problem: (a) any claim with no traceable source anywhere in the repo, (b) any claim \
that contradicts an established source, (c) confident-sounding reasoning that was never \
actually traced back to a source document (a plausible argument is not a citation).

Do NOT flag: something that is simply new, GM-original content with no prior source, as long as \
it doesn't contradict anything -- new creative work is fine when nothing on record already \
decided it differently. Only flag actual contradiction or actual fabrication of something \
presented as already-established fact.

Respond with 'VERDICT: PASS' as the first line if you find nothing wrong. Respond with \
'VERDICT: FAIL' as the first line otherwise, followed by a numbered list of the specific \
problems, each with the exact claim, why it's a problem, and what you checked (or couldn't \
find) to confirm that.""",
    },
    {
        "engine": "opencode",
        "model": "opencode/muse-spark-1.2-contributor-free",
        "name": "Table & Format Usability",
        "prompt": """A file in a tabletop campaign's canon repository was just edited: {path}

This is the TABLE/FORMAT USABILITY pass (CLAUDE.md G12; AI_REASONING_PATTERNS #13, #15, #24). \
Read the CURRENT full content of that file yourself.

This pass only applies to GM-facing REFERENCE/MODULE content meant to be used live at a table \
under time pressure (adventure modules, stat blocks, GM notes, read-aloud text) -- NOT to \
narrative prose chapters meant to be read start to end. If this file is a narrative chapter \
(under The Narrative/) rather than reference/module content, respond 'VERDICT: PASS -- not \
in scope for this pass' and stop there.

Otherwise: compare this file's actual shape against `Toryggs legacy/SESSION FORMAT SAMPLE.rtf` \
in this repo -- read that file too. Check specifically: is GM-rationale prose (design reasoning, \
explanation of WHY something works) bleeding into what's supposed to be scannable content a GM \
reads or glances at mid-session? Are stat blocks and read-aloud text visually separated from \
dense paragraphs, the way the sample does it? If a scene, mechanic, or gated clue is referenced \
or invoked, is its actual content present at the point of use, or just pointed at elsewhere \
("see above")? Would a GM running this live, cold, under pressure, actually be able to find the \
thing they need in the time they have?

Respond with 'VERDICT: PASS' as the first line if the format holds up against the sample. \
Respond with 'VERDICT: FAIL' as the first line otherwise, with a numbered list of specific \
spots where density, structure, or missing inline content would slow a GM down at the table.""",
    },
    {
        "engine": "opencode",
        "model": "opencode/big-pickle",
        "name": "Dialogue & Scene Craft",
        "prompt": """A file in a tabletop campaign's canon repository was just edited: {path}

This is the DIALOGUE & SCENE CRAFT pass (CLAUDE.md Rules 7-8, G6, G8; AI_REASONING_PATTERNS \
#11, #12, #16, #17, #18, #21, #22, #23, #26). Read the CURRENT full content of that file \
yourself, and read the character's own doc in Npcs/ or Players/ for anyone who speaks or acts \
in it.

Check specifically, for every named character's dialogue and action in this file:
1. CAMERA TEST -- does any line narrate a private motive/feeling instead of showing only what a \
camera could film ("he doesn't want an audience" instead of just the action)?
2. DIALOGUE PURPOSE -- does every line serve the SPEAKER'S own want, or does it exist only to \
inform the reader of something the listener already knows?
3. SELF-JUSTIFYING DIALOGUE -- does any line explain, in the same breath, why it's being said \
("I'll tell you X, because Y")?
4. COMPOSURE UNDER SHOCK -- if a character witnesses something genuinely horrifying or extreme, \
is their reaction a polished, quotable line? That's wrong by default -- check what THIS \
character's own doc says they actually do when they care about someone, and whether the draft \
matches that default firing and missing, not a generic composed response.
5. NEGATION/PADDING -- does prose define things by what they are NOT rather than what they ARE? \
Are there hedge words ("simply," "genuinely," "just") that could be cut with no loss?
6. WHOLE-SCENE CONSISTENCY -- does anything contradict an earlier beat in the same file?

Respond with 'VERDICT: PASS' as the first line if none of these fire. Respond with \
'VERDICT: FAIL' as the first line otherwise, with a numbered list of specific lines/passages, \
which rule each violates, and why.""",
    },
    {
        "engine": "agy",
        "model": "gemini-3.7-flash-high",
        "name": "Lore Consistency",
        "prompt": """A file in a tabletop campaign's canon repository was just edited: {path}

This is the LORE CONSISTENCY pass. This campaign is built on real Elder Scrolls (Skyrim) lore, \
with an established compendium of that source material in the `Lore Books/` folder of this \
repo. Read the CURRENT full content of the edited file yourself.

For every claim in that file about REAL Elder Scrolls lore -- a god's domain or nature, a race's \
traits, a historical event, a place's real geography or history, an established magic system \
rule -- check it against the actual content of the relevant file(s) in `Lore Books/`. You have \
file tools; use them for real.

Flag as a problem: (a) any claim about established Elder Scrolls lore that contradicts what \
`Lore Books/` actually says, (b) any claim asserted as real-world-established lore that isn't in \
`Lore Books/` at all and isn't marked as this campaign's own original addition.

Do NOT flag: this campaign's own original inventions layered on top of real lore (new NPCs, new \
plot events, this specific campaign's twists) -- those aren't lore claims, they're the campaign's \
own content. Only flag where something is presented as established Elder Scrolls fact and either \
contradicts or has no support in `Lore Books/`.

Respond with 'VERDICT: PASS' as the first line if nothing contradicts or is unsupported. Respond \
with 'VERDICT: FAIL' as the first line otherwise, with a numbered list of the specific claims, \
what `Lore Books/` actually says (or that nothing there supports it), and why it's a problem.""",
    },
]


def run_pass_opencode(spec: dict, path: str) -> tuple[str, bool, str]:
    prompt = spec["prompt"].format(path=path)
    try:
        proc = subprocess.run(
            [OPENCODE, "run", "-m", spec["model"], prompt, "--format", "json"],
            capture_output=True, encoding="utf-8", errors="replace", timeout=TIMEOUT_SECS,
        )
    except subprocess.TimeoutExpired:
        return spec["name"], False, "TIMEOUT after %ds — treated as FAIL (fail-closed)." % TIMEOUT_SECS
    except Exception as e:
        return spec["name"], False, "ERROR invoking model: %s — treated as FAIL (fail-closed)." % e

    if proc.returncode != 0:
        return spec["name"], False, "Non-zero exit (%d): %s — treated as FAIL (fail-closed)." % (
            proc.returncode, (proc.stderr or "")[:500])

    final_text = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except json.JSONDecodeError:
            continue
        if evt.get("type") == "text":
            t = evt.get("part", {}).get("text")
            if t:
                final_text = t

    if final_text is None:
        return spec["name"], False, "No text response parsed from model output — treated as FAIL (fail-closed)."

    passed = final_text.strip().upper().startswith("VERDICT: PASS")
    return spec["name"], passed, final_text.strip()


def run_pass_agy(spec: dict, path: str) -> tuple[str, bool, str]:
    prompt = spec["prompt"].format(path=path)
    try:
        proc = subprocess.run(
            [AGY, "-p", prompt, "--model", spec["model"], "--output-format", "json",
             "--print-timeout", "25m", "--dangerously-skip-permissions"],
            capture_output=True, encoding="utf-8", errors="replace", timeout=TIMEOUT_SECS,
        )
    except subprocess.TimeoutExpired:
        return spec["name"], False, "TIMEOUT after %ds — treated as FAIL (fail-closed)." % TIMEOUT_SECS
    except Exception as e:
        return spec["name"], False, "ERROR invoking model: %s — treated as FAIL (fail-closed)." % e

    # agy prints diagnostic lines to stdout before the final JSON object on its own line;
    # find the last line that parses as JSON with a "response" key.
    final_text = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            evt = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "response" in evt:
            if evt.get("status") != "SUCCESS":
                return spec["name"], False, "agy status=%s (not SUCCESS) — treated as FAIL (fail-closed)." % evt.get("status")
            final_text = evt.get("response", "")

    if final_text is None or not final_text.strip():
        return spec["name"], False, "No usable response parsed from agy output — treated as FAIL (fail-closed)."

    passed = final_text.strip().upper().startswith("VERDICT: PASS")
    return spec["name"], passed, final_text.strip()


def run_pass(spec: dict, path: str) -> tuple[str, bool, str]:
    if spec["engine"] == "agy":
        return run_pass_agy(spec, path)
    return run_pass_opencode(spec, path)


def main() -> int:
    raw = sys.stdin.read()
    try:
        hook_input = json.loads(raw)
    except json.JSONDecodeError:
        print(json.dumps({"continue": True}))
        return 0

    tool_input = hook_input.get("tool_input", {})
    file_path = tool_input.get("file_path") or hook_input.get("tool_response", {}).get("filePath")
    if not file_path:
        print(json.dumps({"continue": True}))
        return 0

    norm = file_path.replace("\\", "/")
    if not any(("/" + p + "/") in ("/" + norm) or norm.startswith(p + "/") for p in CANON_PREFIXES):
        print(json.dumps({"continue": True}))
        return 0

    # Sequential, not parallel: concurrent opencode-cli invocations were observed
    # contending with each other and timing out on tasks that ran cleanly alone.
    results = [run_pass(spec, file_path) for spec in PASSES]

    failures = [(name, txt) for (name, passed, txt) in results if not passed]

    if not failures:
        print(json.dumps({
            "continue": True,
            "systemMessage": "All %d independent review passes clean for %s." % (len(PASSES), file_path),
        }))
        return 0

    reason_lines = ["Independent review (non-Claude models) flagged this edit to %s:" % file_path, ""]
    for name, txt in failures:
        reason_lines.append("=== %s ===" % name)
        reason_lines.append(txt)
        reason_lines.append("")
    reason = "\n".join(reason_lines)

    print(json.dumps({
        "continue": True,
        "decision": "block",
        "reason": reason,
        "systemMessage": "%d/%d independent review pass(es) flagged %s — see reason." % (
            len(failures), len(PASSES), file_path),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
