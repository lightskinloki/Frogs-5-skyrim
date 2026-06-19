# -*- coding: utf-8 -*-
# Generator for the human-readable (WordPad/RTF) session runsheet.
# Output is the canonical doc the GM reads + hand-edits at the table.
# Run: python _build_session_rtf.py

import os

OUT = r"C:\Users\fbrown\Projects\Frogs-5-skyrim\Toryggs legacy\Adventure modules\choice gate 2\11- the city that didnt need you\NEXT SESSION - forelhost finale to gate 3.rtf"

HEADER = (
    r"{\rtf1\ansi\ansicpg1252\deff0"
    r"{\fonttbl{\f0\fswiss Segoe UI;}{\f1\fmodern Consolas;}}"
    r"{\colortbl;\red0\green0\blue0;\red124\green22\blue22;\red22\green46\blue120;"
    r"\red150\green70\blue0;\red110\green110\blue110;\red150\green20\blue20;}"
    "\n\\f0\\fs24\n"
)
FOOTER = "\n}\n"

def esc(s):
    return s.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")

def inline(s):
    # **bold** -> rtf bold; escape first
    s = esc(s)
    parts = s.split("**")
    out = ""
    for i, p in enumerate(parts):
        out += ("{\\b " + p + "}") if i % 2 else p
    return out

buf = []
def raw(x): buf.append(x)

def scene(title):
    raw("\\pard\\sb280\\sa40\\cf2\\b\\fs40 " + esc(title) + "\\b0\\fs24\\cf1\\par\n")

def subtitle(text):
    raw("\\pard\\sa220\\cf5\\i " + esc(text) + "\\i0\\cf1\\par\n")

def label(text, red=False):
    c = "6" if red else "4"
    raw("\\pard\\sb160\\sa70\\cf" + c + "\\b\\fs26 " + esc(text) + "\\b0\\fs24\\cf1\\par\n")

def readaloud(paras):
    raw("\\pard\\sb80\\sa60\\cf3\\b\\fs26 >> READ ALOUD\\b0\\fs24\\cf1\\par\n")
    body = "\\line\\line ".join(esc(p) for p in paras)
    raw("\\pard\\li600\\ri400\\sa220\\cf3\\i \"" + body + "\"\\i0\\cf1\\par\n")

def handout(title, paras):
    raw("\\pard\\sb80\\sa60\\cf3\\b\\fs26 >> HANDOUT -- " + esc(title) + "\\b0\\fs24\\cf1\\par\n")
    body = "\\line\\line ".join(esc(p) for p in paras)
    raw("\\pard\\li600\\ri400\\sa220\\cf3\\i \"" + body + "\"\\i0\\cf1\\par\n")

def gm(text):
    raw("\\pard\\li360\\sa140 {\\cf2\\b GM:} " + inline(text) + "\\par\n")

def plain(text):
    raw("\\pard\\sa140 " + inline(text) + "\\par\n")

def bullet(text):
    raw("\\pard\\li500\\fi-280\\sa120 {\\cf4\\b\\bullet\\tab}" + inline(text) + "\\par\n")

def statcard(lines):
    raw("\\pard\\li300\\ri300\\sb40\\sa220\\box\\brdrw15\\brdrcf5\\f1\\fs20 ")
    raw("\\line ".join(inline(l) for l in lines))
    raw("\\f0\\fs24\\par\n")

def exit_(text, nxt):
    raw("\\pard\\sb100\\sa240 {\\cf2\\b EXIT ->} " + inline(text) +
        ("   {\\b -> " + esc(nxt) + "}" if nxt else "") + "\\par\n")

def rule():
    raw("\\pard\\brdrb\\brdrs\\brdrw20\\brdrcf2\\sb60\\sa220\\par\n")

# ============================================================ TOP
raw("\\pard\\sb60\\sa40\\cf2\\b\\fs44 NEXT SESSION -- FORELHOST FINALE -> GATE 3\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i Picks up the instant we froze: the trap sprang, Alfonso is a rapier on the cage floor, the False Draugr are stepping out. Open on initiative. Self-contained -- run the night from here. (Old runsheet kept as the play-log.)\\i0\\cf1\\par\n")
rule()

label("TONIGHT: ISMARA AT THE WHEEL  (Davinia's player is late)", red=True)
plain("Davinia's player asked that **Ismara play Davinia** until she arrives. Run it -- and treat it as a milestone: the party's **first real contact with Ismara as a person who can take the wheel and talk back.**")
gm("CDI DOES NOT ADVANCE TONIGHT (GM ruling) -- a cost-free loan of the wheel, not a Sovereign's Domain integration-check. What it DOES do is set the precedent: Ismara can drive, and converse. Future takeovers can carry the usual cost; tonight is the gracious demonstration.")
bullet("**Combat:** a cooler, sharper tactician who PROTECTS the body above all -- spends power freely, takes no risks, never invoices a rescue. Fights with **Ismara's Aegis (frost -- a False Draugr weakness)** and the telekinetic mace; pointedly **will NOT cast Restoration** (the Strain feeds on it). Her Sight reads the False Draugr as eerie soulless BLANKS -- 'furniture that moves' -- and she'll say so, fascinated.")
bullet("**She talks** if engaged, and may open unprompted: helpful, dry, regal, and she NEVER lies -- sees the party as hers to keep (shield-thanes) and files everything. Marquee beat: **Ismara meeting Alfonso-the-sword** -- two souls housed in objects; she's the one voice that fully grasps what he is, and the Crown is already pooling toward his rapier.")
gm("FULL playbook + per-member talking points: `Npcs/Ismara` Sec. VIII (new). Keep her honest, keep her sentences short when she's working, and let the table leave liking her more than is comfortable.")

label("STATE AT THE FREEZE", red=True)
bullet("Alfonso moved to destroy the Tears; the cage dropped -- but they **fought it**: Davinia knocked the cage upward with her telekinetic mace while Alfonso threw a **Wall of Frost under the bars** (jacking it off the floor) and **enchanted the ice with a single Stabilize component** -- the ice is stable and long-lasting, holding the cage jacked up. He was a breath from breaking out when the **timer ran out** -- the field fired and **unmade him anyway**. His soul is in the **rapier on the floor under the jacked-up cage**, and because the cage is displaced, **the extraction arm can't reach it.**")
bullet("Antoine's **False Draugr** are stepping out of the wall alcoves now. Inside/around the cage: **Davinia, Saijah, Orion** (+ Alfonso-as-rapier). Bjorn, Mila, Nora, Esbern, Varon, GEAR, Ylva are outside with the cart.")
bullet("Earlier this session they smashed **Antoine's copper additions on Ulag's stasis-harness** (a separate device from this cage). The Dwemer core survived -- Forelhost can still hold Ulag in **stasis**, but its **disease-processing** function is dead. Consequence: Antoine must rebuild at Bleak Falls; the Strain 2.0 clock **lengthens**. (They don't know they did this.)")

gm("THE TRAP HALF-FAILED -- and that's earned. The field still fired (area effect, on the timer) and destroyed Alfonso's body, but their counterplay saved the rest: the cage is jacked up on Alfonso's ice and **the extraction arm can't reach the rapier**, so Antoine's machine draws **nothing** -- he loses his backup sample. The phylactery is freely recoverable; the only thing in the way is the False Draugr.")
gm("THE STABILIZED ICE -- per the somatic system: STABILIZE makes a state **resistant to entropy and dispelling**, so the ice **won't melt, won't rot, can't be dispelled** -- and baked in as an enchantment (not a held cast) it **persists without Alfonso**. BUT STABILIZE resists decay, NOT force: **raw muscle can still break it.** It's his own working, so he can also drop it himself. See RECOVER THE RAPIER.")

# ============================================================ COMBAT
scene("1   THE LAB, MID-FIGHT  --  ROLL INITIATIVE")
subtitle("The guards deploy. Alfonso is a rapier on the floor under the jacked-up cage -- the extraction never reached him. Goal: clear or hold the Draugr and recover the phylactery.")

