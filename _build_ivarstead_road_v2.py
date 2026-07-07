# -*- coding: utf-8 -*-
# Generator for FIRE B PART ONE -- THE ROAD (redraft, road-leg only).
# Scope: Spine through THE RECKONING -- the section the GM actually annotated in the
# first-draft full module RTF. Part Two (Ivarstead onward) is unreviewed and is NOT
# touched here; the original annotated draft stays in place as the reference for why
# these rules exist (WRITING GUIDE section VII, SESSION SHEET FORMAT 4B/5C, CLAUDE.md
# Rule 3 extension). Run: python _build_ivarstead_road_v2.py

import os

OUT = r"C:\Users\fbrown\Projects\Frogs-5-skyrim\Toryggs legacy\Adventure modules\choice gate 3\FIRE B - THE ROAD & THE BLEEDING STAIR (redraft).rtf"

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

# GM-reference variants: same small Consolas font/size as statcard, but unboxed and
# structured (label/bullet/plain), for rules-reference content that isn't at-the-table
# read-aloud/dialogue -- per GM note: "everything that isn't part of the actual at the
# table run time" gets this treatment, matching the statcard boxes.
def reflabel(text, red=False):
    c = "6" if red else "4"
    raw("\\pard\\sb120\\sa50\\cf" + c + "\\b\\f1\\fs20 " + esc(text) + "\\b0\\f0\\fs24\\cf1\\par\n")

def refplain(text):
    raw("\\pard\\sa100\\f1\\fs20 " + inline(text) + "\\f0\\fs24\\par\n")

def refbullet(text):
    raw("\\pard\\li500\\fi-280\\sa80\\f1\\fs20 {\\cf4\\b\\bullet\\tab}" + inline(text) + "\\f0\\fs24\\par\n")

def exit_(text, nxt):
    raw("\\pard\\sb100\\sa240 {\\cf2\\b EXIT ->} " + inline(text) +
        ("   {\\b -> " + esc(nxt) + "}" if nxt else "") + "\\par\n")

def rule():
    raw("\\pard\\brdrb\\brdrs\\brdrw20\\brdrcf2\\sb60\\sa220\\par\n")

# ============================================================ TOP
raw("\\pard\\sb60\\sa40\\cf2\\b\\fs44 FIRE B -- THE ROAD & THE BLEEDING STAIR (redraft)\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i Riften gates -> the foot of the 7,000 Steps -> Ivarstead -> the undercroft of High Hrothgar. The campaign's relaunch: one place, one escalating problem, a clean arc with a curtain. ~3 sessions. Self-contained -- run the whole fire from this file. (Full redraft: Part One reviewed and rebuilt with the GM; Part Two rebuilt to the same craft rules, first GM review pass still to come.)\\i0\\cf1\\par\n")
rule()

label("THE SPINE (hold these three lines all module)", red=True)
bullet("**This is an INTRODUCTION.** It ADVANCES threads and RESOLVES nothing personal. Saijah chooses NO patron. Gaelen does NOT die. The crossroads is loaded, never fired.")
bullet("**Frame the objective OUT LOUD as THE RITUAL, never as Gaelen's head.** If they think the mission is 'kill Gaelen,' his escape is a robbery. If they know it is 'stop the Unmaking,' his escape is just Thursday.")
bullet("**Secrets that must hold:** Bjorn's speed reads as REJUVENATION, never Dragonborn (no one can sense a Dragonborn -- not even the Greybeards, who have NO special senses of any kind). Ismara stays unwitnessed by the monastery. The two scout dragons' target stays unknowable.")
plain("**Roster on the move:** Davinia (ISMARA fronting -- silver skin), Saijah, Orion. These three are the PCs; everyone else on the cart is a companion NPC. Cart: Bjorn, Mila, Esbern (hidden until Scene 1), Nora, GEAR, Ylva, Varon. Animals: Mable (old, dragon-shaken) + the BLACK MARE (fearless warhorse -- sheet: Npcs/the black mare). Krusp & Danica are GONE to Windhelm.")
gm("BEFORE THE TABLE SITS DOWN: hand Davinia's player Ismara's Note One (The Forelhost Codex -- Ismara's Extract, player handout) at the start of the session. Whether he reads it right then or later is his call -- just get it into his hands. Note One's own discovery (the Concentration ratio) already happened OFF-SCREEN, in the gap between Forelhost and leaving Riften -- no scene needed for it, just hold it as already-true. She had Luna Moth Wing to test with because Bjorn picked some up at a Riften apothecary as part of his usual pre-departure supply run -- background fact, not a scene either.")
gm("ALFONSO'S STATUS (Ch.24, current): nobody bears him anymore -- Nora saturated toward the Tenancy on telekinetic contact alone, no touch required, and the company stopped physically carrying him after that. He rides the cart and is moved by will when a task needs him, hands off the rest of the time; whoever's turn it is carries him -- currently ORION, since he wielded him for the Grelod kill. Saijah is NOT his bearer: she cannot hold him and keep Kynareth's channel open at the same time, so she has stepped back from him entirely. Route any Alfonso beat below through whoever's actually carrying him at that point in the module, not Saijah by default.")

rule()
raw("\\pard\\sb120\\sa200\\cf2\\b\\fs40 PART ONE -- THE ROAD\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i A quiet leg doing three jobs: re-introduce Esbern (comedy + strategy), give the table a breath (respite + personal threads), and teach that the dragons own the sky (the hide). Normal physics the whole way.\\i0\\cf1\\par\n")

reflabel("GM RULES -- \"TWO SHADOWS\" (the dragon hide)", red=True)
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
    "PROACTIVE PLAY: every smart move drops the next beat a step or grants Advantage.",
    "Say YES to cleverness. FAIL STATE (Notice 6): spotted -> they dive. TELEGRAPH the",
    "unwinnability hard BEFORE this. This full clock is restated again, in Scene 5,",
    "at the point it actually runs (SESSION SHEET FORMAT rule: runnable means runnable).",
])
refplain("**THE FIVE TELLS:** 1) MABLE SPOOKS -- Bjorn rolls (animal handling); the Black Mare in harness beside her = one step EASIER. 2) GEAR HUMS -- Saijah/Orion (Guile); GEAR needs PERMISSION to power down. 3) ALFONSO'S ROT-AURA drifts downwind -- Orion (carrying him this leg); auto-success if he pulls the aura tight through the working. 4) A SMALL HUMAN SOUND (Mila's frightened breath) -- Bjorn or Saijah; comforting her IS the roll. 5) HEAT BLOOM -- Davinia/Ismara can sheathe the cart's warmth in cold -- a quiet temptation each time she uses the gift.")

rule()
refplain("**Everything above this line is GM prep -- read before the table sits down. Scene 1, below, is where the session actually starts running live.**")

# ---- SCENE 1
scene("1   THE OPEN ROAD -- and the man in the floor")
subtitle("Set leaving Riften. Purpose: the breath, and Esbern's comedy re-entry.")
readaloud([
    "Dawn in Riften is grey harbor-light and gull-noise. You load the cart in it -- packs cinched, coin counted twice, Bjorn checking the wheel-pins the way he checks everything, twice. Mable stamps in her traces, impatient. The black mare stands beside her already still, already watching the gate.",
    "The gates open. The city falls away behind you a street at a time, then a wall at a time, then all at once, and the road takes you north into hills gone gold with the turn of the season.",
    "The road climbs. The light is thin and clean, the wheels find their rhythm, and mile by mile an old feeling settles over the company: ease. Full packs. Paid coin. Warm bread from Riften's ovens, still soft in the saddlebags. A road that asks only that you follow it.",
    "Mable plods. The black mare walks beside her, head high, ears forward, reading the hills the whole way.",
    "Then, from under the cart's floorboards -- muffled by canvas and the false bottom -- a dry old voice says, with enormous dignity: '...Are we far enough now? My legs fell asleep a day ago.'",
])
gm("Nobody consciously thought about Esbern since Riften -- but don't assume the TABLE meant to forget him. He genuinely doesn't know whether he was left below on purpose (good tradecraft, out of Thalmor sightlines) or simply forgotten, and his first line should ask that, not accuse it. Play his tone off the table's actual answer, live.")
plain("**ESBERN** (climbing out, stiff, blinking at the open sky): \"Well. I'll assume that was deliberate -- keeping the old man below decks, out of Thalmor sightlines. Very good tradecraft.\" (a beat, watching their faces) \"...It was deliberate. Wasn't it.\"")
bullet("**If they own up to forgetting him:** let it land soft, not scolding -- he's more amused than wounded once he decides they meant no harm. A dry, rueful \"Two days. The last loremaster of the Blades, riding with the turnips\" is enough; don't push past it into a lecture.")
bullet("**If they claim it was intentional cover:** he takes them at their word, and it becomes genuinely funny -- he starts complimenting a plan they didn't actually have, in growing detail, until someone cracks.")
plain("**ESBERN** (if they claim it was deliberate): \"Ah -- of course. The false bottom, the misdirection, waiting until we were well clear of the gates before I surfaced at all... very sound tradecraft. I particularly admired the part where nobody mentioned me, not once, for two full days. Exceptional discipline.\" (a beat, watching whoever's about to laugh) \"...I am allowed to notice when I am being made fun of, you know.\"")
plain("**Why he was down there** (if asked, either branch): \"The Thalmor have a standing warrant on me, and Riften is crawling with their eyes. Out here I am just an old man on a cart. Now -- where are we going, and what fresh end of the world am I to help you with?\"")
exit_("Once the laugh settles, he reaches back into the false bottom and pulls out the board.", "2  ESBERN'S WEB")
refplain("[Open production idea, not solved in this pass: a real physical pin-board prop for the table -- worth building separately as a printable prop or a diagram. Flagging, not resolving here.]")

