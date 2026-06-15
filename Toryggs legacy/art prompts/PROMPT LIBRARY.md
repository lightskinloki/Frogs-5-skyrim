# TORYGG'S LEGACY — IMAGE PROMPT LIBRARY
For Nano Banana 2 (Gemini image gen) in Flow. Gritty dark-fantasy 80s anime.

================================================================
THE STYLE BIBLE  —  prepend this to EVERY prompt, verbatim
================================================================
Prepend this block so the model locks the look across the whole set. Then
add the subject block. Then add the SHOT line (aspect/camera) at the end.

>>> STYLE PREAMBLE (copy this exactly):
"1980s-1990s dark fantasy animation aesthetic, in the vein of Disney's
GARGOYLES crossed with Vampire Hunter D and the 1997 Berserk anime.
Hand-painted cel-animation look: bold confident ink linework, heavy
crushed-black shadows, dramatic rim lighting and hard key light, painterly
gouache backgrounds. Muted desaturated palette — slate greys, cold blues,
bone-white, dried-blood crimson — punctuated by one or two glowing accent
colors. Angular, weighty, gothic character anatomy; cinematic low or
canted camera angles; faint film grain and atmospheric haze. NOT modern
3D, NOT photoreal, NOT chibi, NOT bright Saturday-morning color. Grim,
mythic, theatrical."

>>> SHOT LINES (append one at the end):
- Portrait:        "Vertical 3:4 character portrait, chest-up, dramatic key light."
- Full figure:     "Vertical 2:3 full-body character sheet on neutral dark ground."
- Battlemap:       "Top-down orthographic battlemap, bird's-eye, even lighting for VTT use, square-tile readable, 16:9."
- Scene/splash:    "Cinematic 16:9 establishing shot, wide, atmospheric."
- Handout prop:    "Flat overhead scan of an aged in-world document, 3:4, no background beyond the parchment."

CONSISTENCY TIP: generate one "anchor" image per recurring character first,
then in Flow reference it ("same character as [image], now ...") for every
later shot so faces/gear stay stable.

================================================================
SECTION 1 — BATTLEMAPS (top-down, for the table)
================================================================
NOTE: battlemaps want the painterly texture of the style but EVEN top-down
lighting and clean tile readability — say so, or the model dramatizes the
angle and it stops being usable. Reference SVG: battlemaps/forelhost-laboratory.svg

[1.1] FORELHOST LABORATORY (resume-on-initiative — NEEDED FIRST)
"Top-down battlemap of an ancient Dwemer-Nord alchemical laboratory carved
in dark stone. Center: a heavy iron sterilization cage tipped crooked,
jacked up off the floor on a glowing blue wedge of unmelting ice, empty
robes and a corroded rapier lying inside it. Near it, a crescent garden bed
of black wet soil sprouting pulsing crimson flowers (the Tears of Rahgot).
Top of room: an ornate stone sarcophagus standing open, its lid shoved
aside, dust trail leading away. Left wall: a smashed brass harvesting
machine, broken pipes and shattered crystal. Right wall: a retracted
mechanical extraction arm; a small open hidden alcove. Six dark burial
alcoves along the side walls, some open. Scattered alchemy workstations.
Cold blue and amber light, crushed black shadows, faint frost. Stone floor
subtly gridded into square tiles."
+ Battlemap shot line.

[1.2] THE BEE AND BARB / RIFTEN UPPER WALK (Riften finale)
"Top-down battlemap of a canal city tavern interior and the wooden
walkways outside it — Riften: warped timber buildings on stilts over dark
green canal water, plank bridges, market stalls, lantern light. Interior
of a two-level Nord tavern with a central hearth, long tables, a bar.
Autumn dusk, amber lanterns against blue shadow, wet planks. Square-tile
readable."
+ Battlemap shot line.

[1.3] THE BLEEDING STAIR / 7,000 STEPS  (hold for Fire B if chosen)
"Top-down battlemap of an ancient mountain pilgrimage stair climbing a
snowy ridge, broken into switchback tiers. Tall carved prayer waystones
line the path, several oozing black tar-like sap that stains the snow.
Thin air, drifting mist, a wrongness to the light where time bends near
the summit. Cold white and grey, the black sap and faint violet rifts the
only color. Square-tile readable, vertical bias within a 16:9 frame."
+ Battlemap shot line.

================================================================
SECTION 2 — THE PARTY (generate anchors first)
================================================================

[2.1] DAVINIA CAELUS — the General's daughter, the Winter Queen-in-progress
"A stern Imperial noblewoman and battle-leader, dark hair with a single
streak of frost-white. Her eyes are GONE — replaced by faceted ice-crystal
that glows pale blue, no pupils, seeing magic instead of light. Her right
hand is a translucent construct of living ice where flesh should be.
Practical engraved plate armor over imperial blue. An aura of cold control
and buried grief. Faint crown-shaped frost forming at her temples."
+ Portrait shot line.