label("THE ENEMY", red=True)
statcard([
    "**FALSE DRAUGR  x4-6   (TL1-2 Expert)  --  Antoine's make, NOT true undead**",
    "HP 35   |   DR 5 (chem-hardened tissue + copper plate)",
    "Immune:  FIRE / poison / disease / fear / Alfonso's plague-communion",
    "Weak:    COLD x2  AND  LIGHTNING x2  (both also STOP its regen)  |  Sonic = Staggered 1 rd",
    "         Lightning ARCS: 2+ within 10 ft -> half-damage jumps to each neighbor.",
    "Might 14    Agility 8 (SLOW, holds ground)    Magic 6    Guile 4  (rigid scripts, no mind)",
    "REGEN:  +3 HP at the start of its turn UNLESS it took cold or lightning since last turn.",
    "SPLASH: at 0 HP the pressurized fluid bursts -- 3 chem dmg to all within 5 ft.",
    "",
    "Atk  Alchemical Blade -- melee 6 dmg, +2 burn next turn; Std Might or Numbness (-2 Agi, 2 rds)",
    "Atk  Restraining Grapple (replaces atk) -- contested Might (Hard -4) -> Restrained; pile on.",
    "Atk  Breaker's Blow (telegraphed: vents steam first; recharge after a grapple / every other rd)",
    "        -- 10 dmg, ignores half DR, knockback + Staggered. A readied PC can brace or interrupt.",
    "JOB: PIN then SHATTER -- soften with the Blade, grapple, Breaker's Blow the held target.",
])
gm("THE INVERSION IS THE FIGHT -- they are built to punish the anti-draugr playbook. FIRE DOES NOTHING. **Cold, lightning, and sound are the answer, and the party is holding all three:** Saijah's chain-lightning ARCS across the clustered frames (and stops their regen); Davinia's Aegis-frost and Alfonso's Wall of Frost bite double and stop the regen; Orion's War Horn staggers. Without cold/lightning they heal 3/round and it's a grind -- with it, damage sticks.")
gm("ALFONSO'S COMMUNION IS DEAD HERE -- no Dragon Cult substrate. If his player reaches to seize them, it does **nothing**. Let him feel the blank -- the second time Antoine neutralized him (caged body + useless gift).")
bullet("**Tremorsense, not sight** (30 ft): sneaking FAILS (they feel your weight), but standing perfectly still, going invisible, or getting OFF the floor (onto the jacked-up cage, the ice block, a workstation) makes you vanish to them. Mindless -- rigid scripts, a feint or lure works.")
bullet("They grapple/pin whoever goes for the cage, the ice, or the rapier. **Holding them off is the price of the rescue.**")
gm("VITALIS KILL (do NOT hint -- system-mastery reward): they are VENITAS-saturated, so a healing potion POURED on one (Major action, adjacent) deals its HP value as damage and ignores DR -- 4 / 8 / 12 for Minor / Healing / Plentiful. If a player reasons to it from the Essence rules, celebrate it.")

label("RECOVER THE RAPIER")
plain("The rapier is sealed under Alfonso's stabilized ice. STABILIZE means heat, time, and Dispel do **nothing** -- but it resists entropy, not force, so the ice is still **breakable by raw muscle**: a **Hard Might roll (-4)** or two, or a heavy blow, cracks a gap to pull the blade out -- worked under the Draugr's grapples. Simplest of all: once Alfonso reforms, he unmakes his own ice and reclaims it.")
gm("Don't let heat or Dispel touch the ice; do let force break it. If he picks **slow** reform, the party can break it free and carry the rapier (or haul the whole block -- his to drop later). No reverse-rite needed; they out-fought the cage. The phylactery is in no danger either way -- the extraction arm can't reach the displaced cage.")

label("IF A PC WIELDS HIM -- THE BORROWED BODY  (full rules: The Sentient Sword Sec. III)")
plain("A willing PC can pick the rapier up and, while Alfonso is Wakeful, **lend him their body.** Once per round Alfonso takes **one extra Major Action he fully dictates** (his player resolves it) -- move, strike, speak, or cast. PHYSICAL acts use the **bearer's** stats; MAGIC uses **Alfonso's** Magic and his whole spell list; costs are Alfonso's (FP / Surface Rust). This un-benches his player mid-fight -- he acts through someone else's hands.")
bullet("**Touching the iron INFECTS the bearer** automatically (Alfonso's Strain -- the plague doesn't care he likes them; he can't stop it). **Davinia is the worst possible bearer** (it feeds on her Restoration + the Crown); Saijah burns it off; Orion is unpredictable.")
gm("TONIGHT IS SAFE GROUND. A single fight's pickup-and-drop is **Stage 0 Bearing** -- bearer keeps their full turn, Alfonso gets his one dictated action, infection applies, and they can set him down freely. The **TENANCY** takeover (the iron slowly seating Alfonso in a living host -- GM-SECRET, and Alfonso himself can't feel it) only advances per SESSION carried; it will NOT trigger in one combat. Full ladder + the contested-Magic release + the Nora rule: **The Sentient Sword Sec. III.**")

label("ALFONSO REFORMS -- OR DOESN'T  (pure will, not a timer)")
plain("Reformation is **his will alone.** He can pull a body back together in minutes -- or refuse and **stay the blade as long as he likes.** Right now he may not want to come back at all.")
bullet("**Reform** (by will): back in play. The cost is rust -- forcing the body back advances his **Deep Rust.**")
bullet("**Stay a sword** (by will): out of play -- carried, unable to act -- BUT discorporate, his **Deep Rust stops advancing and may even REVERSE.** Resting in the phylactery is how he heals. A real reason to stay gone.")
gm("Why he might refuse to return: Antoine's confession just held a mirror to him (chosen / answered / envied), and rest mends the rust. Let him choose to linger as the blade if his player wants it. Don't narrate what it costs him.")
gm("THE NORA BEAT -- do NOT miss this: Nora (18) carries her dead parents' souls in two black gems and is secretly building toward seating them in a living vessel. Alfonso CHOOSING to persist as a willful soul in a blade is a live proof-of-concept of her whole plan -- and false confirmation that her parents are 'still in there,' intact and recoverable. It is not true; she does not know that. Play her watching the sword; it accelerates her dark turn. (See `Npcs/Nora the haunted`.)")
gm("THE NORA FORESHADOW (fires when she rejoins the party and reaches for the sword -- she's outside during the lab fight, so this lands on the descent / at camp): she WILL volunteer to carry him; she must NOT. She has loosened her own soul-housing with soul-vessel study, so the blade's Tenancy takes root in her in a single SCENE where others have whole adventures. The first time she even holds it, play the wrongness in the open -- she stills, her cadence goes wrong, she won't give it back; Davinia's Sight (if looking) sees the iron sink a root in seconds. The table must learn, wordlessly: never Nora, ever. Rules: **The Sentient Sword Sec. III.**")

# ============================================================ SARCOPHAGUS
scene("2   THE OPEN SARCOPHAGUS  --  the first room a real villain occupied")
gm("Rahgot is NOT here -- he woke, pushed out, and walks elsewhere. No body, no avatar, no ambush. They read him off the marks he left.")
readaloud([
    "Up close the heat off the dais is plain on your face. The lid leans against the stone, a slab two hands thick, split across the middle. A handprint is sunk into the underside, the fingers driven to the second knuckle, the stone dimpled around them as though it had gone soft as tallow under the hand.",
    "The dust in the open box lies even except for one long hollow -- the length of a tall man on his back; at the head of it the dust is scuffed and broken where the shape sat up, and a smear runs over the lip where the legs swung down. From there a line of dusty footprints, carried out of the box, crosses the clean floor to the door -- evenly spaced, each stride the length of the last.",
])
gm("Let the players reach this, or not. Handprint = strength past mortal scale (he pushed the lid one-handed, dented stone). The hollow = he lay an age, then rose. The even prints = he left at an unhurried walk, the bearing of something that owns the room.")
bullet("**Standard Magic:** the death-sleep runes were shut off FROM INSIDE -- he woke and walked out. Their first proximity to a true Dragon Priest; he will remember them. **Rahgot the Angry**, the Avenger -- 4,000 years of vengeance on the bloodline that besieged this fortress (his coming Scourge). The science is Antoine's; the want is his.")
gm("If asked where the mask is: he rose wearing it and walked out with it -- not here. Each of the five masks is with its own priest; that is the 'when the five become one.'")