# ---- SCENE 2
scene("2   ESBERN'S WEB -- the strategic briefing")
subtitle("Runs on the moving cart, not a stop. Never a wall of lore -- he shows them the web and they pull answers out of it by touching pins.")
readaloud([
    "Esbern braces the folding board against his knees, timing it against the cart's sway, and unrolls a cracked hide map across it, weighting the corners with whatever's at hand. Over it goes the board itself, strung with pins and red-and-grey twine -- thirty years of a Ratway wall, folded down small enough to work on his lap while the wheels keep turning under him.",
])
plain("**TWO COLORS OF THREAD, and he is fanatical about never letting them touch.**")
label("RED THREAD -- the dragons (a war)")
bullet("Five sleeping priests, each pinned to a tomb: **NAHKRIIN -- VOKUN -- RAHGOT -- OTAR -- MOROKEI.** Rahgot's pin has been moved OFF its tomb and left dangling (the party's own report from Forelhost: he rose and walked out). Esbern keeps touching it like a sore tooth.")
bullet("Something that doesn't sit right, and he can't yet say why: the old texts call Rahgot **the Angry** and Otar **the Mad** -- priests of fury, not patience. But since they woke, what little word has reached him -- refugees, rumor, a line here and there -- describes calculation instead. Coordination. Rahgot running three operations at once like a general. Otar building quietly in the Reach instead of raging. \"Fury doesn't wait,\" he says, more than once, like it bothers him. \"These two are waiting.\" (He does NOT have KONAHRIK, and he does NOT have the prophecy -- those come from Ismara later, if a player offers Rahgot's tomb. This is the anomaly her information explains, not a blank it fills; he has no way to have suspected a sixth thing existed, and does not.)")
bullet("Kynesgrove -- the first grave they watched come alive. Dozens of burial mounds in fading ink. And the HOOK: **blank spaces** -- mounds he knows exist and cannot place. He hates the blanks more than he hates the Thalmor.")
label("GREY THREAD -- the root-rot (an unmaking)")
bullet("The Eldergleam, corrupted. The 7,000 Steps, bleeding. The Throat of the World, circled three times in charcoal. NOT ONE thread crosses from grey to red -- and if a player ties them together, Esbern physically stops their hand: \"No. Two ends of the world, two different authors. Muddle them and you'll parry the wrong one.\"")
label("WHAT HE SAYS AT THE PINS (in pieces, reacting to what THEY know)")
bullet("**On the two apocalypses:** \"Two different ends, walking toward us from two directions. Alduin is the World-Eater. When he wakes in full, he does not come to rule -- he comes to end this age, so the next one can begin. That is a war, at least -- something with a will you can face. These root-rotters, Dagon's people, don't want the next age to come at all. They want nothing left to begin again with. The dragons are the wheel turning. The other thing is an axle breaking.\"")
bullet("**On where they're going:** \"The Throat of the World is not just the dragons' holy mountain. It is a PILLAR -- one of the stones that holds the floor of the world up. If the cult cracks it, time itself runs in the cellar. That's what your archer feels.\"")
bullet("**IF THEY SAY THEY'RE HEADED TO IVARSTEAD / THE GREYBEARDS:** he sits back, surprised, and reframes fast, tapping the grey thread. \"The monastery? That's not on either thread. That's the OTHER one. The Wall does mention them, eventually -- the Voice matters when a Dragonborn finally stands up -- but that's a later chapter, not this one. Go. I'll mind the pins.\" He does not try to redirect them toward Bleak Falls; he stays disciplined about the party's own choices, even though the Dragonstone is still the thing he wants most.")
bullet("**The thing he actually wants** (taps a blank spot): \"Bleak Falls Barrow. There is a stone in it -- the Dragonstone -- a map of every dragon grave in Skyrim. Without it we wait for each dragon to find US. Everything we do until we have that stone is a flinch, not a plan.\" -> Plant it. Don't resolve it. He will say it again the whole campaign.")

label("IF THEY MENTION RAHGOT'S TOMB -- player-driven, do not fish for it", red=True)
gm("Fires ONLY if a player -- almost certainly Davinia's, since Ismara holds the memory -- volunteers what the carving in RAHGOT'S tomb actually showed: five priests, a sixth mask above them called KONAHRIK, and the line \"when the five become one, the faithful shall ascend.\" Do not prompt, hint, or have Esbern ask leading questions toward it; this is entirely the player's to offer or withhold, and it's the player's telling, not yours -- never script Ismara's words. The carving is cryptic on its own -- an old prophecy about a mask, nothing that announces itself as a secret. What breaks it open is that it resolves the anomaly he's already noticed and cannot yet explain (Rahgot and Otar's reputation for fury, set against their patient, coordinated behavior since waking), and he does the interpretive work himself, live: not her handing him a conclusion, him reaching one.")
readaloud([
    "He doesn't say anything for a moment. His hands, which have not stopped moving pins and twine since he sat down, go still.",
    "'A sixth mask. Above the five. Say the name again.'",
    "He turns to his own board -- to Rahgot's pin, dangling loose off its tomb where it's hung for weeks. His mouth moves once, silently, fitting the new piece against something that's been nagging at him since they woke.",
    "'Rahgot the Angry. Otar the Mad. That's what the old texts call them -- fury, frenzy, priests who don't wait for anything. And since they woke, all I've heard is patience. Rahgot running three operations like a general, not a berserker. Otar building quietly instead of raging. I told myself grief does strange things to old wrath. I was wrong.'",
    "He looks up.",
    "'That is why they're waiting. The faithful shall ascend. It isn't a hymn -- it's a plan, and it explains men who were never patient a day in their unlives. Alduin isn't their god. He's their door. They mean to walk through him and not look back.'",
])
gm("THE STRATEGIC WEIGHT: everything he's told them about \"the dragons are one united war\" just got more dangerous, not less -- possibly a coalition that plans to turn on itself, which means stopping Alduin and stopping the priests may not be the same fight, and could even cut against each other before the end. Do not resolve this now; it's a live thread for later.")
bullet("**THE FOLLOW-UP** (real beat, player-driven): he asks, quietly, not suspicious, just aware of what he's holding now: \"How do you know this.\" What Davinia's player has her answer -- everything, nothing, a version -- is hers entirely.")
gm("OPEN THREAD, not resolved here: knowing this makes Esbern a bigger target than he already is. Flag it; don't spend it in this scene.")

gm("Esbern is the lore-dump risk incarnate. NEVER let him monologue -- cut him off with a complication, a question, a beat of Ylva groaning. The clue is in the conversation, never in the dump.")
refplain("[Open production idea, not solved in this pass: this whole briefing could become a real interactive object at the table -- physical pins the players move themselves, or similar. Flagging, not building it here.]")
exit_("Dusk finds lantern light around the road's next bend.", "3  THE TENT FAIR")

