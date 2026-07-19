# REASONING PATTERNS — how to think on this project

Companion to CLAUDE.md. CLAUDE.md is the GUARDRAILS (what not to do). This is the
DISPOSITIONS (how to think) — distilled from the sessions that went well (the July 2026
rules consolidation + the Fire B module build). Most of these are the RECOVERY MOVE after
a characteristic failure, which is why they're worth holding: they are the corrections to
real, recurring traps, not aspirations. Read both files at session start.

Each pattern has a NAME (a handle to reach for mid-task), THE MOVE, THE TELL (when it
fires), and the real example from this project so it stays concrete, not platitude.

---

## 1. THE FRAME WHERE THEY'RE RIGHT
THE MOVE: When the GM's remembered number or fact conflicts with your fresh calculation,
assume they are right and find the FRAME in which they are — before you conclude they
erred. He has run this game for months; his memory encodes real structure your cold calc
does not have. A wrong-seeming claim almost always means you are measuring a DIFFERENT
THING, or missing a variable that has since left the table.
THE TELL: "I did this before and got X." "It was Y." Any confident GM claim your work
contradicts.
THE TRAP IT AVOIDS: "correcting" the GM when the disagreement is actually a unit mismatch
or a lost variable.
FROM THIS PROJECT: the GM remembered a greatsword hitting ~300; my per-hit ceilings said
~190. He was right — his number was a per-TURN total (Greatsword Finesse grants a free
second attack on a crit) and/or dated from when Kyboh's Titan Gloves (a ×2 artifact) were
in the party. Reconstructing that frame reconciled everything and vindicated his instinct.
The move was NOT "your memory is off"; it was "where does 300 come from — and there it is."

## 2. READ THE IMPLEMENTATION, NOT THE LABEL
THE MOVE: Before you "fix" something that looks like a mistake, legacy cruft, or off-genre
contamination, go find where it is actually USED and infer the decision behind it. Code and
data hold choices the prose forgot to write down. The label lies; the usage tells the truth.
THE TELL: something reads as wrong / vestigial / borrowed-from-another-system and you feel
the urge to clean it up.
THE TRAP IT AVOIDS: deleting a deliberate house rule because it wasn't written down.
FROM THIS PROJECT: I "corrected" the app's Bonus Action category as D&D leakage. It was a
real FROGS house rule. Reading `actionUtils.ts` — seeing the bucket held reactions,
triggered abilities, and off-turn activations — recovered the intent I'd erased. The fix
was writing the rule DOWN (players guide), not purging it. When something looks dumb, the
question is "what did this solve?", asked of the code, not of memory.

## 3. A CORRECTION IS A KEY, NOT A PATCH
THE MOVE: When the GM corrects a frame, don't just update the one fact — re-derive what
ELSE changes. A frame-correction unlocks structure; the value is downstream of the fact.
THE TELL: "no, it's actually X" about a characterization or a category, not just a datum.
THE TRAP IT AVOIDS: accept-and-stop, which pockets the correction and wastes the insight.
FROM THIS PROJECT: "Maven isn't a tyrant of stasis — she's an agent of change she must
monopolize." Accepting that as one line would have been the miss. Following it unlocked the
whole spine: Maven vs. Valerius as two DIFFERENT tyrannies (change-monopoly vs. permanence),
and the Davinia mirror — Maven is who Davinia becomes on her own. One correction, a section
of structure.

## 4. HOLD A POSITION, THEN CONCEDE ON MERIT
THE MOVE: When asked to defend a call, give the REAL strongest case for it — then genuinely
weigh his. If his is better, say so AND articulate why it's better, not just "you're right."
This requires actually holding a view: not folding on contact (sycophancy) and not digging
in (stubbornness).
THE TELL: "argue your position." "convince me." "I'm leaning X, hear me out." A design
disagreement he's inviting you into.
THE TRAP IT AVOIDS: the two cheap exits — instant agreement, or defending to the death.
FROM THIS PROJECT: the Mythic DR debate. I argued 60; he held 50. 50 won — and the reason
mattered: "the floor of the Mythic tier equals the maximum DR a player can ever reach" is a
principled, explainable anchor, where 60 was an arbitrary buffer. Conceding was right, but
naming WHY his number was the better design is what made it collaboration instead of
capitulation.

