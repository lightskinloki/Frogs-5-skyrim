# -*- coding: utf-8 -*-
# Generator for FIRE B -- THE ROAD & THE BLEEDING STAIR (full module RTF).
# Sources: RUNSHEET - the road to Ivarstead (revised), IVARSTEAD bible, scratch §5/§10/§11,
# Npcs/new mythic dawn leader, Npcs/Valerius, Npcs/the black mare. Run: python _build_ivarstead_rtf.py

import os

OUT = r"C:\Users\fbrown\Projects\Frogs-5-skyrim\Toryggs legacy\Adventure modules\choice gate 3\FIRE B - THE BLEEDING STAIR (full module).rtf"

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
raw("\\pard\\sb60\\sa40\\cf2\\b\\fs44 FIRE B -- THE ROAD & THE BLEEDING STAIR\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i Riften gates -> the foot of the 7,000 Steps -> Ivarstead -> the undercroft of High Hrothgar. The campaign's relaunch: one place, one escalating problem, a clean arc with a curtain. ~3 sessions. Self-contained -- run the whole fire from this file.\\i0\\cf1\\par\n")
rule()

label("THE SPINE (hold these three lines all module)", red=True)
bullet("**This is an INTRODUCTION.** It ADVANCES threads and RESOLVES nothing personal. Saijah chooses NO patron. Gaelen does NOT die. The crossroads is loaded, never fired.")
bullet("**Frame the objective OUT LOUD as THE RITUAL, never as Gaelen's head.** If they think the mission is 'kill Gaelen,' his escape is a robbery. If they know it is 'stop the Unmaking,' his escape is just Thursday.")
bullet("**Secrets that must hold:** Bjorn's speed reads as REJUVENATION, never Dragonborn (no one can sense a Dragonborn -- not even the Greybeards, who have NO special senses of any kind). Ismara stays unwitnessed by the monastery. The two scout dragons' target stays unknowable.")
plain("**Roster on the move:** Davinia (ISMARA fronting -- silver skin), Saijah (bearing ALFONSO the rapier), Orion. Cart: Bjorn, Mila, Esbern (hidden until Scene 1), Nora, GEAR, Ylva, Varon. Animals: Mable (old, dragon-shaken) + the BLACK MARE (fearless warhorse -- sheet: Npcs/the black mare). Krusp & Danica are GONE to Windhelm. **Everyone climbs** -- Part Two explains why in fiction.")

rule()
raw("\\pard\\sb120\\sa200\\cf2\\b\\fs40 PART ONE -- THE ROAD\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i A quiet leg doing three jobs: re-introduce Esbern (comedy + strategy), give the table a breath (respite + personal threads), and teach that the dragons own the sky (the hide). Normal physics the whole way; the first faint time-wrongness only at the very end.\\i0\\cf1\\par\n")

label("GM RULES -- \"TWO SHADOWS\" (the dragon hide)", red=True)
statcard([
    "**THE NOTICE CLOCK -- 6 boxes, starts empty. Not a fight; a hide.**",
    "Two Krosulhah-tier dragons hunt overhead; they tick toward awareness on the",
    "party's OWN mistakes. 5 COMPLICATION BEATS, each tied to a party asset.",
    "Responsible character rolls vs an escalating difficulty:",
    "  Beat 1 Easy(+2) -> Beat 2 Standard(0) -> Beat 3 Hard(-4) -> Beat 4 Hard(-4)",
    "  -> Beat 5 Very Hard(-6)",
    "Success: contained, no Notice.   Failure: Notice +1.",
    "Fumble (nat 20): Notice +2; a dragon banks toward them (next beat one step harder).",
    "Crit (nat 1): active masking -- Notice -1 (min 0); next beat one step easier.",
    "PROACTIVE PLAY: every smart move drops the next beat a step or grants Advantage",
    "(douse fires, still the cart, Orion scouts breathless, Ismara sheathes heat in",
    "cold, GEAR powers down on permission). Say YES to cleverness.",
    "FAIL STATE (Notice 6): spotted -> they dive. TELEGRAPH the unwinnability hard",
    "BEFORE this. If they fight anyway it is a TPK and you warned them.",
])
plain("**THE FIVE TELLS:** 1) MABLE SPOOKS -- Bjorn rolls (animal handling); the Black Mare in harness beside her = one step EASIER (the fearless horse steadies the frightened one). 2) GEAR HUMS -- Saijah/Orion (Guile); GEAR needs PERMISSION to power down (Cognitorium callback). 3) ALFONSO'S ROT-AURA drifts downwind -- Saijah (bearer); auto-success if she lets Alfonso pull the aura tight through the link. 4) A SMALL HUMAN SOUND (Mila's frightened breath) -- Bjorn or Saijah; comforting her IS the roll. 5) HEAT BLOOM -- Davinia/Ismara can sheathe the cart's warmth in cold -- but using the gift is a quiet temptation (the sweet pull of the power).")

# ---- SCENE 1
scene("1   THE OPEN ROAD -- and the man in the floor")
subtitle("Set once Riften is well behind them. Purpose: the breath, and Esbern's comedy re-entry.")
readaloud([
    "The gates of Riften shrink behind you, and the road's first long bend folds them away into golden hills of grass. The road climbs. The autumn light is thin and clean, the cart wheels find their rhythm, and mile by mile an old, half-forgotten feeling settles over the company: ease. Full packs. Paid coin. Warm bread from Riften's ovens still soft in the saddlebags, sun on your backs, and a road that asks only that you follow it.",
    "Mable plods. The new black mare walks beside her with her head high and her ears forward, unhurried, reading the hills the whole while. And from somewhere under the cart's floorboards, muffled by canvas and the false bottom, a dry old voice says, with enormous dignity: '...Are we far enough now? My legs fell asleep a day ago.'",
])
gm("Nobody has thought about Esbern since Riften. Let it land -- a pause, the slow dawning. Play it for the laugh.")
plain("**ESBERN** (climbing out, stiff, blinking at the open sky): \"You forgot me. Two days. The last loremaster of the Blades -- the one man alive who can read Alduin's Wall -- and I have been riding under your floor with the turnips, because every single one of you forgot I was there.\" (beat) \"Magnificent. Truly. The fate of the world is in careful hands.\"")
plain("**Why he was down there** (if asked): \"The Thalmor have a standing warrant on me, and Riften is crawling with their eyes. Out here I am just an old man on a cart. Now -- where are we going, and what fresh end of the world am I to help you with?\"")
exit_("Once the laugh settles, he reaches back into the false bottom and pulls out the board.", "2  ESBERN'S WEB")

