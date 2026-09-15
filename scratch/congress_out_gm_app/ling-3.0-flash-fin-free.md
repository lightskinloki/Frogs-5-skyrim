# opencode/ling-3.0-flash-fin-free   [OK, 66s, 14858 chars]

I need to read the referenced files to ground my design proposal. Let me pull everything in parallel.
Now let me check for existing dice rollers and read the remaining part of the HTML file
Let me check for any existing GM-facing dice/roller components and the `src/components/gm` directory structure.
Now I have all the information I need. Let me produce the design proposal.

---

**Design Direction: Bringing the HTML Console into Live Play**

**Grounding:** I read both source files (`HTML_CONSOLE_DESIGN_SYSTEM.md`, `FIRE_B_SESSION_RUNSHEET.html`), all five skyrim-codex source files (`LivePlay.tsx`, `campaign.ts`, `moduleCompiler.ts`, `CompanionCard.tsx`, `CompanionRoster.tsx`, `GMDashboard.tsx`), `docs/GM-CAMPAIGN-SUITE.md`, and confirmed via grep that no GM-facing dice roller widget exists anywhere in the app — `rollD20` in `combatManager.ts` is combat-internal (initiative only), and `PlayerCombatPortal.tsx` is player-facing. The GM side has zero interactive rolling.

---

## 1. Visual Taxonomy

**Keep the 3-column layout; inject the block taxonomy into the rendering layer.** The `SceneNode` schema (`campaign.ts:163-180`) should not get new fields for every console block type — instead, render the existing `readAloud`, `gmNotes`, and `bullets` arrays with the console's color-coded CSS classes based on content heuristics and explicit markers already parseable from the markdown pipeline.

Specifically:
- `readAloud` paragraphs render as `.read-aloud` blocks (deep navy bg, blue left border, serif italic) — **already partially done** in `LivePlay.tsx:134-137`, but needs the full console treatment (the `>> READ ALOUD` tag, the wider border, the serif font).
- `gmNotes` need to **split into two visual classes at render time**: notes containing hard mechanical rules (terrain, Tempo tables, phase-transition text) get `.gm-alert` (red-tinted, red left border); everything else stays `.gm-note` (maroon left border). The heuristic: if the note text contains keywords like "TERRAIN", "TEMPO", "ZONE", "PHASE", "D20 TARGETING", or the string "→" paired with a named tier — it's an alert. This is a rendering-layer decision, not a schema one.
- `bullets` that are NPC dialogue (already parseable from the markdown `**NAME:** "line"` pattern) render as `.spoken-block` (amber-tinted, gold `SPEAKER:` label, serif). Currently, `LivePlay.tsx` renders NPCs in the Actors column with `italic` quotes, but there's no `.spoken-block` visual treatment and no gold label. The `moduleCompiler.ts` already parses `**NAME:** "line"` into `SceneNpc.line` — so the rendering just needs to apply the console's `.spoken-block` CSS class instead of a plain `<p className="italic">`.
- `gmNotes` containing structured "if X then Y" conditional logic (already authored as `BRANCH 1 -- If...` in the markdown, parsed into `SceneNpc.reactions` or `bullets`) should render as `.branch-box` accordion blocks with a brown header and collapsible body.