[2.2] ALFONSO DUET — the Carrion Saint (TWO versions)
2.2a THE BLADE (his true self): "A single corroded iron rapier of old
Dunmer make lying on dark stone, the pitted blade faintly breathing a sick
green inner light along its fuller, as though a soul lives inside the
metal. Beside it, a closed reliquary case holding a jagged bone crown,
never worn. Beetles forming neat rows on the stone. Reverent, still, wrong."
+ Scene/splash shot line (16:9 close still life).
2.2b THE PROJECTION (when embodied): "A gaunt grey-skinned Dunmer
plague-mage with red eyes and an air of clinical detachment, robes the
color of grave-dirt, a corroded rapier at his hip and a cased bone crown
slung at his back (never on his head). Faint spores and rot-motes drift
from his skin. He looks like a man metabolized into something useful."
+ Portrait shot line.

[2.3] SAIJAH — the hound, the unwilling vessel
"A small lithe Bosmer (wood elf) hunter with sharp features and hair gone
prematurely snow-white, dressed in worn green-and-leather ranger gear, a
fine glass bow in hand. One hand glows faintly with green Kynareth life-
magic she didn't ask for; a phantom stag's attention haloes her. Eyes that
feel too much. Forest-shadow palette, a single shaft of holy green light."
+ Portrait shot line.

[2.4] ORION — the liar, the vampire bard
"A handsome, pale Breton man with cold catching eyes and the faint elongated
canines of a vampire, dressed in fitted black ebony armor with a bard's
flourish, a war horn at his belt. A heavy obsidian ring on one finger that
seems to watch. Aristocratic, charming, predatory. Candlelit, half his face
in crushed shadow."
+ Portrait shot line.

[2.5] GEAR — the last scholar
"A unique Dwemer automaton, a 'cognitor' — humanoid bronze and brass,
slender and articulated, more elegant than a hulking centurion. Stylized
Dwemer-helm head with two large glowing amber multifaceted lens-eyes that
click and focus. Soft blue Aetherium glow through crystal chest plating,
visible gears. Gentle, curious posture. Cool museum-blue light on ancient
metal."
+ Full figure shot line.

[2.6] BJORN — the War-Hound, the secret Dragonborn
"A big weathered old Nord carter with kind tired eyes and a grey beard,
plain travel clothes — but painted so the viewer senses the killer
underneath: his frame subtly too strong, his stance too still, faint
golden dragon-soul light bleeding from behind his ribs that he himself
can't see. Beside a humble cart and a horse. Warmth and buried violence."
+ Portrait shot line.

[2.7] NORA THE HAUNTED — the soul-engineer
"An eighteen-year-old human conjuration prodigy, dark-circled haunted eyes
far older than her face, plain robes, clutching two black soul gems that
pulse faintly. Brilliant, grief-driven, walking a dark road she thinks is
rescue. Cold violet conjuration light, deep shadow under the eyes."
+ Portrait shot line.

================================================================
SECTION 3 — IMMEDIATE VILLAINS (Bleak Falls & the fires)
================================================================

[3.1] ULAG THE BREAKER — the man forced into armor
"A towering Dragon Cult war-construct: a living mind sealed inside a brutal
suit of ancient layered Dwemer-Nord siege armor, amber soul-gem eyes
burning in the helm-slit, a massive hammer. Steam venting from joints.
Less a knight than a siege engine that thinks. Industrial reds and black
iron, ember glow."
+ Full figure shot line.