# ---- SCENE 2
scene("2   ESBERN'S WEB -- the strategic briefing")
subtitle("Never a wall of lore. He shows them the web and they pull answers out of it by touching pins.")
plain("He unrolls a cracked hide map weighted with stones, and over it a folding lap-board strung with pins and twine -- thirty years of his Ratway walls condensed into one carryable object. **TWO COLORS OF THREAD, and he is fanatical about never letting them touch.**")
label("RED THREAD -- the dragons (a war)")
bullet("Five sleeping priests, each pinned to a tomb: **NAHKRIIN -- VOKUN -- RAHGOT -- OTAR -- MOROKEI.** Rahgot's pin has been moved OFF its tomb and left dangling (their own report: he rose and walked out). Esbern keeps touching the dangling pin like a sore tooth.")
bullet("Above all five, a sixth marker: **KONAHRIK.** \"When the five become one, the faithful shall ascend.\"")
bullet("Kynesgrove -- the first grave they watched come alive. Dozens of burial mounds in fading ink. And the HOOK: **blank spaces** -- mounds he knows exist and cannot place. He hates the blanks more than he hates the Thalmor.")
label("GREY THREAD -- the root-rot (an unmaking)")
bullet("The Eldergleam, corrupted. The 7,000 Steps, bleeding. The Throat of the World, circled three times in charcoal. NOT ONE thread crosses from grey to red -- and if a player ties them together, Esbern physically stops their hand: \"No. Two ends of the world, two different authors. Muddle them and you'll parry the wrong one.\"")
label("WHAT HE SAYS AT THE PINS (in pieces, reacting to what THEY know)")
bullet("**On the two apocalypses:** \"Two different ends, walking toward us from two directions. The dragons want to rule a dead world. These root-rotters -- Dagon's people -- want there to be nothing left to rule. The dragons are a war. The other thing is an unmaking.\"")
bullet("**On where they're going:** \"The Throat of the World is not just the dragons' holy mountain. It is a PILLAR -- one of the stones that holds the floor of the world up. If the cult cracks it, time itself runs in the cellar. That's what your archer feels.\"")
bullet("**The thing he actually wants** (taps a blank spot): \"Bleak Falls Barrow. There is a stone in it -- the Dragonstone -- a map of every dragon grave in Skyrim. Without it we wait for each dragon to find US. Everything we do until we have that stone is a flinch, not a plan.\" -> Plant it. Don't resolve it. He will say it again the whole campaign.")
gm("Esbern is the lore-dump risk incarnate. NEVER let him monologue -- cut him off with a complication, a question, a beat of Ylva groaning. The clue is in the conversation, never in the dump.")
exit_("Dusk finds lantern light around the road's next bend.", "3  THE TENT FAIR")

# ---- SCENE 3
scene("3   THE RESPITE -- Ahkari's tent fair")
subtitle("A deliberate breath. Warmth, color, the world being alive. NO threat.")
readaloud([
    "The road bends around a stand of red oaks and the dusk ahead is full of lantern light. A ring of tents -- seven, eight of them, dyed saffron and sea-green and patched a hundred times -- stands pitched on the flat ground off the verge, arranged like a tiny town with a cookfire for a square. Rugs are rolled out between the tents and laid with goods: rows of stoppered bottles, hanging bundles of dried herbs, blades in shapes you don't see in Nord smithies. Pack-laden travois lean against the tentpoles; these people came on FOOT, carrying all of it.",
    "A Khajiit in a coat of a hundred patches spreads her arms wide as you approach. 'Ah -- travelers! Good ones, this one can tell, the road is kinder with company. Come, come -- Ahkari has tea, has trinkets, has STORIES, and the stories are free because no one buys them anyway.'",
])
plain("**Why the tents** (only if asked; she says it lightly, an old wound worn smooth): the cities do not let Khajiit inside the walls. So they build their own little towns outside them, a night at a time -- a traveling fair of everything the walled markets never stock.")
label("TRADE -- the exotic fair")
bullet("**Alchemists:** rare reagents the Rift's shops never carry (ash-country fungi, marsh venoms, moon sugar derivatives) -- feeds the Ismara cure-thread and Nora's bench.")
bullet("**Exotic weapons:** blades and bows from outside Skyrim's smithing traditions -- Gear-list racial styles, an Envenomed hunting bow, quality poisons (a Paralysis Poison at a price). Plus arrows for Saijah, small enchanted oddments, road food. Fair-ish prices; haggling is social, not a fight.")
label("RUMORS (roll d20 or pick)")
bullet("**1-5:** \"Ivarstead is emptying. Half the village ran. The other half is too poor or too stubborn -- and something's wrong with the TIME up the steps. A pilgrim walked three days and came down having aged a week.\"")
bullet("**6-10:** \"Windhelm sealed its gates. Plague. They say the Stormcloak army is rotting from the inside -- and that two strangers, a grim swordsman and a coughing priestess, walked IN when everyone sane was walking out.\" [Krusp & Danica, heard as rumor.]")
bullet("**11-15:** \"Black-Briar's looking for someone. Quiet-like. Ahkari does not ask who; Ahkari likes her throat where it is.\" [Seeds the Dirge thread without naming it.]")
bullet("**16-19:** \"The sky's been WRONG east of here. A hunter swore he saw a dragon -- a real one. Two of them. Going toward the Rift.\" [The scouts, third-hand; the target stays unknowable.]")
bullet("**20:** \"You've a sword that watches people. No -- don't show Ahkari. Some things this one is happier not knowing.\" [She has noticed Alfonso. Let it sit.]")
plain("**A small human moment:** Ahkari's people have a child too -- and Mila, who has spent her whole life learning to be invisible, watches the caravan kids play with the careful hunger of a girl who has never been allowed to. Let Bjorn notice. The warm thing in the chapter.")
exit_("Camp, a mile on. The last easy night.", "4  THE CAMP VIGNETTES")

# ---- SCENE 4
scene("4   DOWNTIME & CONNECTION -- the camp vignettes")
subtitle("Fire going, no walls, no Thalmor. Sequential vignettes: GM sets the situation and plays NPCs; players drive entirely. Never write a player's line or decision.")

label("VIGNETTE 1 -- ISMARA'S WORK (early evening, by the fire)")
gm("Ismara (Davinia's player at the wheel) settles with the Forelhost Codex open, the rapier in reach. She brings ONE specific technical question about Alfonso's rot-frequency vs the engineered strain, and opens the floor. AIM: she is WARM here -- genuinely useful, genuinely engaged, no manipulation running. CDI does NOT tick. This is the honey, not the sting.")
bullet("**If the thread engages:** the cure-work advances; something in her settles, briefly, into something almost human. The warmth IS the trap working as designed.")
bullet("**If it doesn't:** she closes the Codex, notes the absence without comment, and rises.")
plain("**CLOSING BEAT -- YLVA (fires the moment Ismara rises; run it HERE so it cannot be skipped):** Ylva has watched the whole time, and Ylva does not brood -- she acts. She crosses the fire and puts herself in Ismara's path. She doesn't have words for what she's feeling and doesn't reach for them: she challenges -- a spar, an arm-wrestle, something immediate and physical. She wants contact with the silver woman and doesn't know if she wants to fight her or hold her. She is in front of her now, and she is waiting.")
gm("ISMARA'S CHOICE (player-driven): engage, deflect with cool precision, or walk past -- all three land. Ylva walks away with something she didn't have before, and it isn't what she wanted; she sharpens her axe and looks at no one for the rest of the night. [GM CALL: if it reads wrong at the table, cut it clean -- nothing downstream depends on it.]")

