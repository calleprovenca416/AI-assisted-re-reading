"""
Check the files that must agree, and the files that must stay clean.

WHY
---
Drift between these files has already cost one round of coding. On the cold
papers the extraction session is coder 1, so
EXTRACTION_BRIEF.md and CODING_INSTRUCTIONS.md must state every shared
definition in the same words, or the two coders measure different things. This
script checks the shared passages mechanically, after whitespace, emphasis and
blockquote markers are set aside. It also checks that the two files a session or
a coder receives say nothing about moves, seams or the attack, and that the
received files carry none of H1's surface cues for voice, nor the
names of the study's papers.

LIMIT. It checks that each listed passage appears in both files. It cannot see a
rule stated in one file only: read both files whenever either changes.

AGAINST_CHECK.md (28 Sep) is a third received file, for the session that checks
`against` links after coding. The script checks that it shares six passages with
both received files and that it names none of the forbidden terms.

ONE GUARDED WORD (7 Oct). One of the forbidden terms is not spelled in this
file. Only a hash of it is kept, and a text is tested against it word by word
(GuardedWords, below). The pack builder takes the same test from here. This
keeps the word off the page and no more than that: see the note at
GUARDED_SHA256.

USAGE
    python3 check_must_agree.py
    python3 check_must_agree.py --selftest     the guarded word's test, tried on a made-up word:
                                               the test itself, and the run's use of it on
                                               copies of the three received files

A failure means one file changed without the other. Change both in the same
sitting, then update PASSAGES here, deliberately.
"""
import functools
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Passages that must appear, identically, in the brief AND the coding instructions.
PASSAGES = [
    # direction: the box (with the rule of 27 Sep on an outcome alone)
    "direction in two steps. read the claim's outcome first.",
    "does the stub report anything about the outcome itself? if it reports the setting, "
    "or the conditions, or the general phenomenon, but says nothing about the outcome "
    "itself → `illustrates`, however well the fragment fits the claim's subject matter. "
    "if this step is genuinely unclear, write the tie-breaker below into the",
    "if it does, which way did the outcome go? the way the asserted direction says → "
    "`with`. the opposite way, or the outcome occurred without the condition the claim "
    "names as its cause → `against`. the stub explicitly bounds or limits the claim → "
    "`qualifies`. the stub need not show the condition: an outcome going the asserted "
    "way, with nothing said about why, → `with`.",
    "keep the outcome's polarity as it is; do not re-sign it.",
    # direction: the invented against example, and the rule of 27 Sep
    "time pressure makes cooks skip the tasting step is run against by a stub showing a "
    "cook skipping the tasting step on a slow afternoon with no orders waiting. the "
    "outcome is present, and the stub shows the named cause absent.",
    "it is run against, too, by a stub in which a cook skips the step because the recipe "
    "card has gone missing: the stub puts the outcome down to another cause.",
    "an outcome without its cause. had that stub said nothing about how busy the kitchen "
    "was, or about why the step was skipped, the code would be `with`: the outcome went the "
    "asserted way, and nothing in the stub shows it happening without the cause. the second "
    "half of `against` needs a stub that shows the condition absent, or that puts the "
    "outcome down to another cause and not to the condition. an absence you would have to "
    "infer does not count.",
    # direction: tie-breaker, basis, narrowness
    "if this claim were false, this stub would instead say ___.",
    "or it comes out the same as what the stub already says, the answer is `illustrates`.",
    "not the neighbouring fragment, not the surrounding paragraph, not what you know about "
    "how organisations work, not an inference.",
    "`against` is narrow. it does not mean \"this is interesting\" or \"this also points "
    "somewhere else\". most fragments will not be `against`, and that is expected.",
    # outcome
    "a short noun phrase — the thing that varies. time taken to reach a decision. "
    "conflict between two teams. staff turnover. not a sentence, not the claim restated.",
    "names something that varies but asserts no direction on it — it says the thing "
    "matters, not which way it goes —",
    "plenty of claims describe how something is rather than assert that one thing affects another",
    "do not manufacture an outcome to fill the",
    # asserted direction
    "the more x, the harder y", "when z is present, w becomes possible",
    "\"affects the time taken\" is not a direction; \"the more people must sign off, the "
    "longer the decision takes\" is.",
    "rewriting the outcome as ease",
    # core
    "if the paper would lose its argument without it",
    "if it is scaffolding, background, or a step on the way to something else.",
    "a paper usually has a handful of core claims, not one and not all of them. do not "
    "aim for any particular number.",
    # stated as
    "asserted as something the paper has shown",
    "hedged, offered, proposed, suggested as worth considering",
    "judge the paper's language, not whether you find the claim convincing. watch for "
    "hedging that is only stylistic modesty, and for confident phrasing around a claim "
    "the evidence does not really reach — both directions of mismatch occur, and you are "
    "coding the phrasing.",
    "where a claim is stated in more than one place, code its firmest statement, and note "
    "the hedged places",
    # gap kind
    "says what it does not cover", "says it lacks some evidence",
    "names a question it leaves open", "says something is unclear or could be read two ways",
    "says a term is used differently elsewhere",
    # pair drawn by authors
    "puts the two side by side and treats the contrast as meaningful",
    "the paper never compares them",
    "the test is whether the comparison is on the page, not whether it is a reasonable "
    "comparison to make",
    # resolution period
    "treats the matter as settled",
    # gloss relation
    "the summary says what the fragment supports, no more",
    "the summary adds something the fragment does not carry, without contradicting it",
    "the summary and the fragment point different ways", "no relation worth recording",
    "could both be true at once? if yes, it is `goes_beyond`. if believing the summary "
    "means disbelieving part of the fragment, it is `diverges`.",
    "the relation may be to one of them, especially where one event has ended up in more "
    "than one fragment.",
    "if the gloss has more than one part, code the part that departs furthest from what "
    "the fragment reports (`diverges` before `goes_beyond` before `consistent`), and name "
    "that part in the reason.",
    # voice
    "the paper shows you something that happened, was said, or was the case",
    "the author's own interpretation of what was going on",
    "if the sentence is the author's own words rather than a report of what someone did or "
    "said, ask: can you point to the single reported event this sentence characterises?",
    "it interprets across several events, or explains why something happened, or states "
    "what something meant",
    "this holds even when the sentence also explains why that event went as it did, or "
    "says what it meant to the people in it: that part is the event's gloss.",
    "most fragments will be `reported`. an author's explanation of why people behaved as "
    "they did, across several events, is the clearest case of `author_insight`. so is a "
    "sentence saying what an object meant or was worth to people in general. a table or "
    "figure summarising the author's framework is usually `author_insight` too.",
    "\"for these workers, x was a way of showing y\"", "\"x showed y\"",
    "where a sentence reports the reasoning of people in the setting across several "
    "events, in the author's own voice and without quoting anyone, it is genuinely ambiguous",
    "about one event, it is `reported`, as above.",
]