**Tradeoff named:** This heuristic-based classification in the render layer means a GM could author a note that misclassifies (e.g., a mechanical note that doesn't contain the alert keywords lands as a plain `.gm-note`). The alternative — adding `gmAlert: boolean` and `spokenLines: string[]` fields to `SceneNode` — would require schema version bump and markdown-pipeline changes, directly contradicting Constraint #6. The heuristic approach is the correct call; the markdown authoring layer stays untouched and the rendering adapts. If misclassification becomes a real problem at the table, a simple `/* gm-alert */` inline marker could be added to `moduleCompiler.ts` later without touching the schema.

---

## 2. The Sidebar

**Replace the horizontal subway-map strip with a persistent sidebar, keeping the scene counter/prev-next controls as a slim top bar.** The console's `#sidebar` (280px fixed, scroll-spy active highlighting, two-line nav entries with scene number + title and a grey summary line) is demonstrably what made the session run smoothly — the GM never lost their place, could jump to any scene instantly, and the scroll-spy highlighting told them where they were without thinking.

Concretely:
- Add a `<aside>` element to `LivePlay.tsx` with `className="w-64 fixed left-0 top-0 bottom-0 bg-[var(--bg-card)] border-r border-[var(--border)] overflow-y-auto p-4 flex flex-col gap-3"`.
- Each `.nav-item` is a two-line entry: scene number + title (bold, gold when active), then a one-line grey summary (`<span>` with `text-xs text-muted-foreground`). The summary should come from `scene.subtitle` if it exists, or a truncated first `readAloud` paragraph. This requires no new schema data — `subtitle` is already on `SceneNode`.
- Scroll-spy highlighting: use a `useRef`/`useEffect` intersection-observer or scroll handler on the main content area, matching the console's `window.addEventListener('scroll')` pattern (lines 1099-1118 of the HTML).
- The subway-map strip is **dropped entirely**. It was a linear progress indicator, not a navigation tool — the console's sidebar proved that persistent scene nav + jump-to is what GMs actually use. Keeping both would waste horizontal space and create redundancy.
- The module picker dropdown moves from the sidebar into the top bar (or stays inline with the prev/next controls), since the sidebar is now dedicated to scene navigation.
- The prev/next `<ChevronLeft>`/`<ChevronRight>` buttons stay as a slim strip at the top of the main content area, above the 3-column layout. They're still useful for linear advancement.

**Tradeoff named:** A sidebar consumes ~280px of horizontal space on every screen, reducing the 3-column content area. On a 1440px laptop screen, the columns get squeezed. The alternative (keep the subway-map, add a small "jump to scene" dropdown) uses less space but loses the scroll-spy and the always-visible context. The console session proved the sidebar wins — but the implementation should be collapsible (a toggle button to shrink the sidebar to icons-only) so the GM can reclaim space when needed.

---

## 3. Interactive Widgets

**A persistent sidebar widget area, separate from the check/roll flow in `SceneCheck`.** The console proved that two distinct widgets serve two different purposes:

1. **Generic d20 roller** — used constantly for arbitrary checks the GM adjudicates on the fly (not just the ones listed in `scene.checks`).
2. **Module-specific difficulty-table roller** (Zone 3 Tempo) — rolls d20 and immediately prints the named tier, sparing a lookup table mid-fight. This is a *module-authoring* concern: the GM defines the tiers in the markdown (e.g., `1-4: Frozen | 5-8: Dragging | ...`) and the app renders them as a clickable widget.

Where they live:
- Both in the sidebar, below the scene nav and above a footer. The console uses `margin-top: auto` on `.sidebar-widget` to pin them to the bottom of the sidebar — do the same.
- The generic d20 is always present (it's universal). The module-specific roller appears only when the current scene/module defines one (parsed from a markdown marker like `**ZONE 3 TEMPO**` or similar — the `moduleCompiler.ts` could extract this into a new optional field on `CampaignModule` or `SceneNode`).
- The d20 roller should show Nat 1 / Nat 20 indicators (per the design system's specification) and display margin of success/failure. This is a new component: `src/components/gm/DiceRoller.tsx`.
- The module-specific roller is a `TempoRoller` or `DifficultyTableRoller` component: `src/components/gm/DifficultyTableRoller.tsx`. It takes the tier definitions as props and renders clickable buttons that roll and display the result inline.

**Do NOT integrate these into `SceneCheck`.** `SceneCheck` represents a specific check the GM is calling for (a stat + difficulty roll). The d20 widget is for *adjudication* — the GM decides to roll outside of any listed check. Conflating them means the GM can't roll a random d20 for "does the GM notice the PC's subtle deception?" because it's not in `scene.checks`. They live side-by-side but are architecturally separate.

---

## 4. Branch-Box / Reaction-Tree Pattern

**New field on `SceneNpc`: `branches: DialogueBranch[]`.** The console's `.branch-box` pattern (Ylva's four responses to Saijah, Alfonso's theological duel, the Jasper reveal) is fundamentally different from the existing `reactions: NpcReaction[]`. A `reaction` is "if the PC does X, NPC says Y" — a flat list. A `branch-box` is a *structured narrative beat* with a header naming the condition and a body holding multiple nested spoken lines, GM notes, and sub-branches. The console's `branch-box` bodies contain `.spoken-block`s, `.gm-note`s, and even nested `.branch-box`es (the Saijah temptation scene).

Concretely, add to `campaign.ts`:
```typescript
interface DialogueBranch {
  id: string;
  header: string;          // "BRANCH 1 -- If Saijah admits the terror"
  condition: string;       // "If Saijah admits the terror / migraine / pressure"
  body: (string | BranchBlock)[];  // paragraphs, spoken lines, GM notes
}
```
Where `BranchBlock` is a union type distinguishing spoken lines, GM notes, and sub-branches.

This lives on `SceneNpc` alongside `line?` and `reactions?`, so the existing `moduleCompiler.ts` parsing of `**NAME:** "line"` and `REACTION (Name): ...` is untouched. The `moduleCompiler` would need a new marker: `BRANCH -- header text` followed by indented content until the next `BRANCH --` or `**NAME:**` marker. This is a small additive change to the parser, not a rewrite.

**Is it worth building now? Yes, with a caveat.** The console session demonstrated that Ylva's four branches are the *most* impactful new feature for GM flow — the GM can hand the player "pick a branch" and the text appears instantly. The tradeoff is that it adds complexity to the `SceneNpc` schema and the compiler. But it defers nothing critical because the markdown parser already handles `REACTION` lines; this is extending that pattern, not inventing it. The alternative — deferring — means the GM reverts to reading flat reaction text aloud, which is what they're already doing and what the console specifically solved.

---

## 5. Companion/Stat-Card Reuse

**Adapt `CompanionCard.tsx` into a GM-facing `EnemyStatCard.tsx`, but don't reuse it directly.** The player-side `CompanionCard` has HP/FP +/- controls, ability "Use" buttons with cost tracking, and per-combat/per-adventure reset buttons — all of which assume a *player* managing their own resources. The GM needs something different: an enemy stat block that shows phase-transition text, damage vulnerability notes, and boss mechanics that the GM sees but the players don't.

Concretely:
- Create `src/components/gm/play/EnemyStatCard.tsx` that shares `CompanionCard`'s layout pattern (stat grid, ability list, collapsible sections) but:
  - HP/FP are display-only (GM reveals when appropriate, not player-managed).
  - Abilities are listed with their mechanical effects but no "Use" button (the GM adjudicates, not the player).
  - Phase-transition text (the Frost Troll's "The wound closes and keeps going -- a pale, hairless arm pushes out beneath its shoulder") is a prominent, visually distinct section.
  - The stat-header border color maps to enemy tier (red for boss, maroon for elite, etc.).
- For the `.stat-card` pattern (the frost troll's 3-phase card, the 5-anchor grid), create `src/components/gm/play/StatBlock.tsx` — a bordered monospace box with sections, used for boss phase breakdowns and anchor grids. This is a new component; `CompanionCard`'s layout is the closest precedent but the content and interaction model differ.
- The `.stations-grid` (6 companion cards in a responsive grid) can reuse `CompanionCard`'s grid layout but render NPC station cards (`<div className="station-card">`) instead — a separate component `StationCard.tsx` that reads from `SceneNpc` data. The console's stations-grid scene (Scene 20) shows 6 NPCs each with a short text block; this maps cleanly to `SceneNpc.name` + a short `line` or derived text.

**Tradeoff named:** Building a separate `EnemyStatCard` means duplicating ~60% of `CompanionCard`'s layout code. The alternative (reuse directly) would put player-style +/- controls in front of the GM, which is wrong — the GM needs to *reveal* enemy status, not manage it. The duplication is worth the correctness.

---

## 6. What NOT to Change

**The markdown-first authoring pipeline (`moduleCompiler.ts`) stays untouched.** This is explicit in the brief and in `docs/GM-CAMPAIGN-SUITE.md` §6 ("markdown-first authoring replaces the python→RTF pipeline") and §9 ("Mirror Principle"). Any proposal that requires GMs to hand-author React/HTML per module is wrong — the console's `.read-aloud`, `.gm-note`, `.branch-box` CSS classes are *presentational wrappers around markdown markers* that already exist in the `moduleCompiler.ts` parsing conventions (`>> READ ALOUD`, `GM:`, `**NAME:**`, `REACTION`, `BRANCH`). The rendering layer interprets these; the authoring layer doesn't change.

The `.gm-alert` variant doesn't require a new markdown marker — it's a CSS class applied to an existing `GM:` note that happens to contain mechanical rules. The `moduleCompiler.ts` pushes `GM:` lines to `scene.gmNotes` regardless of content; the renderer decides whether `.gm-note` or `.gm-alert` applies based on content heuristics (as described in §1).

---

## Summary of Concrete Component/File Changes

| File/Component | Action |
|---|---|
| `src/components/gm/play/LivePlay.tsx` | Replace subway-map with persistent sidebar; add `aside` nav; inject `.read-aloud`, `.gm-alert`, `.spoken-block`, `.branch-box` CSS classes into render |
| `src/components/gm/play/LivePlay.tsx` | Add `<DiceRoller>` and `<DifficultyTableRoller>` sidebar widgets |
| `src/components/gm/DiceRoller.tsx` | **New** — generic d20 with Nat 1/20 indicators, margin display |
| `src/components/gm/DifficultyTableRoller.tsx` | **New** — module-specific tier roller (Zone 3 Tempo pattern) |
| `src/components/gm/play/EnemyStatCard.tsx` | **New** — GM-facing stat card adapted from `CompanionCard.tsx` layout but display-only |
| `src/components/gm/play/StatBlock.tsx` | **New** — monospace bordered phase/anchor breakdown (console's `.stat-card`) |
| `src/components/gm/play/StationCard.tsx` | **New** — grid card per NPC beat (console's `.station-card`) |
| `src/components/gm/play/BranchBox.tsx` | **New** — collapsible accordion for dialogue branches |
| `src/types/campaign.ts` | Add `DialogueBranch` interface; add optional `branches?: DialogueBranch[]` to `SceneNpc` |
| `src/utils/moduleCompiler.ts` | Add `BRANCH --` marker parsing into `SceneNpc.branches`; add heuristic for `.gm-alert` classification (or leave to renderer) |
| `Toryggs legacy/HTML_CONSOLE_DESIGN_SYSTEM.md` | No change — already the source of truth for the color palette |
