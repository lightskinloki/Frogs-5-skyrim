# TORYGG'S LEGACY — IMAGE STYLE BIBLE
For Nano Banana 2 (Gemini image gen) in Flow. Gritty dark-fantasy 80s anime.
(Subject prompts are generated in chat as needed — this file is just the
reusable preamble + the rules that keep the set consistent.)

================================================================
STYLE PREAMBLE  —  prepend to EVERY prompt, verbatim
================================================================
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

================================================================
SHOT LINES  —  append ONE at the end of the subject block
================================================================
- Portrait:     "Vertical 3:4 character portrait, chest-up, dramatic key light."
- Full figure:  "Vertical 2:3 full-body character sheet on neutral dark ground."
- Scene/splash: "Cinematic 16:9 establishing shot, wide, atmospheric."
- Handout prop: "Flat overhead scan of an aged in-world document, 3:4."
  (For handouts ONLY, replace the style preamble with: "Photorealistic flat
   overhead scan of an aged in-world prop document.")

BATTLEMAP shot line (the special case):
"Top-down orthographic battlemap for virtual-tabletop use, true bird's-eye
view straight down, EVEN flat lighting across the whole floor, no
perspective tilt. The room fills the entire frame edge to edge. Drawn over
a visible grid of [N x M] square tiles, each tile sized to hold one
standing figure (5 feet). Keep features spaced generously — readable, not
cramped. 16:9."
  >> Battlemaps cram themselves unless you SET THE GRID COUNT and say
     "fills the frame edge to edge, spaced generously." Always give N x M.

================================================================
CONSISTENCY RULE (most important for a multi-image set)
================================================================
Generate ONE anchor image per recurring character/place FIRST. Then in Flow,
reference it on every later shot ("same character as [image], now ...") so
faces, gear, and palette stay stable across the whole campaign. Generation
order: lab battlemap -> 7 party anchors -> next-dungeon villains -> situational.