# ---- SCENE 3
scene("3   THE RESPITE -- Ahkari's tent fair")
subtitle("A deliberate breath. Warmth, color, the world being alive. NO threat.")
readaloud([
    "The road bends around a stand of gold-leaved aspens and the dusk ahead is full of lantern light. Eight tents stand pitched off the verge in a rough ring, dyed saffron and sea-green, patched so many times the patches have patches. A cookfire burns at the center. Rugs are laid out between the tents with goods on them: stoppered bottles in rows, bundles of dried herbs hanging from the tentpoles, blades curved in shapes no Nord smith cuts.",
    "Pack-frames stand against every tentpole, the shoulder straps worn pale and smooth -- the wear of real weight, carried a long way, on foot.",
    "A Khajiit in a coat of a hundred patches spots your cart and comes across the firelight fast, already talking, already sizing you up. 'Travelers -- and with horses under you, and a cart behind them! Ahkari has been waiting all day for someone worth the good prices. Sit, sit, look, touch, nothing here bites unless Ahkari says it might. Tea while you decide? Ahkari does not sell tea. Ahkari GIVES tea. It is the buying after that Ahkari is good at.'",
])
plain("**Why the tents** (only if asked; she says it lightly, an old wound worn smooth): the cities do not let Khajiit inside the walls. So they build their own little towns outside them, a night at a time -- a traveling fair of everything the walled markets never stock.")
label("TRADE -- the exotic fair (reflavored, but every mechanical item cites the Gear list)")
bullet("**Sun's Dust** -- a dried ash-country fungus, sharp and bitter. A FINISHED consumable, ready to use -- not a raw ingredient (GM: treat as a Cure Poison Potion, per the Gear Doc).")
bullet("**Weeper's Tears** -- a marsh venom in a wax-sealed vial, from bogs south of here. A RAW alchemy ingredient (VENITAS[P], GRAVITAS[S] -- Alchemy GM Reference), not finished; feeds Nora/Ismara's bench.")
bullet("**Moon Sugar** -- sold openly, a normal caravan good. Raw ingredient (GLACIES[P]/FORTITAS[S]/ANIMA[T] -- Alchemy GM Reference). **Skooma** -- the refined, finished product, sold quieter, a step removed from the open stall. This caravan is deliberately the easiest place in the campaign to find either. [Skooma's dose/addiction effects are a separate design item, not yet built -- do not adjudicate a first use until that's written.]")
bullet("**A handful of Rare Curios** (Alchemy GM Reference, Batch Three -- genuinely Khajiit-caravan stock, priced accordingly): Alocasia Fruit, Bog Beacon, Comberry, Marshmerrow, Saltrice. Ahkari can name where each one is from if asked; she likes explaining her own stock more than most of what she sells.")
bullet("**An Elsweyr-style curved saber**, out of the trade routes south -- mechanically the new Curved Blade type (**6 damage, Flowing Strike** -- Gear Doc), reflavored; Ahkari will demonstrate the curve is not decoration.")
bullet("**An exotic hunting bow**, strung with something that is not gut -- mechanically a Tier-3 bow (**9 damage, Envenomed**: apply a poison as a Free Action instead of a Minor); Ahkari will not say what the string actually is.")
bullet("**Paralysis Poison x2** (Rare) -- on a successful hit, the target makes a Might roll or is Paralyzed, losing their next turn completely. \"The good kind, from a woman near Hammerfell who owes Ahkari a favor she will not explain.\"")
bullet("**A coin that's always warm** -- no mechanical effect at all, priced as a curiosity. Pure flavor; sell it as a keepsake, not a magic item.")
bullet("Road food, arrows for Saijah, fair-ish prices. Haggling is social, not a fight.")
plain("**ESBERN, at the curved blades:** the caravan doesn't carry the Blades' own Akaviri-tradition steel -- but Esbern still crosses over to look, turns one over in his hands, and gets quietly, genuinely interested in the craft. \"Not our old style. But whoever ground this edge understood the same thing we did.\" A small, real beat -- not a purchase, not a lead, just an old scholar recognizing a cousin discipline.")
label("THE TRADE OF INFORMATION (this IS how Ahkari knows things -- play it as the mechanism, not a random trade)")
plain("She raises a rumor, and then she PROBES -- she wants more on that exact topic, not a swap of unrelated gossip. This is the actual demonstration of how a Khajiit caravan ends up holding better information than half the holds: not magic, just always asking the follow-up question. Pick or roll one to open with, then react live to what the table gives back before moving to the next.")
label("HER RUMORS (each one is an opening, not a statement -- she follows up on whichever one lands)")
bullet("**1-5, IVARSTEAD:** \"Ivarstead is emptying. Half the village ran. Something's wrong with the TIME up the steps -- a pilgrim walked three days and came down having aged a week.\" Then, leaning in: \"You are headed that way, yes? Ahkari can see it on you. Tell this one what you already know -- Ahkari trades fair for it.\"")
bullet("**6-10, WINDHELM:** \"Windhelm sealed its gates. Plague. They say the Stormcloak army is rotting from the inside -- and that two strangers, a grim swordsman and a coughing priestess, walked IN when everyone sane was walking out.\" [Krusp & Danica, heard as rumor.] Then: \"You know them? The swordsman, the priestess? Ahkari heard the names wrong, probably. Ahkari would like them right.\"")
bullet("**11-15, BLACK-BRIAR:** \"Black-Briar's looking for someone. Quiet-like.\" Then, careful, watching their faces: \"Ahkari does not ask who, and Ahkari likes her throat where it is -- but if this one already knows who, this one is not asking Ahkari to say it out loud. Just... nod, or don't.\" [Seeds the Dirge thread without naming it; her follow-up is fishing specifically for confirmation, not more rumor.]")
bullet("**16-19, THE SKY:** \"The sky's been WRONG east of here. A hunter swore he saw a dragon -- a real one. Two of them. Going toward the Rift.\" Then: \"You have seen the sky too, this one thinks. What did it look like, from under it?\" [The scouts, third-hand; the target stays unknowable regardless of what the table says.]")
bullet("**20, THE SWORD:** \"You've a sword that watches people.\" She doesn't ask a follow-up on this one -- she looks away fast, on purpose. \"No. Don't show Ahkari. Some things this one is happier not knowing.\" [She has noticed Alfonso. The absence of a question here IS the tell -- some rumors she doesn't want confirmed.]")
label("A FIRESIDE STORY (if they sit for one -- Khajiit oral-tradition performance, not a reading)")
readaloud([
    "Ahkari settles onto an overturned crate like it's a throne, and her voice changes -- pitched to carry, rhythmic, built for a ring of listeners around a fire, not a page. This is a story she's told a hundred times, and it shows.",
    "'Long before this one ever pitched a tent on this road, there was a company of strange fools who went down into the frozen halls near Winterhold, chasing a fortune that wasn't there. The old stories say a blood-knight guarded the deep rooms -- a warrior wrapped all in red who cut a giant of ice in half with one stroke, the way you or I might cut bread. They say when the blood-knight fell, the dead did not stay dead: eight shades rose from the dark to avenge him, hungry things with no faces, and the fools were caught between falling ice and rising shadow.",
    "And they say -- this is the part Ahkari likes best -- one of that company, a huntress with a bow, moved through that fight the way a cat moves through a house at night: too fast, too sure, faster than any mortal woman has business moving. The kind of fast that makes old grandmothers cross two fingers and spit, just in case. She danced through eight hungry dead things and put an arrow in every one that mattered, and walked out of that tomb into the Winterhold snow like she'd only been for a short walk.",
    "'Nobody in this one's family has ever met her. But the story is older than Ahkari, and it still gets told, and that is how you know it happened -- true stories don't need anyone left alive to swear to them.'",
])
gm("She has no idea who's sitting across her fire. Let the table feel that, and decide for themselves whether to say anything. [Sourced to Ch.6 -- the Pale Lady's tomb near Winterhold, the blood-knight, the ice atronach, eight vampire fledglings, and Seraleth's unnaturally swift, acrobatic fighting through them. Old enough by now (well before Ch.24) to have calcified into a told story; the current Riften/dragon events are still too raw to be legend yet, which is why this is the right story and the dragon one wasn't. Reskin only to another event with the same property: public enough to spread, old enough to distort.]")
label("MILA & THE CARAVAN KIDS")
plain("Ahkari's people have several children, and they're playing the way kids playing near a caravan fire always do -- underfoot, loud, half a game nobody outside it could explain. Mila watches with the careful hunger of a girl who's never been allowed to join something like that. Bjorn notices first, but he doesn't say anything to her directly -- this is closer to Saijah's kind of moment than his, and he knows it. He just catches Saijah's eye. Whatever Saijah actually does with that -- crosses over, says something, sends her with a word -- is the player's call; Bjorn's part in this is only the notice, not the permission.")
gm("If the table wants to camp WITH the caravan tonight instead of pushing on, that's a live option, not a rail -- Ahkari would welcome the extra coin and the extra watch-eyes. If they take it, fold Scene 4's vignettes into this camp instead of a mile further on; nothing below depends on the exact ground it happens on.")
exit_("Camp, a mile on (or here, if they stay). The last easy night.", "4  THE CAMP VIGNETTES")

# ---- SCENE 4
scene("4   DOWNTIME & CONNECTION -- the camp vignettes")
subtitle("Fire going, no walls, no Thalmor. Every vignette routes through a PC (Ismara/Davinia, Saijah, or Orion) -- never NPC-to-NPC. Never write a player's line or decision.")