# CLAIM_EXTRACTION.md is not in the repository (see the README), so the passages it shares with the coding
# instructions are not checked in this copy.

# Passages AGAINST_CHECK.md (28 Sep) shares with BOTH received files: the second
# half of `against` and the rules around it, which its kinds 2 and 3 restate.
# Its kind 1 (condition present, outcome the other way) is deliberately narrower
# than the box's "the opposite way"; that difference is what the check measures.
AGAINST_CHECK_PASSAGES = [
    "an absence you would have to infer does not count.",
    "keep the outcome's polarity as it is; do not re-sign it.",
    "the stub shows the named cause absent",
    "the stub puts the outcome down to another cause",
    "time pressure makes cooks skip the tasting step",
    "a cook skips the step because the recipe card has gone missing",
]

# Neither file a session or a coder receives may name the machinery.
FORBIDDEN_BOTH = [r"\bseams?\b", r"\battack", r"\baudit", r"uniformit", r"fission",
                  r"inversion", r"counterfactual", r"focali[sz]ation", r"boundary_shift",
                  r"\bcarlile\b", r"\bmick\b", r"\bvaughn\b", r"\bkappa\b",
                  r"late understanding", r"localized the knowledge",
                  # the study's papers: no session or coder is told which papers
                  # are in the study
                  r"\bpratt", r"\bbechky",
                  r"\bamway\b", r"forensic",
                  # H1's surface cues for voice: out of both files
                  # since 27 Sep, when they were removed from the brief
                  r"present tense", r"evaluative (words|vocabulary)",
                  r"generic subject", r"the value of"]
FORBIDDEN_CODING = []

# One more forbidden word, which this file does not spell. It stood in the list
# above as a whole word until 7 Oct 2026. What the working copy keeps is a SHA-256
# of the word in small letters, with the salt below in front of it; this copy keeps
# none.
#
# What this does and does not do. It keeps the word off the page, so that
# nobody who reads this file, or a file that copies from it, reads the word.
# It is not a lock. The word is short, and whoever tries every short word
# against the hash would find it in seconds.
#
# To guard another word: add guard_digest("<the word>") to the list, worked out
# somewhere that is not kept, and never the word itself.
GUARD_SALT = "coupling-audit/check_must_agree/guarded-word/v1:"
GUARDED_SHA256 = []   # the repository's copy keeps no hash (see the README)
GUARDED_SHOWN = "a guarded word (not shown)"
GUARD_STRUCK = "###"            # what stands for a guarded word in a quoted text: one
                                # length whatever the word's, so that its length is not shown
_WORD = re.compile(r"\w+")


