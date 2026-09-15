# opencode/big-pickle   [OK, 195s, 12000 chars]

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