# ============================================================ CARVINGS
scene("3   THE CARVINGS  --  the Konahrik reveal")
plain("**Standard Magic** to read the Dragon Cult notation. Five death-sleeping priests, each with a mask:")
bullet("**Nahkriin** the Guardian -- vengeance; spymaster.")
bullet("**Vokun** the Shadow -- tactician, siege.")
bullet("**Rahgot** the Angry -- fury; alchemist-priest (this tomb).")
bullet("**Otar** the Mad -- madness.")
bullet("**Morokei** the Glorious -- glory; archmage, the strongest.")
plain("The five masks combine into a **sixth: KONAHRIK the Warlord.** \"When the World-Eater returns, the faithful shall rise. When the five become one, the faithful shall ASCEND.\"")
gm("THE REVEAL: the priests have their OWN endgame -- apotheosis. **Alduin is their vehicle, not their master.**")
gm("Alfonso's expertise -- offer it, don't speak it for him: the carvings place Rahgot as an alchemist-priest of environmental warfare, which makes Antoine his **successor, not his inventor** -- the plagues are Rahgot's, Antoine the instrument. If Alfonso's player reaches it, let him land it.")

# ============================================================ FAMILY QUARTERS
scene("4   THE FAMILY QUARTERS  --  a side chamber off the sanctum")
readaloud([
    "Forty niches are cut into the living rock, oldest at the door and freshest at the back, each holding a body wrapped in oiled cloth, the wrappings darkening as the rows march toward the entrance. Three cots stand against the back wall, each the length of a child, the rails worn pale and smooth where small hands gripped them.",
    "A slate leans on the last cot, chalked in two columns -- the alphabet down one side in big careful letters, alchemical sigils down the other, a few of the letters drawn backward. The last niche at the back stands open and swept, a folded cloth set ready at its head.",
    "Against the wall beside the cots: a locked iron chest, old and dented but sound; and on a shelf above it, a cloth-wrapped book thicker than any journal in the refinery, its cover hand-tooled with the same alchemical notation as the practice slate.",
])
gm("Generations born, taught, and buried here. The open niche is the one **Antoine cut for himself**. This is where the hidden journal they found becomes a place.")
label("FIND -- THE FAMILY CACHE")
bullet("**Locked chest** (Hard Agility -4): reagents stored over forty generations -- dried Ancestor Moth silk, crystallized void salt, blackened bone meal, three sealed vials of Tears of Rahgot extract kept apart from the lab. **~1,200g** to an alchemist; worth more as material.")
label("FIND -- THE FORELHOST ALCHEMY CODEX  (the campaign's gateway to Alchemy)")
bullet("The family's master textbook, written and revised by forty generations, annotated in a chain of different hands. A character can tell it is a **complete master text** (the cover notation matches the child's slate).")
gm("HOW IT WORKS: taking and studying it starts a character learning Alchemy **the way Alfonso learned Enchantment** -- they absorb methodology, combinations, technique until they understand the system and can improvise in it. (Alchemy is more complex than Enchantment; full system GM-prepped separately.) Do NOT gate it behind a flat AP buy. At the table now: they gain the book and the path; mechanics to follow.")
gm("It can go to anyone; you'd love it to land with **Saijah** (a tie to the land's materials, a magical purpose she lacks) or Orion -- but it's the players' to claim.")

# ============================================================ CONFESSION
scene("5   ANTOINE'S CONFESSION  --  a loose page at the main bench")
gm("Pressed harder than the tidy logs around it -- written to no one. This is Alfonso's mirror. Present the page; do not narrate Alfonso's conclusion.")
handout("ANTOINE'S CONFESSION", [
    "He is chosen.",
    "I have read the Korvanjund reports three times. He does not calculate the lifecycle. He does not infer it from the residue. He is TOLD it. His god speaks to him and he answers, and his plagues are crude and undisciplined and alive in a way four thousand years of my method has never once been.",
    "Forty generations of my blood have served a god we only ever overheard. We built His shape from what He left behind, the way you reconstruct a face from the dent it pressed into clay. And this untaught thing is spoken to, and answers, and walks in the favor we begged for and were never shown.",
    "I will take what I can of his work and graft the life of it into mine. I will earn by labor what he was given for nothing. I tell myself it can be done. The alternative is that my whole line kept faith for four thousand years with a god who never once turned His head toward us.",
])
gm("Antoine is a true believer who has never been answered, and he envies Alfonso the one thing Alfonso has for free -- a god that chose him and answers. NOTE: Alfonso is PERYITE'S CHOSEN, never a 'carrier' -- Peryite is a Daedra, not a disease to extract. What Antoine covets is the **living quality** of Alfonso's plagues, and he believes, with an engineer's arrogance, that he can graft it onto his own work.")

# ============================================================ CONTRACTOR LETTER
scene("6   THE CONTRACTOR LETTER  --  the lab's maintenance file")
gm("Read it FLAT -- audience-only irony, a crumb to pay off later. It is an ANCIENT artifact: Hjolmar's handoff notes, left WITH the casket at the founding and kept in the family file for 4,000 years. Antoine never met Hjolmar -- the Ice-Shaper was gone four millennia before Antoine was born.")
gm("If a player asks 'who is the Breaker?': it's **ULAG** -- the armored Orc war-engine they FOUGHT at Korvanjund. The name should ring a bell. Confirm that much; the rest is for later.")
handout("THE ICE-SHAPER'S HAND  (ancient -- left with the casket at the founding)", [
    "To the Keeper who comes after me, and to his sons, and to theirs: I have built the Breaker's frame -- the casket, the amber, the soul-gem eyes, the whole apparatus -- and I give it into your line's keeping. Cycle the fluids. Hold the cold. The mind inside will not fail while you tend it. That is your charge, and your blood's, for as long as the Cult has need of him.",
    "Know that the casket is a compromise. It holds a mind in failing flesh and binds a keeper to it forever. I have since finished better work -- a method that needs no original flesh at all. A signature can be lifted whole and seated in a frame that suits it. The vessel is a detail. The song is the asset. The Breaker was made before I was finished; tend him as he is. I do not expect to pass this way again.",
])
plain("**Antoine's margin note** (a hand four thousand years younger): \"Forty of my blood have tended this casket. I have never seen the Ice-Shaper and never will -- he was gone before I drew breath. And yet they say his work walks again in the world. Rahgot says only that the Song is owed a debt, and that I am not to ask. So I do not ask.\"")

# ============================================================ STRAIN 2.0
scene("7   THE STRAIN 2.0 FOLDER  --  the ticking clock")
plain("**Hard Magic (-4)** to parse the technical content (Alfonso reads it free -- his discipline).")
bullet("**Goals:** self-propagating; waterborne + airborne + **Restoration-transmissible** -- 'a healer who cures one becomes the vector for the next hundred.'")
bullet("**Missing piece:** his Strain is a sterile, self-limiting chassis -- it lacks the living, self-propagating quality of Alfonso's plagues. Ulag was infected with Alfonso's strain at Korvanjund; Antoine goes to harvest that living disease from Ulag and graft its life onto Strain 2.0.")
bullet("**His gamble:** whether a chosen's plague keeps its life once cut from the chosen. He believes it will. He may be wrong.")
gm("TIMELINE (updated by their own hand): 6-8 weeks AFTER the harvest -- AND he now needs a processing facility, because they wrecked his Forelhost rig. He must detour to **Bleak Falls** (his old staging ground) to rebuild. The clock **stretches**; the finish line **moves to Bleak Falls.** Counter-play: reach Ulag first, or catch Antoine mid-rebuild at Bleak Falls -> Strain 2.0 never exists.")

# ============================================================ LOOT + TRACKER
scene("8   LOOT, THE TEARS, AND THE DESCENT")
label("LOOT")
bullet("3x **Tears of Rahgot extract** (500g ea; Alfonso may keep) -- plus the 3 vials from the family cache.")
bullet("3x sealed **Strain 1.0** samples (500g ea to Maven; dangerous).")
bullet("**Strain 2.0 folder** (priceless intel) | **Journals 1-3** (Maven evidence).")
bullet("**Master Alchemist's Apparatus** (+2 Alchemy Magic; 2000g) | ~800g assorted reagents. ~2500g/player + the Tears.")
label("THE TEARS -- A STRATEGIC CHOICE (don't editorialize)")
bullet("Take or destroy the Tears -> Antoine loses his binding agent. Leave them -> production continues. The party may not register they are choosing. (Alfonso already moved to destroy them -- the cluster he touched is the trigger; the rest of the bed is still here.)")
gm("DAVINIA / ISMARA LEDGER (carry the state, no beat to run): grant 1 of 5 spent (the biosafe-vial knowledge, last session). 4 free grants remain; then Ismara asks to suppress more; after that, the next yes she STOPS ASKING. Do not telegraph -- the dread is retroactive.")
exit_("The long climb back down. The infection works at its set severity; threads now point at Antoine -> Ulag (the stretched clock), Konahrik / apotheosis, the Ice-Shaper crumb, Alfonso's rust, Davinia's ledger.", "RIFTEN WRAP (next in this doc)")

