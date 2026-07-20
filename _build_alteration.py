# -*- coding: utf-8 -*-
"""Builds 'On the Negotiable Law' -- a Tier-4 school-of-magic treatise on
Alteration, in the voice of an argumentative practitioner-partisan (NOT a
spellbook -- a dense academic monograph), annotated by a cautious colleague
after the author's disappearance. Cross-checked against 'On the Structure of
Magical Law' for somatic-component consistency (Alteration's natural
affinities: ANCHOR, SHIFT, BIND, STABILIZE). Styled .docx, slate/silver vs
warm-parchment palette. Run: python _build_alteration.py"""
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---- palette (Alteration: slate/silver-blue -- vs. Provost's warm parchment ink) ----
SLATE   = RGBColor(0x2C, 0x3E, 0x4A)   # deep slate-blue (headings, Threll's voice)
STEEL   = RGBColor(0x41, 0x5A, 0x68)   # lighter steel (subheads)
SILVER  = RGBColor(0x5E, 0x74, 0x7E)   # cool silver accent (quote ink)
INK     = RGBColor(0x1C, 0x1C, 0x1E)   # near-black body ink
AMBER   = RGBColor(0x6B, 0x4A, 0x1E)   # warm amber (Provost's marginalia ink)
HEADBG  = "D9E1E4"   # cool slate-grey table header
MARGBG  = "EFE6D8"   # warm parchment (Provost note bg)
BORDER  = "9FB1B8"
ACCENT  = "4A6472"   # slate accent for rules/borders
AMBERBAR = "6B4A1E"  # marginalia left border
BODYFONT = "Cambria"

doc = Document()

normal = doc.styles["Normal"]
normal.font.name = BODYFONT
normal.font.size = Pt(11)
normal.font.color.rgb = INK
normal.paragraph_format.space_after = Pt(8)
normal.paragraph_format.line_spacing = 1.14

sec = doc.sections[0]
sec.page_width = Inches(8.5)
sec.page_height = Inches(11)
for m in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, m, Inches(1))
CONTENT_W = 6.5

def _set_cell_bg(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tcPr.append(shd)

def _set_cell_borders(cell, color=BORDER, sz=4, sides=("top","bottom","left","right")):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for s in sides:
        e = OxmlElement("w:" + s)
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), str(sz))
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), color)
        borders.append(e)
    tcPr.append(borders)

def _cell_text(cell, text, bold=False, italic=False, size=10, color=INK, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    r = p.add_run(text)
    r.font.name = BODYFONT; r.font.size = Pt(size); r.font.bold = bold
    r.font.italic = italic; r.font.color.rgb = color
    return p

def heading1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18); p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = BODYFONT; r.font.size = Pt(17); r.font.bold = True; r.font.color.rgb = SLATE
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "4"); bottom.set(qn("w:color"), ACCENT)
    pbdr.append(bottom); pPr.append(pbdr)
    return p

def heading2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = BODYFONT; r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = STEEL
    return p

def body(text, italic=False, size=11, color=INK, align=None, space_after=8):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.font.name = BODYFONT; r.font.size = Pt(size); r.font.italic = italic; r.font.color.rgb = color
    return p

def quote(text):
    """An indented, silver-italic block quotation -- historical fragments, inscriptions, aphorisms."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.4); p.paragraph_format.right_indent = Inches(0.4)
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text)
    r.font.name = BODYFONT; r.font.size = Pt(11); r.font.italic = True; r.font.color.rgb = SILVER
    return p

def attribution(text):
    return body(text, italic=True, size=10.5, color=SILVER, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=10)

def provost_note(label, text):
    """A warm parchment callout with a thick amber left border -- the Provost's hand."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    cell.width = Inches(CONTENT_W)
    _set_cell_bg(cell, MARGBG)
    _set_cell_borders(cell, color=AMBERBAR, sz=4, sides=("top","bottom","right"))
    _set_cell_borders(cell, color=AMBERBAR, sz=22, sides=("left",))
    cell.text = ""
    lp = cell.paragraphs[0]
    lp.paragraph_format.space_after = Pt(2)
    lr = lp.add_run(label.upper())
    lr.font.name = BODYFONT; lr.font.size = Pt(8.5); lr.font.bold = True
    lr.font.color.rgb = AMBER
    bp = cell.add_paragraph()
    bp.paragraph_format.space_after = Pt(2)
    br = bp.add_run(text)
    br.font.name = BODYFONT; br.font.size = Pt(10.5); br.font.italic = True; br.font.color.rgb = AMBER
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t

