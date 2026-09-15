# CONGRESS RESULTS — congress_brief_gm_app_html_console.md
# 3/4 models returned usable answers.


========================================================================================
## opencode/big-pickle   [OK, 195s]

## Design direction: Live Play → the HTML-console model

### The governing diagnosis, in one line

The console wasn't better because of its colors. It was better because **the console is an ordered script and Live Play is a set of buckets.** The console reads top-to-bottom in the exact order the GM does things: read this aloud, say this as Ylva, check this rule, jump to this branch. Every feature that made it "smooth" — two-line nav, scroll-spy, block taxonomy, fixed footer exits, sidebar dice — is a consequence of that linear spine. Live Play's `Narrative / Actors / Action` columns meanwhile flatten the module into *three piles*: all read-aloud together, all NPC beats frozen in collapsed Actors cards, all mechanics quarantined on the right. The GM's eye hops between columns in a mixed order the author intended linearly. That's the gap.

So my answer to "replace or supplement the 3-column layout": **replace the center, keep the edges.** The Narrative column becomes the linear script. The Actors column dissolves — NPC *lines* become spoken-blocks in the script, NPC *detail/reaction material* becomes branch-boxes where they fire. The Action column's controls (checks, findable reveals, enemy deploy, exits) move inline to the script position where they matter. The page becomes: **left sidebar (scene nav) · center script column · slim right rail (live widgets + persistent controls)**. That matches the console's structure while keeping the app's genuine wins (deploy buttons, reveal toggles) attached to the script instead of stranded in a side pane.

---

### Q1 — Visual taxonomy: schema gets one new optional field; the compiler is where the taxonomy is authored

**Pure rendering-layer color rules are insufficient, and the reason is data loss, not styling.** `moduleCompiler.ts` already destroyed the two things the console's taxonomy depends on: (1) *order* — markdown is linear, `SceneNode` buckets are not; (2) *kind* — "alert" vs "note" vs "spoken" is authorial intent that cannot be reliably guessed at render time. You can't recover either from the current schema. So:

- Add **one optional field** to the `SceneNode` schema in `src/types/campaign.ts`: `blocks?: SceneBlock[]`, a discriminated union. This is additive and non-breaking — every existing module renders unchanged through the current bucket path; modules with `blocks` render as the script. All six console classes map to a block type, 1:1:

| Console class | Proposed `SceneBlock` type | Live Play rendering |
|---|---|---|
| `.read-aloud` | `{ type: 'readAloud', text }` | existing blue left-border + deep navy bg, serif italic, spoken-cold |
| `.gm-note` | `{ type: 'gmNote', text }` | dark surface, maroon border, `[GM:]` tag — current `gmNotes` copy, restyled |
| `.gm-alert` | `{ type: 'gmAlert', text }` | red-tinted, "check this" — the **only genuinely new block kind**; needs an authoring marker because no render heuristic can see it |
| `.spoken-block` | `{ type: 'spoken', speaker, lines }` | amber tint, gold `SPEAKER:` — pulls an NPC's `line` out of the collapsed Actors card and into the script where it fires |
| `.branch-box` | `{ type: 'branch', header, branches: [{ when, then }] }` | bordered block, header names the branch — see Q4 |
| `.scene-exit` | renders from **existing** `exits` + `targetSceneId` | sticky footer per scene; the targetSceneId work wired tonight already supplies the jump link |

- **`moduleCompiler.ts` is the correct place for the taxonomy**, which keeps Q6 intact. New markdown conventions (an alert callout, a bold-speaker prefix that makes a quote a `spoken` block, a fenced marker for branches) get compiled *into* `blocks` in order. The markdown already has the order and the speaker names; the compiler just stops throwing them away.

**Tradeoff, named:** this is the biggest single piece of work in the proposal — a schema addition plus a compiler output mode, versus a pure render pass that takes an afternoon. The render-only alternative is real but delivers the *colors* without the *script* — and the script is the thing the GM called perfect. Do the blocks. One further point in its favor: it inherently upgrades *every future module* in the markdown pipeline, not just Live Play's rendering.

---

### Q2 — The sidebar: adopt it, fold the subway-map into it

Yes — a persistent left sidebar replaces the horizontal strip. But Live Play runs **inside a GMDashboard tab**, not as a console-style full page, so the sidebar is not the console's whole-page nav; it's a within-tab rail, which changes two things:

1. **It must collapse** to an icon rail on narrow/embedded widths, or it steals the center column the script needs. The console could afford an always-open sidebar; a tab cannot. This is the real cost of the port, and it's the tradeoff to pay: collapse state is a couple of lines of Tailwind, and the win (never losing your place, scroll-spy) is the win that made the console work.
2. **Scroll-spy ports one level deeper.** The console highlighted scene entries as the GM scrolled a full linear page; LivePlay renders one scene at a time. The faithful version: the sidebar lists **all scenes** (scroll-jump, replacing the subway) and, for the *current* scene, an **expandable block list** (read-aloud 1 · Ylva spoken · Tempo alert · branch) with scroll-spy against the long scenes tonight's module actually produced.

The subway-map's only unique value is module-shape at a glance. Keep *that* as a collapsed "MAP" line in the sidebar header (compact numbered dots, click-to-jump), and drop the strip itself. Don't keep both as equal UI; the subway was, per the brief, never persistent anyway — it was the feature being replaced.

---

### Q3 — Interactive widgets: one roll engine, two affordances; module rollers become data

The console's dice difference wasn't the widget — it was that the widget was **always reachable**. That's the property to keep.

- **One roll engine** (the app currently has none on the GM side). It must be d20-only and apply the difficulty **modifier to the player's TN** — FROGS — never display a GM-set target number.
- **The generic d20 lives in the right rail**, always visible, matching the console's "regardless of scroll" property. Mid-session ad-hoc rolls are exactly what a GM reaches for this for, and routing them through SceneChecks would make him hunt for a check block to roll a dice he wants right now.
- **`SceneCheck` blocks render the second affordance**: "Roll this check," which fires the same engine pre-configured with the check's modifier. Not a second die — one engine, a persistent face and a contextual face.
- **The module-specific roller becomes data, not a component per module.** Tonight's Zone-3-Tempo widget was hand-built for `FIRE_B_SESSION_RUNSHEET.html`; the scalable version is a module-level definition — `{ name: "Zone 3 Tempo", tiers: [Frozen, Dragging, In Step, Quickened, Unmoored] }` — authored in the module's markdown frontmatter and compiled by `moduleCompiler` into a generic rail widget that rolls d20 and prints the tier. That converts "one-off artifact per module" into the thing the brief actually wants. **Tradeoff:** a hand-built widget is smarter than this generic tier-mapper (it could carry bespoke logic tonight's module didn't need); the data-driven version is the difference between a feature and a pile of one-offs. Take the data-driven one; that's the entire point of the brief.

---

### Q4 — Branch-box: build the flat version now, defer the grammar

The `SceneNpc.reactions?` field already exists but has no way to express "if X, NPC says Y; if Z, NPC says W." The console proved this pattern with **Ylva's four branches and the Alfonso/Jasper callouts — tonight on the table**. A Live Play upgrade that can't represent the exact proof-case text is under-delivering on the goal.

- Add `branch` to the `SceneBlock` union (free-standing decision points, no NPC required, which covers Alfonso/Jasper-style beats).
- Upgrade `reactions?` so an NPC's reaction branches render as branch-boxes in-script instead of a flat list inside a collapsed Actor card.

**Worth building now, but only the flat form:** `{ header, branches: [{ when, then }] }`. That covers tonight's shape completely. **Deferred, by name:** nested/sequential branch grammars and reaction trees composed of multiple NPC turns — authoring complexity with no demonstrated table need yet. The tradeoff of building flat: a later schema evolution when nesting arrives; the tradeoff of deferring entirely: the feature that was tonight's centerpiece is a hole in v1. Flat now is the right call.

---

### Q5 — Stat cards: don't reuse `CompanionCard`, extract its shell

`CompanionCard.tsx` works because its *actions* are player-actions (spend FP, use an ability, track uses). Reusing it in GM Live Play leaks player affordances into the GM view — the GM should not see "Use [ability]" buttons on an enemy. But its *presentation* (header, boxed monospace stats, progress bars) is precisely the `.stat-card` DNA.

