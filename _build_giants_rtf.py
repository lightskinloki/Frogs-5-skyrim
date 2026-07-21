# -*- coding: utf-8 -*-
# Generator for WHAT THE GIANTS GUARD (one-shot, full module RTF).
# B-Team anthology piece. Whiterun Hold, well after "The False Flags."
# Run: python _build_giants_rtf.py

import os

OUT = r"C:\Users\crlsd\Downloads\Projects\Frogs-5-skyrim\oneshots\what the giants guard.rtf"

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

def exit_(text, nxt):
    raw("\\pard\\sb100\\sa240 {\\cf2\\b EXIT ->} " + inline(text) +
        ("   {\\b -> " + esc(nxt) + "}" if nxt else "") + "\\par\n")

def rule():
    raw("\\pard\\brdrb\\brdrs\\brdrw20\\brdrcf2\\sb60\\sa220\\par\n")

# ============================================================ TOP
raw("\\pard\\sb60\\sa40\\cf2\\b\\fs44 WHAT THE GIANTS GUARD\\b0\\fs24\\cf1\\par\n")
raw("\\pard\\sa200\\cf5\\i A B-Team one-shot. Whiterun Hold, well after The False Flags -- not an immediate follow-up, anthology-style. Adept Tier, ~8 AP. 2-3 hours, one location, one clean arc. Self-contained -- run the whole thing from this file.\\i0\\cf1\\par\n")
rule()

label("ADVENTURE PROFILE")
bullet("**Location:** the Whiterun Plains -- Hearthfeld steading and the burial ridge above it.")
bullet("**Party:** 4-5 players, Adept Tier (~8 AP each). The B-Team is reasonably known in Whiterun now -- Cloud District errands, one small job for the Jarl's brother -- but nothing like the Lanterns' name.")
bullet("**Duration:** 2-3 hours. **Reward:** 1,200 gold per player, a Dwarven War-Pick if looted, 1 Advancement Point.")

label("ADVENTURE SUMMARY")
plain("The B-Team has hit a wall. Reports place the real Obsidian Lanterns in Winterhold and Riften at once, and now in Windhelm and Ivarstead at once -- every report contradicts the last, and the B-Team can't move until one of them holds. So they've been working Whiterun's odd jobs to stay fed and stay ready. This is the biggest one yet: Proventus Avenicci sends for them directly. Giants have moved against a steading days before harvest, and the mercenaries sent first haven't reported back.")
plain("What waits on the ridge above the farm is a robbery in progress. Someone has been digging up the dead, and the giants are the ones who noticed first. **The giants are the wronged party here, defending what's theirs.** How the table handles that fact decides whether this session ends with an easy fight or a dangerous one.")

label("LOCATION PROFILE STUB: THE WHITERUN PLAINS")
plain("**High Concept:** the gold sea of barley and wheat that feeds every hold in Skyrim, broken by burial mounds older than the city itself.")
plain("**Atmosphere:** flat, open country under a wide sky. Windmills turn. Cart ruts run for miles between steadings that all answer, eventually, to Dragonsreach.")
plain("**Core Conflict:** the harvest keeps its own clock. A ruined field this close to reaping is a hole in the hold's whole winter.")

rule()

# ---- PART I
scene("PART I: THE STEWARD'S REQUEST")
subtitle("Establish the job and the stakes. ~15 minutes.")
readaloud([
    "Dragonsreach smells of woodsmoke and old stone. Proventus Avenicci meets you at a side table off the Jarl's hall, a ledger open in front of him and a quill already moving before he looks up. He is a narrow man with a narrower patience. When he does look up, he sets the quill down without finishing the line he was on.",
])
plain("**PROVENTUS:** \"You're the company my lord's brother spoke of. Good. I don't have time to vet strangers.\" (He turns the ledger to face you -- a column of figures, most circled in red.) \"The Hearthfeld steading, south of the river. Two giants moved on it four nights ago. Trampled half the north field. I sent six sellswords out Tuesday. I have had no word since.\"")
plain("**If asked why this matters to the Jarl personally:** \"Hearthfeld feeds three streets of this city through the winter. I don't need you to care about that. I need you to care about the two hundred gold advance sitting in this drawer, and the same again on completion. Get out there, settle it, and get me a report I can actually use -- not six more silent men.\"")
plain("**If asked what 'settle it' means -- kill the giants, or something else:** \"I want the field safe and the giants gone from it. How you manage that is your business. I am not paying for a story about how they deserved it.\"")
label("KEY INFORMATION (Guile roll, or simply by asking)")
bullet("**The steading:** Hearthfeld, three hours south, run by a widow named Sela Hearthfeld and her two sons.")
bullet("**The missing sellswords:** a company called the Gray Anvils, hired off the usual boards. Competent, not exceptional. Proventus doesn't know if they're dead, fled, or paid off.")
bullet("**The giants:** unusual behavior. Giants near Hearthfeld have kept to the old mound on the ridge above the farm as long as anyone's worked that land. They don't normally come down.")
gm("The mound on the ridge is a giant burial ground. It has been disturbed. Proventus does not know this and will not volunteer it.")
exit_("The road south, three hours to Hearthfeld.", "PART II: HEARTHFELD")