def lore_table(headers, rows, widths):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for j, h in enumerate(headers):
        c = t.cell(0, j)
        c.width = Inches(widths[j])
        _set_cell_bg(c, HEADBG); _set_cell_borders(c)
        _cell_text(c, h, bold=True, size=9.5, color=SLATE)
    for row in rows:
        tr = t.add_row()
        for j, val in enumerate(row):
            c = tr.cells[j]
            c.width = Inches(widths[j])
            _set_cell_borders(c)
            _cell_text(c, val, size=9.5)
    return t

def spacer(pts=2):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(pts); return p

# =====================================================================
# TITLE PAGE
# =====================================================================
tp = doc.add_paragraph(); tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
tp.paragraph_format.space_before = Pt(100)
r = tp.add_run("ON THE NEGOTIABLE LAW")
r.font.name = BODYFONT; r.font.size = Pt(30); r.font.bold = True; r.font.color.rgb = SLATE

sub = doc.add_paragraph(); sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.paragraph_format.space_before = Pt(16)
rs = sub.add_run("Being a Treatise on the True Nature and Mortal Peril\nof the School of Alteration")
rs.font.name = BODYFONT; rs.font.size = Pt(13); rs.font.italic = True; rs.font.color.rgb = STEEL

attrib = doc.add_paragraph(); attrib.alignment = WD_ALIGN_PARAGRAPH.CENTER
attrib.paragraph_format.space_before = Pt(40)
ra = attrib.add_run("Cassian Threll\nMaster of Alteration, College of Winterhold")
ra.font.name = BODYFONT; ra.font.size = Pt(12); ra.font.italic = True; ra.font.color.rgb = SLATE

warn = doc.add_paragraph(); warn.alignment = WD_ALIGN_PARAGRAPH.CENTER
warn.paragraph_format.space_before = Pt(60)
rw = warn.add_run("[ This manuscript was recovered from Master Threll's tower in the eastern\n"
                  "spire, found open upon his writing desk, twenty-two days after he was last\n"
                  "seen by any member of the College. It is published here whole and\n"
                  "unaltered -- including its unfinished final chapter -- because a text a\n"
                  "student cannot see in full is a text they will go looking for elsewhere,\n"
                  "in worse company. The notes in the margin are my own. Where I have grown\n"
                  "afraid partway through a sentence, I have left the fear in. -- Provost Ilde\n"
                  "Marren, College of Winterhold ]")
rw.font.name = BODYFONT; rw.font.size = Pt(10.5); rw.font.italic = True; rw.font.color.rgb = AMBER

doc.add_page_break()

