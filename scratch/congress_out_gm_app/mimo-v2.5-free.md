# opencode/mimo-v2.5-free   [OK, 244s, 14569 chars]

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