[3.2] THE ECHO MIMIC — the false resurrection (wears Kyboh's body)
"A Khajiit warrior-monk in pugilist's wrappings, athletic, scarred snowflake
-marked gauntlets on his fists — but WRONG: his movements and gaze are a
fraction off, his eyes hold a tonal-copy's hollow shimmer instead of a
soul, standing too obediently at a warlord's side like a bodyguard. He
looks exactly like a beloved dead friend and is not him. Uncanny, grief-
baiting. Cold blue copy-light."
+ Full figure shot line.

[3.3] ANTOINE OF FORELHOST — the rival alchemist
"A gaunt, joyless young Dragon-Cult alchemist of an ancient inbred lineage,
pale and meticulous, plague-stained leather apron over funeral black,
surgical tools and reagent vials, eyes that catalogue everything as a
specimen. Cold, envious, brilliant. Sterile lab-light, green reagent glow."
+ Portrait shot line.

[3.4] RAHGOT — the risen Dragon Priest
"An ancient Dragon Priest newly risen: desiccated robed undead crowned with
an ornate golden ceremonial mask (the Rahgot mask), radiating cold authority,
floating dust and necrotic light, an empty stone sarcophagus behind him.
Gold mask against black robes, sickly green glow."
+ Full figure shot line.

[3.5] GAELEN THE ROOT-TWISTER — the warm Mythic Dawn (Fire B boss)
"A disarmingly warm, gentle-faced Mythic Dawn cultist in dagonic red robes
with sincere, sad eyes — the most reasonable monster you'll meet — standing
amid a corrupted holy tree whose roots leak black sap, faint reality-tearing
violet rifts behind him where time bends. Kindness over apocalypse. Warm
candlelight fighting cold violet."
+ Portrait shot line.

================================================================
SECTION 4 — KEY NPCs (as needed)
================================================================

[4.1] ISMARA / THE CROWN OF THE PALE LADY
"An ancient circlet of black Atmoran ice and frost-metal, beautiful and
predatory, faint regal feminine presence haloing it, fused with veins of
frost — an artifact that is secretly a trapped researcher's soul. On dark
stone, breathing cold mist. Pale blue, bone, black."
+ Scene/splash close still life.

[4.2] KRUSP FANCK — the Ashen Blade (the rival hero)
"A noble Reachman legendary warrior in silver-inlaid heavy plate, a gleaming
silver longsword, weary righteous eyes, the bearing of an immovable shield-
wall. A subtle obsidian ring on his hand glowing faintly (a hidden curse he
doesn't know). Heroic but doomed, holy gold light with a creeping cold edge."
+ Full figure shot line.

[4.3] VARON — the carved hound (Shadowscale in disguise)
"A wiry man who reads as a plain Breton traveler but is WRONG: surgically
altered Bosmer features, unnatural reptilian stillness, murky grey eyes that
should be black, a concealed kusarigama chain-blade. Stillness like a held
breath. Flat muted palette, one cold highlight."
+ Portrait shot line.

[4.4] YLVA THE CLEAVER — the joyful werewolf
"A big grinning Nord warrior-woman mid-laugh with a heavy cleaver over her
shoulder, scarred, gleeful, the faint amber eyeshine and lengthening shadow
of a barely-hidden werewolf. Joy in violence. Warm firelight, wild energy
against the grim palette."
+ Portrait shot line.

[4.5] DANICA PURE-SPRING — the hardened priestess
"A Kynareth priestess who has hardened: chainmail hauberk pulled over green
healer's robes, calloused hands, weary resolve, a quiet door closed behind
her eyes. Soft green holy light over cold steel."
+ Portrait shot line.

================================================================
SECTION 5 — SET-PIECE SPLASH MOMENTS (for chapter art / hype)
================================================================

[5.1] THE UNMAKING: "Wide cinematic shot inside the dark Forelhost lab: a
white sterilization pulse fills an iron cage tipped on a wedge of glowing
ice; a Dunmer's body dissolving into nothing mid-stride, one hand reaching
free, leaving only empty robes and a corroded rapier falling to the floor.
Horror and stillness." + Scene/splash.

[5.2] BJORN AND THE DEAD BOY (false resurrection): "Wide shot, a warlord's
torchlit lair: a beloved Khajiit fighter standing as a hollow bodyguard
beside a hulking armored warlord, while across the room recognition and
dread dawn on the faces of his old companions. Grief weaponized." + Scene.

[5.3] THE THREE MASTERWORKS triptych: "Three-panel composition — a noble
ringed warrior (Krusp), a gentle bronze automaton (GEAR), and a hollow-eyed
khajiit copy (the Echo) — united by an identical glowing snowflake maker's
mark, the signature of one ancient soul-smith. Cold, clinical, tragic."
+ Scene/splash.

================================================================
SECTION 6 — PLAYER HANDOUT PROPS (in-world documents)
================================================================
Style note: for props, DROP the cel-anime preamble and instead say:
"Photorealistic flat overhead scan of an aged in-world prop document."

[6.1] ANTOINE'S HIDDEN JOURNAL: "aged water-stained alchemist's journal page,
cramped obsessive ink handwriting in an arcane hand, anatomical and
chemical diagrams in the margins, a pressed dead flower, burn marks. 3:4."

[6.2] THE KONAHRIK PROPHECY CARVING: "rubbing/etching of an ancient Nordic
stone relief showing five masked dragon-priest figures whose masks combine
into one great warlord's mask, runic border. Aged parchment. 3:4."

[6.3] MAVEN'S PATRON CONTRACT: "formal aged parchment contract sealed with a
black-briar wax seal, elegant intimidating calligraphy, ledger figures, a
line for a signature. 3:4."

[6.4] GALMAR'S PLEA / THE COURIER'S LETTER: "a hastily written, blood-flecked
field letter on cheap paper, urgent soldier's hand, a Stormcloak bear sigil
smudged at the top. 3:4."

================================================================
GENERATION ORDER (recommendation)
================================================================
1. Forelhost lab battlemap (1.1) — needed at the table first.
2. Party anchors (2.1-2.7) — generate once, reference forever.
3. Bleak-Falls villain set (3.1-3.4) — the next dungeon's cast.
4. Riften battlemap (1.2) + handouts (6.x) for the finale.
5. Fire-B map (1.3) + Gaelen (3.5) ONLY once the table picks Fire B.
6. Splash art (Section 5) whenever you want hype / chapter headers.