rule()
raw("\\pard\\sb120\\sa200\\cf2\\b\\fs40 RIFTEN WRAP\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i None of this happened yet -- the party went straight into Forelhost. Run it before or after the dungeon as the table moves.\\i0\\cf1\\par\n")
gm("PACING / TRIAGE -- the night is big; protect the spine. LOAD-BEARING (do not cut): the lab fight + rapier recovery, the open-sarcophagus / Konahrik reveal, and the **Gate 3 choice + fire matrix** (the session MUST end on a committed fire). Everything in this Riften Wrap is MODULAR -- run what time allows, any order. If short: prioritize the **Maven debrief** (bounty + promotion) and the **Gate-3 due-diligence + Bjorn/horse**; Hemming, Balimund, and the camp vignettes can compress or carry. **Orion's Grelod infiltration is a whole set-piece** -- if he commits, strongly consider giving it its OWN session rather than cramming it. Land Gate 3 clean over rushing six social scenes.")

# ================= THE CAMP =================
scene("THE CAMP  --  THE RETURN  (the canal camp, dusk)")
subtitle("The company reunites after a day-plus apart -- and the party comes back CHANGED (Ismara fronting in Davinia's body, Alfonso a sword in Saijah's hand). Each beat below has a line to say and a thing it offers; weave them, Mila first. Marked [PLAYED] = already happened, now canon.")
readaloud([
    "The cart-camp sits where you left it, tucked against the canal wall below the Bee and Barb -- woodsmoke, wet stone, the green smell of the water. Esbern's lantern burns in the wagon; Nora's bent over her books in its light. Mila's on the tailgate, the heel of a loaf going stale in her fist. Bjorn's at the fire, and he's on his feet before you've cleared the bridge, counting heads the way he does now.",
    "Four went south to that mountain, and four come back -- but the count doesn't sit right with him, and you watch the moment he sees why. The one in the grey cloak walks like Davinia and isn't quite: skin gone silver-pale, hair fallen straight, the eyes a degree too calm. And one of you carries a rapier held wrong for a weapon -- held the way you'd carry something that's awake.",
])
gm("The camp's first look at BOTH changes. Don't explain either -- let the crew react and the players manage it. Mila and Bjorn below PLAYED this session (canon now); the rest are live for any return to this camp.")

label("MILA (8) -- the safe hand, and the question  [PLAYED]")
plain("She doesn't run -- Warrens kids don't run -- but when **Saijah** crosses the camp her shoulders come down a notch. She goes to her, takes her hand, holds it. After a while, not looking at anyone:")
plain("**MILA:** \"...When can I go home? I don't mean now. Just -- when. Is all.\"")
gm("What it offers: the going-home ache, no clean answer (her mother sold her; thread stays open -- see OPEN THREADS). Saijah is the safe hand; she keeps clear of **Orion** (he showed her his fangs). Don't solve it -- let Saijah hold it. She will NOT cry in front of anyone.")

label("MILA -> BJORN -- the question that landed wrong  [PLAYED]")
plain("Earlier she'd gone to Bjorn -- she likes him -- and asked the thing a sharp, lonely kid asks the strangest grown-up in camp:")
plain("**MILA:** \"Why do you feel like more than one person? Like there's somebody else in there with you.\"")
gm("She's brushing the BIGGEST SECRET (the two dragon souls / the de-aging) and can't name it -- she just feels it. REACTION (Bjorn): it unsettled him badly; no anger, he goes quiet and finds somewhere else to be, and has kept his distance since. The guardian recoiling from the child who sees too much -- the Vow still holds underneath; friction, not a break. NEVER let her perceptiveness become Dragonborn-confirmation.")

label("MILA -> ISMARA -- 'where's Davinia?'  [PLAYED]")
plain("She clocked the silver skin before any adult said a word:")
plain("**MILA:** \"You're not her. Where's Davinia?\"   **ISMARA** (gentle, unhurried): \"Oh -- no need to fret, little one. Davinia's right here. She's only resting; I'm minding things for her.\"")
gm("Classic Ismara: true, warm, closes the question without a lie. Mila didn't press. Leave the small unease in -- a sharp kid only half-buys it. (Ismara files Mila as 'sharp.')")

label("BJORN -- the horse  [opens the unresolved beat]")
plain("Once the camp's settled he plants himself in front of you, gruff, the real thing on his mind:")
plain("**BJORN:** \"Mable's done. Took bad hurt off that dragon and she's earned her field -- she'll stay long enough to teach the new one the ropes, then home to my farm to live easy. Which leaves us short a horse, and a cart's no good without one.\" A breath. \"I've put in every coin I've got. I'm asking the rest from you. A GOOD one, mind -- not some broke-down nag.\"")
gm("Opens the horse decision (its own scene). The tell: he glances at Mila on 'a cart's no good' -- it's her he's thinking of. UNRESOLVED at session end; the loneliness beat is gated behind a quality mount (Grey/Black Mare).")

label("NORA (18) -- the sword")
plain("Her eyes haven't left the rapier in Saijah's hand since you crossed the bridge. She closes her book.")
plain("**NORA:** \"That's... him. He's in there, isn't he. He chose to stay.\" Quiet, certain, hungry. \"...May I hold it?\"")
gm("THE FORESHADOW (Sentient Sword Sec. III). If anyone lets her: run the instant-wrongness -- she stills, her voice goes wrong, she won't want to give it back; Saijah or Bjorn should clock that Nora + that sword is OFF. REACTION (Nora rebuffed): she retreats, stung, files it as one more reason her work matters. Either way the table learns, wordlessly: never Nora.")

label("YLVA -- the favour she didn't get")
plain("She's been circling **Saijah** since Hircine's favour fell on her unasked. Too close, needling:")
plain("**YLVA:** \"Smell different, don't you. He's got his eye on you, and you didn't even kneel for it. Some of us would have.\"")
gm("Rivalry, not bond (the rebound is far off). Offers a dig at Saijah's patron-pull and a little menace. GM only: a door stays open to make Ylva powerful another way -- she has no idea it exists.")

label("VARON -- the deadliest goof")
plain("The most lethal blade on Tamriel, reduced to hovering since he tried to kiss Saijah and she bolted. He catches you alone:")
plain("**VARON:** \"Does she -- is she still -- never mind. Forget I said. ...How was the mountain.\"")
gm("Light relief + the Saijah thread. He won't push the Grelod clock here -- too distracted. No mechanics; texture and a laugh.")

label("GEAR & ESBERN")
bullet("**GEAR:** has been quietly cataloguing Mila -- the construct studying the child. If addressed, states flat observations ('elevated stress markers; she rations food she does not eat') with no notion it's unsettling.")
bullet("**ESBERN:** buried in his books and winding tighter -- \"We should not be sitting still. We leave soon -- yes?\" Nudges (gently) toward Bleak Falls / the Dragonstone.")

# ================= SCENE 9: ORION / GRELOD =================
scene("9   ORION'S BUSINESS: GRELOD / HONORHALL")
subtitle("NOT a dungeon -- social investigation + infiltration. No combat unless Orion makes it. The solution is his; do NOT suggest it.")

label("THE JOB + FOUR MASTERS")
plain("Brotherhood contract (client: **Aventus Aretino**) to kill **Grelod the Kind** -- the most beloved woman in Riften, secretly running a child-abuse / Thieves Guild training pipeline. He must also deal with **Constance Michel.**")
gm("The Ring check-in already happened: Valerius ordered Constance enthralled THROUGH the Ring -- and in doing so taught Orion two things: he CAN enthrall (if fully sated), and the Ring has BLIND SPOTS (Valerius isn't always listening). He knows he could hide a betrayal.")
bullet("**Aventus (client):** Grelod SUFFERS. Children KNOW they're free. Public.")
bullet("**Maven / Guild:** pipeline continues. Constance takes over. No disruption.")
bullet("**Valerius (Ring):** Constance enthralled through the Ring -> Court asset.")
bullet("**Orion himself:** obey Valerius, or take Constance for himself?")
plain("**VARON** isn't pushing the clock -- he's **distracted.** The deadliest blade on Tamriel, turned nervous and goofy because he tried to kiss Saijah at the bar, she dodged and bolted, and he's been replaying it since. If Grelod comes up at all it's half-hearted: \"Contract's nearly spent, I know... do you think she's still angry? Saijah. Do you -- never mind.\" Lethal everywhere except within ten feet of her. (The Grelod urgency is narrative -- every day she lives, the children suffer -- not Varon nagging.)")

