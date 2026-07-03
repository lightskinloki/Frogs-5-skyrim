# -*- coding: utf-8 -*-
# Generator for FIRE B PART ONE -- THE ROAD (redraft, road-leg only).
# Scope: Spine through THE RECKONING -- the section the GM actually annotated in the
# first-draft full module RTF. Part Two (Ivarstead onward) is unreviewed and is NOT
# touched here; the original annotated draft stays in place as the reference for why
# these rules exist (WRITING GUIDE section VII, SESSION SHEET FORMAT 4B/5C, CLAUDE.md
# Rule 3 extension). Run: python _build_ivarstead_road_v2.py

import os

OUT = r"C:\Users\fbrown\Projects\Frogs-5-skyrim\Toryggs legacy\Adventure modules\choice gate 3\FIRE B PART ONE - THE ROAD (redraft).rtf"

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
raw("\\pard\\sb60\\sa40\\cf2\\b\\fs44 FIRE B, PART ONE -- THE ROAD (redraft)\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i Covers the road leg only -- the Spine through THE RECKONING -- the section already reviewed in the first-draft full module. Part Two (Ivarstead onward) is unreviewed and lives only in that original file for now; it stays untouched as the record of why the rules below (WRITING GUIDE VII, SESSION SHEET FORMAT 4B/5C) exist. Riften gates -> the foot of the 7,000 Steps.\\i0\\cf1\\par\n")
rule()

