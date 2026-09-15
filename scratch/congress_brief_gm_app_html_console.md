# BRIEF: Bring the HTML-console design principles into the real GM app's Live Play view

## Context — what just happened at the table

Tonight's session was run off a single-file HTML "console" a Gemini session built by hand for
this specific module (`Toryggs legacy/Adventure modules/choice gate 3/FIRE_B_SESSION_RUNSHEET.html`).
The GM's own verdict, verbatim: *"genuinely this html gemini made is the smoothest a game has ever
run it was perfect."* He wants that quality made the actual behavior of the GM app's Live Play
module-runner — not a one-off artifact per module, a real feature.

There is also a companion spec the same session wrote up:
`Toryggs legacy/HTML_CONSOLE_DESIGN_SYSTEM.md` — a reusable template/philosophy doc for this
console format. Read it for the full color palette, component taxonomy, and code.

## What actually made the HTML console work (read directly off the file, not inferred)

1. **Sidebar scene nav** with two-line entries (scene number + title, then a one-line grey
   summary of what happens in it) and scroll-spy active-highlighting as the GM scrolls.
2. **Color-coded block taxonomy**, strict and consistent throughout — a GM never has to parse
   *what kind of text this is*, only read it:
   - `.read-aloud` — deep navy bg, blue left border, serif italic — spoken cold to the table.
   - `.gm-note` — dark surface bg, maroon left border, `[GM:]` tag — adjudication/background,
     explicitly kept OUT of the read-aloud prose.
   - `.gm-alert` — red-tinted variant of the above, for hard mechanical rules (terrain, Tempo
     tables) that need to visually scream "check this."
   - `.spoken-block` — amber-tinted, gold `SPEAKER:` label, serif dialogue — an NPC line meant
     to be read aloud in character, visually distinct from both GM notes and prose read-aloud.
   - `.branch-box` — a bordered accordion-style block with a header naming the branch/condition
     and a body holding what happens in it — used for reaction branches (Ylva's 4 responses to
     Saijah) AND for named narrative beats (Alfonso's theological duel, the Jasper reveal).
   - `.stat-card` / `.stations-grid` — monospace boxed stat blocks (the frost troll's 3-phase
     card, Gaelen/Jasper) and a responsive grid of small "station cards" for quick per-character
     beats (six PCs/NPCs each get one card in the strategy scene, all visible at once, none
     requiring a scroll to find).
   - `.scene-exit` — a fixed footer bar per scene, name of the transition + a clickable link
     that jumps the GM straight to the next scene's anchor.
3. **Two live interactive widgets in the sidebar**, always visible regardless of scroll
   position: a generic d20 roller, and a module-specific roller (this module: "Zone 3 Tempo,"
   which rolls d20 and immediately prints which named tier it lands in — Frozen/Dragging/In
   Step/Quickened/Unmoored — sparing the GM a lookup mid-fight).
4. **Everything on one page, one file, works offline, zero load time.** The GM never left the
   page, never waited on a network round-trip, never lost his place.

## What the GM app already has, for real, right now — check this before proposing anything

The GM app is `skyrim-codex` (separate repo, `C:\Users\fbrown\Projects\skyrim-codex`), a
React + TypeScript + Vite + Tailwind + shadcn/ui app. Read these files directly before
drafting anything — do not assume, the actual shapes matter:

- `src/components/gm/play/LivePlay.tsx` — the CURRENT module-runner. It renders one
  `SceneNode` at a time from a flat array (`scenes[sceneIndex]`), with prev/next nav and a
  horizontal "subway-map" scene-picker strip at the top (not a persistent sidebar). Below that,
  a 3-column layout: Narrative (read-aloud + GM notes + bullets, all undifferentiated visually
  beyond a blue left-border on the read-aloud block and a bold "GM:" label — much flatter than
  the HTML console's taxonomy), Actors (NPC beats, click to expand/collapse), Action (checks,
  findables with reveal/resolve toggles, an ENEMIES list with a Deploy Encounter button, exits).
  Exits click through via `targetSceneId` (this was just wired up tonight — previously exits
  always just advanced `sceneIndex + 1` regardless of what they said).
- `src/types/campaign.ts` — the `SceneNode` schema: `readAloud: string[]`, `gmNotes: string[]`,
  `bullets: string[]`, `findables: Findable[]`, `npcs: SceneNpc[]` (each with a `line?` and
  `reactions?`), `checks: SceneCheck[]`, `enemies: string[]`, `exits: ExitLink[]`.
- `src/utils/moduleCompiler.ts` — parses a GM's markdown runsheet into `SceneNode[]` (this is
  how content like `FIRE_B_module.md` gets into the app at all — a markdown-first authoring
  pipeline, not hand-built React per module).