# ---- PART II
scene("PART II: HEARTHFELD")
subtitle("Meet the farmer, see the damage, find the first evidence something is wrong beyond giants got hungry. ~20-30 minutes.")
readaloud([
    "The road drops out of the hills and the farm opens below you -- long rows of barley, gold and heavy, cut clean through in two places, a straight furrow of trampled stalks running the length of the field. At the edge of the ruined field, a woman stands with a boy of maybe twelve gripping her sleeve. Both of them are watching the ridge above the farm, where a shape moves between the standing stones -- too big, too slow, unmistakably a giant.",
])
plain("**SELA HEARTHFELD:** \"You're from the steward.\" (flat, already certain) \"Then you're later than I hoped and earlier than I feared. Come -- you'll want to see the mercenaries' camp before you want to see the ridge.\"")
label("THE GRAY ANVILS' CAMP (a short walk from the farmhouse)")
plain("Tents still standing, a cookfire burned out, ash gone grey, packs left full behind. The six men who own them are elsewhere.")
bullet("**Guile roll (Standard):** the packs are still full of coin and gear -- whoever emptied this camp came for the men themselves.")
bullet("**Might or Agility roll (Standard):** drag marks leading away from camp, toward the ridge -- boot-sized, human tracks headed uphill.")
plain("**SELA (if asked about the mound itself):** \"That ridge has had giants on it longer than my grandmother's grandmother worked this land. Always up on their stones, minding their own business, until four nights back. Whatever changed, it changed up there.\"")
plain("**If asked why she didn't just abandon the farm:** \"And go where, with what? This is the harvest. If I don't bring it in, my sons don't eat come Frostfall. I need that ridge settled.\"")
gm("Do not have any PC realize the giants were provoked. Present the packs, the drag marks, the widow's testimony that the giants never behaved this way before. Let the table draw the line themselves.")
exit_("The path up the ridge, worn smooth by feet far larger than theirs.", "PART III: THE RIDGE")

# ---- PART III
scene("PART III: THE RIDGE")
subtitle("Read what happened here, and choose whether this becomes a fight. This is the fork the whole adventure turns on. ~20-30 minutes.")
readaloud([
    "The path up the ridge is old, worn glass-smooth by feet far larger than yours. At the crest, the standing stones come into view: a ring of them, weathered and lichen-black, each one taller than a man and carved with shapes too worn to read. Between the stones, the earth has been broken open in clean spade-cuts, the turf peeled back in squared sections.",
])
label("WHAT'S HERE (present each as a physical fact; let the players connect them)")
bullet("Three graves within the ring, opened. Bones displaced, grave-goods (bronze arm-rings, a carved bone flute, a scattering of worked amber) missing from two of the three, still present and untouched in the third.")
bullet("A broken spade, iron-headed, human-made, snapped at the haft and left behind.")
bullet("A strip of grey cloth snagged on the lowest stone, the tear clean and straight -- caught once, pulled free in a single motion.")
bullet("Boot prints, several sets, leading off the ridge's far side, away from Hearthfeld, toward a stand of pine along the river. The same tread as the drag marks at the Gray Anvils' camp.")
label("THE GIANT AT THE RING", red=True)
plain("One giant stands over the one undisturbed grave, unmoving. It watches whoever gets close to the two robbed graves, and it watches whoever gets close to the flute and the amber still lying loose in the dirt.")
bullet("**If the party leaves the ring alone** -- stays back from the remaining grave-goods, keeps its distance, doesn't draw weapons: the giant lets them pass. It stays at the ring. The party can proceed to Part IV without incident, and the giant is not present at the Barrow-Pickers' camp -- this thread and that one stay separate. This is how the whole adventure can close without ever meeting the giant's full stat block.")
bullet("**If the party engages the giant** -- attacks it, takes the remaining grave-goods, or otherwise provokes it directly: this is the fight, and it happens here, now -- unlike anything else in this adventure, full commitment from both sides.")
gm("This is the actual fork in the whole module. Don't resolve it for the table and don't signal which choice is correct -- present the giant's stillness and the untouched grave exactly as written, and let what happens next be theirs.")