label("BELOVED 1 -- THE MARKET SAINT")
readaloud(["The crowd parts with warm murmurs. A small elderly woman in a grey dress, wicker basket on her arm, white hair under a modest cap -- the face of someone's grandmother. Every merchant greets her by name. 'Mother Grelod!' Madesi presses a silver pendant into her hand. 'For the children.' Balimund hands her new blankets. 'Kynareth bless you -- the little ones will sleep warm.' A guard tips his helmet. A merchant's daughter hugs her legs; Grelod bends with effort and smooths her hair. She moves on, trailing warmth."])
label("BELOVED 2 -- THE MEMORIAL SPEECH")
readaloud(["Grelod stands at the plague memorial, voice thin but carrying. 'We lost good people. But Riften endures because we care for each other. The orphanage took in six children during the plague. They told me they were scared, and I told them what I tell every child: You are safe now. You are loved. You will never be alone again.' The crowd applauds; three people embrace her before she can leave."])
label("BELOVED 3 -- THE UNTOUCHABLE")
plain("A newcomer grumbles about coin going to the orphanage. The room turns on HIM -- a regular toasts \"Mother Grelod, the kindest soul in the Rift,\" a guard walks the grumbler out. Orion watches every door to an accusation close at once.")
label("BELOVED 4 -- BJORN, CHARMED  (before he knows who she is -- HOLD THIS BEAT)")
plain("Bjorn, running an errand, sees a gracious old woman struggling with a heavy basket. De-aged by the dragon souls, he looks slightly younger than her.")
plain("**GRELOD:** \"Oh -- you mustn't trouble yourself --\"   **BJORN:** \"Ma'am, a man who won't carry a kind woman's basket isn't much of a man. Here. Where to?\"   **GRELOD:** \"Such manners. What's your name, young man?\"   **BJORN:** [a rusty grin at 'young man'] \"Bjorn. My pleasure, ma'am.\"   **GRELOD:** \"You'll make some lucky woman very happy.\" [pats his arm, moves on]   **BJORN:** [to himself] \"...Huh. Riften's not all bad.\"")
gm("The horror is retroactive. When Bjorn learns who she was, he can't square it -- his own charmed reaction makes him DOUBT the party: \"That sweet old woman? You're SURE? The whole city loves her.\" Their moral anchor doubting them is the loudest proof no one will ever believe Orion -- it isolates him. Press with evidence and he comes around, sick about it; the instinctive doubt is the point.")
label("ABUSE 1 -- THE PRIVATE CRUELTY / HROAR  (only if Orion watches after dark; Hard Guile -4 to approach unseen)")
readaloud(["By the ninth bell a light burns in Grelod's upper quarters. Through the window: a different woman. She reviews a ledger with a quartermaster's focus. A boy, maybe ten, holds a heavy book on each outstretched palm, arms trembling. She does not look up. 'Your hands are shaking, Hroar. A pickpocket with shaking hands gets caught. Worthless children do not eat breakfast. Hold them steady, or you hold them until morning.'"])
label("ABUSE 2 -- THE CELLAR / LUCIA")
plain("Via Saijah's senses through the wall, or Orion's night-watch: Grelod locks **Lucia, 10,** into the lightless cellar for taking bread. Lucia begs; Grelod stays flat: \"You'll come out when you've learned what hunger is for.\" The door shuts. (This is why Lucia won't enter a dark room.) Only the party sees this.")

label("THE PEOPLE")
plain("**GRELOD:** public = warm grandmother who LOVES visitors (they validate her); private = flat, precise, no affect; a light sleeper, upstairs only after the kids are abed. If the party visits, she tours the main hall (children playing, too-perfect, too silent -- they track her hands, not her face). Asked about upstairs: \"Just my quarters. An old woman's clutter.\" -- **Very Hard Guile (-6)** to catch the lie.")
plain("**CONSTANCE MICHEL** (the moral center): late 20s, knows everything, does the real caregiving, silenced years ago by a Guild man; stays for **Jon**, age 6. Talk privately, away from Grelod:")
bullet("**Standard Guile:** she'll talk -- \"everything is fine\" (the reflex).")
bullet("**Hard Guile (-4):** past the wall -- \"She's protected. The Guild, Maven, the guards. They'll believe her, not me, not the children.\"")
bullet("**Very Hard Guile (-6):** the full picture (training, pipeline, the threat, why she stays). Cries silently; wipes her eyes before any child sees.")
gm("If she witnesses the kill she does NOT scream or call guards. She closes the door and asks: \"What happens to the children now?\" -- the enthrall trigger.")
plain("**AVENTUS ARETINO** (client, at the Bee and Barb): adult ~30s, scarred hands -- she broke them twice. WANTS: \"I want her to suffer. For them. And I want the children to KNOW. Publicly. Undeniably free.\" Siblings still inside: Hroar, Runa.")

label("LAYOUT & SECURITY")
bullet("Kitchen back window (canal entry): **Easy Agility (+2)**.  Front door at night: **Hard Agility (-4)**.")
bullet("Upstairs door locked at night; Grelod sleeps UPSTAIRS. Desk drawer (ledger): **Hard Agility (-4)**.")
bullet("Chest under bed: **Very Hard Agility (-6)** -> 800g coin, Brynjolf letters, list of 'graduated' children + Guild assignments.")
bullet("Training room: master lock, **Very Hard Agility (-6)** or Grelod's key -- practice locks with bloody small fingerprints, leather strap, sewer-map chalkboard, stopwatch.")
bullet("No guards -- the conditioned children ARE the security. Guild check-in Thursdays. Grelod's day: public AM -> training 2-6pm -> dinner performance -> kids abed by 8 -> ledger till midnight. Constance: up first, last to sleep.")

label("THE KILL: CONSTRAINTS  (Orion's solution; do NOT pitch these)")
bullet("(a) Public exposure -> Jarl arrest/execution (**Very Hard Guile -6** to present evidence; satisfies Aventus, kills pipeline, Maven enemy).")
bullet("(b) Silent kill + framing (no suffering, pipeline preserved).")
bullet("(c) Theatrical kill before the kids (Aventus's dream; traumatic but free; Maven enemy).")
bullet("(d) Expose the training room publicly, then quiet kill in the scandal (suffering + deniability).")
gm("MAVEN: quiet death = she shrugs; public destruction = serious enemy who investigates (Delvin warned him in the Flagon). [Optional, his to find: Orion can try to win Maven's blessing to remove Grelod during the sec-11 debrief -- Very Hard Guile -6.]")

