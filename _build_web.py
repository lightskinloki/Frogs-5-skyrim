# -*- coding: utf-8 -*-
"""THE WEB builder.

Scans the campaign corpus, merges the curated annotation layer, computes
connection CANDIDATES (shared tags / heavy co-occurrence with no authored
edge), and emits:
  web/web.json   - machine view (an AI reads this first)
  web/web.html   - human view (self-contained force-graph app, no internet)

Run after any writing session:  python _build_web.py
"""
import json, os, re, sys, html
from collections import defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(ROOT, "web")
SCAN_DIRS = ["Toryggs legacy", "Lore Books", "GM Guide", "campaign advice"]
SCAN_FILES = ["campaign_status_update.md", "Spell list", "Location Reference",
              "Gear, Consumables, and the forge", "players guide"]
SKIP_EXT = {".rtf", ".docx", ".svg", ".py", ".json", ".html", ".png", ".jpg"}
SKIP_DIRS = {".git", "web", "__pycache__"}
# aliases matched case-SENSITIVELY (too noisy lowercase)
CS_ALIASES = {"gear": "GEAR"}
# aliases skipped entirely (too generic)
NOISY = {"grant"}

def load(p):
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def corpus_files():
    out = []
    for d in SCAN_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS]
            for fn in filenames:
                if os.path.splitext(fn)[1].lower() in SKIP_EXT:
                    continue
                out.append(os.path.join(dirpath, fn))
    for f in SCAN_FILES:
        p = os.path.join(ROOT, f)
        if os.path.isfile(p):
            out.append(p)
    return out

def main():
    reg = json.loads(load(os.path.join(WEB, "registry.json")))["entities"]
    ann = json.loads(load(os.path.join(WEB, "annotations.json")))
    edges, secrets = ann["edges"], ann["secrets"]
    ids = {e["id"] for e in reg}
    for ed in edges:
        for k in ("src", "dst"):
            if ed[k] not in ids and ed[k] != "party":
                print(f"  [warn] edge references unknown id: {ed[k]}")

    # compile alias patterns
    pats = []  # (entity_id, compiled, case_sensitive)
    for e in reg:
        for a in e["aliases"]:
            if a in NOISY:
                continue
            if a in CS_ALIASES:
                pats.append((e["id"], re.compile(r"\b" + re.escape(CS_ALIASES[a]) + r"\b"), True))
            else:
                pats.append((e["id"], re.compile(r"\b" + re.escape(a) + r"\b", re.IGNORECASE), False))

    mentions = defaultdict(lambda: defaultdict(int))   # ent -> relpath -> count
    snippets = defaultdict(dict)                        # ent -> relpath -> snippet
    files = corpus_files()
    print(f"scanning {len(files)} files...")
    for path in files:
        text = load(path)
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        for eid, pat, cs in pats:
            ms = list(pat.finditer(text))
            if not ms:
                continue
            mentions[eid][rel] += len(ms)
            if rel not in snippets[eid]:
                i = ms[0].start()
                s = text[max(0, i - 90):i + 110].replace("\n", " ").strip()
                snippets[eid][rel] = ("..." + s + "...")

    # co-occurrence (shared files, weighted by min count, top 8 per node)
    cooc = defaultdict(int)
    by_file = defaultdict(list)
    for eid, fm in mentions.items():
        for rel, c in fm.items():
            by_file[rel].append((eid, c))
    for rel, lst in by_file.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                a, ca = lst[i]; b, cb = lst[j]
                key = tuple(sorted((a, b)))
                cooc[key] += min(ca, cb)
    per_node = defaultdict(list)
    for (a, b), w in cooc.items():
        per_node[a].append((w, a, b)); per_node[b].append((w, a, b))
    keep = set()
    for n, lst in per_node.items():
        for w, a, b in sorted(lst, reverse=True)[:8]:
            keep.add((a, b))
    cooc_edges = [{"a": a, "b": b, "w": cooc[(a, b)]} for (a, b) in keep]

    # candidates: shared tags or heavy co-occurrence, with NO authored edge
    authored = {tuple(sorted((e["src"], e["dst"]))) for e in edges}
    tagmap = {e["id"]: set(e["tags"]) for e in reg}
    GENERIC = {"party", "cart", "location", "concept", "artifact", "faction",
               "villain", "monster", "clock", "plague", "daedra", "aedra", "riften",
               "dead", "child", "witness"}
    tag_freq = defaultdict(int)
    for e in reg:
        for t in e["tags"]:
            tag_freq[t] += 1
    cands = []
    seen = set()
    for i, e1 in enumerate(reg):
        for e2 in reg[i + 1:]:
            key = tuple(sorted((e1["id"], e2["id"])))
            if key in authored or key in seen:
                continue
            shared = (tagmap[e1["id"]] & tagmap[e2["id"]]) - GENERIC
            w = cooc.get(key, 0)
            # rare shared tags are the interesting ones: a tag held by only
            # 2-3 entities scores far higher than one held by 15
            rarity = sum(40.0 / max(tag_freq[t], 2) for t in shared)
            score = rarity + min(w, 30)
            if shared or w >= 12:
                cands.append({"a": key[0], "b": key[1], "sharedTags": sorted(shared),
                              "cooc": w, "score": round(score, 1)})
                seen.add(key)
    cands.sort(key=lambda c: -c["score"])
    # never cap tag-sharing candidates (the high-value ones);
    # cap the cooc-only noise
    tagged = [c for c in cands if c["sharedTags"]]
    cooc_only = [c for c in cands if not c["sharedTags"]][:40]
    cands = sorted(tagged + cooc_only, key=lambda c: -c["score"])

    data = {
        "built": str(date.today()),
        "readme_for_ai": ("THE WEB: read this file before campaign design work. "
            "'edges'+'secrets' are AUTHORED canon (trust them). 'cooc' is lexical "
            "co-occurrence (signal, not canon). 'candidates' are pairs that share "
            "curated tags or co-occur heavily but have NO authored story edge - "
            "these are the connections the GM and you might be missing; review them, "
            "author the real ones into web/annotations.json, rerun _build_web.py."),
        "entities": reg,
        "edges": edges,
        "secrets": secrets,
        "mentions": {k: dict(sorted(v.items(), key=lambda x: -x[1])[:6]) for k, v in mentions.items()},
        "snippets": {k: {r: v[r] for r in list(dict(sorted(mentions[k].items(), key=lambda x: -x[1])[:3]))} for k, v in snippets.items()},
        "cooc": sorted(cooc_edges, key=lambda e: -e["w"]),
        "candidates": cands,
    }
    with open(os.path.join(WEB, "web.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print(f"web.json: {len(reg)} entities, {len(edges)} authored edges, "
          f"{len(cooc_edges)} cooc edges, {len(cands)} candidates")

    tpl = load(os.path.join(WEB, "viewer_template.html"))
    out = tpl.replace("/*__DATA__*/", "const DATA = " + json.dumps(data, ensure_ascii=False) + ";")
    with open(os.path.join(WEB, "web.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("web.html written.")

if __name__ == "__main__":
    main()