label("THE GIANT OF THE GIANTS' REST (Boss -- only if fought)", red=True)
statcard([
    "**Archetype:** Adept Tier, Threat Level 3 Boss (Brute)",
    "**Stats:** Might 18 (Primary) / Agility 12 / Guile 16 / Magic 8",
    "**HP:** 540   **DR:** 14 (weathered hide)   **Damage:** 26 (Ironwood club)",
    "",
    "**GROUNDBREAKER SWING** | Major Action | A low, wide arc. Everyone in melee",
    "range rolls Agility (Standard) or is knocked Prone and takes half damage (13).",
    "**GRIEF-QUAKE** | Villain Action (end of every 2nd player turn) | The club",
    "comes down on the earth. Everyone within 20 feet rolls Agility at Hard (-4)",
    "or is knocked Prone and takes 8 shockwave damage.",
    "**Phase Bar** (2 bars, 270 HP each): on the first break, the giant tears a",
    "standing stone free of the ring and wields it in place of the club --",
    "Damage rises to 32 and it gains Sunder (ignores 2 pts of target DR), but",
    "its guard opens: DR drops to 10 for the rest of the fight.",
])
plain("**Tactics:** it fights until it or its enemies fall. This is a giant defending its dead. Treat this exactly as the serious problem it is billed as -- full commitment, no held punches, no scripted mercy.")
plain("**Loot, if defeated:** the giant carries nothing worth taking. Proventus's contract is satisfied either way -- the field is safe, the giant is gone -- but Hrodulf and his crew are untouched by this fight and still out in the pines with the goods, unresolved unless the party goes after them separately.")
exit_("Boot prints lead into the pines along the river.", "PART IV: THE PINES")

# ---- PART IV
scene("PART IV: THE PINES")
subtitle("Find the Barrow-Pickers' camp and the missing Gray Anvils. ~30-40 minutes.")
readaloud([
    "The pines close in fast, needle-floor swallowing sound. Smoke threads up through the branches ahead -- a cookfire, banked low, ringed with wet turf to choke the smell.",
])
plain("A lean crew of relic-hunters calling themselves the Barrow-Pickers, led by Hrodulf the Bonepicker, a freelance antiquities broker who sells 'authentic Nord grave-work' to collectors in Solitude. Four of his crew, plus three of the missing Gray Anvils -- alive, disarmed, and doing forced labor sorting looted grave-goods at knifepoint.")
plain("**HRODULF (if the party is spotted or chooses to talk first):** \"Another crew sent to clear the giants off my dig? Steward's throwing coin at this like it'll grow back. Here's the arithmetic: three graves up there, easily four thousand gold in worked bronze and amber between them. I am not walking away from that for six farmhands with swords, and I won't walk away from it for you either. Turn around, or turn around after.\"")
plain("**The captive Gray Anvils, if freed or spoken to quietly:** they surrendered rather than die for a steward's contract that never mentioned grave-robbers. They will fight alongside the B-Team if freed, adding two allies to the coming fight (use Barrow-Picker stats below, friendly).")
label("APPROACH OPTIONS (present, don't dictate)")
bullet("**Stealth:** free the captives quietly first, thin Hrodulf's numbers before a fight starts.")
bullet("**Confrontation:** walk in and make the demand directly. Hrodulf won't yield without a fight regardless.")
bullet("**The giant:** if it was left in peace at the ridge, it does not appear here. This thread stays clean and separate no matter how Part III went.")
exit_("Hrodulf will not surrender the haul. Combat begins.", "PART V: THE BONEPICKER'S RECKONING")

# ---- PART V
scene("PART V: THE BONEPICKER'S RECKONING")
subtitle("The climax fight -- deliberately the much easier of the two possible boss encounters this session. ~20-30 minutes.")