# =====================================================================
# I. THE FALSE PARTITION
# =====================================================================
heading1("I.  The False Partition")
body("Every apprentice is taught the same comforting lie in their first week at any college of magic: that the six schools name six different kinds of power. Destruction burns. Restoration mends. Illusion deceives. Conjuration summons. Alteration merely adjusts. The lie is comforting because it is orderly, and orderly things are easy to grade on an examination.")
body("It is also false. There are not six powers. There is one power, and it does not originate in the caster at all. Magicka descends from Aetherius, pouring down through the rifts Magnus tore in the sky when he and the greater part of the et'Ada fled the unfinished work of Mundus rather than pay its price in full. Every mage who has ever lived draws from that same falling light, whether they call it down to burn a bandit's flesh or to knit a child's broken arm. The schools are not six rivers. They are six words for the same river, spoken by scribes who needed a filing system more than they needed the truth.")
body("I do not say this to diminish my colleagues in Destruction or Restoration. I say it because the filing system has a cost that no one troubles to mention in the first week, or the fifth year, or ever: it has taught every mage in every college on this continent to stop asking what a spell actually does to reality, so long as they can say which drawer it belongs in.")
provost_note("Provost Marren, in the margin",
    "I want the reader to notice, before Cassian has finished his first chapter, that he has already told you the schools are a fiction invented by frightened clerks. Hold that claim loosely. It is the same claim every partisan of every school eventually makes about the schools he does not practice. I have read the Destruction masters' pamphlets. They say precisely this about everyone else's discipline. What follows is not proof that Alteration is the one honest school. It is an argument, made by a man who loved his discipline more than was good for him.")

# =====================================================================
# II. THE SIEGE THAT COULD NOT BE WON
# =====================================================================
heading1("II.  The Siege That Could Not Be Won")
body("Let me offer the proof before the philosophy, because philosophy unearned by evidence is only opinion dressed for company.")
body("When the slave-queen Alessia's rebellion had broken the Ayleid dominion across most of Cyrodiil, the city that would come to be called Bravil, on the Niben, held against her for far longer than its garrison should have allowed. Four times her Centurions -- the field-officer rank of her own young army, no kin to the Dwemer's mechanical namesakes -- took the streets by open combat, drove the defenders back within their own walls, and camped their soldiers to hold the gates through the night. Four times, dawn found every occupying soldier dead and the Ayleids walking their own battlements again, and no one among the living had heard a fight.")
body("The easy explanation -- that the elves had never truly lost the city, that some trick of theater had convinced weary soldiers they had won a battle they had not -- satisfied no one who had actually stood in those streets and watched the enemy break. The harder truth took one Centurion's unusual patience to find: Te'o Bravilius Tasus, who noted shallow handholds worn into the stone far above any soldier's reach, and, once, a single footprint pressed into riverbank mud beside a garrison that had posted no one near the water that night. The Ayleids were not holding the city by force of arms at all. They were holding it by making the stone climbable to hands it had no business admitting, and the river breathable to lungs that should have drowned in it, until an army convinced of its own victory had nothing left to fight. The city keeps his name still, worn down by the centuries the way his own find wore down the stone: Bravilius become Bravil.")
quote("\"They found us four times and lost us four times, for what they were hunting for was men, and men were not what waited above them in the wall.\"  -- fragment, Ayleid garrison marker, provenance disputed")
body("Here is what the College will not put on an examination, because it unravels the examination's whole premise: no lockpick, ward, or fire-spell ended that siege. Reality itself was renegotiated -- stone made climbable, water made breathable, the defenders' own shapes made other than what they were -- and a superior army could find nothing to fight because there was, by any honest accounting of what is normally true, nothing there to find. This is not a parlor trick with a generous name. This is the oldest recorded use of this school, and it very nearly held an empire at bay by itself.")
provost_note("Provost Marren, in the margin",
    "Historically sound, so far as the fragmentary record allows, and I will not quarrel with a single Centurion's report that is four thousand years dead. But mark the shape of the argument Cassian is building on top of it: a single well-documented siege, generalized without pause into a claim about what the whole school IS. One siege proves the Ayleids were extraordinarily skilled. It does not yet prove that every hedge-wizard who casts Oakflesh before a bar fight is quietly rehearsing the same power that broke an empire's patience. Watch for that leap. He makes it again before the chapter is out.")