So: **extract a presentational `StatCard` shell** (header + boxed stat rows + progress bars + footer slot), have `CompanionCard` refactor to consume it, and build a **GM-side variant** for Live Play: enemy/NPC stat blocks with HP bars, phase-transition text (tonight's 3-phase troll card), and deploy/advance controls. The GM needs to see phase data and transitions the players don't — that's the whole reason a variant is justified.

**Tradeoff:** refactoring a component shipped *tonight* risks touching working player-side behavior. Mitigate by keeping the extraction purely presentational (move markup, move zero logic) and guarding it with the per-combat/per-adventure reset behavior already in `CompanionCard`. Small risk, paying the abstraction cost once — versus building a parallel stat-card with no shared shell, ensuring the two drift apart across every future campaign. Pay the extraction.

---

### Q6 — What stays: the markdown pipeline is the load-bearing wall

I fully agree the compiler pipeline is the right direction, and I'm not flagging an exception. It's worth stating *why* it makes the rest of this proposal cheap rather than expensive: **everything above is designed so `moduleCompiler.ts` is the only authoring-side surface.** The taxonomy, alert markers, speaker detection, branch grammar, and module-roller frontmatter all enter through markdown conventions the compiler emits. GMs keep writing `FIRE_B_module.md`; the app keeps rendering whatever the compiler produces. The only scenario where I'd reconsider is if a future measure shows GMs needing per-module interactivity beyond the tier-roller (bespoke graphs, bespoke state machines) — and even then the right answer is richer compiler conventions, never per-module React. The pipeline is the feature; Live Play is just its renderer.

---

### Build order (if this lands)

1. **Day-one, zero schema:** restyle current `readAloud`/`gmNotes`/bullets by kind (note → maroon + `[GM:]`; spoken NPC lines pulled from Actors to script) and the sticky scene-exit footer from existing `exits`/`targetSceneId`.
2. **The big lift:** `blocks` union + compiler emission + convert `FIRE_B_module.md` to the new conventions — proves taxonomy *and* ordered script on the exact module that earned the verdict.
3. **Sidebar:** scene list + expandable block scroll-spy + collapsed subway map; collapsible rail.
4. **Branch blocks + structured reactions** (flat form).
5. **`StatCard` shell extraction + GM enemy variant.**
6. **Roll engine + rail d20 + data-driven module roller.**

### Where I explicitly pushed back, restated

- The 3-column layout should **not** be "supplemented" — its bucketing *is* the disease (Q1).
- `CompanionCard` should **not** be reused in Live Play — its shell should be extracted (Q5).
- The subway-map should be **folded into the sidebar**, not kept alongside it (Q2).
- The markdown pipeline **should** stay as-is, and that's load-bearing for everything above, not incidental (Q6).

========================================================================================
## opencode/muse-spark-1.2-contributor-free   [ERROR, 12s]

*(no usable answer: ERROR — [91m[1mError: [0mUnexpected error, check log file at C:\Users\fbrown\.local\share\opencode\log\2026-09-08T205753.log for more details

Failed to run the query 'PRAGMA journal_mode = WAL')*

========================================================================================
## opencode/mimo-v2.5-free   [OK, 244s]

I need to read the required onboarding docs and the files referenced in the brief before producing the design proposal.
Now let me read the skyrim-codex files referenced in the brief.
Let me check for the CompanionRoster and confirm no GM-side dice roller exists.
Let me check the companion types to understand the existing data model.
I've read all the source files. Here is the design proposal.

---

## Design Proposal: HTML Console Principles → GM App Live Play

### 1. Visual Taxonomy — Rendering-Layer Change, Not Schema Rewrite

**The short answer:** this is a rendering-layer change, with two small schema additions.

The existing `SceneNode` schema already holds the right data — `readAloud: string[]`, `gmNotes: string[]`, `bullets: string[]`, `npcs: SceneNpc[]` — but `LivePlay.tsx:131-147` renders them all in a single column with minimal visual differentiation. The read-aloud block gets a blue left border (line 134), GM notes get a bold `GM:` label (line 140), and bullets are just an unordered list (line 143). Everything else is visually flat.

The HTML console proves that six distinct block types earn their keep at the table: read-aloud, gm-note, gm-alert, spoken-block, branch-box, and stat-card. These map cleanly onto what the schema already contains — the problem is rendering, not data.

**What to do:**

- **Read-aloud** → already `readAloud: string[]`. Render with the console's deep-navy bg, blue left border, serif italic, and the `>> READ ALOUD` tag. This is the closest existing match — `LivePlay.tsx:134` already has `border-blue-500 bg-blue-500/5`, just needs the font-serif, italic, and tag styling from the HTML console's `.read-aloud` class.

- **GM notes** → already `gmNotes: string[]`. Two rendering sub-types needed, distinguished by a new optional field on individual notes. Currently `gmNotes` is a flat `string[]`. Add an optional `gmNotesTyped` field (or a lightweight wrapper): `{ text: string; severity?: 'note' | 'alert' }[]`. When `severity === 'alert'`, render the red-tinted variant (`.gm-alert`) with the danger border — the console's visual scream for "check this mechanic." The flat `gmNotes` array stays for backward compatibility; `gmNotesTyped` is an opt-in richer rendering path that the module compiler populates when it encounters `>> GM ALERT:` or similar markers.

  **Concrete schema change in `campaign.ts`:**
  ```
  // Add alongside existing gmNotes:
  gmNotesTyped?: Array<{ text: string; severity: 'note' | 'alert' }>;
  ```

- **Spoken NPC lines** → already `npcs[].line`. The console's `.spoken-block` with its amber-tinted bg, gold `SPEAKER:` label, and serif dialogue font is a pure rendering upgrade. `LivePlay.tsx:164` currently shows NPC lines as plain italic in a collapsible div. Render them in the amber/gold spoken-block style instead, with the NPC's name as the speaker label.

- **Branch-boxes** → this is the one gap. The console uses `.branch-box` for two things: reaction trees (Ylva's 4 responses to Saijah) and special dialogue callouts (Alfonso's theological duel, the Jasper reveal). The current `SceneNpc` type has `reactions?: NpcReaction[]` where `NpcReaction = { action: string; response: string }` — this is a flat list, not a conditional tree. See section 4 below for the schema question.

- **Stat-cards** → enemy stat blocks currently live in `src/data/enemies.ts` as `EnemyTemplate[]` and are shown as name badges in `LivePlay.tsx:229-231`, with the full block only visible after deploying to combat. The HTML console renders stat-cards inline (the frost troll's 3-phase card, the 5 anchors card, Gaelen/Jasper cards). This is a rendering upgrade: pull the `EnemyTemplate` data into an inline stat-card component in the Narrative column (or a new fourth column), not just a badge + deploy button.

- **Bullets** → the catch-all for unrecognized prose (`moduleCompiler.ts:222`). Keep them as-is but style them more deliberately — they're the "everything else" bucket and shouldn't try to be anything fancier.

**What NOT to change in the schema:** `readAloud` stays `string[]` (array of paragraphs). `bullets` stays `string[]`. `findables` stays as-is. The markdown-first pipeline (`moduleCompiler.ts`) is untouched except for one addition: recognizing `>> GM ALERT:` as a severity marker for gmNotesTyped.

---

### 2. The Sidebar — Yes, Adopt It; Drop the Subway Map

**Recommendation:** replace the horizontal subway-map strip (`LivePlay.tsx:101-118`) with a persistent vertical sidebar. The subway map has three concrete problems the console solved:

1. **It doesn't scale.** At 6+ scenes, the horizontal scrollArea becomes a scroll-to-find problem. The console's vertical sidebar with two-line entries (scene number + title, one-line grey summary) shows all scenes at once and is always visible.

2. **It has no scroll-spy.** The console highlights the active scene as the GM scrolls (`FIRE_B_SESSION_RUNSHEET.html:1099-1125`). The subway map highlights only by click — it can't tell the GM which scene they're currently reading.

3. **It can't hold widgets.** The console's sidebar holds the d20 roller and Tempo roller at the bottom, always visible. The subway map is just navigation — there's no room for interactive tools.

**Implementation:** extract a `LivePlaySidebar` component from the scene-nav portion of `LivePlay.tsx`. The sidebar sits to the left of the main content (like the console's `#sidebar`), fixed position, with:
- Scene nav entries (two-line each: number + title, subtitle/summary below in muted text)
- Scroll-spy active highlighting (IntersectionObserver on scene sections)
- Quick tools widget at the bottom (see section 3)
- A module picker at the top (move the `<select>` from line 86 into the sidebar header)

The existing `live` tab in `GMDashboard.tsx:78` stays as the tab trigger — the sidebar is internal to the LivePlay view, not a separate tab.

**Tradeoff:** the sidebar takes horizontal space (280px, matching the console). On smaller screens this compresses the 3-column scene layout. Mitigation: collapse the sidebar to a hamburger on `< 1024px` viewport width, or slide it over the content.

---

### 3. Interactive Widgets — Sidebar-Persistent, Not Inline

**The d20 roller** and **the module-specific difficulty-table roller** both earned their place. The question is where they live.

**Recommendation:** persistent sidebar widget, matching the console's `.sidebar-widget` pattern. Two buttons: "Roll d20" and a module-specific roller whose label and lookup table are set per-module (not hardcoded to "Zone 3 Tempo").

**Why sidebar-persistent, not integrated into the check flow:** the checks in `SceneCheck` are authored ahead of time — they're pre-declared difficulties the GM knows about. The d20 roller is for *ad-hoc* rolls the table calls for mid-scene: "I'm checking Perception," "How far did that arrow go?" These aren't in the runsheet. The module-specific roller (Tempo, or any future table) is for recurring rolls tied to the module's mechanics. Both need to be one click away at all times, not buried behind a "click this check badge to roll" interaction.

**Schema change needed:** `CampaignModule` (`campaign.ts:182-189`) needs a new optional field for the module-specific roller configuration:
```
moduleRoller?: {
  label: string;        // e.g. "Zone 3 Tempo"
  table: Array<{ min: number; max: number; result: string }>;
}
```
The markdown compiler (`moduleCompiler.ts`) would parse a new marker like `>> ROLLER: Zone 3 Tempo` followed by table rows. The d20 roller needs no schema change — it's always the same.

**Tradeoff:** if the sidebar is collapsed (mobile), the rollers are hidden. Alternative: put them in a floating action button. But the sidebar is the simpler, more consistent choice — the console proved it works there.

---

### 4. Branch-Box / Reaction-Tree Pattern — Build Now, But Limited

**The current state:** `SceneNpc.reactions` is `NpcReaction[]` where each reaction is `{ action: string; response: string }` — a flat list of "if X happens, NPC says Y." This covers simple reactions but not the console's richer pattern: four named branches with different conditions, each with its own NPC response *and* a GM stop prompt.

The console's branch-boxes do three things the current schema doesn't:
1. A **condition/label** for each branch ("If Saijah admits the terror", "If Saijah pushes back")
2. Each branch contains a **spoken-block** (NPC response) *and* optional **gm-note** (GM stop prompt)
3. They're **visually grouped** as an accordion-style container

**Recommendation:** add a `branches` field to `SceneNpc`:
```
branches?: Array<{
  id: string;
  condition: string;      // e.g. "If Saijah admits the terror"
  response: string;       // NPC spoken line
  gmPrompt?: string;      // "GM STOP: Turn to Saijah's player..."
}>;
```

This is a new field alongside the existing `line` and `reactions`. The `reactions` flat list stays for simple cases. `branches` is for conditional dialogue trees. The compiler would parse a new markdown pattern:
```
BRANCH: If Saijah admits the terror
**YLVA:** "He doesn't leave..."
GM STOP: Turn to Saijah's player...
```

**Why build now rather than defer:** the Fire B module already uses this pattern heavily (Ylva's 4 branches in Scene 21, the Alfonso theological duel, the Jasper reveal in Scene 22). Every new module will use it. Deferring means the next module authoring session still can't represent this in-app, and the GM is back to the HTML console for the parts that matter most.

**Tradeoff:** the `branches` field adds complexity to the `SceneNpc` type and the compiler. The alternative is to represent branches as separate `SceneNpc` entries with synthetic names (e.g., "Ylva (Branch 1)"). That's hacky and loses the visual grouping. The schema addition is cleaner and matches what the data actually is.

---

### 5. Companion/Stat-Card Reuse — GM Gets Its Own Variant

**`CompanionCard.tsx`** is player-facing: it shows HP/FP with +/- controls, abilities with "Use" buttons that spend resources, and reset buttons. This is the right *pattern* (interactive stat card with actionable controls) but the wrong *content* for GM Live Play.

**The GM needs to see:**
- Enemy HP bars (current/max, clickable to adjust) — same as CompanionCard
- Phase-transition text (the frost troll's 3-bar structure: what changes at each threshold)
- Special rules (villain actions, fire vulnerability, targeting tables)
- Terrain rules for the scene

**The GM does NOT need:**
- Ability "Use" buttons (the GM doesn't play enemies the same way)
- FP tracking (enemies don't spend FP the way player companions do)
- Equipment lists (enemies have attacks, not gear inventories)

**Recommendation:** create a `GmStatCard` component that reuses the CompanionCard's *layout pattern* (header with name/tier, resource bars with +/-, expandable sections) but with GM-specific content:
- HP bar with phase-transition markers (colored segments showing the 300/600/900 thresholds)
- A `statRows` prop for the stat grid (Might/Agility/Magic/Guile)
- A `specialRules` prop for the text callouts (villain action, fire vuln, etc.)
- A `terrainRules` prop for the scene-specific environment text

This would be a new component in `src/components/gm/play/` (e.g., `GmStatCard.tsx`), not a modification of the player-side `CompanionCard.tsx`. The two share CSS class patterns (the shadcn Card, Badge, Button components) but diverge in functionality.

**Data source:** the `EnemyTemplate` type in `src/data/enemies.ts` needs to be extended with optional `phases` (array of `{ name: string; hpThreshold: number; description: string }`) and `specialRules: string[]`. The markdown compiler would parse stat-card blocks from the runsheet (the console's `.stat-card` pattern already has clear visual markers: `FROST TROLL, DAGON-WARPED | TL 3 BOSS | Expert Tier | AP ~12`).

---

### 6. What NOT to Change

- **Markdown-first authoring pipeline** (`moduleCompiler.ts`). The GM-CAMPAIGN-SUITE.md is explicit: "markdown-first authoring replaces the python→RTF pipeline" and "the prep tool authors in markdown (the Forge)." The rendering layer changes; the authoring layer stays. Any proposal requiring GMs to hand-author React/HTML per module is wrong.

- **The `SceneNode` core shape.** The additions above (`gmNotesTyped`, `branches`, module roller config) are opt-in extensions, not replacements. The flat arrays that already work stay flat. The schema version bumps to 2 with a migration that populates defaults for the new optional fields.

- **The 3-column layout structure.** The Narrative/Actors/Action columns in `LivePlay.tsx:129` stay. The HTML console's flat single-column scroll works because it's one file offline; the app's 3-column layout works because it surfaces different *kinds* of information simultaneously. The visual taxonomy upgrades happen *within* each column, not by collapsing columns.

- **The combat tracker integration.** `onDeployEncounter` and the `handleDeployEncounter` flow in `GMDashboard.tsx:42-52` stay exactly as-is. The stat-card renders inline in Live Play for quick reference, but deploying to the full combat tracker remains the action for complex fights.

---

### Summary of Concrete Changes

| File | Change |
|---|---|
| `src/types/campaign.ts` | Add `gmNotesTyped?`, `branches?` to `SceneNpc`, `moduleRoller?` to `CampaignModule`, `phases?` and `specialRules?` to `EnemyTemplate` (in data/). Bump schema version. |
| `src/utils/moduleCompiler.ts` | Add parsers for `>> GM ALERT:`, `BRANCH:`, `>> ROLLER:`, and stat-card blocks. One new regex each, same pattern as existing markers. |
| `src/components/gm/play/LivePlay.tsx` | Replace subway-map with sidebar. Add scroll-spy. Render gmNotes with severity styling. Render NPC lines as spoken-blocks. Render branches as branch-boxes. Add inline stat-cards from enemy data. |
| `src/components/gm/play/LivePlaySidebar.tsx` | New component: scene nav, scroll-spy, roller widgets. |
| `src/components/gm/play/GmStatCard.tsx` | New component: enemy stat-card with phase bars, special rules, terrain. |
| `src/components/gm/play/BlockRenderers.tsx` | New component: renders read-aloud, gm-note, gm-alert, spoken-block, branch-box with the console's visual taxonomy. |
| `HTML_CONSOLE_DESIGN_SYSTEM.md` | Already exists as the reference — no changes needed. |

The total schema surface change is three new optional fields and one new optional array. The rendering changes are the bulk of the work, which is exactly right: the data was already there, the visual language just wasn't.

========================================================================================
## opencode/ling-3.0-flash-fin-free   [OK, 66s]

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