label("VIGNETTE 2 -- NORA + GEAR (early evening, edge of firelight)")
gm("Nora with her notes on a flat stone, asking GEAR about phylacteries -- specifically whether a soul anchored in an object can be COPIED rather than transferred. GEAR answers with complete technical precision and no filter; he is describing Hjolmar's mechanism and does not know it is dangerous. The rapier is across the fire. Her eyes go to it twice.")
bullet("Does anyone notice? Does anyone intervene? She knows more by the end of it than she did at the start, regardless.")

label("VIGNETTE 3 -- NORA'S COUNSEL (mid-evening; MUST run before Vignette 4)")
plain("Nora has decided that tonight she decides about Orion. And Nora is a researcher: before any experiment, she gathers data. Three consultations, in ascending order of danger.")
bullet("**SAIJAH** (a PC -- frame the ask, the player answers): she asks straight, in her precise, over-prepared way: how do you know when wanting something is worth what it costs? She has rehearsed the question and none of the possible answers. Whatever Saijah gives her, she writes NONE of it down -- the first thing all week she hasn't taken notes on.")
bullet("**YLVA** (NPC -- sharpening, doesn't stop): \"You want him? Go lie down next to him. If he says no, come back and sharpen something. Why is this a conversation.\" (beat, the closest she comes to tenderness tonight) \"Wanting things isn't complicated, little witch. People just make it complicated so they can lose slower.\"")
bullet("**ISMARA** (player-driven -- AIM only): the dangerous one. She files everything, never lies, and is one of the only beings in camp who can SEE the Ring on Orion's finger for what it is -- and she does not spend true things unless they buy trust. A warning would be true, kind, and a deposit in the account of a girl whose soul-vessel research fascinates her. Or she says something warm and general and keeps the Ring for a better price. Open the floor; the choice is entirely the player's.")
gm("Nora hears all three, then does what she always does with data: draws her own conclusion anyway. She walks toward Orion's edge of the camp.")

label("VIGNETTE 4 -- NORA & ORION (late evening; fire burned low)")
gm("She sits down next to him -- close. This has been building a long time; tonight she decides. What she brings is earnestness: she is 18 and means it completely. She tells him something true -- why she is here, what she wants from him specifically -- and makes herself available. The choice belongs to Orion.")
bullet("**If Orion does not engage:** she accepts it without drama, says goodnight, goes to her bedroll. The door stays open. Nothing is destroyed.")
bullet("**If Orion engages:** they sleep together. The night is theirs. Nothing interrupts it.")
gm("EITHER WAY -- THE RING SAW ALL OF IT. It always does. Somewhere in Solitude, Valerius files the most valuable thing this night produced: the empty man still leans toward ONE thing, and now it has a name. NORA. When the reckoning comes (Part One's final scene -- it does NOT fire here), he arrives already holding that lever.")

label("VIGNETTE 5 -- SAIJAH & VARON (late evening, after camp quiets)")
gm("The migraine -- which Alfonso's rot-aura had been quietly dampening -- is coming back: a low directional ache, pointing south, toward the mountains. She knows what it means. Tomorrow will be different. Then VARON steps into the light across the camp, just far enough to be visible. He meets her eyes. A small gesture, no pressure: come talk, or don't.")
bullet("**If she comes:** he apologizes -- plainly, without excuse. He fled her at the moment she needed steadiness and knows the cost. He does not ask forgiveness; he offers presence.")
bullet("**If she doesn't:** in the morning there is a small carved piece left near her bedroll, made overnight. An apology in object form. He will not approach again unless she comes to him. He means it.")

label("VIGNETTE 6 -- BJORN & MILA (late evening, at the cart)")
gm("Mila can't sleep -- up on the cart, blanket around her shoulders, watching the coals. Bjorn has kept a careful distance since she asked why he feels like more than one person. Tonight he closes it. He sits, lets the silence be what it is, then tells her something true -- what a promise actually WEIGHS. That he made one once and broke it and carried it forty years, and that he is not going to let that happen again. Plain, in the voice he uses for the things that matter.")
plain("Then he gets up and shows her: left side of the horse, breathing even, hands open. The black mare -- proud, unbothered by almost everything -- suffers the careful child where she suffers nobody else. Mila brushes the mare. Somewhere in the middle of it her hands stop shaking. Bjorn watches her face and does not let her see him watching.")
exit_("Morning. The open stretch.", "5  THE HIDE")

# ---- SCENE 5
scene("5   THE SHADOW ON THE SNOW -- the hide")
subtitle("The set-piece. Two dragons, open ground, a child and an old man in a cart. The only play is to not be seen.")
label("THE TERRAIN (give the table ALL of it -- their plans are built from this)", red=True)
bullet("**THE SADDLE:** a mile and a half of open, snow-dusted ground between two low shoulders of rock; the road runs straight down the middle. The party is a THIRD of the way across when the shadows come -- too far in to go back, too far out to sprint the rest.")
bullet("**THE SCREE BANK (north):** a steep gravel embankment, 10-15 ft, undercut in places into shallow overhangs -- the ONLY overhead cover. The cart cannot get under it; people and horses pressed flat are out of a flying eye's sightline. It is LOOSE -- scree slides if handled carelessly (Scene 6 uses this).")
bullet("**THE MELT-DITCH (south):** a frozen drainage cut, 3 ft deep, parallel to the road. A person can lie full-length in it; the cart cannot. Anyone in it is hidden from above but LYING ON ICE.")
bullet("**THE CART:** canvas over bows, dirty-white and grey -- from altitude, STILL, with fire-colors hidden, it can read as a wagon-shaped drift. MOVEMENT is what kills: wheels turning, animals shifting, faces looking up.")
bullet("**Nothing else.** No trees, no walls, no structures for a mile in any direction.")
readaloud([
    "The road tops a bare rise and the land opens -- a mile and more of white, empty saddle, the sky enormous over it, and you are a third of the way across when the sun goes out. Not a cloud. A SHADOW, vast and wing-shaped, pours across the snow ahead of the cart -- and your whole body understands it before your mind does, because there is a sound with it, the long tearing rhythm of wingbeats bigger than sails, and you have heard that sound exactly twice in your lives and both times people died. Then a SECOND shadow crosses the first.",
    "Two of them. Krosulhah -- the one that nearly killed all of you -- was ONE.",
    "They wheel out over the valley, unhurried, patient, reading the ground the way Saijah reads a trail. They are not passing through. They are LOOKING for something. And every one of you knows, in the animal floor of your brain where the truth lives: if those two shapes see this cart, there is no fight. There is no clever plan. There is only how far you get before the sky comes down. They have not seen you yet.",
])
plain("**FRAME THE STAKES OUT LOUD:** you fought ONE dragon and barely lived. There are TWO. On open ground. With a child and an old man in a cart. There is no version of this fight you survive. The only play is to not be seen. Then hand them the terrain and let them work.")
gm("Run the NOTICE CLOCK (rules block, top of Part One). Walk the five tells; reward every proactive idea. **ESBERN**, low, mid-tension: \"Look at them. They aren't roosting -- they're RANGING. Ahead of something. Alduin is raising his kin and sending them out to look.\" He does NOT know their target; keep the dread general.")
bullet("**If Notice fills:** the nearer dragon's head turns, the throat lights from within -- RUN. Scatter, abandon the cart; Bjorn's speed (Scene 6) is the only thing that saves anyone. TPK is on the table and earned.")
exit_("At Beat 5, or on any failure that puts the dragons lowest -- the danger reaches Mila.", "6  BJORN'S SECOND FLARE")