# =====================================================================
# III. THE LIE OF UTILITY
# =====================================================================
heading1("III.  The Lie of Utility")
body("Ask any journeyman what Alteration is for and you will hear the same short list, recited like a nursery rhyme: hardened skin for a fighter who forgot their armor, a lighter load for a packhorse, breath underwater for a diver, an open lock for a thief too proud to carry picks. Useful. Modest. A trade for people who did not have the stomach for real magic.")
body("I have taught this list myself, to students who wanted nothing more from it, and I do not regret teaching it to them. But I want to set down plainly what that list is actually made of, because no one before me has troubled to say it in a single sentence: every spell on it is a small, deliberately unthreatening demonstration that the properties of matter are not fixed. Flesh becomes as resistant as oak, and then as stone, and then, at the furthest reach any living mage has documented, as resistant as the black metal drawn from fallen stars. Lungs that require air stop requiring it. A body's own weight -- weight, which every apprentice is taught is the most basic fact an object can have -- becomes a number the caster may simply choose.")
body("Say it plainly and the modesty falls away at once. This is not a trade for the timid. This is the school that has quietly demonstrated, in every college on this continent, for as long as there have been colleges, that the physical world holds no fact so basic the right working cannot set it aside.")
provost_note("Provost Marren, in the margin",
    "I concede the observation, because it is simply correct, and I would rather concede a true thing than dispute it out of general unease. What I do not concede is the framing that follows it, which he is already circling like a hawk: that because the effects are large, the danger of contemplating them honestly must also be large. A fact can be enormous and also safe to know. The bones in your own body are enormous facts. I have known them my whole life without incident.")

# =====================================================================
# IV. WHAT LAW ACTUALLY IS
# =====================================================================
heading1("IV.  What Law Actually Is")
body("Master Imedril of Artaeum, five centuries dead and still the clearest mind our discipline has produced, wrote the sentence that every mage in this college now recites without understanding it: Magicka does not respond to desire. It responds to relationship. A spell is not an imposition on reality. It is a negotiation with it.")
body("I ask my colleagues in the other schools to sit with that sentence honestly for a moment, because I do not believe most of them have. A Destruction mage who casts Firebolt is negotiating too, by Imedril's own account -- COMMAND and PROJECT, forcing fire to manifest and travel. But COMMAND is the loudest, crudest term in that negotiation, the one that most resembles simply shouting. It is negotiation the way a bandit's demand at knifepoint is negotiation.")
body("Look instead at where our own discipline's fluency actually lives, by the Archivists' own accounting: ANCHOR, SHIFT, BIND, STABILIZE. Not force. Rootedness. Adaptation. Persistence. Correctness. These are not the vocabulary of a school that pushes against law from the outside. They are the vocabulary of a school that has gone inside law's own house and learned to speak its language on its own terms -- to root oneself so thoroughly in a claim about reality that reality finds it easier to agree than to argue, to insist that a changed state is not a temporary exception but the new and simple truth, until the world stops bothering to disagree.")
lore_table(
    ["Component (per Imedril)", "What it says, in Threll's reading"],
    [["ANCHOR", "I am not asking the world to change around me. I am becoming, myself, the fixed point the world must now account for."],
     ["SHIFT", "I do not command the law where to go. I have made myself fluent enough in its own inclination that it goes where I already am."],
     ["BIND", "This is no longer a request. It is a fact now, and facts do not require the world's permission to persist."],
     ["STABILIZE", "I am not holding this against reality. I have convinced reality that this was always the true state, and it is arguing with itself, not with me."]],
    [2.1, 4.4])
body("This is why Alteration alone, of the six schools, keeps producing practitioners who cannot stop asking what law itself is made of. The other schools borrow law's power and spend it. Ours learns law's grammar and speaks it back. A mage who has genuinely done this for long enough stops experiencing the physical world as fixed and begins experiencing it as merely well-defended -- persuasive, consistent, extremely convincing, and, underneath all of that, negotiable.")
provost_note("Provost Marren, in the margin",
    "This chapter is the finest piece of scholarship in the manuscript and the one that frightens me most, in that order. He has not said anything false. Imedril's own components genuinely do cluster the way Cassian describes; I checked his citations myself before agreeing to publish this. What troubles me is the word he has chosen to end on. 'Negotiable' is not a neutral word. A student who believes the floor beneath his boots is negotiable stands differently on it than one who believes it is fixed. I do not yet know whether that different standing is wisdom or the first symptom of something else. Cassian, by the end of this manuscript, did not know either.")