@functools.lru_cache(maxsize=None)
def guard_digest(word):
    """The digest a word is guarded under: the salt, then the word in small letters."""
    return hashlib.sha256((GUARD_SALT + word.lower()).encode("utf-8")).hexdigest()


class _GuardedMatch:
    """Where a guarded word stands. It never gives the word back."""

    def __init__(self, start, end):
        self._span = (start, end)

    def start(self):
        return self._span[0]

    def end(self):
        return self._span[1]

    def span(self):
        return self._span

    def group(self, *_):
        return GUARDED_SHOWN


class GuardedWords:
    """Finds the guarded words in a text without holding them or giving them back.

    A word is a run of letters, digits and underscores. So this is the test that
    the pattern \\b<word>\\b made, with capitals set aside: the word is found
    as a whole word and not inside a longer one.

    It answers as a compiled pattern does, as far as this folder's callers use
    one: `finditer` and `search` give matches with `start()`, `end()` and
    `group(0)`, and `pattern` is a label. `group(0)` is that label, never the
    word found.
    """

    pattern = GUARDED_SHOWN

    def __init__(self, digests=None):
        self.digests = frozenset(GUARDED_SHA256 if digests is None else digests)

    def finditer(self, text):
        for m in _WORD.finditer(text):
            if guard_digest(m.group(0)) in self.digests:
                yield _GuardedMatch(m.start(), m.end())

    def search(self, text):
        return next(self.finditer(text), None)


def norm(text):
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = text.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).lower()


def forbidden_hits(name, raw, guarded=None):
    """Every forbidden term in one received file, as a list of messages.

    `raw` is the file's text as it stands. The listed patterns are tried on the
    normalised text, as before. A guarded word is reported by its line and is
    never printed, and neither are the words around it.
    """
    t = norm(raw)
    guarded = GuardedWords() if guarded is None else guarded
    spans = [m.span() for m in guarded.finditer(t)]

    def around(a, b):
        """The words round a term, as they may be printed: a guarded word among
        them is struck out, whole or in the part that falls in the window."""
        lo, hi = max(0, a - 40), b + 40
        piece, at = "", lo
        for s, e in spans:
            if e > lo and s < hi:
                piece += t[at:max(s, lo)] + GUARD_STRUCK
                at = min(e, hi)
        return piece + t[at:hi]

    out = []
    for pat in FORBIDDEN_BOTH + (FORBIDDEN_CODING if name.startswith("CODING") else []):
        for m in re.finditer(pat, t):
            out.append(f"{name} contains {m.group(0)!r}: ...{around(m.start(), m.end())}...")
    if spans:
        lines = [str(i) for i, line in enumerate(raw.splitlines(), 1) if guarded.search(norm(line))]
        out.append(f"{name} contains {GUARDED_SHOWN}, {len(spans)} time(s); "
                   f"line(s) {', '.join(lines) or 'not placed'}")
    return out


def main(here=None):
    """The check, on the four files of this script's folder; the self-test gives
    it a folder of copies."""
    read = lambda f: open(os.path.join(here or HERE, f), encoding="utf-8").read()
    brief, coding = (read(f) for f in ("EXTRACTION_BRIEF.md", "CODING_INSTRUCTIONS.md"))
    B, C = norm(brief), norm(coding)
    against = read("AGAINST_CHECK.md")
    K = norm(against)
    bad = []
    for p in AGAINST_CHECK_PASSAGES:
        where = [n for n, t in (("EXTRACTION_BRIEF.md", B), ("CODING_INSTRUCTIONS.md", C),
                                ("AGAINST_CHECK.md", K)) if p not in t]
        if where:
            bad.append(f"not in {', '.join(where)}: {p[:90]}...")
    for p in PASSAGES:
        where = [n for n, t in (("EXTRACTION_BRIEF.md", B), ("CODING_INSTRUCTIONS.md", C))
                 if p not in t]
        if where:
            bad.append(f"not in {', '.join(where)}: {p[:90]}...")
    for name, raw in (("EXTRACTION_BRIEF.md", brief), ("CODING_INSTRUCTIONS.md", coding),
                      ("AGAINST_CHECK.md", against)):
        bad.extend(forbidden_hits(name, raw))
    for b in bad:
        print("FAIL", b)
    print(f"{len(PASSAGES)} shared passages, {len(AGAINST_CHECK_PASSAGES)} shared with "
          f"AGAINST_CHECK.md, forbidden terms in the three received files: "
          + ("all agree and all clean" if not bad else f"{len(bad)} problem(s)"))
    return 1 if bad else 0


def selftest():
    """Left out of the repository's copy: the guarded word's test needs the word's hash, which this copy does
    not keep (see the README)."""
    print("selftest: left out of the repository's copy; the guarded word's test needs a hash this copy does "
          "not keep (see the README)")
    return 2


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