label("THE INFILTRATION: GETTING IN AND OUT CLEAN", red=True)
plain("For a vampire lordling, getting IN is trivial. The mission is to leave NOTHING behind -- no witness, no trace, and above all no sign of what he is. **Detection here doesn't summon guards. It detonates.**")
gm("THE STAKES (the player must feel this): the Lanterns are beloved heroes. Picture the most beloved hero in Skyrim found creeping a darkened room of sleeping orphans -- no context survives that image. And under the hero is a VAMPIRE: one child sees his eyes catch wrong, sees him move too fast, sees him feed -> 'the monster wears the hero's face,' and that thread unravels the party, Valerius, the whole Court. Every witness is a two-jawed trap: kill them (a child -- the moral floor) or leave them (and pray). The art is being seen by no one.")
plain("**VAMPIRE GIFTS ARE HIS** -- but they trivialize the PHYSICAL challenge, not the CONSEQUENCE. Power is the LOUD path; each witnessed use of the inhuman is another thread.")
bullet("Quiet/speed: sneaking is trivial UNLESS someone is looking. Nightsight: the dark Lucia fears is his medium (no candle).")
bullet("The Voice / seduction: can settle a half-woken child or still Constance -- but glamour on a child is its own weight, and a glamour a second pair of eyes catches is the worst tell.")
bullet("Feeding: he must come ALREADY SATED to have the self-enthrall option (B); he will NOT feed on a child. Mist/shadow (by tier): the clean exit.")
plain("**THE CHILDREN ARE THE ALARM** (this IS the mission -- a field of fuses, not one roll):")
bullet("**Samuel (13)** wakes -> conditioned to REPORT to Grelod. Worst draw.")
bullet("**Sofie/Fastred** wake -> cry -> wake others, draw Constance.  **Lucia (10)** stirs in dark -> panics.")
bullet("**Mila (8)** wakes -> not broken; challenges aloud.  **Hroar/Francois** (broken) -> wake and WATCH in silence -- a kid who saw a Lantern kill its tormentor is its own dangerous witness.")
gm("A fumble doesn't just 'alert' -- it tells you WHICH child stirred, and that child sets the shape of the trouble.")
plain("**CONSTANCE = the patrol he CANNOT remove.** Roving (carries Jon, hushes criers), no fixed post. Killing her fails the contract 3 ways (Aventus + kids + Valerius all need her alive). If she catches him pre-kill it's a scene, not a fight -- she knows what Grelod is; she may whisper \"...Are you here for her?\" -- she might even HELP.")
statcard([
    "**THE EXPOSURE LADDER  (run this, not pass/fail)**",
    "CALM     -- a ghost. No one knows anyone was here.",
    "STIRRING -- a thread: a sound, a half-seen shape, a moved object. Recoverable.",
    "ROUSED   -- a witness is awake and knows a person is here. The trap is open.",
    "EXPOSED  -- the inhuman is seen, or a witness who'll be believed. Catastrophe.",
    "",
    "Failed beat = +1 rung.  Samuel reaching Grelod = +2.  Witnessed inhuman -> EXPOSED.",
    "STIRRING/ROUSED walk back (settle the child, vanish, wait). EXPOSED does NOT reset.",
])
gm("EXPOSED transforms, it doesn't end the night: rumor by morning -> the Jarl's questions, Maven's leverage, the Brotherhood exposed as contractor; or a whisper-hunt for the thing wearing a Lantern's face; or Valerius's cleaners move on a house full of witnesses (a horror Orion authored). The cost stays and compounds. NO hard reset.")
gm("INVESTIGATION BUYS IT DOWN: Runa's trust -> creaky boards, Grelod sleeps light, where the key hangs (biggest edge). Blaise -> the Ratway/canal approach unseen. Constance's trust -> upstairs layout + locks. A thorough Orion glides; a rushed one finds the fuses with his shins.")

label("THE FIRST KILL  (his first by DECISION, not hunger)", red=True)
plain("He has killed to FEED -- hunger chooses, the body is fuel. This is the other thing: no hunger, just a name on a contract and his own will. Tonight makes him an assassin in fact, not just in title.")
readaloud(["She is small in sleep. The blanket rises and falls. Up close she is exactly what the city sees -- a tired old woman with white hair and a grandmother's hands, wrists thin as a girl's. Nothing about her asleep argues for what he came to do. The argument is in a locked room one floor up, in bloodied lockpicks and a leather strap on a hook, and he has to hold that room in his mind while he looks at this face."])
plain("**IF SHE WAKES:** no scream, no fear -- orphans have threatened her forty years and she outlived them all. No struggle he can dress as self-defense. Flat: \"...Of course. Orphans always come back. You think you're the first to stand there? Get on with it, then. Or put the knife down and crawl back to whatever they made of you.\" She gives no mercy and asks none; she makes him do it eyes open.")
gm("THE LOAD-BEARING RULE: do NOT narrate what Orion feels. No guilt, no ease, no meaning. Present the body, the stilled breath, the silence, his own hands, the one fact that it can't be undone -- then STOP. His player names it, in his time, or not at all. The weight is the gift; don't spend it for him. (If he feeds to kill, it leaves his signature in her blood -- one more thread.)")

label("THE ENTHRALLMENT: CONSTANCE  (after the kill)")
bullet("**A -- via Ring (obey Valerius):** she's the Court's. Perfect cover. Kids feed a vampire lord intel. Orion gains nothing personal.")
bullet("**B -- own power (requires FULLY SATED):** she's ORION's. Valerius blind to it (the blind spots) -- catastrophic if discovered. Personal Riften network.")
bullet("**C -- don't enthrall:** she runs a real home; children actually free. Valerius's order disobeyed -- he notices eventually.")
bullet("**D -- via Ring + GOOD orders:** obey Valerius AND make her protect the kids + report. The 'pragmatic' answer. Still mind control. Better than Grelod?")

label("AFTERMATH & CHILDREN")
bullet("**Quiet death:** Constance takes over; pipeline continues; Aventus disappointed but accepts; Maven doesn't notice.")
bullet("**Exposed AND killed:** scandal rocks Riften; Maven FURIOUS, loses the pipeline, investigates; kids placed under Constance by the Jarl; Aventus weeps -- \"They're actually free.\"")
bullet("**Orion refuses:** reverts to general assignment; another assassin does it messily; Brotherhood notes the refusal; Grelod dies worse.")
gm("CHILDREN (not props -- give them specific moments): Hroar(14, bleeding-hand star pupil) / Runa(15, oldest, knows the routine, cracks if trusted) / Samuel(13, child-spy) / Lucia(10, fears the dark) / Sofie(9, grooming phase) / Jon(6, silent, Constance carries him) / Yrsa(5, the kids' one protected thing). EDGE: cart-Mila just escaped child-abuse; tonight Orion walks a child-abuse factory. The Vow is live; even Bjorn was fooled -- that's how total her cover is.")

# ================= SCENE 10: DANICA =================
scene("10   THE DANICA FAREWELL + THE DYING RUNNER")
subtitle("Danica left WITH KRUSP'S GROUP last session; not rejoining. She + Krusp are tending the dying Stormcloak runner upstairs (they're Windhelm-bound) -- which is where the party crosses them. NO money beat: she keeps the bounty to fund the Windhelm work ahead.")
readaloud(["Danica finds you before you find her. She's dressed for the road now -- mail under the priestess robes, a pack already shouldered, Kynareth's light worn like a weapon. Krusp stands a few paces behind her, arms folded, saying nothing. She stops in front of you and doesn't sit down."])
plain("**DANICA:** \"I'm not here for a scene. I'm here because I don't leave debts or doors I haven't closed. I wanted to say it to your faces: thank you for the start. And goodbye.\"")
gm("DAVINIA'S CHANCE -- THE AMULET OF MARA: if Davinia tries to give Danica the amulet, LET HER TRY. As she reaches/speaks, the Crown does its quiet work -- the words arrive as a transaction, framed and controlled; or her right hand moves wrong (Ismara's architecture) so the gesture reads as a price, not a heart. Don't roll it away; play the wrongness.")
plain("**DANICA** (going still): \"...What is that.\" Then, understanding: \"You're doing it again. A symbol instead of the thing. You can't hand me a marriage charm in place of an apology, Davinia. When you can stand in front of me with empty hands and just say the true thing -- come find me. Not before.\" She doesn't take it.")
gm("This very likely DIGS THE HOLE DEEPER, and that's correct -- the point is that Davinia reaches and the table watches the Crown and her own detachment sabotage the one honest thing she wanted. Door still 'cracked to a paw print': Danica returns only on a genuine reckoning.")
bullet("**KRUSP** (only if addressed): \"I told you at Kynesgrove what I thought of you. Nothing's changed it. But this is her business, not mine.\" If threatened: \"Try.\"")
bullet("**Alfonso callback:** last session he was unexpectedly KIND to Danica and called her leaving a mistake. If he speaks here that warmth can return -- the monster gentler to her than her own leader managed.")
label("THE DYING RUNNER -- WINDHELM INTEL  (a few questions before he fades)")
bullet("**Situation:** Galmar's army is rotting from a plague the healers' magic only FEEDS; Galmar holds the barricades alone and begs them to come.")
gm("THE KEY: this is NOT Antoine's Strain 1.0 -- it is **Alfonso's own pathogen**, the living Korvanjund plague he seeded into the Stormcloaks. So the native expert on the Windhelm sickness is **Alfonso** -- it's his disease, read from the inside. That's the Fire-A leg-up: his understanding (and the Codex's GRAVITAS Keeper's-Stay, not healing) is the answer no one in Windhelm has. And Danica is walking straight into the lesson that Restoration feeds it -- the thing that scars her lungs.")
exit_("She rides out with Krusp's people -- toward Windhelm, and the quarantine that will scar her.", "11  MAVEN")

