# SYNTHESIS: Live Play redesign, from the 3-model congress

## Audit addendum — verified against the real skyrim-codex source (not the congress's citations)

Read `LivePlay.tsx`, `campaign.ts`, `moduleCompiler.ts`, `GMDashboard.tsx`, `CompanionCard.tsx`,
`enemies.ts`, `combatManager.ts`, `docs/GM-CAMPAIGN-SUITE.md` directly. Schema, line-number
citations, and the "no dice roller exists" claim all checked out exactly as the models described.
Three things they got wrong or missed:

1. **Read-aloud styling is further along than credited.** `LivePlay.tsx:133-137` already has the
   blue border, tinted bg, italic text, and a "▶ READ ALOUD" tag. The Day-1 restyle task is
   cheaper than framed — the real remaining gap is just the serif font and it not looking
   distinct enough from GM notes at a glance.
2. **`GMDashboard.tsx:73` wraps every tab in `container mx-auto px-4`** — a capped max-width, not
   a full-bleed page. None of the three named this specifically. It makes the sidebar-space
   squeeze sharper than any of them modeled: a fixed sidebar competing with an already-3-column
   grid inside a capped container is tight on a real laptop. **Decision: sidebar defaults
   collapsed** (icon rail, click/hover to expand) rather than open-by-default.
3. **Branch-box is a bigger lift than described.** `moduleCompiler.ts:181-186`'s `REACTION`
   marker captures **no condition text at all** — `NpcReaction.action` is hardcoded to the
   literal string `'reaction'` in code, never populated from markdown. This isn't upgrading an
   existing flat structure into a conditional one; there is currently no way to author a
   condition in the markdown at all, so this needs a new marker designed from scratch.
   **Decision: stays at build-order step 3 anyway** — still the single feature named from
   tonight's table, worth the extra design cost now rather than deferring.


Source: `scratch/congress_out_gm_app/ALL.md` (big-pickle, mimo-v2.5-free, ling-3.0-flash-fin-free —
muse-spark errored). Brief: `scratch/congress_brief_gm_app_html_console.md`.

All three independently read the same five skyrim-codex files plus both console docs. Where they
agree, that's a strong signal. Where they split, I've argued it below and picked a side.

---

## Q1 — Visual taxonomy: THE one real fight. Verdict: phased — render-first, schema second.

Three different answers:
- **big-pickle**: full schema rewrite now — add `blocks?: SceneBlock[]` (discriminated union),
  compiler emits it in document order. Argument: the current `readAloud`/`gmNotes`/`bullets`
  split already destroyed *order* and *authorial kind* — a render-only pass can restyle a GM
  note red, but it can't put a spoken NPC line back between two read-aloud paragraphs where it
  actually happened, because that position was never stored.
- **mimo**: middle ground — two small additive fields (`gmNotesTyped` with severity, keep
  everything else untouched).
- **ling**: pure render layer, zero schema change — classify `gmNotes` as alert-vs-note by
  keyword heuristic ("TERRAIN", "ZONE", "→"), style NPC lines as spoken-blocks, leave the rest.
  Explicitly invokes constraint #6 (don't touch the pipeline) as the reason.

**big-pickle is right about the actual defect, and ling's own proposal proves it**: ling's
heuristic can only reclassify text that's *already sitting in the right bucket*. It cannot
interleave a spoken NPC line at the point in the read-aloud where it's supposed to fire, because
`npcs[].line` and `readAloud[]` are two separate arrays with no shared position. That's not a
styling gap, it's a data-loss gap — the compiler threw away order when it split markdown into
buckets. No amount of render-layer cleverness recovers position that was never recorded.

But big-pickle's full rewrite is more than tonight needs, and doing it in one shot risks exactly
the kind of change that's hard to verify before the next session. **Phase it:**

1. **Now, zero schema risk**: restyle what already exists — read-aloud gets the full console
   treatment (serif italic, `>> READ ALOUD` tag), GM notes split note/alert by ling's keyword
   heuristic, NPC `line` renders as a gold spoken-block instead of plain italic. This alone
   recovers most of the console's *feel* with no data-model change and is safe to ship before
   the next session if wanted.
2. **Next, additive only**: add big-pickle's `blocks?: SceneBlock[]` as an *optional* field on
   `SceneNode` — old modules with no `blocks` keep rendering exactly as they do today through the
   existing arrays; nothing breaks. `moduleCompiler.ts` learns to emit `blocks` in document order
   when the markdown uses new conventions (a bold-speaker line becomes a `spoken` block in place,
   an explicit alert marker becomes `gmAlert`). Prove it by recompiling `FIRE_B_module.md` — the
   exact module that earned the verdict — into the new shape.

This is the one place none of the three proposed a staged rollout; I think it's the correct
answer precisely because it lets you ship the visible win immediately without committing to the
bigger schema change before the GM's seen it live.

---

## Q2 — Sidebar: unanimous. Adopt it, fold the subway map in, make it collapsible.

All three agree on all points:
- Persistent left sidebar replaces the horizontal strip.
- Two-line entries (number + title, one-line grey summary — `scene.subtitle` already exists,
  zero new data needed).
- Scroll-spy active-highlighting.
- **Must collapse** on narrow widths — the console got to assume a full page; Live Play lives
  inside a `GMDashboard` tab and can't spend 280px unconditionally. This is the one thing the
  console didn't have to solve and Live Play does.