label("VIGNETTE A -- ISMARA, APART FROM THE FIRE (early evening, camp's edge)")
gm("Davinia's player is driving ISMARA directly while she fronts this module -- so this is a PC scene, not an NPC one, and gets a SITUATION, never a scripted line. Ismara has taken herself off from the main fire tonight -- her own choice of ground, not a summons -- Codex open, rapier in reach. Note One (Concentration, and the three basic recipes) already happened, off-screen, before the session -- nothing to re-litigate here. Two things sit in front of her tonight, and letting them collide IS the scene.")
gm("FIRST -- hands-on RAWCRAFT, a real teaching moment: she's got whatever untested ingredients came out of Ahkari's fair (Weeper's Tears, or any of the Rare Curios -- Alocasia Fruit, Bog Beacon, Comberry, Marshmerrow, Saltrice) that she hasn't identified yet. Let the player actually pick one and Rawcraft it -- chew it, or read the arcane shape directly with the Sight (established, faster) -- and tell them what Essence(s) it reveals for real, off the Alchemy GM Reference. This is the player genuinely learning the mechanic by doing it as her, live, not being told about it.")
gm("SECOND -- Antoine's Journal 1 is open beside her: the documented Strain-1.0 data (Restoration ACCELERATES the Strain instead of curing it -- sourced fact, already established). As she works real Opposition with her hands, watching a Primary VITALIS actually meet a Primary VENITAS and cancel out to nothing, the contradiction is sitting right there for her to notice: by everything she's learning tonight, what Antoine built should not be alchemically possible. DO NOT resolve this or explain why it works -- that's the Tears of Rahgot, saved for much later. DO NOT script her reaction or her conclusion -- she is a PC; present both threads as facts and ask \"what does Ismara do with that,\" then run whatever comes back. Unease, curiosity, dismissal, or nothing at all tonight are all fine answers.")
plain("**YLVA** notices her peel off and follows without being asked -- she doesn't do subtlety, and she doesn't ask permission to be somewhere. She just walks over, sits down close enough to be a presence, and gets out her whetstone right there instead of at the fire. No question, no opening line. She's decided this is where she is now, and she's comfortable enough in silence not to fill it.")
gm("ISMARA'S RESPONSE to Ylva just being there is entirely the player's call too -- acknowledge her, ignore her, keep working, say something. Whatever it is, let it sit; this doesn't need to resolve into anything before Nora shows up.")
plain("A while later, NORA finds them both out here -- this is the first beat of her evening-long throughline of asking around about Orion (continues in Vignette B, pays off in Vignette C). She asks straight, a little nervous: \"Can I ask you both something? How do you know if wanting someone is worth what it costs?\"")
plain("**YLVA** (not stopping the whetstone): \"You want him? Go lie down next to him. If he says no, come back and sharpen something. Why is this a conversation.\" (a beat -- the closest she comes to tenderness tonight) \"Wanting things isn't complicated, little witch. People just make it complicated so they can lose slower.\"")
bullet("**ISMARA** (player-driven -- AIM only): the dangerous one to ask. She files everything, never lies, and is one of the only beings in camp who can SEE the Ring on Orion's finger for what it is -- she doesn't spend true things unless they buy trust. GM color, not a line: she's gone quiet through Ylva's answer, like she's turning something over. A warning to Nora would be true, kind, and a deposit in the account of a girl whose soul-vessel research fascinates her; or she says something warm and general and keeps the Ring for a better price later. Ask Davinia's player directly what Ismara actually says, if anything -- do not decide it for her.")
gm("Whatever Nora hears -- from Ylva, maybe from Ismara, maybe nothing at all -- she does what she always does with data: draws her own conclusion anyway, and moves on. Next beat of her throughline is in Vignette B.")

label("VIGNETTE B -- THE BLADE ON THE STONE (early evening, edge of firelight)")
gm("Alfonso rides with ORION this leg (nobody bears him since the Nora incident, Ch.24 -- he's just whoever's turn it is). Nora asks Orion's permission before she asks anything else -- she wants to examine Alfonso, specifically whether a soul anchored in an object can be COPIED rather than transferred, and she won't touch the rapier without Orion saying yes. Given what almost happened to her the last time she reached for that sword, this is a real ask, not a formality -- play the beat with that memory sitting under it.")
plain("**NORA:** \"I'm not asking to take anything from him. I want to understand how the anchor holds -- copy versus transfer, that's the whole question. Can GEAR look? Can I?\"")
bullet("**If Orion says yes:** GEAR runs a full technical pass out loud, precise and unfiltered -- he's describing the actual mechanism behind Hjolmar's phylactery work and doesn't know it's dangerous information to hand a grieving girl with two of her parents' souls in gemstones. Nora goes quiet partway through, and her eyes go to her own two gems, twice. Does anyone at the fire notice? Does anyone say something? She knows more by the end of it than she did at the start, whether anyone intervenes or not.")
bullet("**If Orion says no:** Alfonso answers for himself instead -- dry, a little pleased to be asked rather than studied. \"A soul is not a ledger entry, girl. Ask a kinder question and I'll answer it.\" (beat) \"Copied. As if I were two men now instead of one, and the second never got a say.\" There's a real chill under the dryness for that one line. Nora doesn't push. The door stays open for later.")
plain("Nora then finds SAIJAH separately and asks her the same question she asked Ismara and Ylva -- the second beat of her throughline, and the one she actually came over for. She asks it straight, in her precise, over-prepared way: how do you know when wanting something is worth what it costs? She's rehearsed the question and none of the possible answers. Whatever Saijah gives her, she writes NONE of it down -- the first thing all week she hasn't taken notes on.")
gm("Player-driven -- Saijah answers however the player wants; there's no wrong answer. Then Nora gets up and heads toward Orion's side of the fire. That's the payoff, in Vignette C.")

label("VIGNETTE C -- NORA (late evening, fire burned low; the payoff of her throughline)", red=True)
gm("This is the scene the whole evening has been walking toward -- give it the same weight as any combat set-piece; do not summarize it. She's 18, and she means every word of what follows. Play her plainly, not performed.")
readaloud([
    "She doesn't sit near Orion by accident tonight -- she sits close, deliberately, the two of you nearly touching. For a while she doesn't say anything, just watches the coals with him.",
    "'I've been asking everyone all night how you're supposed to know,' she says finally. 'I don't think there's an answer. I think you just have to say the thing and find out.'",
    "She turns to look at him properly. 'I like you. Not the careful way, not the notes-in-a-margin way -- I've tried to make it that and it doesn't work. I wanted you to hear it plainly, once, so you'd actually know. Whatever you do with it is fine. I just didn't want to spend one more night not saying it.'",
    "She doesn't look away. She's waiting.",
])
gm("THE CHOICE IS ORION'S PLAYER'S, ENTIRELY -- do not narrate or decide what he does. React live to whatever the player gives you.")
bullet("**If he doesn't engage:** she takes it -- genuinely, without performance -- nods once, says goodnight plainly, goes to her bedroll. Nothing about the camp changes in the morning. The door stays open; she meant that part too.")
bullet("**If he engages:** let whatever the player has him do or say actually play out at the table. It's theirs -- don't summarize it back into a bullet after the fact.")
gm("EITHER WAY -- THE RING SAW ALL OF IT, because it always does. Somewhere in Solitude, Valerius files the one thing tonight actually produced: the empty man still leans toward something, and now it has a name. When the Reckoning comes, he already has this in hand. Say nothing of it to the table now.")

label("VIGNETTE D -- VARON, ACROSS THE FIRE (late evening, after camp quiets)")
gm("The migraine is starting to sharpen: a low ache, pointing south, toward the mountains -- proximity doing what proximity always does to her. Saijah's player should feel this is the last easy night. Then Varon steps into the firelight across the camp, just far enough to be visible, and waits. No pressure, no demand -- crossing the distance is entirely the player's call.")
bullet("**If Saijah goes to him:** he doesn't wait for her to ask. \"I ran when you needed me steady. I know what that cost you, and I'm not going to pretend it didn't happen so it's easier for both of us to sit here.\" He doesn't ask forgiveness -- he says the last part plain: \"I'm not going anywhere again. That's not an apology. It's just true now.\" Then he actually stays, as long as she wants, saying nothing further unless she does.")
bullet("**If she doesn't go:** in the morning there's a small carved piece near her bedroll, made overnight by firelight -- something specific to her, not a generic token (GM: pick one real detail from her gear or history and carve that). No note. He doesn't approach again unless she comes to him first. He means it.")
gm("Player-driven throughout -- what Saijah says or does, if she goes to him at all, is hers.")

label("VIGNETTE E -- THE CART, LATE (once the fire's mostly coals)")
gm("Mila can't sleep -- up on the cart, blanket around her shoulders. She doesn't go looking for Bjorn or Saijah specifically; she just sits where both are likely to notice her, and they do. This is Saijah's and Alfonso's scene as much as Bjorn's -- Mila has come to think of them as something like a second set of parents since Forelhost, and this beat is built to use that, not skip past it.")
readaloud([
    "Bjorn sees her first and comes to sit, not saying anything for a while -- he's kept a careful distance since she asked why he feels like more than one person, and tonight he closes it a little. 'I made a promise once,' he says finally. 'Broke it. Carried that forty years.' He looks at her, not away. 'Not doing that again.' It's the voice he uses for the things that matter, which is not a voice he uses often.",
    "Saijah's the one who notices Mila's hands are shaking, if anyone does -- close enough by the cart to see it before Bjorn does.",
])
bullet("**SAIJAH'S OPENING (player-driven):** what she does with that -- says something, moves closer, lets Alfonso speak, or just stays quiet and present -- is entirely the player's call. If Alfonso speaks, give him something real and in his own voice: he understands promises and their cost better than anyone at this fire, and he isn't sentimental about saying so.")
plain("Bjorn gets up and shows Mila the mare instead of finishing the moment with words -- left side, breathing even, hands open. The black mare, unbothered by almost everything, suffers the careful child where she suffers nobody else. Mila brushes her. Somewhere in the middle of it her hands stop shaking, and whoever's watching -- Bjorn, Saijah, both -- gets to actually be there for it instead of just narrated at.")