label("THE SPINE (hold these three lines all module)", red=True)
bullet("**This is an INTRODUCTION.** It ADVANCES threads and RESOLVES nothing personal. Saijah chooses NO patron. Gaelen does NOT die. The crossroads is loaded, never fired.")
bullet("**Frame the objective OUT LOUD as THE RITUAL, never as Gaelen's head.** If they think the mission is 'kill Gaelen,' his escape is a robbery. If they know it is 'stop the Unmaking,' his escape is just Thursday.")
bullet("**Secrets that must hold:** Bjorn's speed reads as REJUVENATION, never Dragonborn (no one can sense a Dragonborn -- not even the Greybeards, who have NO special senses of any kind). Ismara stays unwitnessed by the monastery. The two scout dragons' target stays unknowable.")
plain("**Roster on the move:** Davinia (ISMARA fronting -- silver skin), Saijah (bearing ALFONSO the rapier), Orion. These three are the PCs; everyone else on the cart is a companion NPC. Cart: Bjorn, Mila, Esbern (hidden until Scene 1), Nora, GEAR, Ylva, Varon. Animals: Mable (old, dragon-shaken) + the BLACK MARE (fearless warhorse -- sheet: Npcs/the black mare). Krusp & Danica are GONE to Windhelm.")

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
refplain("**THE FIVE TELLS:** 1) MABLE SPOOKS -- Bjorn rolls (animal handling); the Black Mare in harness beside her = one step EASIER. 2) GEAR HUMS -- Saijah/Orion (Guile); GEAR needs PERMISSION to power down. 3) ALFONSO'S ROT-AURA drifts downwind -- Saijah (bearer); auto-success if she lets Alfonso pull the aura tight through the link. 4) A SMALL HUMAN SOUND (Mila's frightened breath) -- Bjorn or Saijah; comforting her IS the roll. 5) HEAT BLOOM -- Davinia/Ismara can sheathe the cart's warmth in cold -- a quiet temptation each time she uses the gift.")

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
bullet("Five sleeping priests, each pinned to a tomb: **NAHKRIIN -- VOKUN -- RAHGOT -- OTAR -- MOROKEI.** Rahgot's pin has been moved OFF its tomb and left dangling. Esbern keeps touching it like a sore tooth.")
bullet("**HOW HE KNOWS** (if asked): he overheard it, not divined it -- two Thalmor agents talking low in a Riften teahouse, thinking the old man three tables over was deaf as well as harmless. He hasn't stopped turning it over since.")
bullet("Above all five, a sixth marker: **KONAHRIK.** \"When the five become one, the faithful shall ascend.\"")
bullet("Kynesgrove -- the first grave they watched come alive. Dozens of burial mounds in fading ink. And the HOOK: **blank spaces** -- mounds he knows exist and cannot place. He hates the blanks more than he hates the Thalmor.")
label("GREY THREAD -- the root-rot (an unmaking)")
bullet("The Eldergleam, corrupted. The 7,000 Steps, bleeding. The Throat of the World, circled three times in charcoal. NOT ONE thread crosses from grey to red -- and if a player ties them together, Esbern physically stops their hand: \"No. Two ends of the world, two different authors. Muddle them and you'll parry the wrong one.\"")
label("WHAT HE SAYS AT THE PINS (in pieces, reacting to what THEY know)")
bullet("**On the two apocalypses:** \"Two different ends, walking toward us from two directions. The dragons want to rule a dead world. These root-rotters -- Dagon's people -- want there to be nothing left to rule. The dragons are a war. The other thing is an unmaking.\"")
bullet("**On where they're going:** \"The Throat of the World is not just the dragons' holy mountain. It is a PILLAR -- one of the stones that holds the floor of the world up. If the cult cracks it, time itself runs in the cellar. That's what your archer feels.\"")
bullet("**IF THEY SAY THEY'RE HEADED TO IVARSTEAD / THE GREYBEARDS:** he sits back, surprised, and reframes fast, tapping the grey thread. \"The monastery? That's not on either thread. That's the OTHER one. The Wall does mention them, eventually -- the Voice matters when a Dragonborn finally stands up -- but that's a later chapter, not this one. Go. I'll mind the pins.\" He does not try to redirect them toward Bleak Falls; he stays disciplined about the party's own choices, even though the Dragonstone is still the thing he wants most.")
bullet("**The thing he actually wants** (taps a blank spot): \"Bleak Falls Barrow. There is a stone in it -- the Dragonstone -- a map of every dragon grave in Skyrim. Without it we wait for each dragon to find US. Everything we do until we have that stone is a flinch, not a plan.\" -> Plant it. Don't resolve it. He will say it again the whole campaign.")
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
bullet("**An Elsweyr-style curved saber**, out of the trade routes south -- mechanically the new Curved Blade type (**6 damage, Flowing Strike** -- Gear Doc), reflavored; Ahkari will demonstrate the curve is not decoration.")
bullet("**An exotic hunting bow**, strung with something that is not gut -- mechanically a Tier-3 bow (**9 damage, Envenomed**: apply a poison as a Free Action instead of a Minor); Ahkari will not say what the string actually is.")
bullet("**Paralysis Poison x2** (Rare) -- on a successful hit, the target makes a Might roll or is Paralyzed, losing their next turn completely. \"The good kind, from a woman near Hammerfell who owes Ahkari a favor she will not explain.\"")
bullet("**A coin that's always warm** -- no mechanical effect at all, priced as a curiosity. Pure flavor; sell it as a keepsake, not a magic item.")
bullet("Road food, arrows for Saijah, fair-ish prices. Haggling is social, not a fight.")
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
gm("Davinia's player is driving ISMARA directly while she fronts this module -- so this is a PC scene, not an NPC one, and gets a SITUATION, never a scripted line. Ismara has taken herself off from the main fire tonight -- her own choice of ground, not a summons -- Codex open, rapier in reach, working a real technical fork in tonight's passage: one reading slows the rot faster but costs the patient strength for a week, the other's gentler and slower. That's all you supply. Whether she raises it with anyone, works it in silence, or does something else with her evening entirely, is the player's call -- ask \"what does Ismara do out here,\" then run whatever she gives you.")
plain("**YLVA** notices her peel off and follows without being asked -- she doesn't do subtlety, and she doesn't ask permission to be somewhere. She just walks over, sits down close enough to be a presence, and gets out her whetstone right there instead of at the fire. No question, no opening line. She's decided this is where she is now, and she's comfortable enough in silence not to fill it.")
gm("ISMARA'S RESPONSE to Ylva just being there is entirely the player's call too -- acknowledge her, ignore her, keep working, say something. Whatever it is, let it sit; this doesn't need to resolve into anything before Nora shows up.")
plain("A while later, NORA finds them both out here -- this is the first beat of her evening-long throughline of asking around about Orion (continues in Vignette B, pays off in Vignette C). She asks straight, a little nervous: \"Can I ask you both something? How do you know if wanting someone is worth what it costs?\"")
plain("**YLVA** (not stopping the whetstone): \"You want him? Go lie down next to him. If he says no, come back and sharpen something. Why is this a conversation.\" (a beat -- the closest she comes to tenderness tonight) \"Wanting things isn't complicated, little witch. People just make it complicated so they can lose slower.\"")
bullet("**ISMARA** (player-driven -- AIM only): the dangerous one to ask. She files everything, never lies, and is one of the only beings in camp who can SEE the Ring on Orion's finger for what it is -- she doesn't spend true things unless they buy trust. GM color, not a line: she's gone quiet through Ylva's answer, like she's turning something over. A warning to Nora would be true, kind, and a deposit in the account of a girl whose soul-vessel research fascinates her; or she says something warm and general and keeps the Ring for a better price later. Ask Davinia's player directly what Ismara actually says, if anything -- do not decide it for her.")
gm("Whatever Nora hears -- from Ylva, maybe from Ismara, maybe nothing at all -- she does what she always does with data: draws her own conclusion anyway, and moves on. Next beat of her throughline is in Vignette B.")

