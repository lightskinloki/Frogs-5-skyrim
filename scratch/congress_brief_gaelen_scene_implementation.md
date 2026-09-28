# Design brief: implementing Gaelen's confrontation

We need design the playable procedure for Fire B Scene 22, the confrontation with Gaelen the Root-Twister, Jasper Avalon, and the Mythic Dawn assistants.

This is a tabletop RPG scene. The problem is implementation, not character invention. The GM and players already know the following:

- Gaelen is sincere, compassionate, and trying to save Skyrim. He is not deceiving the party, performing villainous cryptic rhetoric, or trying to win a formal debate.
- Gaelen does not attack or defend himself. He continues the ritual and continues speaking even if the party attacks him.
- The Dawn assistants and Jasper freely protect the ritual because they believe the Dawn is saving Skyrim. They are not mind-controlled servants and Gaelen does not own them.
- Jasper was abandoned in the Pale Lady's Tomb, rescued in a snow-drift in Winterhold, and later gave himself to the Dawn. The Dawn genuinely rescued him. He is content and cannot be 'saved' by the party.
- The party and all of its important NPC companions are present: Ismara/Davinia, Orion, Nora, Saijah, Alfonso, Ylva, Varon, Esbern, Bjorn, Mila, and GEAR.
- Gaelen's arguments expose real wounds. GEAR may be drawn toward recognition and an answer to his unresolved existence; Varon toward relief from his pain and imposed identity; Ylva toward Gaelen's critique of judgment, though Alfonso's acceptance of her undercuts it; Esbern remains opposed as a Blade facing an ancient enemy; Bjorn is tempted by an end to grief and future loss but resists; Mila is concrete, protective, and difficult to persuade.
- The scene should make the players seriously consider Gaelen's offer. It should also make them manage their own NPCs: some may waver, some may oppose Gaelen, some may try to protect the ritual, and the party may need to talk them down.
- The ritual continues visibly while Gaelen talks. The chamber contains multiple assistants who keep working while he speaks with different people.
- The intended shape is closer to the Blue Palace sequence in `Toryggs legacy/Adventure modules/5- echoes of a fallen king`: multiple different social tests and choices in one room, including a final pure-roleplay question, rather than a single persuasion roll against one NPC. Relevant structure includes Tullius's scrutiny, the Whispering Court's multiple NPC interactions, the Thalmor moral confrontation, and Torygg's final question.
- This should not become a conventional social-combat system where the players roll to convince Gaelen. Gaelen is trying to convince them. Player choices and roleplay should drive the scene. Rolls, if any, should only resolve a genuinely uncertain player attempt to influence an NPC or interact with the ritual; they must not replace the central decision.
- Combat begins when someone takes physical action against an anchor, the ritual, Jasper, an assistant, or otherwise crosses the agreed threshold. Gaelen still does not become a combatant.

Read the relevant source files in the project before answering, especially:

1. `Toryggs legacy/AI_README`
2. `AI_REASONING_PATTERNS.md`
3. `Toryggs legacy/Adventure modules/choice gate 3/FIRE_B_module.md` (especially Scene 22)
4. `Toryggs legacy/The Narrative/chapter 30`
5. `Toryggs legacy/Npcs/new mythic dawn leader`
6. `Toryggs legacy/Adventure modules/5- echoes of a fallen king` (especially the Blue Palace social sequence)
7. The writing guide and relevant mechanics references if needed.

Design question:

What is the best concrete, runnable procedure for the GM to run this confrontation at the table? Explain the scene loop, how Gaelen chooses or responds to people, how NPC wavering/defection/resistance should be tracked without reducing it to arbitrary persuasion rolls, how the ritual's continuing progress creates pressure, how player choices transition into combat, and how to preserve genuine agency if the party agrees with Gaelen. Distinguish established canon from your proposed design. Favor a procedure the GM can actually run while improvising conversation, not a fully scripted monologue.

Do not edit files. Do not make tool calls. Do not ask questions. Produce a complete written design answer only. Do not assume the GM wants a conventional social-combat subsystem. Do not write Gaelen's dialogue or solve the scene's prose; design the implementation procedure.
