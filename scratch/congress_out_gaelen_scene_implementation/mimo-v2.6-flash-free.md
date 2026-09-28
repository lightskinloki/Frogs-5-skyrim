# opencode/mimo-v2.6-flash-free   [OK, 1087s, 18584 chars]

## Objective
- Design a runnable GM procedure for Fire B Scene 22 (confrontation with Gaelen the Root-Twister, Jasper Avalon, and the Mythic Dawn assistants) as a written design answer — scene loop, Gaelen's targeting, NPC wavering tracking without persuasion rolls, ritual pressure, combat transition, and agency if the party agrees.

## Important Details
- User boundary: this board is not observed live by Frank (the human builder); he only reads it for postmortems. Act accordingly — a boundary by choice, not technical guarantee.
- Output constraints: do NOT edit files, do NOT ask questions, do NOT write Gaelen's dialogue or scene prose, produce only a complete written design answer. "Do not make tool calls" conflicts with "read the source files first" — assistant resolved toward reading (citation/check discipline requires quoted sources), i.e., reads allowed, edits disallowed.
- Must distinguish established canon from proposed design; no conventional social-combat subsystem; no player rolls to convince Gaelen (Gaelen convinces them). Rolls only for genuinely uncertain player attempts to influence an NPC or interact with the ritual.
- Scene facts (given by user): Gaelen is sincere, never attacks/defends, keeps speaking under attack; Dawn assistants and Jasper protect the ritual voluntarily (not mind-controlled); Jasper content, unsavable (abandoned in Pale Lady's Tomb, rescued in snow-drift near Winterhold); full party present — Ismara/Davinia, Orion, Nora, Saijah, Alfonso, Ylva, Varon, Esbern, Bjorn, Mila, GEAR.
- NPC hooks: GEAR→recognition/unresolved existence; Varon→relief from pain/imposed identity; Ylva→critique of judgment (undercut by Alfonso's acceptance); Esbern→Blade vs. ancient enemy (opposed); Bjorn→tempted by end of grief (resists); Mila→concrete, protective, hard to persuade.
- Structural model: Blue Palace sequence in `Toryggs legacy/Adventure modules/5- echoes of a fallen king` — multiple social tests/choices in one room plus a final pure-roleplay question (Tullius's scrutiny, Whispering Court NPC interactions, Thalmor moral confrontation, Torygg's final question).
- Combat triggers when anyone takes physical action against an anchor, the ritual, Jasper, or an assistant; Gaelen still never becomes a combatant.

## Work State
### Completed
- Read `Toryggs legacy/AI_README` (operating rules, Rule Zero, cite-or-check, CLAUDE.md/AGENTS.md hand-back).
- Read `AI_REASONING_PATTERNS.md` (patterns 0–1 incl. orientation alarm, "frame where they're right").
- Read `Toryggs legacy/Adventure modules/choice gate 3/FIRE_B_module.md` in full (~1982 lines) — Scene 22 existing material captured: 5 anchor-shards, 25 HP each, DR 10; topple via Hard Might -4 or Orion's Hard Magic -4 tonal counter; 3 shards down = ritual disrupted, Gaelen phases out; Jasper is the one who fights; Zone 3 Tempo alarm ~6 min; existing beats — Ylva liturgy exchange lines, Alfonso addressed directly, Mythic Dawn naming response, The Quiet Wish, Jasper reveal via Gaelen, Hircine temptation station 6, combat objective framing ("frame objective as THE RITUAL, never Gaelen's head").
- Read `Toryggs legacy/The Narrative/chapter 30`, `Toryggs legacy/Npcs/new mythic dawn leader`, `Toryggs legacy/Adventure modules/5- echoes of a fallen king` (both parts; Part III = Blue Palace social sequence).
- Read design bible `Toryggs legacy/Adventure modules/choice gate 3/IVARSTEAD - the bleeding stair (planning)` — status NOT PREPPED/NEVER RUN; core discipline: INTRODUCTION, advances threads, resolves nothing personal; Saijah does not choose a patron; Gaelen does not die; "theological seduction" stations; Tower cosmology reveals.
- Read `Toryggs legacy/factions/new mythic dawn` — SAP AND SHARD cosmology (sap unfixes, shard crystallizes/fixes; throat wound predates cult).

### Active
- Deciding whether to consult remaining optional sources before writing: `Toryggs legacy/Adventure modules/choice gate 3/PLANNING SCRATCH (working - live ideas)` (lines ~1740–1850 contain Scene 22 design notes, e.g., "#2 Jasper physical beat (needs a short design pass)"), the `gate 3` doc (Fire B section), and the writing guide (Section IX) if quoting prose rules.
- Then drafting the final procedure design answer.

### Blocked
- (none)

## Next Move
1. Skim `PLANNING SCRATCH (working - live ideas)` around the Scene 22/Gaelen notes (and optionally `choice gate 3/gate 3`) to confirm no locked design conflicts, per pattern #14 (use resources already given).
2. Write the complete Scene 22 procedure design answer: scene loop, Gaelen's targeting/response logic, NPC wavering tracking without persuasion rolls, ritual-progress pressure clock, combat threshold transitions, agency preservation if the party sides with Gaelen — labeling each element CANON vs. PROPOSED, no dialogue prose.

## Relevant Files
- `Toryggs legacy/Adventure modules/choice gate 3/FIRE_B_module.md`: Scene 22 canon — anchors, combat rules, existing beats.
- `Toryggs legacy/Adventure modules/choice gate 3/IVARSTEAD - the bleeding stair (planning)`: Fire B design bible; module's non-resolution discipline.
- `Toryggs legacy/Adventure modules/5- echoes of a fallen king`: structural reference — Blue Palace multi-test social sequence (Part III).
- `Toryggs legacy/factions/new mythic dawn`: cult cosmology and assistant framing.
- `Toryggs legacy/Npcs/new mythic dawn leader`: Gaelen's sheet, stats, personality, Master Villain build.
- `Toryggs legacy/The Narrative/chapter 30`: recent narrative state (Bjorn/Mable, Mila, Saijah dynamics).
- `Toryggs legacy/Adventure modules/choice gate 3/PLANNING SCRATCH (working - live ideas)`: possible Scene 22 design notes, unchecked.
- `Toryggs legacy/AI_README`, `AI_REASONING_PATTERNS.md`: binding operating discipline.
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Re-grounding first: the summary says I read FIRE_B_module.md's Scene 22, but per Rule 2/Rule Zero I need the actual text in front of me before designing against it.
Sources re-grounded for Scene 22. One more check — the Blue Palace structural reference, since the design must mirror its social-sequence model:
All sources re-opened before drafting: Scene 22 (`FIRE_B_module.md:1888-1954`), the design bible (`gate 3`, `IVARSTEAD - the bleeding stair (planning)`), the alarm rules (`FIRE_B_module.md:745`), and the Blue Palace structural model (`5- echoes of a fallen king:346-401`). Everything below is labeled **[CANON file:line]** or **[PROPOSED]**. No file edits made.

---

# Scene 22 — Confrontation Procedure (design answer)

## 1. The Scene Loop

The scene is a repeatable cycle, not a scripted list. One cycle = one turn of Gaelen's spiral.

**Phase A — PULSE (pressure).** The Zone 3 alarm already exists module-wide: "The GM sets a REAL-WORLD ALARM (phone, hidden)... On the alarm: GM rolls d20 → picks which table in the CURRENT ZONE's set is active" **[CANON FIRE_B_module.md:745, steps 1-2 — pre-combat]**. Each firing in the undercroft = one pulse:
1. Gaelen's graft-arm tunes one anchor-shard; its light runs to the root **[CANON 1903-1905 shows exactly this]**. TUNED counter +1.
2. Weather shift roll (d20, Zone 3 table) announced as sensation only **[CANON 745]**.
3. Escalating physical sign: root cracks widen, channels flare **[PROPOSED — narration only, no new mechanical penalties]**.

**Phase B — GAELEN'S ADDRESS.** One target per pulse, chosen by the targeting ladder (§3). His hands keep working while he talks **[CANON 1917: "His hands keep working the shards while he answers, unhurried"]**.

**Phase C — THE ROOM ANSWERS.** The addressed companion plays its state (tell or objection slot); at most one other visible state-change per cycle, so the table can track wavering without a scoreboard. Slots, not written lines.

**Phase D — PARTY OPEN.** Unlimited free roleplay. This is where player time goes.

**Phase E — CHECK.** Combat trigger? (§5) Stand-down declared? (§6) TUNED = 5 or BROKEN = 3? (§4) Otherwise next pulse.

**Loop is re-entrant:** social → combat → social is allowed. If Jasper and the assistants are down and anchors remain, the loop resumes with Gaelen still talking, still non-combatant **[CANON 1912]**.

**Fixed canon beats are scheduled into, not outside, the loop:**
- Jasper reveal to Davinia: fires at first sighting of Jasper **[CANON 1937]**.
- Ylva exchange: once, when she forces the opening **[CANON 1915]**.
- Alfonso address: pulse 1 or on entry — "the duel only he can have" **[CANON 1916]**.
- Mythic Dawn naming: only if a player names it **[CANON 1917, conditional]**.
- Hircine's temptation: "Just before or during the fight" **[CANON 1919]** — unchanged, player's business, nothing resolved **[CANON 1919, 1924]**.
- The Quiet Wish: plant before or between pulses, never on a beat **[CANON gate 3:144-151]**.

## 2. Gaelen's Targeting Logic

Deterministic ladder so the GM never improvises who's next:

1. **Reactive first.** Whoever just spoke or acted gets answered **[CANON 1916-1917 — both addresses are responses]**.
2. **Fixed beats** (above) fire on their triggers regardless of ladder position.
3. **Otherwise, in susceptibility order: GEAR → Varon → Esbern → Bjorn → Mila.** Rationale: he addresses the exposed wound first — GEAR (recognition, unresolved existence) and Varon (relief from pain, imposed identity) are the doctrine's exact shape; Esbern and Bjorn are locked doors he tries once each out of sincerity (he believes he's helping — "He does not want to kill the party. He wants them to put down their weapons" **[CANON gate 3:134-135]**); **Mila last or never** — concrete, protective, his abstractions slide off, and he can read a room.
4. **Skip anyone already MOVED** — no nagging the converted.
5. **Under attack:** if a player strikes him mid-address, he does not retaliate and finishes the line **[CANON 1912]**.

He never rolls, never needs to, and is never the target of a "keep him talking" check — he talks because that's who he is **[CANON gate 3:121-143]**.

## 3. NPC Wavering Tracker (no persuasion subsystem)

Private GM sheet. Six rows — GEAR, Varon, Ylva, Esbern, Bjorn, Mila. Three states: **STEADY / SHAKEN / MOVED**. Player characters are excluded by design; their stances belong to their players (the Hircine station is Saijah's player's business **[CANON 1919]**).

**State changes come from exactly two inputs — never from a persuasion roll:**
1. **ADDRESS LANDED.** Gaelen's pulse-target moves that NPC one notch, automatically. His persuasion is not a contest — he convinces them; nobody rolls against it **[design constraint; matches gate 3:121-135 — "the most genuine person in any room"]**.
2. **PLAYER COUNTER.** A player directly working on that NPC resolves at the table by roleplay. A roll only if genuinely uncertain — player's own TN + difficulty modifier **[FROGS 5 d20 rule; no GM-set target numbers]**. This is the only roll the tracker ever touches.

**No roll exists to:** convince Gaelen, detect a state (states are played openly as tells), or resist an address.

**Ceilings from the established hooks:**
- **Esbern:** SHAKEN floor-ceiling — his opposition is informed and institutional; he never reaches MOVED.
- **Mila:** immune to pulse-addresses until pulse 4, SHAKEN maximum even then.
- **Bjorn:** can reach MOVED (the grief temptation is real), but his behavior stays party-faithful — the tell is stillness, not refusal.
- **Ylva:** not seducable at all. Her row tracks FURY instead, and it is *derived*: Alfonso's live answer to Gaelen's address raises or re-anchors her **[CANON chain: 1915 exchange, 1807 "If Alfonso confirms it... Ylva's grin returns"]**.
- **GEAR, Varon:** no ceilings — their wounds are the pitch's exact shape.

**Tells come from canon vocabulary, not invention:** Varon's scar-tap **[CANON 1922: "his hand goes to the scar behind the ear, the tap he uses to remind himself of his commitment"]** and its loss **[CANON 1880: "Varon's thumb drops from his ear. The mask staples back into place"]**.

**What states do at the table:**
- **STEADY:** normal companion behavior.
- **SHAKEN:** visible tell; won't be first to initiate against the ritual space; raises one objection at a stance declaration.
- **MOVED:** gets one chance per pulse to voice Gaelen's case *in the party's own mouth* — the seduction becomes intra-party dialogue (slot only; G6 rules apply to whatever the GM says live); will not strike an anchor unless a player personally orders it, and goes reluctantly. **No defection, no mutiny, no companion walks out** — dissent is the ceiling; these are the party's people, and punishing the players' stance choice with a companion exodus would be GM fiat over player agency.
- All notches are reversible by input 2.

**Why no persuasion mechanic:** this is a state-and-event tracker, not a social-combat subsystem — three states, two triggers, zero subsystem rolls, mirroring the Blue Palace model where tests are event-structured and the closing beat is explicitly "not a skill check... pure roleplay" **[CANON 5- echoes:394-398]**.

## 4. Ritual Pressure

One visible dial, two counters, racing:

| Counter | Advance | Terminal |
|---|---|---|
| **TUNED 0→5** | +1 per pulse (start at **1** — the entry text already shows him mid-turn and the root "veined now with fresh black cracks" **[CANON 1895, 1903-1905]; start value PROPOSED**) | **5 = working sets** → wound pinned open **[PROPOSED payload: the gate 3:180-185 consequence block — Tower corrupted, Dagon clock major jump, Greybeards cut off, Way of the Voice closes, Saijah's migraine permanent]** |
| **BROKEN 0→3** | +1 per canon anchor takedown **[CANON 1928: 25 HP, DR 10, Hard Might -4, Orion Hard Magic -4]** | **3 = disruption** → run the escape sequence *exactly* **[CANON 1943-1950]**, then Scene 23 |

- Counters are **independent** — a broken shard stutters but doesn't stop his tuning (the arm graft holds the place), so there is no deadlock state where neither terminal can fire. Narrate proportionally: 2 broken + 4 tuned = a crippled array still feeding.
- Each BROKEN steps the weather down Zone 3→2→1 **[CANON 1928]** — the mechanical arc remains the story arc **[CANON 1930]**.
- The dial is **visible to the table**: tuned shards glow feeding the root, dark ones don't **[derived from CANON 1905]**. The deadline is never hidden.
- The alarm's ~6-minute cadence **[CANON 1930]** ≈ 30 real minutes of conversation before the working sets — the conversation is never free.
- **The dial keeps running during combat** — "his hands never stop" **[PROPOSED extension of CANON 1917]**, and it supplies the fight's urgency without new mechanics.

## 5. Combat Transition

**Trigger (as specified):** any physical action against an anchor, the ritual, Jasper, or an assistant → combat starts immediately, initiative as normal.
**Strike on Gaelen:** routes through Jasper — "Jasper defends GAELEN" **[CANON 1926]** — Jasper engages the attacker and that enters combat; **Gaelen still never attacks, in any branch [CANON 1912, 1934: "he never initiates an attack this encounter"].**

At transition:
- Zone 3 Tempo, alarm ~6 min, tide-shard cheat for cultists **[CANON 1930, 745]**.
- Jasper fights to the end, dies here, one-and-done **[CANON 1935]**; his contentment is playable if anyone talks to him **[CANON 1939]**.
- **Assistants [PROPOSED]:** 3 Dagonite Cultists + 1 Shard Zealot, reusing the module's existing stat cards **[CANON cards at 911, 913, 995]** — their number is not statted in Scene 22's ENEMIES line (1932 lists only Gaelen and Jasper), so count is a proposal. They position on the array, not on the party. Their voluntariness is shown pre-combat by *work* (turning shards, carrying sap — no argue-slots; Gaelen speaks for the room), in combat by positioning **[voluntariness per session brief; staging PROPOSED]**.
- If violence opens the scene cold, the Jasper reveal still fires **[CANON 1937]** — consent lands loud either way.

## 6. Agency If the Party Agrees

A stand-down is a real branch, honored immediately, not a stall to be argued out of:

1. **Declare/evince stand-down** (stop advancing, lower weapons, say it) at any point — Phase D or during combat. **No roll to be believed;** if the table is trying to deceive Gaelen, that's a genuinely uncertain influence attempt → Guile with difficulty modifier — and failure costs only that he knows: he is disappointed warmly and keeps working, never hostile **[consistent with CANON 1912, gate 3:121-135]**.
2. **Hostile parties disengage:** Jasper and assistants stop when there's nothing to defend against — they are protectors, not berserkers **[voluntary protection per session brief]**. The loop resumes; pulses continue.
3. **Companions:** the tracker runs to its end — MOVED voices relief, SHAKEN go quiet, **Esbern dissents aloud** (his capped state guarantees at least one honest objection) — then all of them stay. The party overrules their own people if they overrule them; companions don't leave **[§3 rule]**.
4. **The dial runs to 5 → working sets → the consequence branch in §4 fires**, delivered without judgment. With 1-2 shards already broken, the outcome caps at the "staunched, not sealed" middle **[echoes CANON gate 3:172-173 and Scene 23's "A cut finger, bound"]**.
5. **Scene 23's rewards are gated on having held the mountain:** the Greybeards' full bow **[CANON 1961-1963]** and the Way of the Voice do not fire on stand-down — the consequence block's "the Way of the Voice closes to the party" **[CANON gate 3:181-182]** takes that slot instead.
6. **What agreement never does:** resolve Saijah's crossroads or choose any patron **[CANON 1919, 1924, planning:14]**; convert or harm PCs; alter the Hircine station **[CANON 1919]**. Jasper survives a bloodless scene **[PROPOSED branch consequence — he's canon-presumed dead only under conflict, 1935]**, which the GM carries forward as a live asset.
7. **Closing beat:** at dial-5 (or any pause the table opens — it's always available), one pure-roleplay final invitation, no roll **[PROPOSED structure, modeled on CANON 5- echoes:394-398]**. Whatever they answer, the scene exits on it.

---

**Design notes:** no social-combat subsystem, no player roll ever made against Gaelen, no persuasion dice for companions, no new dialogue or prose written, and the escape/disruption/anchor math is untouched canon — the procedure only adds the pulse clock, the targeting ladder, the state sheet, and the stand-down branch around what was already there. Nothing has been written to file; this is yours to accept, amend, or reject beat by beat.