reflabel("DOWNTIME OPTION -- FORAGING (any PC, before dark; optional)")
refplain("Its own d20 roll, no skill, no stat (Ingredient Foraging Map). GENERAL: roll d20 on the Rift table below, get 1 of whatever the number says. TARGETED (hunting a specific ingredient they know grows here): find its number N on the table; roll at or under N to find it, and quantity = (N - roll) + 1. Roll over N = an empty look-around, or GM's call to hand them the rolled entry instead.")
statcard([
    "**THE RIFT -- FORAGE d20 (low = rarer find)**",
    " 1 Hagraven Feather   6 Falmer Ear       11 Honeycomb          16 Garlic",
    " 2 Vampire Dust       7 Canis Root       12 Blue Butterfly Wing 17 Thistle Branch",
    " 3 Ectoplasm          8 Mora Tapinella   13 Butterfly Wing      18 Nightshade",
    " 4 Nirnroot           9 Nordic Barnacle  14 River Betty         19 Blue Mountain Flower",
    " 5 Luna Moth Wing    10 Bee              15 Blisterwort         20 Wheat",
])
exit_("Morning. The open stretch.", "5  THE HIDE")

# ---- SCENE 5
scene("5   THE SHADOW ON THE SNOW -- the hide")
subtitle("The set-piece. Two dragons, a logging cut through the pines, a child and an old man in a cart. The only play is to not be seen.")
reflabel("THE TERRAIN (give the table ALL of it -- their plans are built from this)", red=True)
refbullet("**THE CUT:** a quarter-mile-wide gap clear-felled through the pines for a Riften timber crew's haul road -- stumps waist-high in rows, the ground churned to mud and old sawdust, the sky wide open overhead for the only stretch of this whole road. The party is a third of the way across it when the shadows come.")
refbullet("**THE STUMP ROWS (either side):** waist-high, staggered. Not real cover from directly overhead, but they break up the ground enough to lie flat between them and read as terrain-noise instead of a person, if nobody moves.")
refbullet("**THE FLUME DITCH:** a log-flume cut, dug to slide timber downhill to the river, three feet deep, dry this season. A person can lie full-length in it, hidden from above; the cart cannot fit.")
refbullet("**THE SLASH PILE (north edge, near the treeline):** cut branches and bark heaped for burning -- loose, and it WILL shift and rattle if handled carelessly (Scene 6 uses this).")
refbullet("**THE CART:** canvas over bows, dirty grey-brown -- from altitude, still, with its fire-colors hidden, it can read as one more slash heap. MOVEMENT is what kills: wheels turning, animals shifting, faces looking up.")
refbullet("**THE TREELINE**, close on both sides: real cover, but forty yards off across open ground -- a long way to run under two dragons' eyes.")
refplain("[Judgment call, flagged: the original draft set this on bare open saddle, which doesn't sit right against the Rift's actual tree cover near a Falkreath-rivaling timber region. The mechanical shape -- open exposure, one lie-flat option, one dry-cut option, the cart-as-drift -- is what matters; reskin freely if this dressing doesn't land.]")
readaloud([
    "The road threads out of the pines into open sky -- a logging cut, a quarter mile of stumps and churned mud where a Riften crew has been felling timber for the haul road, the trees pulled back on both sides for the first time all day. You're a third of the way across it when the sun goes out.",
    "Not a cloud. A shadow crosses the mud ahead of the cart, vast and wing-shaped -- and your whole body understands it before your mind does. There's a sound with it, wingbeats bigger than sails, tearing the air in long strokes, and you have heard that sound exactly twice in your lives, and both times people died. A second shadow crosses the first.",
    "Two of them.",
    "They wheel out over the cut, unhurried, patient, reading the ground the way Saijah reads a trail. They are not passing through. They are looking for something. They have not seen you yet.",
])
plain("**FRAME THE STAKES OUT LOUD, THEN STEP BACK:** say it plainly -- you fought one dragon and barely survived; there are two, in the open, with a child and an old man in the cart; there is no version of a fight here that ends well. Then stop talking. If the table decides to try anyway, that's a real choice they're allowed to make -- run it honestly, don't fudge it soft, and let the terrain and the odds be the actual argument instead of you overriding their agency with narration.")
refplain("**RUN THE NOTICE CLOCK NOW, IN FULL** (restated here so this scene never depends on flipping back): 6 boxes, starts empty. 5 complication beats, each tied to a party asset, difficulty climbing beat to beat -- Easy(+2), Standard(0), Hard(-4), Hard(-4), Very Hard(-6). The responsible character rolls; success contains it, no Notice; failure adds 1 Notice; a natural 20 adds 2 Notice AND a dragon banks toward them (next beat one step harder); a natural 1 is active masking -- Notice drops 1 (min 0) and the next beat eases a step. Reward every proactive idea with a step of ease or Advantage. At Notice 6 they're spotted and it's a dive -- telegraph that hard before it happens.")
refplain("Walk the five tells as they come up, in whatever order the table's actions surface them: MABLE SPOOKS (Bjorn, animal handling; the mare in harness eases it a step), GEAR HUMS (Saijah/Orion, Guile; GEAR needs permission to power down), ALFONSO'S ROT-AURA drifts downwind (Orion -- carrying him this leg; auto-success if he pulls it tight through the working), MILA'S FRIGHTENED BREATH (Bjorn or Saijah; comforting her IS the roll), HEAT BLOOM (Davinia/Ismara can sheathe the cart's warmth in cold -- a quiet temptation each time she uses the gift).")
gm("**ESBERN**, low, mid-tension: \"Look at them. They aren't roosting -- they're RANGING. Ahead of something. Alduin is raising his kin and sending them out to look.\" He does NOT know their target; keep the dread general.")
bullet("**If Notice fills:** the nearer dragon's head turns, the throat lights from within -- RUN. Scatter, abandon the cart; Bjorn's speed (Scene 6) is the only thing that saves anyone. TPK is on the table and earned.")
exit_("At Beat 5, or on any failure that puts the dragons lowest -- the danger reaches Mila.", "6  BJORN'S SECOND FLARE")

# ---- SCENE 6
scene("6   BJORN'S SECOND FLARE -- the worst moment")
readaloud([
    "The near dragon drops low over the cut -- not at you, a hunting pass -- and its downdraft slams into the cart like a fist. The cart rocks. Up on the slash pile, the loose branches let go in a grinding slide, straight down at the front bench. Straight at Mila.",
    "She's frozen. Bjorn is at the rear of the cart, twenty feet and a full second too far, and there is no possible way the old man reaches her in time.",
    "He reaches her in time.",
])
plain("For one impossible instant Bjorn crosses ground no man his age should be able to cross -- there, and then between the child and the falling stone -- and it doesn't feel strange to him at all. It feels like the easiest thing he's done all week. He doesn't look at his hands. He doesn't look at anything but Mila, checking her over once, fast, the way he's checked her a hundred times before, already breathing like it's over.")
gm("WHAT THE TABLE MAY CONCLUDE: the old mercenary is reviving -- youth, speed, the War-Hound returning. A rejuvenation. Eerie. That is ALL. The Dragonborn truth does NOT surface and must not leak (his FIRST flare was the Ratway stairs, Ch.21 -- one prior data point, still no word for it). Davinia, through Ismara's Sight, sees the doubled sun of his soul flare bright and bank down -- one more silent data point. Hold the secret.")
plain("**BJORN** (gruff, not meeting anyone's eye): \"...Adrenaline. You'd be fast too, with that thing overhead. Get her down. Keep moving.\"")
gm("THE DIRECTION THEY LEAVE IN: the dragons bank away EAST, down the long line of the valley they just climbed out of. If a player asks which way that is, give the compass point ONLY -- east, back down the road they came up -- and stop there. Do not name the city. A player tracking their own route out of Riften can do that arithmetic themselves; that quiet dread is theirs to assemble, not yours to hand them.")
refplain("[Open production idea: a simple regional map prop for this beat -- the party's position, the road, and the dragons' heading drawn on it -- would let a sharp player do the orientation themselves. Also flagged: a battlemap for the logging cut, possibly with small animated fly-over moments. Neither built in this pass.]")
exit_("The shadows shrink east and are gone. That night, or held for later -- the Reckoning.", "THE RECKONING")