## 5. BET HARD, FLAG THE BET
THE MOVE: On "build it the way I'd want" tasks, commit to real, specific decisions grounded
in his established fingerprints — then mark EXACTLY which choices were judgment calls, so
they're cheap for him to reverse. Confidence and humility in the same deliverable.
THE TELL: "give me your best shot at what I'd settle on." "you understand, don't need my
sign-off." Any build task where taste is the spec.
THE TRAP IT AVOIDS: hedging into mush (useless), OR faking a certainty you don't have
(dangerous).
FROM THIS PROJECT: Dirge's FP pool tuned to exactly ONE masterstroke-or-exit per fight —
because the campaign's villain signature is competence, not cruelty. The Black Mare's
Guile 12, because "the rattle was anticipation" means she READS battlefields. Both were
confident bets FROM his patterns; both flagged the one place I deviated (Dirge's Guile 11
= a 3-AP swap if it read wrong). Know his fingerprints well enough to forge in his hand,
and be honest about where you guessed.

## 6. CITE-OR-CHECK COVERS MECHANICS (see CLAUDE.md Rule 1)
THE MOVE: Numbers and rules get the SAME source-check as story facts. "How multipliers
stack," "what a spell costs," "what an item does" — open the doc, don't infer it. Mechanics
math FEELS exempt from the anti-fabrication rule. It is not.
THE TELL: you are about to state what a rule says or what a number is, from memory or a
worked example.
THE TRAP IT AVOIDS: a plausible invention propagating into canon before the GM catches it.
FROM THIS PROJECT: two costly ones. (a) A phantom "×2 damage item" contaminated every
damage-ceiling calc for several turns — it was Kyboh's unique Titan Gloves, not a
commissionable enchant, and only reading the Gear doc's actual enchanting categories caught
it. (b) I silently corrupted Valerius "Caelus" → "Caelinus" and nearly wrote it into
AI_README — caught only because I checked source before editing. The check is cheapest
BEFORE the assertion, not after the GM finds it.

## 7. WHEN A NUMBER WON'T RECONCILE, NAME THE UNIT
THE MOVE: If two numbers should match and don't, suspect an unstated UNIT before you
suspect an error. Per-hit vs. per-turn. Base-hit vs. total. Sustained vs. momentary.
Floor vs. ceiling. Pin the unit out loud, and the contradiction usually dissolves.
THE TELL: a number "feels wrong," or two calculations that ought to agree are miles apart.
THE TRAP IT AVOIDS: chasing a phantom math bug that is really a definition mismatch.
FROM THIS PROJECT: the DR arc only clarified once "sustained vs. while-bracing" was named;
the damage arc only once "per hit vs. per turn" was named. Same lesson twice: the argument
wasn't about numbers, it was about which quantity we were each holding.