# ---- SCENE 6
scene("6   BJORN'S SECOND FLARE -- the worst moment")
readaloud([
    "The near dragon drops -- not at you, just LOW, a hunting pass, its downdraft slamming the saddle like a fist. The cart rocks. A loose drift of scree comes down off the bank above in a grinding slide -- straight at the front bench. Straight at Mila. She's frozen. Bjorn is at the rear of the cart, twenty feet and a full second too far, and there is no possible way the old man reaches her in time.",
    "He reaches her in time.",
])
plain("For one impossible instant Bjorn CROSSES GROUND no man his age could cross -- there and gone, his body between the child and the falling stone -- and then he's just STANDING there, breathing hard, looking at his own hands like they belong to a stranger. Younger in the eyes than he was a second ago.")
gm("WHAT THE TABLE MAY CONCLUDE: the old mercenary is reviving -- youth, speed, the War-Hound returning. A rejuvenation. Eerie. That is ALL. The Dragonborn truth does NOT surface and must not leak (his FIRST flare was the Ratway stairs, Ch.21 -- one prior data point, still no word for it). Davinia, through Ismara's Sight, sees the doubled sun of his soul flare bright and bank down -- one more silent data point. Hold the secret.")
plain("**BJORN** (gruff, not meeting anyone's eye): \"...Adrenaline. You'd be fast too, with that thing overhead. Get her down. Keep moving.\"")
exit_("The shadows shrink east and are gone. Choose: fire the RECKONING at the next camp, or hold it for Ivarstead.", "THE RECKONING / 7")

# ---- RECKONING
scene("THE RECKONING -- Valerius comes in person")
subtitle("GM CHOICE on timing: a later road-camp after the hide, or early at Ivarstead. Full build: Npcs/Valerius + scratch 19/22. Not a fight. Not survivable as one.")
plain("Seeded by Orion disobeying the Constance-enthrall order (Ch.24). Valerius Caelus, **AP 30-35**, arrives at the camp IN THE FLESH -- the whole camp awake and watching, which is the point: a private punishment performed in public. The Contest Level-Gap Penalty (**-20 to -25** on any will-vs-will resistance) is the wall, and the rules back it.")
bullet("**THE ARRIVAL:** no wings, no drama coming in -- he walks out of the dark into the firelight, courteous, unhurried, dressed like a visit. The Ring goes from cold to KILLING cold. (The mare -- FEARLESS, the one animal that stands -- goes utterly still and watches him. Use her.)")
bullet("**BEAT 1 -- THE INTERROGATION (the camp hears every word):** he does not ask where they are going. He asks Orion about THEM -- who loves whom, who needs what, who holds the sword and who the sword answers to. Orion answers; his blind spots protect the Crown, Bjorn, and what Davinia truly is (he doesn't know them). Resisting is will-vs-will at -20/-25 -- let a player try; let the die be the lesson.")
bullet("**BEAT 2 -- THE TRIM:** \"You served me well. For a long time -- understand, that is not nothing. But you are a hand. And a hand that will not close when I will it, is trimmed.\" He does NOT do it. **He compels Orion to do it himself** -- Orion's own blade, his own arm, the off-hand below the elbow, the camp watching. Clean, efficient, no cruelty in the voice at any point. **MECH (permanent):** any Minor Action requiring the off-hand becomes a MAJOR Action until Orion acquires a prosthesis. No save.")
bullet("**BEAT 3 -- THE FETCH (the seed, never the reveal):** he sends Orion -- bleeding, one-handed, NOW -- to bring him \"the Lady Caelus. We are family, after all. It would be rude to leave without paying my respects.\" The audience is PLAYER-DRIVEN: the GM aims Valerius (courteous, probing the succession, taking her measure) and plays THE NAG -- she reads older, stiller, colder than a Breton woman should, and his instincts will not settle. Whether Ismara surfaces belongs entirely to Davinia's player. He should leave more unsettled than he arrived.")
bullet("**THE EXIT:** only now the drama -- he thanks the camp for its hospitality, steps beyond the firelight, and comes apart upward into the winged vampire-lord shape, one long climbing beat of membrane and cold air, gone south. The last image of the scene.")
gm("If Vignette 4 fired (either branch), he arrives already knowing about Nora. He needs to do nothing with it tonight. Knowing is the leverage.")

# ---- SCENE 7
scene("7   THE FAINT WRONGNESS -- the approach")
readaloud([
    "The two shadows shrink into the east and are gone, and the breath goes out of all of you at once. The road drops toward a valley, and at the bottom of it, small and grey against the immensity of the mountain behind it, sits Ivarstead. You are nearly there.",
    "Then, on the last mile, each of you catches it -- once, and only once. A footprint appears in the mud of the road a heartbeat BEFORE Bjorn's boot comes down to make it. A word someone said comes back off the rocks a moment too late, in their own voice. The cart's shadow lags a half-step behind the cart. Small things. A day of being hunted has rubbed you raw enough to see them.",
    "The mountain waits. And the time on it is already beginning to come loose.",
])
exit_("Part Two. The temporal weather switches ON at the town line.", "PART TWO -- IVARSTEAD")

rule()
raw("\\pard\\sb120\\sa200\\cf2\\b\\fs40 PART TWO -- IVARSTEAD & THE BLEEDING STAIR\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i The party's first contact with the Dagon apocalypse and with Gaelen the Root-Twister. Advance, never resolve: the Tower cosmology lands HARD; everything personal stays loaded. Sections: the town -> the ascent -> High Hrothgar -> the undercroft -> the sealing.\\i0\\cf1\\par\n")