label("HRODULF THE BONEPICKER (Elite)")
statcard([
    "**Archetype:** Adept Tier, Threat Level 2 Elite (Skirmisher)",
    "**Stats:** Might 17 (Primary) / Agility 15 / Guile 12 / Magic 8",
    "**HP:** 175   **DR:** 11 (Reinforced Leather)",
    "**Damage:** 20 (Dwarven War-Pick, Sunder: ignores 2 pts of target DR)",
    "",
    "**BURY THE LEAD** | Major Action | Hurls a satchel of grave-dirt and bone-",
    "shard. Target rolls Agility at Hard (-4) or is Blinded (Disadvantage on",
    "attacks) until the end of their next turn.",
])
plain("**Tactics:** protects the haul first, himself second. Below roughly a third of his HP, he offers to split the grave-goods rather than keep fighting -- a genuine option for the table.")

label("BARROW-PICKER (x4, or fewer if thinned)")
statcard([
    "**Archetype:** Adept Tier, Threat Level 1 Minion",
    "**Stats:** Might 16 / Agility 14 / Guile 12 / Magic 8",
    "**HP:** 70   **DR:** 7 (Studded Leather)   **Damage:** 13 (Steel Shortsword)",
    "**Tactics:** fight in pairs, try to flank. Flee at half their number remaining.",
])
plain("**Environmental hazard, the campfire pit:** a shove or trip into the banked coals deals 2 damage per turn in contact, usable tactically by either side.")

# ---- Resolution
scene("RESOLUTION")
readaloud([
    "Whatever fight was left in the Barrow-Pickers goes out of them with their captain down. The pines go quiet except for the fire.",
])
plain("If Hrodulf is dealt with and the grave-goods recovered, the clean close is returning them to the ring:")
readaloud([
    "The bronze arm-rings and the carved flute go back into the earth the way they came out of it -- awkward, human hands doing a job built for larger ones. At the ring's edge, the giant stops pacing. It crosses to the grave, kneels, and sets the amber back in place with two fingers, careful as thread through a needle. Then it settles back against the tallest stone, still.",
])
plain("The freed Gray Anvils corroborate the whole account to Proventus, thank the party, and go find new work. Sela Hearthfeld gets her field back with the harvest still in reach. Proventus asks one question when they report back: is the field safe. He pays the full contract on a yes, whichever way it was won. The moral weight of the choice is itself the reward -- Proventus's ledger never has to know.")

label("REWARD")
bullet("**Gold:** 1,200 per player from Proventus, plus Hrodulf's own coin purse (roughly 300 gold) and any grave-goods the party chose to keep rather than return.")
bullet("**Item:** a Dwarven War-Pick (Damage 8, Sunder: ignores 2 pts of target DR) -- Hrodulf's own weapon, if looted.")
bullet("**Advancement:** 1 AP each.")

label("DIRECTOR'S NOTES")
plain("**The giant is objectively right.** Hrodulf's crew desecrated a burial ground for four thousand gold in relics. Play it as settled fact -- Sela, Proventus, and the physical evidence all point the same direction. The only real question is how hard the table wants this to be.")
plain("**The two paths are asymmetric by design.** A party that reads the ridge right and leaves the giant alone gets a 175 HP Elite and a quiet trip home. That's the whole fight. A party that fights the giant, for any reason, gets a real 540 HP boss with Villain Actions and a Phase Bar, and the fight costs the same whether their reasons were good or not. That asymmetry is the whole point: smart, patient play earns an easier session, and a better ending too.")
plain("**If a table wants the epic fight on purpose** -- they've heard TL3 boss and want it -- that's a legitimate table to run. Warn them once, out of character if needed, then commit fully once they choose it.")
plain("**Pacing note:** if the giant fight happens, budget an extra 20-30 minutes over the estimate -- a 540 HP Phase-Bar boss runs longer than a straightforward Elite skirmish.")
label("FAILURE STATES")
bullet("**What if the party fights the giant, then also goes after Hrodulf?** Valid -- they arrive at the pines already spent from the boss fight. Let that tension be real; don't pad Hrodulf's stats to compensate.")
bullet("**What if they free the Gray Anvils but the fight still goes badly?** The Anvils fight to the same standard as a Barrow-Picker ally -- two extra bodies, no more than that. Let the table earn it.")
bullet("**What if they side with Hrodulf instead?** He'll cut them in for a third of the take. A legitimate table choice -- Proventus still pays for a field made safe, he never learns the whole truth, and the giants get robbed twice. Play the consequence, don't punish the choice.")

exit_("The B-Team banks 1,200 gold each and a solid local reputation -- still no word on where the real Lanterns actually are.", "")

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