# =====================================================================
# V. ILLUSION'S LESSER TRUTH
# =====================================================================
heading1("V.  Illusion's Lesser Truth")
body("My colleagues in Illusion will object to everything in this chapter, and I invite the objection, because the distinction is worth stating precisely rather than gesturing at.")
body("An Illusion spell convinces a mind that something is true. A Fear spell does not summon a real threat; it manufactures, inside a single skull, the conviction that a threat is present, and the body obeys a conviction exactly as readily as it obeys a fact. This is powerful, and I do not belittle it. But it is also, by its own definition, a lie that only one mind believes. Break the caster's concentration, and the target's own reasoning may claw its way back to what was actually true the entire time, because the entire time, something was actually true, and the Illusion mage never touched it.")
body("An Alteration spell that hides a body among the stones of a wall, or grants it breath in water where breath is not naturally owed, produces no such gap between belief and fact. There is nothing for a clear-headed target to claw their way back to, because nothing was ever merely believed. The stone really did become passable. The lung really did stop requiring air. Any observer, however skeptical, however unaffected by any spell of persuasion, will find the same altered fact waiting for them that the target finds. This is not illusion's cousin. This is illusion's superior, doing the harder work honestly instead of the easier work by suggestion.")
quote("\"A lie only one mind believes can be argued out of that mind. A truth every mind must now agree to has no mind left to argue with.\"")
provost_note("Provost Marren, in the margin",
    "I have shown this chapter to Master Delvarn of the Illusion faculty, who read it twice and then asked me, not unreasonably, whether Cassian had ever tried to escape a locked room using Fear rather than a spell of true opening. His point, stripped of its irritation, is fair: usefulness is not the same axis as honesty, and Cassian has quietly swapped one for the other partway through this argument without telling the reader he has done so. I let the chapter stand because the underlying observation about the two schools' relationship to fact is genuinely correct. I flag the substitution so the student notices it happening, rather than absorbing it as settled.")

# =====================================================================
# VI. THE TREMBLING BONES OF THE WORLD
# =====================================================================
heading1("VI.  The Trembling Bones of the World")
body("We are taught, correctly, that the greater et'Ada who remained after Mundus was made poured themselves into its foundations rather than abandon the unfinished work entirely. Akatosh gave time its shape and its single direction. Kynareth gave the elements their behavior and the sky its wind. Every law a mage of any school negotiates with is, at bottom, a fragment of one of these old and willing sacrifices, still holding a shape it agreed to hold before any mortal existed to ask it to.")
body("Consider, then, what it actually means when a mage roots their own flesh in the resilience of stone, or teaches their own lungs to disregard the law that Kynareth's own gift established for breathing creatures, or fixes a changed state so thoroughly that the world's own tendency toward its original arrangement -- what my colleagues in Destruction call, correctly, entropy, and what I prefer to call law's memory of what it used to be -- simply gives up trying to reassert itself. We are not borrowing a convenient exception. We are placing a small, specific, unmistakable pressure directly against a promise a god made before recorded history, and finding, every time, that the promise yields.")
body("It always yields to a small enough pressure. That is the comfort every teacher of this school offers a nervous apprentice, and it is true as far as it goes. I no longer find it as comforting as I once did. A promise that yields to a small pressure has not been shown to be unbreakable. It has only been shown to have never yet been pushed hard enough to learn where its edge is.")
provost_note("Provost Marren, in the margin",
    "Here is where I set the pen down for an evening before annotating further, and I want the reader to know that I did. Cassian is not wrong that our spells lean on the same foundational promises that hold Mundus together at all. He is also, in this very paragraph, wondering out loud what happens if someone finds the edge of one of those promises. I do not think a Provost's marginal note is the correct place to answer that question. I am not certain any place is. I include the paragraph because striking it would be its own kind of lie, and this whole manuscript is, whatever else it is, an argument against those.")