label("VIGNETTE B -- THE BLADE ON THE STONE (early evening, edge of firelight)")
gm("Nora asks Saijah's permission before she asks anything else -- she wants to examine Alfonso, specifically whether a soul anchored in an object can be COPIED rather than transferred, and she won't touch the rapier without Saijah saying yes. This is Saijah's call, not GEAR's and not Alfonso's alone.")
plain("**NORA:** \"I'm not asking to take anything from him. I want to understand how the anchor holds -- copy versus transfer, that's the whole question. Can GEAR look? Can I?\"")
bullet("**If Saijah says yes:** GEAR runs a full technical pass out loud, precise and unfiltered -- he's describing the actual mechanism behind Hjolmar's phylactery work and doesn't know it's dangerous information to hand a grieving girl with two of her parents' souls in gemstones. Nora goes quiet partway through, and her eyes go to her own two gems, twice. Does anyone at the fire notice? Does anyone say something? She knows more by the end of it than she did at the start, whether anyone intervenes or not.")
bullet("**If Saijah says no:** Alfonso answers for himself instead -- dry, a little pleased to be asked rather than studied. \"A soul is not a ledger entry, girl. Ask a kinder question and I'll answer it.\" (beat) \"Copied. As if I were two men now instead of one, and the second never got a say.\" There's a real chill under the dryness for that one line. Nora doesn't push. The door stays open for later.")
plain("Before Nora goes, she asks Saijah the same question she asked Ismara and Ylva -- the second beat of her throughline, and the one she actually came over for. She asks it straight, in her precise, over-prepared way: how do you know when wanting something is worth what it costs? She's rehearsed the question and none of the possible answers. Whatever Saijah gives her, she writes NONE of it down -- the first thing all week she hasn't taken notes on.")
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
gm("The migraine -- which Alfonso's rot-aura had been quietly dampening -- is starting to come back: a low ache, pointing south, toward the mountains. Saijah's player should feel this is the last easy night. Then Varon steps into the firelight across the camp, just far enough to be visible, and waits. No pressure, no demand -- crossing the distance is entirely the player's call.")
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
    "Two of them. Krosulhah -- the one that nearly killed all of you -- was one.",
    "They wheel out over the cut, unhurried, patient, reading the ground the way Saijah reads a trail. They are not passing through. They are looking for something. They have not seen you yet.",
])
plain("**FRAME THE STAKES OUT LOUD, THEN STEP BACK:** say it plainly -- you fought one dragon and barely survived; there are two, in the open, with a child and an old man in the cart; there is no version of a fight here that ends well. Then stop talking. If the table decides to try anyway, that's a real choice they're allowed to make -- run it honestly, don't fudge it soft, and let the terrain and the odds be the actual argument instead of you overriding their agency with narration.")
refplain("**RUN THE NOTICE CLOCK NOW, IN FULL** (restated here so this scene never depends on flipping back): 6 boxes, starts empty. 5 complication beats, each tied to a party asset, difficulty climbing beat to beat -- Easy(+2), Standard(0), Hard(-4), Hard(-4), Very Hard(-6). The responsible character rolls; success contains it, no Notice; failure adds 1 Notice; a natural 20 adds 2 Notice AND a dragon banks toward them (next beat one step harder); a natural 1 is active masking -- Notice drops 1 (min 0) and the next beat eases a step. Reward every proactive idea with a step of ease or Advantage. At Notice 6 they're spotted and it's a dive -- telegraph that hard before it happens.")
refplain("Walk the five tells as they come up, in whatever order the table's actions surface them: MABLE SPOOKS (Bjorn, animal handling; the mare in harness eases it a step), GEAR HUMS (Saijah/Orion, Guile; GEAR needs permission to power down), ALFONSO'S ROT-AURA drifts downwind (Saijah as bearer; auto-success if she lets Alfonso pull it tight), MILA'S FRIGHTENED BREATH (Bjorn or Saijah; comforting her IS the roll), HEAT BLOOM (Davinia/Ismara can sheathe the cart's warmth in cold -- a quiet temptation each time she uses the gift).")
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

plain("**[END OF THIS DRAFT -- Scene 7 (\"The Faint Wrongness\") and all of Part Two remain unreviewed and stay in the original full-module file for now. Once this road leg is signed off, they get the same redraft treatment.]**")

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