label("GM RULES -- THE TEMPORAL WEATHER (proximity zones + the alarm)", red=True)
plain("The distortion is a SIDE EFFECT: the cult corrupts the TOWER from the undercroft; the mountain's existing Time-Wound turns that violence into weather. The cult does not target the Wound and does not control the weather -- they just know how to surf it.")
statcard([
    "**HOW IT RUNS (core, locked):**",
    "1. The GM sets a REAL-WORLD ALARM (phone, hidden). It fires with NO warning;",
    "   the players learn to dread the sound.",
    "2. On the alarm: GM rolls d20 -> picks which table in the CURRENT ZONE's set is",
    "   active ('the weather shifts'). Announce nothing but the sensation.",
    "3. In combat, every character rolls d20 TEMPO at the start of their turn on the",
    "   active table -> that is their action economy this turn.",
    "4. THE GRADIENT = two dials: higher zones have NASTIER tables AND the alarm",
    "   fires MORE OFTEN.",
    "5. SEPARATION IS EXPOSURE: anyone who strays from the group slips out of the",
    "   shared 'now' -- they face this zone's weather ALONE, no one to pull them",
    "   back into sequence. A tight, roped body is the only anchor.",
    "",
    "**ENEMIES CHEAT:** Dagonites carry grafted TIDE-SHARDS (obsidian slivers fused",
    "at the sternum) -- they choose their Tempo result instead of rolling. THE",
    "COUNTER: destroy the shard -- a Called Shot (Very Hard -6), or Sunder aimed at",
    "it, or it shatters on their death -- and that cultist rolls like everyone else.",
    "Ylva FEELS every cheat as a broken hunt-rhythm (hackles, growl) before any",
    "mortal can name it.",
])
statcard([
    "**ZONE TABLES (d20 TEMPO -- roll at start of each combat turn)**",
    "",
    "ZONE 0 -- THE TOWN (faintest; alarm ~every 25 min real time)",
    "  1 Frozen (0 actions) | 2-4 Dragging (Major OR Minor) | 5-16 In step (normal)",
    "  | 17-19 Quickened (+1 Minor) | 20 Unmoored (full extra turn after this one)",
    "  Social distortion instead of combat weather: see Scene 8's card.",
    "",
    "ZONE 1 -- THE LOWER STEPS, Waystones 1-2 (alarm ~15 min)",
    "  1-2 Frozen | 3-5 Dragging | 6-15 In step | 16-19 Quickened | 20 Unmoored",
    "",
    "ZONE 2 -- THE UPPER STEPS, Waystone 3 -> High Hrothgar (alarm ~10 min)",
    "  1-3 Frozen | 4-7 Dragging | 8-13 In step | 14-18 Quickened | 19-20 Unmoored",
    "",
    "ZONE 3 -- THE UNDERCROFT (worst; alarm ~6 min)",
    "  1-4 Frozen | 5-8 Dragging | 9-12 In step | 13-17 Quickened | 18-20 Unmoored",
    "  PLUS: any natural 1 or 20 on Tempo ALSO triggers a SECONDARY HORROR (d20):",
    "   1-4  your spell/attack this turn resolves at the START of your NEXT turn",
    "   5-8  damage you deal this turn already landed LAST round (retroactive; if the",
    "        target acted since, it staggers them now instead)",
    "   9-12 echo-step: you are suddenly 15 ft from where you stood (GM places you",
    "        where you were 1 round ago)",
    "   13-16 doubled: act twice this turn, then LOSE your next turn entirely",
    "   17-20 the initiative order reshuffles (reroll all) at this turn's end",
])
gm("The zone tables and secondary-horror list are built to the locked dials (scratch 5); adjust freely at the table -- the ALARM and the DREAD are the mechanic, the numbers are servants.")

label("GM RULES -- SAIJAH'S DOUBLE MIGRAINE", red=True)
statcard([
    "**THE DOUBLE MIGRAINE (triggers the instant she touches the first black sap)**",
    "Two Towers scream at once: the Eldergleam she always feels + the Throat under",
    "fresh assault. While anywhere in the corrupted zone (the whole Stair):",
    "   -2 Guile   |   -2 Agility   |   +2 damage taken from all sources",
    "Sustained and brutal BY DESIGN -- the player must FEEL it, because that ache is",
    "exactly what gives Hircine's 'I can make it stop' its hook (Scene 11).",
    "(Replaces the -1 city penalty here.)",
])

# ---- SCENE 8
scene("8   THE FOOT OF THE STAIR -- Ivarstead is the bottom edge of the unmaking")
subtitle("Set-piece + social. The frightened half-empty town, the first Waystone, the inn that is not a haven. ZONE 0.")
readaloud([
    "Ivarstead is a handful of grey houses pressed against the biggest thing in the world. Half of them stand with their doors open on emptied rooms -- packed in a hurry, gone. Smoke rises from three chimneys. A barricade of farm carts and fence posts blocks the lane toward the river, manned by nobody.",
    "At the bridge, the first Waystone leans in its socket, and it is bleeding: a slow black sap crawling UP the carved stone, against gravity, pooling in the old runes until they read wet and dark. Where a drop falls, it falls slowly -- slower than it should, like it is falling through deeper water than the world's.",
    "A big man sits on the inn's steps with a loaded pack at his feet -- packed for the climb he has not made. He watches you come in the way a man watches the first help arrive at a fire that has already taken the roof.",
])
plain("**KLIMMEK:** \"You came. Gods -- somebody came.\" (a breath, steadying) \"I still have the supplies for the monastery. Been packed nine days. Every time I set foot past the third stone something... happens to the walk. Hours go by that I don't remember walking. Once I came down and my beard had grown out three days. The masters are up there ALONE, and I can't -- I can't make the climb.\" He pushes the pack toward you. \"You're climbing. I know you are. Take it. Please.\"")
gm("SAIJAH -- STATION 1 fires at the Waystone: the black sap NAGS -- familiar, can't place it. An itch, not a recognition. (The DOUBLE MIGRAINE fires the instant she TOUCHES it -- debuff card ON for the rest of the Stair.) Davinia's Sight: the corruption reads as a structured working running DOWN into the mountain's root, not spilling up from the stone.")
label("THE TOWN'S BROKEN TIME (Zone 0 -- social, not lethal)")
statcard([
    "**TOWN DISTORTION (color any conversation with one of these; light touch):**",
    "- An answer arrives BEFORE the question finishes being asked.",
    "- A villager repeats the last exchange verbatim, unaware; it plays like an echo.",
    "- Someone thanks the party for a thing they have not done yet.",
    "- A door is heard closing a full breath before it visibly closes.",
    "In fights here: Zone 0 Tempo, alarm rare. The horror is social first.",
])
label("NO HAVEN AT THE FOOT (the everyone-climbs logic -- play it, don't announce it)", red=True)
bullet("The corruption is creeping DOWN into the streets, and Dagonites move through the empty half of town after dark. There is nowhere safe to leave a child, an old man, or a horse.")
bullet("**If they shelter at the inn** (the least-bad option): it is ATTACKED in the night -- Dagonites and a shard-grafted zealot, torches, the Kvatch register: this is what Dagon taking a space looks like. People are hurt. The horse must come INSIDE (the mare, fearless, walks in like she has always lived indoors). Anything left OUTSIDE is destroyed or taken.")
bullet("**The lesson the fiction teaches:** to wait below is to wait inside the thing they came to stop. Bjorn will not be parted from Mila; the party will not abandon either of them; and on the mountain, the weather ISOLATES stragglers. The whole crew climbs as one -- guarding their two most precious people up a mountain of cosmic horror.")
label("THE ENEMY -- DAGONITES (Expert-tier per the master table)", red=True)
statcard([
    "**DAGONITE CULTIST  x4-8  (TL1, Expert)** -- razor-scarred, ash-grey robes",
    "HP 100  |  Dmg 20 (jagged glass-steel)  |  DR 11  |  17/15/13/8 (P=Might or Magic)",
    "Tide-shard graft: CHOOSES Tempo (see weather card) until the shard is destroyed.",
    "Fights to the end; retreat is not in the liturgy.",
    "",
    "**SHARD ZEALOT  (TL2, Expert)** -- the graft has spread up the throat; voice doubles",
    "HP 250  |  Dmg 31  |  DR 17  |  18/16/13/8 (P=Magic)",
    "Casts Ash Shell (4 FP) and Firebolt (3 FP, 6 dmg) between blade-work.",
    "Cheats Tempo; on its death the shard bursts -- 5 dmg to all within 5 ft.",
])
exit_("Dawn after the inn night. Klimmek's pack on someone's shoulders. The first of seven thousand steps.", "9  THE BLEEDING STEPS")