# =====================================================================
# VII. THE APEX OF THE DISCIPLINE
# =====================================================================
heading1("VII.  The Apex of the Discipline")
body("I will state the final claim of this treatise as plainly as I am able, because plainness is the only honesty available to a claim this large. If law itself is a promise rather than a wall -- if Akatosh's time and Kynareth's elements and every other foundation are agreements the world's makers chose to keep rather than facts the world was simply born already possessing -- then a mage who has become fluent enough in the grammar those makers used has not learned a trick. They have learned the same language the makers themselves were speaking when they built the promise in the first place.")
body("I do not claim to have reached that fluency. I know of no living mage who credibly has. But I have read, in fragments too old and too carefully guarded to cite by source, hints that certain individuals of legend did not merely negotiate with a single law of Mundus but arrived, by some route this school's own grammar makes at least thinkable, at the recognition that the whole architecture of law was itself a kind of agreement -- and that an agreement recognized clearly enough by a mind confident enough to hold that recognition without flinching stops binding the mind that sees through it in quite the same way.")
body("I will not name what is said to happen to a mind that reaches that recognition and does not flinch. I am not certain it can survive being named plainly on a page, and I have grown, in the writing of this final chapter, considerably less certain that it can survive being pursued honestly at all.")
provost_note("Provost Marren, in the margin",
    "The manuscript changes here. The hand is Cassian's own -- I have compared it against a dozen years of his correspondence and I have no doubt of that -- but it no longer reads like a lecture prepared for students. It reads like a man thinking on the page, alone, past the hour when he ought to have set the candle down. I considered omitting this chapter entirely. I have decided against it, for the same reason I gave in the last chapter, and because I believe any student determined enough to chase this line of thought to its end deserves to see exactly how far Cassian got before the manuscript stops answering."
)

# =====================================================================
# VIII. WHERE THE MANUSCRIPT ENDS
# =====================================================================
heading1("VIII.  Where the Manuscript Ends")
body("[ The following is the last page found on Master Threll's writing desk. It is reproduced exactly as it was found, unfinished sentence and all. -- I.M. ]")
quote("I believe I have found the shape of the thing I have been circling for eleven years, and I do not know yet whether to be glad of it. It is not a spell. It was never going to be a spell. It is closer to a question, and the question is one I am no longer certain I am asking from a safe enough distance to")
body("[ The page ends there. There is no further page. -- I.M. ]")
attribution("-- the last known writing of Cassian Threll, Master of Alteration, College of Winterhold")

# =====================================================================
# CLOSING REMARKS
# =====================================================================
heading1("Closing Remarks")
provost_note("Provost Ilde Marren, closing the file",
    "I have published this manuscript against the advice of two colleagues who believe it should have been burned in the tower where it was found. I disagree with them, but I understand them better than I did a month ago. Every argument in these pages that I have been able to check against Imedril's own work, against the old sieges, against the plain evidence of what our own spells actually do, has checked out true. That is precisely what troubles me. A student who reads this and finds nothing false in it has no honest reason to stop where Cassian stopped. I do not know what waits past that stopping point. I know that a man who spent eleven years walking toward it is no longer available to tell us. If you are reading this and you find yourself doing the arithmetic he was doing, close the book, walk outside, and put your hand flat against the nearest stone wall until it feels, again, entirely and reliably solid. That is not cowardice. Master Threll would tell you, if he could still be asked, that it is the one experiment in this whole discipline that every mage should be willing to fail."
)

# ---- save ----
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lore Books")
out_path = os.path.join(out_dir, "On the Negotiable Law.docx")
doc.save(out_path)
print("SAVED:", out_path)