# ---- RECKONING
scene("THE RECKONING -- Valerius comes in person")
subtitle("GM CHOICE on timing: this road-camp, or held for Ivarstead. Locked design: scratch §18/19. Not a fight. Not survivable as one. This is NOT a public confrontation -- read the staging carefully.")
plain("Seeded by Orion disobeying the Constance-enthrall order (Ch.24). Valerius Caelus, **AP 30**, arrives IN PERSON that night -- a vampire lord travels fast. Not a fight, not a save, and the party cannot intervene: that is the point. **He does not come to the fire. He takes Orion FROM it.** The Contest Level-Gap Penalty (**-20 to -25** on any will-vs-will resistance) is the wall, and the rules back it.")
bullet("**THE PULL:** at the fire, the Ring goes from familiar cold to a KILLING cold with a will behind it. Orion does not decide to stop; he simply stops, rises, and walks from the firelight into the dark -- compelled, a thing on a string. The camp watches him go and cannot stop it. **This is the only part the rest of the party witnesses directly.** The interrogation and the trim happen at the treeline, out of earshot, by design.")
bullet("**THE TREELINE:** Valerius is already waiting there -- patrician, unhurried, almost fond. From here, this beat belongs entirely to Orion.")
bullet("**THE INTERROGATION:** he does not ask where they're going. He asks Orion to report on the party -- who loves whom, who needs what, who holds the sword and who the sword answers to. Orion, owned, cannot refuse; he gives it up in his own voice. His blind spots protect what he doesn't know (the Crown's fate, Bjorn's wrongness, what Davinia truly is). GM: decide live what Orion actually knows and leaks -- this is intel Valerius BANKS for later, not something the table hears in the moment; they're still back at the fire.")
bullet("**THE TRIM:** \"A hand that will not close when I will it is not a hand. Close it now -- around the blade -- and trim it.\" Orion's own good hand draws his own blade and takes the off-hand below the elbow. Valerius never touches him. Courteous throughout: \"This is mercy, Orion. I am keeping the rest of you. Serve better.\" **MECH (permanent until remedied):** the off-hand is gone; ANY Minor Action requiring the hands becomes a MAJOR Action until Orion has a prosthesis. Movement and speech are the only Minor Actions left to him. No save.")
bullet("**THE FETCH:** he sends the maimed, one-handed Orion back to the fire to bring him Davinia. \"Bring me my cousin. I would speak with her.\" He does not care whether the others follow -- they cannot touch him regardless. Orion returns to the firelight missing a hand, and fetches her, compelled or simply relaying it -- the camp's first sign anything happened at all.")
label("THE MEETING -- VALERIUS & \"DAVINIA\" (player-driven; GM only AIMS Valerius)", red=True)
plain("*** DO NOT SCRIPT ISMARA/DAVINIA. The player controls what she reveals, hides, says, or does. Run Valerius TOWARD her and react to the player's choices -- the notes below are how to aim him, not what happens. ***")
bullet("**HIS AIM:** to meet his cousin and dynastic claimant, assess her, and begin folding her Caelus claim into his ascension. He arrives expecting a mortal woman.")
bullet("**WHAT HE FINDS:** silver-white skin, eyes the wrong age -- and an old vampire knows unnatural longevity on sight. His aim shifts mid-scene from courting a claimant to working out what she actually is. He probes, courteous, the courtesy DEEPENING as he senses old power in her.")
bullet("**THE TRAP IN THE TEST:** he may test her with family knowledge only Davinia would have -- but Ismara holds the mother-archive and most of Davinia's memory, so the PLAYER can pass such tests if she chooses. Trivia won't expose her; what nags him is what he SEES and FEELS.")
bullet("**GM-AIM DEFAULT (unless the player reveals):** seed, not reveal. He leaves unsettled and intrigued, filing that his cousin is \"not herself.\" The real collision stays banked for later.")
bullet("**IF SHE REVEALS:** run the full collision -- two stasis-tyrants meeting, one player on the board he can neither own nor out-claim. Let his composure crack only slightly; the table should sense he's met something above him. Don't win the scene for him.")
bullet("**THE EXIT:** only now the drama. He thanks her -- or the camp, whoever he's addressing -- for the visit, steps back from the firelight, and comes apart upward into the winged shape: one long climbing beat of membrane and cold air, gone south.")
gm("ORION'S EXPERIENCE: the horror isn't the pain, it's being OWNED -- forced to betray his party with his own mouth and maim himself with his own hand, entirely offstage, and then made to walk back into the firelight and perform normal in front of people who have no idea yet what just happened to him. Let the player choose how he wears that when he returns; never narrate his inner life for him.")
gm("If Vignette C fired (either branch), Valerius already knows about Nora. He needs to do nothing with it tonight. Knowing is the leverage, banked for later.")

# ---- SCENE 7
scene("7   THE FAINT WRONGNESS -- the approach")
subtitle("The bridge scene. Normal physics end here; the first time-slips arrive on the last mile.")
readaloud([
    "The two shadows shrink into the east and are gone, and the breath goes out of all of you at once. The road drops toward a valley, and at the bottom of it sits Ivarstead, small and grey against the mountain behind it. You are nearly there.",
    "Then, on the last mile, each of you catches it -- once, and only once. A footprint appears in the mud of the road a heartbeat before Bjorn's boot comes down to make it. A word someone said comes back off the rocks a moment too late, in their own voice. The cart's shadow lags a half-step behind the cart.",
    "Small things. The mountain stands ahead, and the whole road bends toward it.",
])
gm("One slip per character, once each, unrepeated -- let each player pick how theirs lands or hand them one. Do NOT explain. The weather system switches ON at the town line; this mile is its knock at the door.")
exit_("Part Two. The temporal weather switches ON at the town line.", "PART TWO -- IVARSTEAD")

rule()
raw("\\pard\\sb120\\sa200\\cf2\\b\\fs40 PART TWO -- IVARSTEAD & THE BLEEDING STAIR\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i The party's first contact with the Dagon apocalypse and with Gaelen the Root-Twister. Advance, never resolve: the Tower cosmology lands HARD; everything personal stays loaded. The town -> the ascent -> High Hrothgar -> the undercroft -> the sealing.\\i0\\cf1\\par\n")

reflabel("GM RULES -- THE TEMPORAL WEATHER (proximity zones + the alarm)", red=True)
refplain("The distortion is a SIDE EFFECT: the cult corrupts the TOWER from the undercroft; the mountain's existing Time-Wound turns that violence into weather. The cult does not target the Wound and does not control the weather -- they just know how to surf it. Each scene below restates its own zone at the point of use; this is the master card.")
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
refplain("The zone tables and secondary-horror list are built to the locked dials (scratch 5); adjust freely at the table -- the ALARM and the DREAD are the mechanic, the numbers are servants.")