# ---- SCENE 9
scene("9   THE BLEEDING STEPS -- the ascent")
subtitle("ZONES 1-2. Waystone by Waystone the world comes loose. Dagonite ambushes that cheat. Saijah stations 2-4. Keep the rope tight.")
readaloud([
    "The Steps are older than any road you have walked -- worn hollow in the middle by seven thousand years of pilgrims -- and they climb out of the valley in long switchbacks that vanish into cloud. Every few hundred steps a Waystone stands in its socket, and every one of them is bleeding the same slow black sap, the runes drowned dark.",
    "At the first stone the snow around your boots falls UPWARD for three heartbeats, a soft reversed flurry, and settles as if nothing happened. By the third stone your own voices start coming back off the rock faces a moment too late. By the fourth, you walk beside your own afterimages -- a half-second echo of each of you, following a half-step behind.",
])
gm("ZONE 1 through Waystone 2; ZONE 2 from Waystone 3 up. Run the alarm honestly -- the dread of the sound is the mechanic. ROPE RULE out loud once: stay together; anyone who strays faces the weather alone (separation = the Zone's Tempo with nobody to pull you back).")
label("SAIJAH -- STATIONS 2-4 (paced, never a lecture)")
bullet("**Station 2 (deeper):** she PLACES the signature -- \"I've felt this before\" (Thornheart; the Solitude temple tree) -- but reads it as coincidence. Two points, no pattern.")
bullet("**Station 3:** the migraine DOUBLES -- two simultaneous sources, which makes no sense to her. The -2/-2/+2 is fully on. Something is deeply wrong; she does not know what.")
bullet("**Station 4 (Gaelen's voice -- through the corrupted leylines, to her alone, mid-climb):** warm, sincere, reasonable: \"You feel it as pain because you were taught the cage is your body. Forests that burn and regrow in a breath. Beasts that never stop becoming. I am not breaking anything, little sentinel. I am opening a door that was nailed shut before you were born.\" -- and the SCALE slips: \"...prisons. I have been opening them for years. This is not the first, or the last.\" A clue she cannot yet hold.")
label("COMBAT -- THE CHEATED GAME (Dagonite ambushes)", red=True)
gm("Use CULTISTS + a ZEALOT per ambush (cards, Scene 8). They surf the weather: stolen turns, doubled moves, strikes out of sequence -- while the party rolls Tempo. Make the unfairness VISIBLE. Then let the party break the shards and even the game -- that reversal is the fun.")
plain("**YLVA -- THE REFEREE'S WRATH (this develops SAIJAH, not Ylva):** the first time a cultist cheats, Ylva's hackles rise BEFORE it happens -- she growls at empty air a half-second early, then the cheat comes. She cannot name 'temporal weather'; she knows a FOUL happened. \"They're cheating. The hunt has RULES.\" Her fury is theological -- the laws make the game sacred; these people spit on the game itself. Saijah, watching, is seeing the exact hunt-rhythm sense Hircine could one day give HER. **VARON** agrees from the opposite pole -- Shadowscale doctrine kills clean INSIDE time's rules -- and the two who cannot stand each other fight back to back, aligned. Give it one beat out loud.")
gm("BJORN: his speed may FLICKER again on the climb if Mila is threatened -- shorter than the road flare, still read as rejuvenation, never named. NORA (if a player pulled her up rather than cart-side... she climbs -- everyone does): the broken time does something WRONG to her two black gems -- her parents' souls flickering, stuttering, DOUBLING. A horror beat, not a resolution. ALFONSO: what does a mountain of broken time do to a soul living in iron? Let the sword be uneasy -- a wrongness he will not explain.")
exit_("The last switchback. Grey stone walls in the cloud. The monastery.", "10  HIGH HROTHGAR")

# ---- SCENE 10
scene("10   HIGH HROTHGAR -- the quarantine of the masters")
subtitle("Character scene at the top of the world. The TOWER hard-reveal, Kynareth's first new word in years, and the Ring feeding it all to Solitude.")
readaloud([
    "The monastery is grey stone against grey sky, and the doors stand barred from within. When they open -- slowly, to Klimmek's pack and your knock -- the man inside has a face like a starved hawk and hands that tremble with something past exhaustion. Behind him, in the great cold hall, three more grey-robed figures sit in a triangle around a brazier, and the air between them HUMS -- a note below hearing, steady as a heartbeat, that you feel in your teeth and the floor and the old stone walls.",
    "They are not meditating. They are HOLDING something. You can feel the mountain trying to shake itself apart beneath you, gentled -- barely -- by the hum.",
])
plain("**MASTER ARNGEIR** (voice cracked from disuse and overuse at once): \"You climbed through THAT. Then you have seen what is happening to the mountain.\" (he looks at the pack, and something in the hawk face almost breaks) \"...Klimmek's bread. Forgive me. It has been -- some time.\"")
label("WHAT THE MASTERS GIVE (scholarship, not senses)")
bullet("**THE HARD REVEAL -- the word TOWER:** \"You stand on one of the pillars of the world. The Throat is a TOWER -- one of the stones that holds Mundus against Oblivion. The zealots below are not desecrating a holy place. They are cutting a load-bearing wall of the WORLD. The shaking you feel in time is the Tower beginning to fail.\" -> The party LEAVES KNOWING they are in the main plot. Land it plainly.")
bullet("**The Way of the Voice OPENS:** the masters accept the party as the first help to reach them; the door stands open hereafter (scholarship, Word Wall locations for seekers -- the masters themselves cannot shout offensively enough to leave; holding the mountain takes everything they have).")
bullet("**What they CANNOT do (hold this line):** no special senses of ANY kind. They do not see Ismara in Davinia. They do not sense anything in Bjorn. They cannot name a Dragonborn -- no one can. They hold the summit by Voice and endurance, and they are losing.")
bullet("**The geography clue:** \"The working is BELOW us -- in the undercroft, at the mountain's root. The summit path is SEALED (only a Shout clears it, and none of us can be spared from the holding). Whatever you came to stop, you will find it downstairs.\"")
label("KYNARETH'S REVEAL (Saijah -- station 5; the goddess, NOT the masters)")
gm("At Kyne's own peak, the goddess finally gives Saijah something NEW -- cryptic, non-verbal, the first fresh thing after all the repeated instructions. An IMAGE she cannot decode: a wind carrying a great soul upward -- toward a hall of mist and warriors -- and the certainty, wordless and enormous, that her ENDURING matters to the end of the world. Somewhere in the image, unnamed, a shape like a big man standing between a child and the sky. She gets a FEELING about Bjorn, never a label. This is the reason to endure the pain -- delivered the night BEFORE Hircine offers to end it.")
label("THE OTHERS AT THE MONASTERY")
bullet("**DAVINIA/ISMARA:** her Sight is the only thing that can READ the Tower -- the leyline lattice, the corruption's shape crawling the root. A Sight showcase. And ISMARA'S TEMPTATION: amid the breaking time she offers to FREEZE the wound locally -- stasis against chaos, tactically real, self-corrupting. **Using it advances the CDI.** Offer it once, cleanly, and let the player choose. (The masters see none of this.)")
bullet("**ORION -- the tonal architect:** the corruption is a FREQUENCY phenomenon and he is the one person equipped to read it as MECHANISM. Diagnostic Song against the hum: he maps the working's structure (this feeds Scene 11's disruption options and his Severance research) and earns the masters' respect as a fellow student of tone -- a real tie, a real spotlight. THE GUT-PUNCH (GM-only, say nothing): the Ring has fed Valerius the entire apocalypse, live, all climb.")
bullet("**GEAR** (he climbed; everyone climbs): quantifies the break -- \"local causality variance exceeds Dwemer tonal tolerances by a factor of nine. I have no protocol for this. I find I do not enjoy that.\" Pairs with Orion. Light.")
bullet("**ESBERN:** among the masters' books like a starving man at a feast -- and the one who says the OTHER quiet part: \"The Wall shows a council of heroes when the Dragonborn fails. It never shows what holds the SKY up while they argue. Now we know.\"")
exit_("Down the inner stair. The hum fades above; something older hums below.", "11  THE UNDERCROFT")

