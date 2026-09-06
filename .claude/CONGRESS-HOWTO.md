# How to run the model congress (for the Gemini/Antigravity session)

You kept failing at this. Here is exactly how it works, and the one script that does it.

**Moved 2026-09-03: the actual script now lives outside this project.** All three
multi-model tools (`run_congress.py`, plus the debate and board drivers that used to be
Frogs-Lancer-only) are now shared at `C:\Users\fbrown\Projects\ai-panels\`, project-agnostic,
so this project can use all three, not just the congress. **Read
`C:\Users\fbrown\Projects\ai-panels\README.md` first** — it has the full picture (all three
tools, a real naming-collision warning worth knowing before trusting an older comment
anywhere that says "the congress," and the history of why this moved). This file only covers
the congress-specific operational details relevant to this project.

## Non-observation disclosure (permanent, added 2026-09-03)

`run_congress.py` automatically prepends a standing disclosure to every brief: Frank
doesn't watch congress runs live, only checks them directly for a postmortem when something
went wrong, and this is a boundary he keeps by choice, not a technical guarantee. This is
baked into the script itself (the `DISCLOSURE` constant in `ai-panels\run_congress.py`) — do
not write it into brief files by hand, and do not remove it when writing a new brief. It's
kept in sync on purpose with the same wording in `ai-panels\run-debate.sh` and
`ai-panels\run-board.sh`. If you ever change the wording in one place, change it in all three.

## The rules

1. **The panel is OpenCode CLI free models ONLY.** `opencode/big-pickle`,
   `opencode/muse-spark-1.2-contributor-free`, `opencode/mimo-v2.5-free`,
   `opencode/ling-3.0-flash-fin-free`. These are free.
2. **NEVER use `agy` / Antigravity for the panel.** Those spend Frank's real money. They are
   reserved for a single human-approved highest-difficulty task and you will almost never need
   them. Using them without explicit approval is a serious failure.
3. **A congress with fewer than 3 models returning is not a congress.** The entire point is
   multiple distinct perspectives argued against each other. One model back = you failed the
   task. Retry the failures.
4. **You do the synthesis.** The script gets you 4 raw answers. Reading them, extracting each
   one's distinct take, arguing them against each other, and producing the merged best answer
   is *your* job — that's the part that matters and the part you can do natively.

## The one command

```
python C:\Users\fbrown\Projects\ai-panels\run_congress.py <brief_file> --dir <project_dir> --out <out_dir>
```

- **Write the brief to a file first.** A long multi-line prompt on the command line will break
  on quoting. Put the whole brief in `scratch/congress_brief.md` and pass that path.
- The brief should end with: *"Written answer only. Do NOT edit files, do NOT make tool calls,
  do NOT ask questions — produce your complete design/answer in one response."* (Otherwise
  big-pickle in particular wanders off trying to edit things.)
- `--dir` lets the models read the campaign files (the narrative, the trackers). Point it at
  `C:\Users\fbrown\Projects\Frogs-5-skyrim`.
- `--out scratch/congress_out` writes one `.md` per model plus a combined `ALL.md`.

## What NOT to do (your past mistakes)

- **Do not set a short timeout.** The script default is 1200s (20 min) per model. These models
  genuinely take 1–15 minutes. Your 300s timeout was clipping Muse Spark and Big Pickle at the
  exact moment they finished.
- **Do not poll every 30 seconds.** The script runs all 4 models in parallel and prints one
  line as each finishes. Kick it off, then check back once at ~12 minutes.
- **Do not run them one at a time.** Parallel = total wait ≈ the slowest single model
  (~15 min). Sequential = the sum (~1 hour). The script is parallel by default.
- **Kill orphaned processes first.** If a previous run left `OpenCode.exe` instances resident:
  `taskkill /F /IM OpenCode.exe` before the next run.

## The flags that stop it hanging (baked into the script)

- `--dangerously-skip-permissions` — without it, `opencode run` blocks forever on an
  interactive permission prompt.
- `stdin` piped from `DEVNULL` — the CLI never sits waiting on the terminal.
- plain `run` output captured from stdout — no `--format json` / NDJSON parsing needed.

## How Claude does it (same thing, by hand)

Claude runs, per model, one background shell command:

```
opencode-cli.exe run --model opencode/<id> --dangerously-skip-permissions --dir <project> "<brief>"  > out/<id>.md 2>&1
```

…all four launched at once, then reads every output file when they finish and synthesizes.
`run_congress.py` is exactly this, wrapped so you don't have to babysit it.

## Iterated back-and-forth debates and collaborative builds — now available here too

A one-shot congress (above) gets 4 independent takes with no discussion. If a question
genuinely needs to be *argued to a resolution*, not just surveyed, use
`ai-panels\run-debate.sh` instead — same panel plus Gemini, blind first round, then a real
multi-pass conversation until convergence or a stall. If instead you want several models to
actually *build* something together (not argue toward one verdict), use
`ai-panels\run-board.sh`. Both now take this project's directory as an argument the same way
the congress does — see `ai-panels\README.md` for exact usage of each. Both used to be
Frogs-Lancer-only; that's no longer true.