# ================= SCENE 11: MAVEN =================
scene("11   MAVEN DEBRIEF + PROMOTION  (Meadery office; NOT gated)")
subtitle("They hold enough to satisfy the contract (Forelhost location + the Meadery evidence). Running the dungeon only strengthens it. She points them to Hemming after.")
readaloud(["Up a narrow stair to a door you didn't know existed: a small, functional office. A heavy oak table buried in ledgers, trade-route maps, correspondence under half the holds' seals. An iron lockbox bolted to the floor. Maven at the head -- no housecarls, no drink, no performance. The amused matriarch is gone. This is the woman who runs Riften's criminal infrastructure, working. 'Sit. Show me what you found.'"])
bullet("**The intel:** a living Dragon Priest (Rahgot) + his alchemist (Antoine) out of FORELHOST poisoned her Meadery (Tears of Rahgot). If they ran the dungeon: the journals, sealed culture samples, the Strain 2.0 folder.")
plain("Her hands go still -- not because she knows Rahgot (she doesn't) but the implication: an ancient power used her city as a test site and her operation as an ingredient. \"A Dragon Priest. An hour south of my city. Using my Meadery to run a field test. He doesn't know my name. He will.\"")
label("HOW MAVEN TAKES IT  (run her reactions -- don't just read the offer)")
bullet("**To the intel itself:** the amused matriarch is GONE. Very still, then very precise -- the woman who actually runs Riften, working a threat to it. She does not fear Rahgot; she is OFFENDED. \"He used my city. My operation. As an INGREDIENT.\" She wants him found.")
bullet("**To the cosmic scale (Strain 2.0 / apotheosis):** she doesn't grasp it and won't pretend to -- she narrows it to what she owns: \"I don't care what he wants to become. I care that it started in my mead. Cut the root.\"")
bullet("**If they ACCEPT (patron):** brisk, satisfied, instant -- counts the advance, names terms, treats them as hers from that breath. The warmth is transactional but real: \"Good. You're mine now. Try not to make me regret it.\"")
bullet("**If they REFUSE:** no anger -- a long look and a cooling. \"...Pity. I don't ask twice.\" She still PAYS the bounty (a debt is a debt), but the open doors quietly shut -- no network, no harbor, no advance. NOT an enemy; she remembers. She'll still send them to Hemming (that gratitude is his, not hers to withhold). [THIS is the branch they took.]")
bullet("**If they NEGOTIATE:** independence and refusal-rights she grants easily (she respects a hard bargainer); transparency into HER business is a flat no -- press it and the temperature drops fast.")
bullet("**The 5,000g bounty:** counted out of the lockbox. Debt settled.")
plain("**THE PROMOTION (the patron offer):** \"Hunt Antoine and his master. Dismantle it. Bring me Antoine ALIVE. In return, the Black-Briar family is your PATRON -- funding, safe harbor in any hold my name reaches, my network Solitude to Windhelm, protection. My enemies become yours. The Obsidian Lanterns become my hand. Deniable. Well compensated.\"")
bullet("**Why alive:** \"A dead alchemist doesn't unmake what's in my mead, doesn't say who else drank it, doesn't name who he answers to. The antidote, the exposure list, the name above him. Then he can die.\"")
bullet("**Accept:** +2,000g advance; a line of credit with Keerava; she keeps the Strain 2.0 folder, they keep the journals. **Negotiate:** independence (fine), refusal rights (fine, she remembers a no), transparency into her business (HARD no). **Refuse:** the 5,000g is still theirs, but \"doors that were open are now merely... closed.\"")
gm("THE PROMOTION IS A GOLDEN CAGE: once they're her people, walking away is political, refusing is political, and every secret they carry becomes leverage if she ever learns it.")
gm("OPTIONAL -- ORION'S GRELOD PITCH (Very Hard Guile -6): if Orion frames Grelod's removal as operational security (swap to the manageable Constance), SUCCESS -> Maven authorizes it (\"Handle it. Quietly. If there's noise, I hold you personally responsible.\") -- solving his whole tangle. PARTIAL -> she asks how he knows what the orphanage really is (Hard Guile -4 to deflect, blame Krusp's investigation). FAIL -> \"Stay in your lane.\" CRIT FAIL -> \"Someone put you up to this. Who?\" -> she hunts the source. Don't pitch it; it's his to find.")
exit_("\"Hemming wants to meet the people who sent the woman who saved his life. Indulge him. Ten minutes.\"", "12  HEMMING")

# ================= SCENE 12: HEMMING =================
scene("12   HEMMING  (Black-Briar Manor; pure RP, no checks)")
readaloud(["Up through the manor to a warm bedroom -- fire in the hearth, juniper incense over the bitter undertone of healing poultices. Hemming Black-Briar propped on a four-poster, late forties, Maven's sharp features softened by a gentler temperament. Cheeks hollow, hands thin, skin waxy -- a man recently near death, only now remembering how to be alive. But his eyes are clear, and when he sees you he smiles -- real, glad, unguarded."])
bullet("Details if they look: a pressed wildflower from the memorial (Danica brought it); a blanket on the bedside chair -- MAVEN slept there every night through the worst (a housecarl confirms reluctantly). Complicates her; doesn't redeem her.")
plain("**On Danica** (quiet, reverent, touching the flower): \"They told her healing me would kill her. She knelt and didn't just cast a spell -- she GAVE something. Her actual life, pouring in. The sickness screamed -- I heard it in my blood -- and then it was gone. She was standing when she started. On the floor when it ended. She aged. Years of her life. For me. I am a merchant's son. I am not worth that. But she did it anyway.\"")
gm("DRAMATIC IRONY -- do NOT narrate: Davinia drove Danica away; Danica saved Riften ALONE using the Lanterns' name because it was still hers. Hemming thanks them for 'sending' her. Let every word land on Davinia. If anyone corrects the record: \"Then she's even braver than I thought... That doesn't change what I owe you. You built the company that shaped her.\" (Worse for Davinia than the misplaced gratitude.)")
plain("**THE GIFT -- HEMMING'S LETTER OF INTRODUCTION** (personal signet): once per major city, present it to a grey-area NPC -> disposition flips to FRIENDLY for one major interaction. COST: every use permanently links the Lanterns to the Black-Briar network in that city -- a leash they put on themselves.")
gm("No checks. The most sincere person they've met -- not manipulating, not leveraging. The knife is that they didn't earn it. Don't twist it; let it sit. The Letter is a slow-burn reward -- it matters in three sessions, not tonight.")

# ================= SCENE 13: BALIMUND =================
scene("13   BALIMUND'S INVESTMENT  (the money conflict)")
subtitle("Their trusted smith. He sets down the hammer and gets straight to it.")
readaloud(["Got a moment? Good -- I'll be blunt, it's the only way I know how. Old Borgakh's forge, two holds over -- she passed last month. Skyforge-trained, best hands in a generation, and her whole shop's for sale: her tools, her private technique-notes, a stock of ore you cannot buy twice in a lifetime. On my name alone I've got first refusal. What I don't have is the coin. I'm not asking charity -- I'm asking PARTNERS. Most folk never need a master smith. You need one every other week. So this isn't really my investment. It's yours. I'd just be the hands."])
bullet("**Skill now:** funding it unlocks BURNT-SLOT RESTORATION (recover ruined improvement slots) and puts BEST-IN-SKYRIM in reach.")
bullet("**Reach (the real hook):** apprentices + a courier 'Lantern mark' -- master-grade work ON THE ROAD, not just Riften. A party that's never home needs a smith that follows them.")
bullet("**A stake:** a small recurring cut + a permanent grateful master smith -- a CLEAN relationship asset, unlike Maven's leash.")
gm("SMITH PROGRESSION (track cumulative spend; investment counts): +5,000g -> restore burnt slots. +10,000g beyond that -> best in Skyrim (can't fail an improvement; all improvement values +1).")
gm("THE CONFLICT: the buy-in (~5k) competes head-on with Bjorn's horse (a good one is 9-12k, next scene). Gear + reach vs. the Bjorn/Mila payoff vs. liquidity. There is no clean 'do it all.'")