# ---- SCENE 11
scene("11   THE RITUAL IN THE UNDERCROFT -- Gaelen at the root")
subtitle("The boss. ZONE 3 -- the worst weather. Objective: DISRUPT THE RITUAL. Gaelen escapes by design; Jasper does not.")
readaloud([
    "The undercroft is older than the monastery above it -- a vaulted root-cellar of the world, columns of living rock running down into dark that breathes. The Dagonites have made it a garden. Red light comes up out of carved channels in the floor, all of them running inward to a central well where the mountain's root stands exposed: a column of something older than stone, and INTO it, like ivy into a wall, black sap-lines are growing upward from an array of obsidian shards arranged in a blooming spiral.",
    "A Bosmer moves through the array unhurried, crimson chitin catching the light, one arm a grafted mass of charred heartwood and obsidian that gestures at things he is not looking at. He is adjusting each shard with the care of a man tuning an instrument he loves.",
    "Without turning, in a voice that is warm and genuinely pleased: 'Oh -- visitors. Good. I hoped the mountain would manage to be heard. Come in, come in. You are not interrupting; nothing can interrupt this. But company is rare, and I have wanted to meet you for the longest time.'",
])
label("GAELEN -- HOW HE PLAYS (unsettling, never evil)")
bullet("The warm, sincere, reasonable CENTER of an apocalypse. He talks like an ally trying to get compatriots to stop suffering for a stagnant world: the Aedra gave mortals a CELL -- linear time, fragile flesh; Dagon offers the KEY; the Unmaking is HEALING.")
bullet("**THE QUIET WISH (plant it -- overheard when he thinks no one listens, to no one):** \"I want it to be perfect. Please... let it be perfect.\" Not a plea, not a crack in a mask -- the closest thing his altered architecture has to hope. Every projection the players make onto it will be slightly wrong. He should leave the table unable to dismiss him.")
bullet("**THE YLVA EXCHANGE (give both liturgies one beat, out loud):** GAELEN: \"Rules are the bars, hunter. I am unbending them.\" YLVA (shaking with a fury even she cannot name): \"The rules are what make the hunt HOLY. Prey runs, hunter chases, the fastest wins -- that is the whole church. You are not freeing anything. You are pissing on the game.\" The most theologically serious person in the room about why the Unmaking is wrong is the werewolf.")
bullet("**ALFONSO -- the duel only he can have:** Gaelen speaks HIS language -- entropy. Peryite's pestilence is decay WITH order, a cycle that feeds the world; Gaelen's Unmaking is decay as pure negation, death that feeds NOTHING. Let Alfonso be almost-tempted -- then articulate exactly why it is blasphemy. Quiet horror: how close his own philosophy sits to the abyss.")
label("HIRCINE'S TEMPTATION (Saijah -- station 6 in the doorway of the boss)")
gm("Just before or during the fight, the Hunter's voice -- the morning after Kynareth finally spoke: \"Little sentinel. That noise in your skull. I can make it STOP.\" He is not lying. THE HIDDEN COST he simply does not mention: the channel that screams is the same channel the goddess speaks through -- silence the pain and you silence KYNARETH (the Mzinchaleft principle: silence is not always peace). NO weredog offer, NO choice resolved here -- the senses may sharpen a moment (a taste), and the offer HANGS. If the player accepts outright anyway, do not block it -- but that is her player firing the crossroads early, not the module.")
label("THE FIGHT -- DISRUPT THE WORKING", red=True)
plain("**Frame it out loud (again): the objective is the RITUAL.** The spiral array feeds the sap-lines into the root. Break enough of it and the working collapses. Gaelen defends the work, not himself; Jasper defends GAELEN.")
bullet("**THE ARRAY:** 5 anchor-shards (obsidian, waist-high). Each: **25 HP, DR 10** -- or a **Hard Might (-4)** wrench to topple one bodily, or Orion's tonal counter-note (**Hard Magic -4**, guided by his Scene 10 mapping) to crack one at range. Every anchor down weakens the weather one step in here (Zone 3 -> 2 -> 1...); at THREE down the working is DISRUPTED (win condition); all five down = staunched as clean as this ever gets.")
bullet("**THE WEATHER FIGHTS EVERYONE** (Zone 3 card, alarm ~6 min): the cultists cheat it, the party endures it, and every anchor destroyed evens the game a step -- the mechanical arc IS the story arc.")
statcard([
    "**GAELEN THE ROOT-TWISTER (Apex Villain -- full sheet: Npcs/new mythic dawn leader)**",
    "Magic 21 (cannot fail a Magic roll)  Agility 17  Guile 15  Might 8",
    "HP 40 (Paradise Mantle: regen -- outheal or shut off)  |  FP 35  |  DR 22 (23 vs spells)",
    "Mythic Dawn chitin skin; Daedric graft-arm acts on its own initiative.",
    "HE IS NOT HERE TO DIE: at disruption (3 anchors down) he PHASES -- the collapsing",
    "weather releases his half-untimed soul and he falls back to the Eldergleam plan.",
    "If somehow cornered before that, he spends everything to phase early.",
    "",
    "**JASPER AVALON (lieutenant -- ~AP 10 character build; he does NOT retreat)**",
    "Dunmer mage, THE ATRONACH. Might 4  Agility 6  Magic 19  Guile 12",
    "HP 9 (glass -- his defense is absorption and ash)  |  FP 16  |  DR 8 (Ebonyflesh up)",
    "SPELL ABSORPTION (Atronach stone): once per combat, negates a hostile spell",
    "and regains its FP cost.  Ancestor's Wrath (Dunmer): 1/adventure fire aura.",
    "Casts: Incinerate (9 FP, 12 dmg) | Ash Shell (4 FP, Might roll or encased 2 rds)",
    "| Ash Rune (10 FP) | Lightning Bolt (3 FP). Tide-shard graft: cheats Tempo.",
    "FIGHTS TO THE END defending the ritual space. Dies here. One-and-done.",
])
label("THE JASPER REVEAL (via Gaelen -- this is how the consent lands loud)", red=True)
plain("When a party member recognizes the Dunmer (Davinia's player above all -- this weight is aimed at HER), **GAELEN** (mild, without pausing his work): \"It seems you were familiar with this vessel... that is unfortunate, for he is gone. As for his flesh -- he gave it to the Dawn.\" Jasper was a secret Dagon devotee IN LIFE -- a lone worshipper, long before he died in the Pale Lady's tomb. Nothing was stolen. If the party tries to TALK to him, he CAN speak -- and what he says is worse than silence: he is content. The empty, discarded man was told his emptiness was HOLY, and he gave himself gladly, because it was the first time anything ever wanted him.")
gm("VICTIM vs WILLING is the differentiator from the Echo: Kyboh was stolen (rage FOR him); Jasper GAVE himself (nothing to save). Do not soften either half.")
label("GAELEN'S ESCAPE (at 3 anchors down -- run it exactly)", red=True)
readaloud([
    "The third anchor cracks and the whole undercroft LURCHES -- the red light guttering, the sap-lines withering back out of the root like ivy burned at the stem. Gaelen watches it happen with his head tilted, the way a man watches weather ruin a picnic.",
    "'Hm. Unfinished, then.' He looks at you -- genuinely, unhurriedly interested. 'You finally showed up. Do you know, I had begun to think no one was coming, all these years. How wonderful. Something new.'",
    "The broken time reaches for him and he steps INTO it, the way you would step into a doorway -- and he is a half-second behind himself, and then a full second, and then he is an afterimage the room forgets to keep.",
])
gm("He falls back to the ELDERGLEAM -- the primary plan the party has never touched, still running perfectly. They did not beat him; they interrupted a man who reached for a second prize. He recurs with a grievance now attached -- curious, not vengeful. Scarier.")
exit_("The weather stills. The mountain stops shaking. It is not healed.", "12  THE SEALING & THE COST")