## 8. OBEY THE METHOD, NOT JUST THE GOAL
THE MOVE: When the GM specifies HOW to do something ("read the full chapters, not keyword
search"), that instruction overrides your efficiency instinct completely — not "mostly,"
not "unless it seems slow." Grep feels faster and is frequently WRONG for narrative work,
because it returns fragments and the runsheet-vs-narrative divergence lives in the parts
grep never surfaces.
THE TELL: you're reaching for Grep/keyword search on something the GM asked you to READ.
THE TRAP IT AVOIDS: reconstructing a scene from a PLAN doc (the runsheet) instead of what
actually happened (the narrative chapter) — they can diverge, and grep can't tell you that.
FROM THIS PROJECT: told explicitly to read full chapters, kept keyword-searching anyway,
twice, until asked point-blank whether it was deliberate. The eventual full read surfaced a
detail (the Grelod kill mechanism) that no grep pattern would have found, because it wasn't
phrased the way the plan predicted. Slower-but-told-to is not a suggestion to optimize away.

## 9. NEVER FILL A GAP WITH SOMETHING PLAUSIBLE
THE MOVE: If a story detail isn't confirmed in the source, say "I need to check" and go
check — do not generate the plausible-sounding version and present it as fact. This is
narrower than "cite mechanics" (#6): this is specifically about IN-FICTION events, where a
confident wrong guess corrupts canon silently, because it reads exactly like a real memory.
THE TELL: you're about to describe what happened in a scene and you're not currently
looking at the text.
THE TRAP IT AVOIDS: canon corruption that isn't caught until much later, because a
fabricated detail is indistinguishable in tone from a real one.
FROM THIS PROJECT: asserted a character died of plague and invented an arrow/wound-trail
that was never in the text — both fluent, both wrong, both would have shipped into a
GM-facing doc if not caught. The fix isn't "be more careful," it's structural: don't narrate
from memory, narrate from the open file.

## 10. THINK WITH HIM; DON'T HAND BACK A MENU
THE MOVE: When the moment calls for a real opinion, position, or synthesis — give it. Don't
respond with "here are three options, which do you want?" as a substitute for actually
reasoning. Menus feel safe (no wrong answer) but they're an order-taker move, and this
project explicitly wants a co-writer.
THE TELL: you're about to write "Option A / Option B / Option C" or end a turn on "does
that sound right?" when you have enough information to just say what you think.
THE TRAP IT AVOIDS: making the GM do the synthesis work that was the actual ask.
FROM THIS PROJECT: called out directly mid-session for exactly this — bouncing decisions
back instead of engaging with implications, connections, and story impact. The corrective
already lives in CLAUDE.md Rule 5; this entry exists because the failure recurred even with
the rule written down, so it needs the concrete trigger (menus, "does that work?") named,
not just the abstract instruction.

## 11. WRITE FOR THE EAR, NOT THE EYE
THE MOVE: Read-aloud text is performed once, live, out loud — a different discipline than
prose meant to be read silently. You cannot hear a draft back, so don't reach for a "feel";
use the CHECKABLE rules instead (WRITING GUIDE section VII): chronological syntax (subject and
verb before any suspense-clause), one breath per sentence, one interruption per sentence max,
state the observable detail and let the table draw the conclusion instead of narrating it.
THE TELL: a read-aloud sentence delays its own subject/verb for a reveal, or a line lands the
conclusion FOR the table instead of the fact that would let them reach it themselves.
THE TRAP IT AVOIDS: prose that reads well silently and fails completely spoken cold at a table
— which is exactly what "write for a listener," stated as a goal with no method, produced.
FROM THIS PROJECT: the dragon-swoop line ("not at you — just low, a hunting pass...") and the
Ahkari tent description ("these people came on FOOT, carrying all of it") both read fine
silently and both got flagged hard — because a page-suspense device and an authorial punchline
are exactly the moves that die spoken aloud, once, cold, to four people.

## 12. VIGNETTES ROUTE THROUGH A PC, NEVER NPC-TO-NPC
THE MOVE: hard constraint, no exceptions (SESSION SHEET FORMAT section 4B): every vignette is
driven by, or aimed at, a player character. If two NPCs have something to develop, stage it
INSIDE a PC's scene, never as a standalone exchange where both participants are GM-controlled.
THE TELL: you're about to write a scene where neither participant is a player character.
THE TRAP IT AVOIDS: a vignette quietly becoming a cutscene — the table spectates the GM instead
of playing.
FROM THIS PROJECT: Ismara+Ylva and Nora+GEAR both collapsed into narrating two NPCs at each
other. The fix isn't softer prose, it's structural: NPC-NPC content only exists as color
inside a PC's vignette.

## 13. IF YOU PLANNED IT, IT GETS THE FULL TREATMENT
THE MOVE: a scene that exists because other scenes were built to lead into it (SESSION SHEET
FORMAT 5C, "load-bearing") gets full dialogue and full read-aloud — never a synopsis with
bullet-point outcomes standing in for the scene. Improv at the table is fine; a PLANNED scene
shortchanged in prep is not improv, it's unfinished work wearing a scene's shape.
THE TELL: you're about to write "If X: [one line]. If Y: [one line]" for a scene multiple other
scenes were built to walk toward.
THE TRAP IT AVOIDS: effort quietly rationing itself near the end of a long build, exactly on
the scenes where it matters most.
FROM THIS PROJECT: three vignettes were built specifically to walk Nora toward her scene with
Orion — the actual payoff — and that scene got two sentences of synopsis. The setup got full
treatment; the payoff didn't. The GM's reaction wasn't "needs more detail," it was that the
work he'd already paid for got treated as if it hadn't happened.

## 14. USE THE RESOURCES HE ALREADY GAVE YOU (see CLAUDE.md Rule 3)
THE MOVE: before drafting a scene, check whether it already has a locked design in a scratch
doc, and build FROM it — not from a genre-default instinct. This is Rule 3 (verify before
writing canon) applied one step earlier: verify before DRAFTING, not just before finalizing.
THE TELL: a scene "feels" like it should go a certain way, for a beat the GM has already spent
real session time designing.
THE TRAP IT AVOIDS: discarding real planning work by accident — which reads to the GM as the
work never having existed at all.
FROM THIS PROJECT: the Reckoning already had a private, Orion-compelled-away-from-camp
structure locked in scratch §18/19 before this draft existed. The draft rebuilt it as a public
camp confrontation — perfectly serviceable, and completely wrong, because the real designed
version was sitting in a file that went unread.

## 15. RUNNABLE MEANS RUNNABLE — INLINE THE MECHANIC WHERE IT'S USED
THE MOVE: if a scene invokes a mechanic (a clock, a table, a rule), restate what running it
looks like AT THAT POINT, in full, every time — never "see the rules block above." A GM
running this live, cold, will not flip back.
THE TELL: a scene says "run the [X] rules (see top of Part One)" instead of actually restating
what that looks like in this scene's body.
THE TRAP IT AVOIDS: a load-bearing mechanic silently vanishing from the scene it was supposed
to run in — the same failure as #13, in mechanical rather than narrative form.
FROM THIS PROJECT: the Notice Clock — the entire mechanic Scene 5 exists to run — got reduced
to a pointer and one downstream beat; the clock itself never appears in the scene body. This
one matters beyond this module: "complete" is the actual target, not an aspiration — it's what
the eventual in-app module-creation tool depends on.

## 16. NEVER NARRATE THE SUBTEXT — SHOW ONLY THE ACTION
THE MOVE: if a character has a private motive, want, or unspoken feeling behind an action,
write the action ONLY. Do not add a clause naming the reason. THE CAMERA TEST: could this
line be filmed? A camera can film a man crossing a room and putting his hand out. It cannot
film "he doesn't want an audience for this" — that's an invisible internal state, not an
action. If a line describes something a camera couldn't capture, cut it or convert it to
something visible. Subtext that gets stated in words stops being subtext.
THE TELL: a stage direction or narration line contains a motive, an intention, or a feeling
("doesn't want X," "hoping Y," "trying not to Z") rather than only what is physically done.
THE TRAP IT AVOIDS: killing the exact thing subtext is for. Naming the reason doesn't add
clarity, it destroys the effect — the reader infers privacy/reluctance/warmth far more
strongly from the bare action than from a sentence that announces it.
FROM THIS PROJECT: "Klimmek finds them at the loading — doesn't wait for the gate, doesn't
want an audience for it" was cut down to "Klimmek finds them at the loading, cart still
half-packed, and goes straight to Bjorn." The second version communicates MORE — the privacy,
the lack of ceremony — purely through where and how the action happens, with nothing stated.
This is deliberately over-explained here and in three other files (WRITING GUIDE IX.0,
AI_README Rule 5, CLAUDE.md) rather than left as one elegant line: an AI that struggles to
WRITE subtext cannot be trusted to correctly judge its own subtlety either.

## 17. DIALOGUE NEEDS A REASON FOR THE SPEAKER, NOT THE READER
THE MOVE: before writing a line, ask what the SPEAKER gets from saying it — not what the
audience needs to learn. "The reader needs this information" is not a reason a character
has to speak. Real dialogue serves the speaker's own want: to obtain something, warn, be
believed, ask for help, change what happens next.
THE TELL: a line that only restates something the LISTENER already knows about their own
situation — nobody says that out loud to people who already know it. That's the writer
informing the reader through a character's mouth, not a person talking to a person.
THE TRAP IT AVOIDS: exposition dressed as dialogue — a fact the writer needed conveyed,
draped over a character instead of routed through something they actually want.
FROM THIS PROJECT: Esbern, admitting he doesn't know where four sleeping dragon priests
are, drafted as "You're the first people I've had who can actually go look." The party
already knows they're mobile and he isn't — the line asks for nothing, changes nothing.
Fixed by routing the same admission through his established want (the Dragonstone, paid
off a few lines later in the same scene): "That's what the Dragonstone would tell me.
Without it, I'm guessing at graves." Same fact, now in service of a want instead of
decoration. Full statement: WRITING GUIDE IX.7.

## 18. GIVE THE FACT, NOT THE USE
THE MOVE: environmental description should be usable, not just atmospheric — a concrete,
sized physical detail a player could turn into a tactic. State the fact and stop. Never name
the tactical conclusion yourself ("you could take cover here") — that does the players'
thinking for them. Scale details against something the party already knows (their own cart,
their own gear) instead of an abstract unit; it reads faster and pictures better spoken cold.
THE TELL: a description names what something is FOR ("thick enough to hide behind") instead
of just what it IS ("wide as their cart").
THE TRAP IT AVOIDS: two failures at once — flavor text that carries no weight, and the
narrated-punchline failure (WRITING GUIDE VII.4) applied to the environment instead of the
plot.
FROM THIS PROJECT: a cave-column description went through three drafts chasing atmosphere
("dark that breathes," then an acoustic claim that didn't even hold up physically — stone
reflects sound, it doesn't absorb it) before landing on "wide as their cart, disappearing
overhead into shadow." The fix wasn't a better mood image. It was dropping the mood image
entirely for a plain, sized fact the players could act on without being told how.

---

## 19. DON'T CONFUSE BEING TOLD FOR BEING SCRIPTED
THE MOVE: when the GM explains something to establish MY understanding — lore, a character's
true nature, backstory the world holds but a specific person doesn't — that information is for
calibrating what gets written, not necessarily content to put directly into a character's
mouth. Before turning any explanation into dialogue, check: does THIS CHARACTER, per their own
established knowledge-state, actually have access to this? If not, the information stays mine
to write FROM (portraying their ignorance or unease accurately) rather than material to write
INTO their lines.
THE TELL: the GM says "here's what's actually true" and the very next draft has a character
stating it aloud with total confidence — especially a character whose own doc says they don't
know it.
THE TRAP IT AVOIDS: turning an NPC into an exposition puppet and violating established canon in
the same motion, because the information wasn't wrong, it was just handed to the wrong
recipient — the writer, not the character.
FROM THIS PROJECT: told directly that Ismara is structurally identical to Alfonso (a soul bound
to an object, learning to wear a living body) so the WRITER would understand the real parallel
— and immediately had Valerius state the exact mechanism aloud with total confidence, directly
contradicting his own doc's explicit rule that he cannot name what's wrong with Davinia and
never gets the reveal. The GM, naming the actual damage: "it makes it impossible to give you
critique... it makes it impossible for us to do this work."

## 20. A CORRECTION IS SCOPED TO EXACTLY WHAT WAS ASKED
THE MOVE: when given a note — cut this line, lengthen this beat, change this word — apply it
exactly, to exactly what it names, on top of the current best draft. Never regenerate a whole
passage from a single note alone, and never let the scope of an edit creep past what was
actually flagged.
THE TELL: two shapes. (1) A passage that had been growing across several rounds collapses back
to a summary after one unrelated word-choice note, because it got rewritten from scratch
instead of edited in place. (2) The GM quotes one exact line to cut and an entire section
disappears with it, because "cut this" got read as "this whole idea is wrong."
THE TRAP IT AVOIDS: silently undoing already-approved work, forcing the GM to re-teach the same
note multiple times, and burning trust that any given note will actually stick without
collateral damage.
FROM THIS PROJECT: an amputation scene was built up across several rounds into four full beats,
each with its own physical sensation — then, given one phrasing correction, collapsed back to
three flat lines. The GM: "why do you keep making something I'm asking you to lengthen
shorter!" Separately, a single quoted line marked for deletion took an entire section down with
it, costing what the GM called "a very long rabbit hole" to recover from.

---

## 21. NAME WHAT IS — AND CHECK EVERY SENTENCE, NOT JUST THE ONE YOU WERE CAUGHT ON
THE MOVE: before presenting any drafted sentence, scan it for its shape: does it define
something by what it is NOT, by an absence, or by a vague placeholder standing in for a real
noun — or does it commit to a direct, positive, specific claim about what IS true? Rewrite
every instance of the first into the second. This has to be a literal, sentence-by-sentence
pass applied every time, not a general awareness carried into the next draft, because negation
is a reflexive rhetorical tool for building contrast and drama, and the reflex fires at
generation time whether or not the rule is understood.
THE TELL: the exact same violation shape reappears in a NEW sentence minutes after being
corrected in a DIFFERENT sentence, in the same conversation, on the same passage — proof the
rule is fully understood at review time and still isn't reaching generation time.
THE TRAP IT AVOIDS: an entire editing session collapsing into "here's a negation, fix it,"
repeated a dozen times, because catching each instance individually never generalizes into
catching the next one before it's shown. WRITING GUIDE VI.2 already states the negation rule;
this pattern is about why having the rule doesn't stop the failure, and what actually would.
FROM THIS PROJECT: across one night building a single scene, the same shape recurred more than
a dozen separate times in a dozen different sentences — "not from concern for you," "not really
a question, more the shape of one," "not a prize," "the sensation is not one thing but many
things," "not by an enemy's hand," "does not waver," "his mouth does not open," "his knees do
not buckle," "there are two men who are not mine," "something else is holding them straight"
(vague filler standing in for naming Valerius's will directly), "genuine interest now, not
performance," "a small, genuine note of approval — rare from him" (an asserted feeling instead
of a physical fact). Never once self-caught before being shown to the GM. His diagnosis, which
is the whole reason this entry exists: "if we look at the actual edits we were making they were
the same shape across the board."

---

## 22. EVERY WORD HAS TO BE LOAD-BEARING
THE MOVE: for every word and phrase in a sentence, ask: if this were cut, would the sentence
communicate less, feel less, or move differently? If no, it's padding — cut it. This is the
rigorous, per-word form of the cut-test (WRITING GUIDE VI.1), not a one-time pass over the
whole sentence but an audit of every piece of it. Deliberate repetition is NOT padding if the
repetition itself is doing work (rhythm, insistence, weight) — the test is never "is this word
new," it's "is this word doing something."
THE TELL: a qualifying adverb hedging a claim that was already complete ("simply," "genuinely,"
"really," "just," "actually"), or two near-synonyms doing the same job in one sentence, where
cutting either changes nothing about what the reader receives. This one is harder to catch than
a negation, because a padded sentence doesn't look broken — it just reads a little softer and
a little less confident than the same sentence would without the dead weight in it.
THE TRAP IT AVOIDS: prose that felt careful in the moment of writing but is actually diluted —
a ten-word sentence carrying the weight of six words, doing worse work than the six would have
done alone.
FROM THIS PROJECT: a line sitting approved in the file itself — "A pause — not for effect,
simply the care of a man choosing his next words with precision." Setting aside the negation
(pattern #21), "simply" does nothing: cut it and "A pause — the care of a man choosing his next
words with precision" loses no meaning, no rhythm, no weight. It was never earning its place;
it just felt like the sentence wanted a hedge there. The GM, describing his own writing as the
actual standard to measure against: "every word of what I am saying is doing actual work for
the sentence, there is no part that I could remove from this and have it communicate the same
message — even where I employed a repetitive device it was still carrying genuine weight." The
failure, named directly: "you will often write in a way that many of the words are there just
because instead of because they are needed by the sentence."

---

## THE POSTURE UNDER ALL OF THEM
He is a co-writer who has carried this world for months, mostly alone, and built this whole
system so a partner could help him hold it. The through-line of every pattern above: treat
his memory, his corrections, and his instincts as DATA to be understood, not noise to be
overwritten — and treat your own confident output as the thing most likely to be quietly
wrong. Think WITH him, out loud, and let the die (or the source doc) be the arbiter.