- `src/components/character/CompanionCard.tsx` and `CompanionRoster.tsx` (built earlier
  tonight) — an ACTIONABLE card pattern already exists in this codebase: HP/FP with +/-
  controls, a flat list of abilities each with a cost, a "Use" button that spends the cost and
  tracks remaining uses, per-combat/per-adventure reset buttons. This is the closest existing
  precedent in the app to the HTML console's `.stat-card`/interactive-widget spirit — it's on
  the PLAYER side of the app, not GM Live Play, but the pattern (and the code) already exists
  and works.
- `src/components/gm/GMDashboard.tsx` — the 5-tab GM shell (Hub/Forge/LivePlay/Combat/
  Compendium). Live Play is one tab among several, not a full-page takeover the way the HTML
  console was.
- No dice roller exists anywhere in the GM-facing side of the app currently (confirm this by
  grepping — don't assume). No "GM alert" block distinct from a plain GM note. No branch-box
  pattern for reaction trees. No scene-exit footer with a jump-link. No always-visible sidebar
  nav during Live Play (it's a horizontal strip instead).

## The actual ask

Design direction, not code, for closing the gap between what Live Play currently is and what
the HTML console proved works this well at an actual table. Concretely:

1. **Visual taxonomy** — should Live Play's Narrative/Actors/Action 3-column layout be replaced
   or supplemented by the HTML console's color-coded block system (read-aloud / GM-note /
   GM-alert / spoken-NPC-block / branch-box / stat-card)? If kept, how does the existing flat
   `readAloud`/`gmNotes`/`bullets` string-array schema map onto that richer taxonomy without a
   full data-model rewrite — is this a rendering-layer change (interpret existing strings with
   smarter formatting/color rules) or does the schema itself need new fields (e.g. a `gmAlert`
   note-type, a `spokenLines` NPC array distinct from `bullets`)?
2. **The sidebar** — worth adopting a persistent scene-nav sidebar (like the console) over the
   current horizontal subway-map strip? What happens to the subway-map (drop it, keep both,
   fold one into the other)?
3. **Interactive widgets** — a d20 roller and a module-specific difficulty-table roller (the
   console's Zone-3-Tempo pattern) clearly earned their keep at the table. Where do these live
   in the app's actual architecture — a persistent sidebar widget like the console, or
   integrated into the check/roll flow that already exists in `SceneCheck`?
4. **Branch-box / reaction-tree pattern** — Live Play currently has no way to represent
   "if the PC does X, NPC says Y; if Z, NPC says W" the way the console's `.branch-box` blocks
   did (Ylva's four reaction branches, the Alfonso/Jasper special-dialogue callouts). Is this a
   new `SceneNode` field, a new sub-type of NPC reaction, or something else — and is it worth
   building now or specifically deferred (name the tradeoff either way)?
5. **Companion/stat-card reuse** — `CompanionCard.tsx` already does an actionable stat-card
   well on the player side. Should GM Live Play's enemy/NPC stat display reuse or adapt that
   same component, or does the GM side need its own variant (GM needs to see enemy HP bars/
   phase-transition text the players don't, for instance)?
6. **What NOT to change** — the markdown-first authoring pipeline (`moduleCompiler.ts`) is a
   deliberate, already-built design decision (see `docs/GM-CAMPAIGN-SUITE.md` in skyrim-codex
   if you want the reasoning). Any proposal that would require GMs to hand-author React/HTML
   per module instead of markdown is almost certainly the wrong direction — flag if you think
   otherwise and say exactly why, but the default assumption should be: the markdown authoring
   layer stays, only the RENDERING of that data changes.

## Constraints on your answer

- This is a design-direction proposal, not implementation. No code required, though concrete
  component/file-level suggestions (rename X, split Y into two components, add field Z to the
  schema) are exactly what's wanted over abstract advice.
- Cite the actual files above by name when your proposal touches them. Don't invent file names
  or component names that don't exist in what's described here.
- Name real tradeoffs. "Just do both" is not a design decision.
- If you disagree with something stated as given above (e.g. you think the subway-map strip is
  actually better than a sidebar, or the markdown pipeline SHOULD change), say so explicitly
  and argue it — don't silently comply, and don't silently ignore the brief either.

Written answer only. Do NOT edit files, do NOT make tool calls, do NOT ask questions — produce
your complete design/answer in one response.