# ---- SCENE 12
scene("12   THE SEALING & THE COST -- staunched, not sealed")
subtitle("The curtain. Rewards, the seeds that finish growing AFTER, and the doors this module opens.")
readaloud([
    "The masters come down the inner stair when the shaking stops -- slowly, holding the walls, men walking after weeks at an oar. Arngeir stands a long time at the wounded root, where the black lines have withered to scars in the stone.",
    "'Staunched,' he says at last. 'A cut finger, bound. The body of the thing that attacked this mountain is still out there, and still working.' He looks at each of you in turn, and bows -- the full bow, to all of you. 'The Way of the Voice is open to you. It is a small thing to offer the people who held up the sky. It is what we have.'",
])
label("REWARDS")
bullet("**1 AP each** (a full fire completed) -- plus dragon-kill AP if any dragon somehow died this module (it should not have).")
bullet("**The Way of the Voice:** High Hrothgar open as sanctuary + scholarship; the masters know WHERE Word Walls are for specific shouts a seeker might want (they cannot shout them; reference, not power).")
bullet("**Loot:** the zealots' tide-shards (inert now -- but Nora or Ismara will want them badly: crystallized wrong-time, priceless to a researcher and mildly unwholesome to carry). Klimmek's gratitude and Ivarstead's -- the town half-returns as word spreads the mountain has quieted.")
label("SEEDS PLANTED (they finish growing AFTER the module -- do not harvest early)")
bullet("**Saijah's realization (station 7, ON THE ROAD OUT, days later):** gildergreens + the Throat + the word TOWER + TWO migraines finally assemble -- one tree, it is a Tower, TWO Towers are under attack, and there is a HEART she has never found. The module plants; the realization grows. Let her player say it first if they get there.")
bullet("**The heart-hunt -> DANICA:** the true Eldergleam's location is the chosen sisters' deepest secret (a women's mystery -- no man may ever know). Three living sisters: Danica, one in Whiterun (cold to the Lanterns -- Danica's letters made the party the temple's cautionary tale), one visiting Solitude. The road to the cure runs through the reconciliation. The braid is now load-bearing.")
bullet("**The two cure-routes (set up, never forced):** KYNARETH -- heal the heart (needs Danica). HIRCINE -- no Danica needed at all: the Alpha and the cull. If reconciliation looks impossible, Hircine's road becomes the shortcut priced in Saijah's soul.")
bullet("**Node-saving (the standing open door):** every gildergreen node is SAVEABLE; the party has simply kept not going. From here on, offer node-defense chances on the road; the Solitude node (slow, strong, a chosen sister already present) is the best first savable win.")
bullet("**Valerius knows everything** the Ring saw -- the Tower, the apocalypse, the party's capabilities. File it; spend it later.")
bullet("**Gaelen, unfinished:** \"you finally showed up.\" The Eldergleam campaign continues off-screen. He is curious about them now. That is worse.")
label("CONSEQUENCE LEDGER (what the OTHER fires did while they climbed)")
bullet("**Fire A (Krusp & Danica at Windhelm):** rumor arrives -- the plague fought to a standstill at a cost. Danica's cough, when they finally hear her again, has teeth in it. [Attrition canon: her lungs.]")
bullet("**Fire C (ignored -- Bleak Falls):** Antoine rebuilds unobserved on top of the Dragonstone. The 6-8 week Strain 2.0 clock RUNS. Esbern says the Dragonstone line again on the road out. He will keep saying it.")
exit_("The cart rolls down out of the grey hills with the mountain quiet behind it -- and the Dragonstone pressure, the Dirge reckoning, and the road to Bleak Falls ahead.", "NEXT MODULE: FIRE C / BLEAK FALLS")

# ---------------------------------------------------------------- write
rtf = HEADER + "".join(buf) + FOOTER
bal = 0
for ch in rtf:
    if ch == "{": bal += 1
    elif ch == "}": bal -= 1
    if bal < 0: break
assert bal == 0, "RTF brace balance broken: %d" % bal
with open(OUT, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
    f.write(rtf)
print("wrote", OUT, "braces balanced OK, %d chars" % len(rtf))