# ================= SCENE 14: CART DEPARTURE + GATE 3 =================
scene("14   CART DEPARTURE + THE GATE 3 CHOICE  (session close)")
subtitle("First the homework, then the choice, then the road. The choice triggers the fire matrix.")
label("BEFORE THE ROAD -- DUE DILIGENCE  (optional, and rewarded)")
plain("Two of the three couriers are still here to question -- a party that does its homework walks into the fire forewarned and supplied (mirror the Grelod loop: good questions buy a real edge in the chosen fire). The third witness, the Stormcloak runner, they met at Danica's bedside (sec 10).")
bullet("**KLIMMEK (at the bar) -> the Throat, Fire B.** Shaken, fragmentary -- coax it (Guile / kindness), and Saijah's nose corroborates. He provisions the Greybeards, so he knows the **route**: the safe rest-points, the offering custom, which stretches of the 7,000 steps were worst (the time-bent zones). LEG-UP: his map and warnings = advantage navigating the climb.")
bullet("**ESBERN (in the cart) -> Bleak Falls, Fire C.** Eager to talk (he wants OUT of Riften). The Dragonstone is a MAP -- strategy over reaction; it opens Alduin's Wall. LEG-UP: real barrow intel -- the claw-puzzle door, the layout, the draugr, what the stone looks like -- plus the warning that the **Thalmor watch the door** (and, quietly, that it was Antoine's staging ground, where he is now rebuilding his wrecked processing rig).")
gm("Last session's lean: it's IVARSTEAD (the Throat) vs WINDHELM -- they weren't planning Riverwood/Bleak Falls at all. So talking to Esbern may just confirm they're IGNORING Fire C -- which has teeth: Antoine rebuilds there unobserved. Make the choice informed; don't push one.")

plain("**BJORN:** \"Before I point this cart anywhere, I want it from your own mouths. Three roads, and we can only take one. One -- WINDHELM: that boy upstairs is dying of the same sickness eating Galmar's whole army; folk are dying NOW. Two -- THE MOUNTAIN: Klimmek's seven thousand steps, bleeding black, men with faces of horn and fire, the air gone wrong. Three -- BLEAK FALLS: the old man's stone tablet; no one's dying on a clock for it, but without it we spend our lives a step behind the end of the world. So. Which is it? Mable can only face one way, and I mean to be on the road by dark.\"")
gm("Let them argue and commit. Do NOT push a hook.")
label("MABLE'S RETIREMENT + THE HORSE")
plain("**BJORN:** \"Mable took bad hurt after that dragon; she's done. She goes back to my farm to live easy -- but she stays long enough to teach the new one the ropes. So we need a new horse. A good one. And a good one isn't cheap. I've put in every coin I've got; I'm asking you to cover the gap.\"")
gm("HOFGRIR (stable by the gate) is grieving and short-handed since the frenzied horse killed his stable boy; prices are up. The surviving girl witness has described the attack -- a quiet investigation thread.")
bullet("**The Bay** -- 6,500g (was 5,000).   **The Grey** -- 9,000g (haggles slightly).   **The Black Mare** (the one Bjorn wants) -- 12,000g, not a septim less (haggle and it goes UP 100g each try).")
bullet("**The Fury Horse** -- 1,500g: the one Alfonso cast Fury on. Traumatized, flinches at noise/blood, refuses riders who recall the dead boy. Hofgrir just wants it gone.")
gm("BJORN'S LONELINESS BEAT -- gated behind a QUALITY horse (Grey or Black Mare). Buy the cheap Fury horse and it's locked. At a quiet campfire he opens up about forty lonely years in the Rift, and his terror of de-aging into the War-Hound -- but he's glad for their company. GRELOD FALLOUT: he knows her true nature now (Davinia told him); past denial into quiet fury -- the inn flirtation is retroactive horror.")
gm("MONEY CRUNCH: a horse (1,500-12,000g) + Balimund (~5k) + a reserve. They cannot fund everything. Buying a quality mount vs. cheaping out on a traumatized beast reflects their care for the child's guardian.")
label("THE FIRE MATRIX  (on the moment they commit)")
gm("Narrate Krusp's True Wardens taking the SECOND fire (+ its attrition) and apply the IGNORED third fire's world effect.")
bullet("**FIRE A -- WINDHELM BARRICADES:** PARTY: Alfonso raises a Stormcloak thrall-army, seeks the Afflicted Conclave scripture (phylactery cure-lead), Orion runs the Hroki contract, Davinia's lie to Galmar comes due. KRUSP TAKES IT: he + Danica quarantine and purge -- Danica contracts the rot, lungs PERMANENTLY scarred. IGNORED: Stormcloak army collapses; Windhelm sealed; the Cult claims ~5,000 corpses; the Empire takes Eastmarch.")
bullet("**FIRE B -- THE BLEEDING STAIR:** PARTY: Saijah climbs; GAELEN the Root-Twister's intro at the Time-Wound; her Kynareth-vs-Hircine choice forced; Bjorn-Dragonborn pressure near High Hrothgar. KRUSP TAKES IT: shields the waystones -- a close hireling is caught in a time-stutter, aged to dust. IGNORED: Dagon clock jumps; the steps fracture into Deadlands loops; the Way of the Voice closes. MOST cosmically dangerous to leave.")
bullet("**FIRE C -- THE DRAGONSTONE / BLEAK FALLS:** PARTY: silent infiltration vs a THALMOR blockade; retrieve the Dragonstone; **Alfonso can intercept Antoine here, rebuilding his processing rig** (the party wrecked his Forelhost one); opens Alduin's Wall / Sky Haven. KRUSP TAKES IT: secures the stone -- a young guide is captured and executed. IGNORED: the stone is lost to a Cult retrieval; Sky Haven stays closed; the party stays permanently reactive.")
label("SESSION CLOSE")
bullet("**Ride out:** the cart rolls; the world tilts -- Krusp toward the second fire, the ignored third worsening off-screen.")
bullet("**Award:** \"For tonight, you each gain 1 Advancement Point.\" (Forelhost makes it a meaty session; earned either way.)")
gm("LOOK-AHEAD (read the one for the chosen fire): WINDHELM -- \"the wind off Windhelm carries woodsmoke and something sweet and wrong underneath; Galmar is holding a wall he doesn't know you helped build. We'll end there.\" THROAT -- \"Saijah's wire pulls tighter every mile; the air at the foot of the steps already tastes like time going wrong; somewhere up there a gardener is humming.\" BLEAK FALLS -- \"Esbern clutches three books and a thirty-year hope as the barrow rises over Riverwood -- and so do the gold-eyed patrols already watching its door.\" If they bail all three: the world doesn't wait -- TWO fires escalate. Close on the cost.")
exit_("Stop. Next session opens on the chosen fire.", "12  OPEN THREADS")

# ================= SCENE 15: OPEN THREADS =================
scene("15   OPEN THREADS  (carry forward, not for tonight)")
bullet("**Strain 2.0 clock:** lengthened -- 6-8 weeks AFTER Antoine harvests from Ulag, AND he must rebuild his processing rig at Bleak Falls (they wrecked the Forelhost one). The trap got NO Alfonso sample -- Ulag is now his ONLY route. Catch Antoine at Bleak Falls, or reach Ulag first, and Strain 2.0 never exists.")
bullet("**Ulag / Forelhost:** the Dwemer core survived -- Forelhost still holds Ulag in STASIS, but its disease-processing (Antoine's copper additions) is dead. Rahgot is AWAKE and traveling; the five-priest Konahrik apotheosis prophecy.")
bullet("**Maven patronage** (if accepted): the golden cage tightens; refusing her jobs becomes political; their secrets become her leverage.")
bullet("**Balimund:** cumulative-spend thresholds now active (5k -> burnt-slot restoration; +10k -> best in Skyrim). Track total spend. **Hemming's Letter:** one grey-area NPC per city flips Friendly; each use entangles them with Black-Briar.")
bullet("**Orion:** the Constance enthrall choice (A/B/C/D), and whether he obeys or usurps Valerius via the Ring's blind spots.")
bullet("**Riften's coming plague (background -- pull later):** Mila's mother is alive in the Warrens, an asymptomatic carrier of Alfonso's living strain, and back on skooma -- spreading it. Alfonso's plague is DIVINE pestilence: it evolves on its own, fast. It will grow new vectors (an STD among the rest) and, in time, ravage Riften. Tick it quietly off-screen; the party caused it and doesn't know.")
bullet("**Davinia:** CDI 0.45; father's network alerted after the Solitude gate. Ledger at grant 1 of 5. **Alfonso:** Deep Rust set by his reform CHOICE -- forcing the body back advances it; staying a sword arrests/reverses it. Surface rust = spell fuel, resets on rest. **Saijah:** Hircine's 'free trial' senses; the Kynareth/Hircine crossroads; the Ylva rivalry; holds both Hawk tokens.")

# ---------------------------------------------------------------- write
with open(OUT, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
    f.write(HEADER)
    f.write("".join(buf))
    f.write(FOOTER)
print("wrote", OUT)