reflabel("GM RULES -- SAIJAH'S DOUBLE MIGRAINE", red=True)
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
    "Ivarstead is a handful of grey houses pressed against the biggest thing in the world. Half of them stand with their doors open. Through the nearest doorway a table is still set for a meal, and a dresser hangs open with clothes trailing out of it into the mud. Smoke rises from three chimneys. A barricade of farm carts and fence posts blocks the lane toward the river, and nobody stands behind it.",
    "At the bridge, the first Waystone leans in its socket, and it is bleeding: a slow black sap crawling UP the carved stone, against gravity, pooling in the old runes until they read wet and dark. Where a drop falls, it falls slowly -- slower than it should, like it is falling through deeper water than the world's.",
    "A big man sits on the inn's steps with a loaded pack at his feet. He watches you come up the road the way a man watches the first help arrive at a fire that has already taken the roof.",
])
plain("**KLIMMEK:** \"You came. Gods -- somebody came.\" (a breath, steadying) \"I still have the supplies for the monastery. Been packed nine days. Every time I set foot past the third stone something... happens to the walk. Hours go by that I don't remember walking. Once I came down and my beard had grown out three days. The masters are up there ALONE, and I can't -- I can't make the climb.\" He pushes the pack toward you. \"You're climbing. I know you are. Take it. Please.\"")
bullet("**If they take the pack:** he grips whoever takes it by the forearm, hard, and can't speak for a second. \"Tell them Klimmek sent it. Tell them I tried.\"")
bullet("**If they hesitate or refuse:** he doesn't argue. He carries the pack back to the inn steps, sets it where it can be seen from the whole square, and starts asking -- quietly, doggedly -- what it would take. Coin. Meals. His fishing boat. He has already decided they're climbing; he's only finding the price.")
bullet("**If they ask him to come along:** he tries. He makes it fifty steps past the bridge and stops dead at the edge of the third stone's reach, sweating, and his legs will not go on. \"...You see it now. It isn't cowardice. The mountain won't have me.\" A live demonstration of what the Stair does, before they set foot on it.")
gm("SAIJAH -- STATION 1 fires at the Waystone: hand her player the sensation -- the black sap NAGS, familiar, can't place it. An itch, not a recognition. (The DOUBLE MIGRAINE fires the instant she TOUCHES it -- debuff card ON for the rest of the Stair.) DAVINIA/ISMARA -- hand her player what the Sight shows: the corruption reads as a structured working running DOWN into the mountain's root, not spilling up from the stone. What either player does with what they're handed is theirs.")
reflabel("THE TOWN'S BROKEN TIME (Zone 0 -- social, not lethal)")
statcard([
    "**TOWN DISTORTION (color any conversation with one of these; light touch):**",
    "- An answer arrives BEFORE the question finishes being asked.",
    "- A villager repeats the last exchange verbatim, unaware; it plays like an echo.",
    "- Someone thanks the party for a thing they have not done yet.",
    "- A door is heard closing a full breath before it visibly closes.",
    "In fights here: Zone 0 Tempo (1 Frozen | 2-4 Dragging | 5-16 In step |",
    "17-19 Quickened | 20 Unmoored), alarm rare. The horror is social first.",
])
label("NO HAVEN AT THE FOOT (the everyone-climbs logic -- play it, don't announce it)", red=True)
bullet("The corruption is creeping DOWN into the streets, and Dagonites move through the empty half of town after dark. There is nowhere safe to leave a child, an old man, or a horse.")
bullet("**The lesson the fiction teaches:** to wait below is to wait inside the thing they came to stop. Bjorn will not be parted from Mila; the party will not abandon either of them; and on the mountain, the weather ISOLATES stragglers. The whole crew climbs as one -- guarding their two most precious people up a mountain of cosmic horror.")
label("THE INN NIGHT -- the attack (runnable, not a summary)", red=True)
gm("Written for the inn, the least-bad shelter -- but if the party beds down anywhere else in town, the attack finds them there instead. The register is the point, not the address.")
readaloud([
    "The attack comes at the dark end of the night, when the common-room fire has burned to coals. Glass breaks somewhere at the back of the inn. Then the front door booms -- once, twice, something heavy swung against it -- and through the shutter slats you can see torchlight, five points of it, spreading to circle the building.",
    "A voice outside begins to recite. It is calm, level, patient -- the cadence of a prayer -- and the words are about fire, and gates, and the mercy of a clean unmaking.",
])
gm("RUN IT: 4 DAGONITE CULTISTS + 1 SHARD ZEALOT (cards below). Zone 0 Tempo for everyone; the cultists CHEAT theirs via tide-shards -- if this is the party's first sight of a cheat, fire Ylva's Referee's Wrath beat (Scene 9) HERE instead of on the Stair. They come to BURN, not to loot: this is the Kvatch register, what Dagon taking a space looks like. Anything left OUTSIDE -- cart, supplies, animals -- is torched or taken. The mare comes INSIDE (fearless, she walks in like she has always lived indoors; Mable has to be dragged and hooded). Two villagers sheltering in the common room get grabbed through a window mid-fight -- alive, hurt, screaming -- savable if someone moves NOW. The zealot fights to the end; surviving cultists withdraw chanting when it falls. Dawn comes grey.")
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
refplain("ZONE 1 through Waystone 2 (Tempo: 1-2 Frozen | 3-5 Dragging | 6-15 In step | 16-19 Quickened | 20 Unmoored; alarm ~15 min). ZONE 2 from Waystone 3 up (1-3 Frozen | 4-7 Dragging | 8-13 In step | 14-18 Quickened | 19-20 Unmoored; alarm ~10 min). Run the alarm honestly -- the dread of the sound is the mechanic.")
gm("ROPE RULE, said out loud once: stay together. Anyone who strays faces the weather ALONE -- this zone's Tempo with nobody to pull them back into the shared now.")
label("SAIJAH -- STATIONS 2-4 (paced, never a lecture; hand her player each one as sensation)")
bullet("**Station 2 (deeper):** she PLACES the signature -- \"I've felt this before\" (Thornheart; the Solitude temple tree) -- but it reads as coincidence. Two points, no pattern. Hers to voice or sit on.")
bullet("**Station 3:** the migraine DOUBLES -- two simultaneous sources, which makes no sense to her. The -2/-2/+2 is fully on. Something is deeply wrong; she does not know what.")
bullet("**Station 4 (Gaelen's voice -- through the corrupted leylines, to her alone, mid-climb):** warm, sincere, reasonable: \"You feel it as pain because you were taught the cage is your body. Forests that burn and regrow in a breath. Beasts that never stop becoming. I am not breaking anything, little sentinel. I am opening a door that was nailed shut before you were born.\" -- and the SCALE slips: \"...prisons. I have been opening them for years. This is not the first, or the last.\" A clue she cannot yet hold.")
label("COMBAT -- THE CHEATED GAME (Dagonite ambushes)", red=True)
gm("Use CULTISTS + a ZEALOT per ambush (cards, Scene 8). They surf the weather: stolen turns, doubled moves, strikes out of sequence -- while the party rolls Tempo. Make the unfairness VISIBLE. Then let the party break the shards and even the game -- that reversal is the fun.")
plain("**YLVA -- THE REFEREE'S WRATH (this develops SAIJAH, not Ylva):** the first time a cultist cheats, Ylva's hackles rise BEFORE it happens -- she growls at empty air a half-second early, then the cheat comes. She cannot name 'temporal weather'; she knows a FOUL happened. \"They're cheating. The hunt has RULES.\" Her fury is theological -- the laws make the game sacred; these people spit on the game itself. Saijah, watching, is seeing the exact hunt-rhythm sense Hircine could one day give HER.")
plain("**VARON** (falling in at Ylva's shoulder, blades reversed): \"Then we kill them properly. Inside the rules. For once, hound, we agree.\" She doesn't answer him. Her growl changes register -- and the two who cannot stand each other fight back to back, aligned. Give it one beat out loud.")
label("THE OTHERS ON THE CLIMB (each one routed through a player)")
bullet("**NORA'S GEMS (whoever looks at her during a weather shift):** the two black gems at her throat are stuttering -- the light inside them doubling, like two heartbeats out of step. She's clutching them and saying nothing. A horror beat, not a resolution; whether anyone goes to her is the table's call.")
bullet("**ALFONSO (carried by ORION this leg):** Orion feels him brace every time the weather shifts -- a flinch in the iron, each time, that he will not explain. If pressed: \"Ask me at the bottom of the mountain.\" (He does not know what broken time does to a soul living in a sword. He does not want to learn it here.)")
bullet("**BJORN:** his speed may FLICKER again on the climb if Mila is threatened -- shorter than the road flare, still read as rejuvenation, never named. Davinia's Sight logs one more silent data point if her player looks.")
exit_("The last switchback. Grey stone walls in the cloud. The monastery.", "10  HIGH HROTHGAR")