- The subway-map's only surviving value is at-a-glance module shape — keep that as a compact
  numbered-dot strip inside the sidebar header, don't run it alongside the sidebar as a second nav.

No real disagreement here — build it as described.

---

## Q3 — Widgets: unanimous. Sidebar-persistent, separate from SceneCheck, tables become data.

All three land in the same place:
- One d20 engine, always visible in the sidebar regardless of scroll (matches the console's
  actual proven property — not the dice graphic, the *always-reachable* part).
- `SceneCheck` gets a second affordance — "Roll this check" — that fires the same engine
  pre-loaded with that check's modifier. Not a separate roller.
- The module-specific tier roller (tonight's Zone 3 Tempo) stops being a one-off hand-built
  widget and becomes **data**: a table of tiers authored in the module's markdown, compiled into
  a generic rail widget. This is what turns "one artifact per module" into an actual feature —
  named explicitly by big-pickle as "the entire point of the brief," and I agree that's the
  correct read of what the GM actually asked for.
- FROGS is d20-only — the engine applies the difficulty modifier to the player's TN, never
  displays a GM-set target number to anyone.

---

## Q4 — Branch-box: unanimous on "build now," split on shape. Verdict: flat now, defer nesting.

All three agree this is needed now, not deferred — Ylva's four branches and the Alfonso/Jasper
callouts are the single feature the GM called out by name as the table-proven case, and every
future module will use this pattern.

Shape differs:
- **big-pickle / mimo**: flat — one condition, one response, optional GM prompt. Covers tonight's
  module completely.
- **ling**: nested — a branch's body can hold sub-branches, multiple spoken lines, GM notes
  mixed in (`body: (string | BranchBlock)[]`). More expressive, more schema surface.

**Flat now.** Two independent models converged on the same minimal shape without coordinating,
and it covers every branch that actually fired at the table tonight (Ylva's 4, the two special
callouts). ling's own writeup names no case from tonight's module that needs nesting — it's
justified by "the Saijah temptation scene" as a hypothetical, not by something that happened.
Add nesting later if a real module needs it; don't pay the complexity now for a case that hasn't
shown up yet.

```
branches?: Array<{
  id: string;
  condition: string;   // "If Saijah admits the terror"
  response: string;    // NPC spoken line
  gmPrompt?: string;   // "GM STOP: turn to Saijah's player..."
}>
```
on `SceneNpc`, alongside existing `line` and `reactions`.

---

## Q5 — Stat-card reuse: unanimous "don't reuse CompanionCard directly," split on HOW. Verdict: build a separate GM component now, extract a shared shell later if a third need appears.

All three agree `CompanionCard.tsx` is wrong to reuse as-is — its actions (+/- FP, "Use" ability
buttons that spend a player's resources) are player affordances that have no business in front
of a GM looking at an enemy.

- **big-pickle**: extract a presentational `StatCard` shell now, refactor `CompanionCard` to
  consume it, build the GM variant on top of the shared shell.
- **mimo / ling**: build a separate GM-only component (`GmStatCard` / `EnemyStatCard`) that
  copies the layout pattern but shares no code; ling explicitly accepts ~60% duplication as the
  price of not touching a component that just shipped and works.

**Side with mimo/ling here — build separate, don't extract yet.** `CompanionCard` was built,
tested live in-browser, and committed *tonight*. Refactoring it to serve a second consumer before
that consumer exists is the more expensive, higher-risk move for a win (shared styling) that a
second real component can just as easily copy by eye. Rule of three: duplicate once on purpose,
extract the shell only when a third stat-card need shows up and the duplication is actually
costing something. big-pickle's instinct isn't wrong in the abstract — it's just early.

The GM-side card needs, concretely (all three agree): HP bars with **phase-transition markers**
(the frost troll's three-body-state structure), special/villain rules as callout text, no
ability "Use" buttons, no FP tracking. Data source: extend `EnemyTemplate` in `enemies.ts` with
optional `phases?` and `specialRules?` — additive, not a breaking change to what's already there.

---

## Q6 — Markdown pipeline: unanimous, no dispute.

All three affirm `moduleCompiler.ts` stays the only authoring surface — every proposal above
(blocks, branches, roller tables) is designed to enter through markdown conventions the compiler
already parses or gains new markers for. Nobody hand-authors React or HTML per module. This one
wasn't actually contested by any model, including the one instructed to push back if it disagreed.

---

## Build order (merging all three "what to do first" lists, reconciled with the phasing above)

1. **Render-only pass, ship first**: read-aloud full styling, gm-note/gm-alert split by keyword,
   NPC lines as spoken-blocks. Zero schema risk.
2. **Sidebar**: replace subway strip, scroll-spy, collapsible, module-shape dots folded in.
3. **Branch-box (flat)**: new `branches?` field on `SceneNpc`, compiler marker, render as
   accordion block.
4. **d20 roller + data-driven tier roller**: sidebar-persistent, `SceneCheck` gets the "roll
   this" affordance.
5. **`GmStatCard`** (separate component, not shared shell): phase markers, special rules, no
   player controls. Extend `EnemyTemplate` with `phases?`/`specialRules?`.
6. **`blocks?: SceneBlock[]`** (the big one): additive schema field, compiler emits in document
   order for modules that opt in; prove it by recompiling `FIRE_B_module.md`.

Steps 1-5 are all additive/non-breaking and independently shippable. Step 6 is the only one
that's genuinely structural, which is why it's last, not first — ship the visible wins, then do
the harder data-model work once the rest is already proving the direction is right.