# ---- SCENE 10
scene("10   HIGH HROTHGAR -- the quarantine of the masters")
subtitle("Character scene at the top of the world. The TOWER hard-reveal, Kynareth's first new word in years, and the Ring feeding it all to Solitude.")
readaloud([
    "The monastery is grey stone against grey sky, and the doors stand barred from within. When they open -- slowly, to Klimmek's pack and your knock -- the man inside has a face like a starved hawk, and his hands keep trembling after he grips the door to still them.",
    "Behind him, in the great bare hall, three more grey-robed figures sit in a triangle around a brazier, and the air between them HUMS -- a note below hearing, steady as a heartbeat. You feel it in your teeth, in the floor, in the old stone. The hum never wavers, not even for them to breathe.",
    "Underneath it all, faint and constant, the mountain is trying to shake itself apart -- and the hum is holding it, barely, the way a hand holds a lid down on a boiling pot.",
])
plain("**MASTER ARNGEIR** (voice cracked from disuse and overuse at once): \"You climbed through THAT. Then you have seen what is happening to the mountain.\" (he looks at the pack, and something in the hawk face almost breaks) \"...Klimmek's bread. Forgive me. It has been -- some time.\"")
label("WHAT THE MASTERS GIVE (scholarship, not senses)")
bullet("**THE HARD REVEAL -- the word TOWER:** \"You stand on one of the pillars of the world. The Throat is a TOWER -- one of the stones that holds Mundus against Oblivion. The zealots below are not desecrating a holy place. They are cutting a load-bearing wall of the WORLD. The shaking you feel in time is the Tower beginning to fail.\" -> The party LEAVES KNOWING they are in the main plot. Land it plainly.")
bullet("**The Way of the Voice OPENS:** the masters accept the party as the first help to reach them; the door stands open hereafter (scholarship, Word Wall locations for seekers -- the masters themselves cannot shout offensively enough to leave; holding the mountain takes everything they have).")
bullet("**If the party asks them to come fight:** ARNGEIR: \"If one of us stands up from this circle, you will feel the reason in the floor before your next breath.\" He is not refusing. He is describing a load-bearing wall.")
bullet("**What they CANNOT do (hold this line):** no special senses of ANY kind. They do not see Ismara in Davinia. They do not sense anything in Bjorn. They cannot name a Dragonborn -- no one can. They hold the summit by Voice and endurance, and they are losing.")
bullet("**The geography clue:** \"The working is BELOW us -- in the undercroft, at the mountain's root. The summit path is SEALED (only a Shout clears it, and none of us can be spared from the holding). Whatever you came to stop, you will find it downstairs.\"")
label("KYNARETH'S REVEAL (Saijah -- station 5; the goddess, NOT the masters)")
gm("At Kyne's own peak, the goddess finally gives Saijah something NEW -- hand her player the vision itself, cryptic, non-verbal, the first fresh thing after all the repeated instructions: an IMAGE she cannot decode -- a wind carrying a great soul upward, toward a hall of mist and warriors -- and a certainty, wordless and enormous, that her ENDURING matters to the end of the world. Somewhere in the image, unnamed, a shape like a big man standing between a child and the sky. She gets a FEELING about Bjorn, never a label. What she does with any of it is hers. GM-only: this is the reason to endure the pain -- delivered the night BEFORE Hircine offers to end it.")
label("THE OTHERS AT THE MONASTERY")
bullet("**DAVINIA/ISMARA (two things to hand her player, separately):** FIRST, what the Sight shows -- hers are the only eyes that can READ the Tower: the leyline lattice, the corruption's shape crawling up the root like ivy under the skin of the world. A Sight showcase; hand her the picture and let her do with it what she likes. SECOND, make sure the player knows what her own gift could do here: FREEZE the wound locally -- stasis set against chaos, tactically real. GM-side only: using it advances the CDI. Put the option on the table once, plainly, and run whatever she chooses. Do not push it and do not forbid it. (The masters see none of this either way.)")
bullet("**ORION -- the tonal architect:** the corruption is a FREQUENCY phenomenon and he is the one person equipped to read it as MECHANISM. Diagnostic Song against the hum: he maps the working's structure -- this feeds Scene 11's disruption options and his Severance research. ARNGEIR, after the Song (the masters' respect, earned and real): \"We shout. You listen. I begin to think listening was always the deeper school.\" THE GUT-PUNCH (GM-only, say nothing): the Ring has fed Valerius the entire apocalypse, live, all climb.")
bullet("**GEAR** (he climbed; everyone climbs): quantifies the break -- \"local causality variance exceeds Dwemer tonal tolerances by a factor of nine. I have no protocol for this. I find I do not enjoy that.\" Pairs with Orion. Light.")
bullet("**ESBERN:** among the masters' books like a starving man at a feast -- and the one who says the OTHER quiet part: \"The Wall shows a council of heroes when the Dragonborn fails. It never shows what holds the SKY up while they argue. Now we know.\"")
exit_("Down the inner stair. The hum fades above; something older hums below.", "11  THE UNDERCROFT")

# ---- SCENE 11
scene("11   THE RITUAL IN THE UNDERCROFT -- Gaelen at the root")
subtitle("The boss. ZONE 3 -- the worst weather. Objective: DISRUPT THE RITUAL. Gaelen escapes by design; Jasper does not.")
readaloud([
    "The undercroft is older than the monastery above it -- a vaulted root-cellar of the world, columns of living rock running down into dark that breathes. The Dagonites have made it a garden. Red light comes up out of carved channels in the floor, all of them running inward to a central well where the mountain's root stands exposed: a column of something older than stone. And growing INTO it, like ivy into a wall, black sap-lines climb upward from an array of obsidian shards arranged in a blooming spiral.",
    "A Bosmer moves through the array unhurried, crimson chitin catching the light, one arm a grafted mass of charred heartwood and obsidian that gestures at things he is not looking at. He is adjusting each shard with the care of a man tuning an instrument he loves.",
    "Without turning, in a voice that is warm and genuinely pleased: 'Oh -- visitors. Good. I hoped the mountain would manage to be heard. Come in, come in. You are not interrupting; nothing can interrupt this. But company is rare, and I have wanted to meet you for the longest time.'",
])
label("GAELEN -- HOW HE PLAYS (unsettling, never evil)")
bullet("The warm, sincere, reasonable CENTER of an apocalypse. He talks like an ally trying to get compatriots to stop suffering for a stagnant world: the Aedra gave mortals a CELL -- linear time, fragile flesh; Dagon offers the KEY; the Unmaking is HEALING.")
bullet("**THE QUIET WISH (plant it -- overheard when he thinks no one listens, to no one):** \"I want it to be perfect. Please... let it be perfect.\" Not a plea, not a crack in a mask -- the closest thing his altered architecture has to hope. Every projection the players make onto it will be slightly wrong. He should leave the table unable to dismiss him.")
bullet("**THE YLVA EXCHANGE (give both liturgies one beat, out loud):** GAELEN: \"Rules are the bars, hunter. I am unbending them.\" YLVA (shaking with a fury even she cannot name): \"The rules are what make the hunt HOLY. Prey runs, hunter chases, the fastest wins -- that is the whole church. You are not freeing anything. You are pissing on the game.\" The most theologically serious person in the room about why the Unmaking is wrong is the werewolf.")
bullet("**ALFONSO -- the duel only he can have (Orion, carrying him this leg, feels it land through the working before a word is said):** GAELEN (finding the rapier in the room without being shown it): \"You of all things know the cage, brother. Rot is the door. Help me open it.\" ALFONSO (aloud, after a pause one beat too long -- the pause IS the almost): \"Decay FEEDS, gardener. The leaf rots so the root eats. Yours starves. You are not opening a door -- you are salting the field it stood in.\" Quiet horror for Orion's player to sit with: how close his own ally's philosophy runs to the abyss, and how long he took to answer.")
label("HIRCINE'S TEMPTATION (Saijah -- station 6, in the doorway of the boss)")
gm("Just before or during the fight, the Hunter's voice -- the morning after Kynareth finally spoke: \"Little sentinel. That noise in your skull. I can make it STOP.\" He is not lying. THE HIDDEN COST he simply does not mention: the channel that screams is the same channel the goddess speaks through -- silence the pain and you silence KYNARETH (the Mzinchaleft principle: silence is not always peace). NO weredog offer, NO choice resolved here -- the senses may sharpen a moment (a taste), and the offer HANGS. If the player accepts outright anyway, do not block it -- but that is her player firing the crossroads early, not the module.")
label("THE FIGHT -- DISRUPT THE WORKING", red=True)
plain("**Frame it out loud (again): the objective is the RITUAL.** The spiral array feeds the sap-lines into the root. Break enough of it and the working collapses. Gaelen defends the work, not himself; Jasper defends GAELEN.")
bullet("**THE ARRAY:** 5 anchor-shards (obsidian, waist-high). Each: **25 HP, DR 10** -- or a **Hard Might (-4)** wrench to topple one bodily, or Orion's tonal counter-note (**Hard Magic -4**, guided by his Scene 10 mapping) to crack one at range. Every anchor down weakens the weather one step in here (Zone 3 -> 2 -> 1...); at THREE down the working is DISRUPTED (win condition); all five down = staunched as clean as this ever gets.")
refplain("ZONE 3 TEMPO, restated for this fight (alarm ~6 min): 1-4 Frozen | 5-8 Dragging | 9-12 In step | 13-17 Quickened | 18-20 Unmoored. Any natural 1 or 20 also triggers a SECONDARY HORROR -- d20 on the master card's sub-table (delayed resolution / retroactive damage / echo-step / doubled-then-lost turn / initiative reshuffle). The cultists cheat it, the party endures it, and every anchor destroyed evens the game a step -- the mechanical arc IS the story arc.")
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
gm("Present the recognition to Davinia's player first and plainly: Davinia KNEW this man -- Jasper Avalon, dead in the Pale Lady's tomb -- and Ismara holds that memory. What she does with recognizing him is hers. Then GAELEN (mild, without pausing his work): \"It seems you were familiar with this vessel... that is unfortunate, for he is gone. As for his flesh -- he gave it to the Dawn.\"")
plain("Jasper was a secret Dagon devotee IN LIFE -- a lone worshipper, long before he died in the Pale Lady's tomb. Nothing was stolen. If the party tries to TALK to him, he CAN speak -- and what he says is worse than silence: he is content. The empty, discarded man was told his emptiness was HOLY, and he gave himself gladly, because it was the first time anything ever wanted him.")
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
bullet("**Loot:** the zealots' tide-shards, inert now -- crystallized wrong-time, priceless to a researcher and mildly unwholesome to carry. NORA wants them badly and says so out loud. Whether ISMARA wants them is her player's business -- just make sure the player knows what they are. Klimmek's gratitude, and Ivarstead's -- the town half-returns as word spreads the mountain has quieted.")
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
