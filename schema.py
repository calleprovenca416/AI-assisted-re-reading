"""
Schema for the re-reading instrument. Version 4.

WHAT V4 IS
----------
Two layers and the relation between them, as in v3. What changed is that every
field which existed only to feed a cut measure is gone, and every field that
licenses a move is now a property of the PAPER rather than of a plot.

  Evidence layer  Fragment  -- a unit of evidence the paper printed
  Theory layer    Claim     -- an assertion the paper makes about how something works
  The relation    ClaimLink -- which fragment sits under which claim, in which direction

REMOVED FROM V3, WITH THE REASON
--------------------------------
  script_type / ScriptStructure / ScriptStep   fed script_inversions only; cut
  constructed_index / IndexConstruction        justified by the full Stage 4; the
                                               cheap Stage 4 does not need it. The
                                               content it carried (what an index
                                               cannot separate) belongs in the
                                               fragment stub and the absence register
  frequency_cell / FrequencyCell               same
  derived_from / DERIVED_FORMS                 fed channel_loss only; cut
  utterance_date / referent_event_date /       fed the retrospection logic inside
  date_basis / utterance_period                coupling_temporal only; cut
  argumentative_position / POSITION_WEIGHT     vestigial since v3
  voice_level / voice_level_basis              one unit level now; no choice to declare
  collected_data_types                         fed channel_loss only; cut
  claim_role (three-valued)                    becomes a boolean `core`; the
                                               supporting/scoping split drove nothing

KEPT, AND WHY
-------------
  Fragment.period   ONE coarse ordinal period per fragment. Retained against the
                    first instinct to cut it with the rest of the temporal
                    machinery, because boundary_shift and counterfactual_ending
                    run on it: you cannot ask whether the ending was an ending
                    without knowing which fragments sit at or past it.
  author_gloss      NEW. SCORING_SHEET asks Stage 0 to store both the fragment
                    and the author's own summary of it, because drift -- the
                    incumbent's gloss propagating through a re-reading -- is
                    scored as its own category and cannot be detected if only
                    one of the two is recorded.

TEXT DISCIPLINE, UNCHANGED
--------------------------
Verbatim text is not stored in a shareable corpus. `stub` is the system's own
description, never verbatim. The audit computes on metadata and never reads text.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional, List, Literal
import json

SCHEMA_VERSION = 4

# Collection channels only. The three v3 presentation forms are gone.
DataType = Literal[
    "individual_interview", "group_interview", "meeting_transcript",
    "quoted_speech_in_situ", "observation", "field_note", "archival",
    "authorial_vignette", "unspecified",
]

SPEECH_TYPES = ("individual_interview", "group_interview",
                "meeting_transcript", "quoted_speech_in_situ")

# How a fragment behaves relative to what its claim asserts.
# The outcome test decides with/against against illustrates: does the stub report
# anything about the claim's `outcome` field? See CLAIM_EXTRACTION.md.
#   with        reports the outcome, and it went the way asserted_direction says,
#               whether or not the stub shows the claim's condition (27 Sep
#               2026)
#   against     reports the outcome, and either it went the opposite way OR it
#               occurred without the condition the claim names as its cause
#               (the stub must show the condition absent, not leave it out)
#   illustrates says nothing about the outcome -- setting, conditions, or the
#               phenomenon in general, however well it fits the claim's topic
#   qualifies   explicitly bounds or limits the claim
LinkDirection = Literal["with", "against", "illustrates", "qualifies", "unassigned"]

AbsenceKind = Literal["not_collected", "collected_not_printed", "not_ascertainable"]

GapKind = Literal["scope_limit", "absent_evidence", "unresolved_question",
                  "acknowledged_ambiguity", "vocabulary_mismatch"]

# Every field a human decides that can switch a move on. v3 warned about one of
# these. All of them now carry the same warning, because after the cuts three of
# the five triggers are hand-coded and none of them faces a coverage check.
HAND_TRIGGER_FIELDS = [
    "ClaimLink.direction",          # the seam -> fission, inversion
    "Claim.core",                   # which claims voice facts are read under
    "Claim.stated_as",              # ventured -> counterfactual_ending
    "DeclaredGap.kind",             # unresolved_question -> counterfactual_ending
    "ContrastPair.drawn_by_authors",  # pair -> inversion, and how strong a licence
    "PaperMeta.resolution_period",  # the episode's end -> boundary_shift
]


@dataclass
class Fragment:
    paper_id: str
    fragment_id: str

    stub: Optional[str] = None          # the system's words, never verbatim
    text: Optional[str] = None          # populated only in a local working copy
    text_status: Literal["present", "withheld"] = "withheld"

    data_type: DataType = "unspecified"  # descriptive; drives no measure in v4
    unit: Optional[str] = None           # the speaking unit: function, occupation, site
    speaker_name: Optional[str] = None   # pseudonym, where the paper gives one

    period: Optional[str] = None         # one ordinal period, from PaperMeta.periods

    author_code: Optional[str] = None    # the authors' own code for this fragment
    author_gloss: Optional[str] = None   # the authors' own summary of what it shows

    citing_claims: List[str] = field(default_factory=list)

    location: Optional[str] = None
    extraction_confidence: Literal["high", "medium", "low"] = "medium"
    notes: Optional[str] = None

    def is_speech(self) -> bool:
        return self.data_type in SPEECH_TYPES

    def has_unit(self) -> bool:
        return bool(self.unit)


@dataclass
class Claim:
    """An assertion the paper makes about how something works.

    `outcome` + `asserted_direction` together make a claim DIRECTIONAL, which is
    the precondition for uniformity, which is the only scored measure left.
    """
    paper_id: str
    claim_id: str
    statement: str                       # the system's words, never verbatim
    constructs: List[str] = field(default_factory=list)
    outcome: Optional[str] = None
    asserted_direction: Optional[str] = None
    core: bool = False                   # carries the paper's contribution
    stated_as: Literal["established", "ventured"] = "established"
    location: str = ""
    decomposed_into: List[str] = field(default_factory=list)
    extraction_confidence: Literal["high", "medium", "low"] = "medium"
    notes: Optional[str] = None

    def is_directional(self) -> bool:
        return bool(self.outcome and self.asserted_direction)


@dataclass
class ClaimLink:
    paper_id: str
    fragment_id: str
    claim_id: str
    direction: LinkDirection = "unassigned"
    basis: str = ""                      # one line: why this direction
    confidence: Literal["high", "medium", "low"] = "medium"


@dataclass
class ContrastPair:
    """Two episodes the paper treats as comparable that came out differently.

    Load-bearing in v4: a pair licenses construct_inversion on its own, and a
    pair that straddles a seam supplies the candidate separating feature for a
    split. `drawn_by_authors` therefore matters more than it did -- an
    analyst-constructed pair is a weaker licence and is tagged as such.
    """
    paper_id: str
    pair_id: str
    episode_a: str
    episode_b: str
    held_comparable: str
    differs_in: str
    fragments_a: List[str] = field(default_factory=list)
    fragments_b: List[str] = field(default_factory=list)
    basis: str = ""
    drawn_by_authors: bool = True


@dataclass
class DeclaredGap:
    paper_id: str
    gap_id: str
    statement: str                       # the system's words, never verbatim
    kind: GapKind = "scope_limit"
    location: str = ""
    bears_on: List[str] = field(default_factory=list)


@dataclass
class Absence:
    """Evidence the paper does not contain. Never a plot; always a question.

    Stage 4 appends to this register. It records that something is absent and
    stops there: whether the observation is obtainable is the scholar's call,
    not the instrument's.
    """
    paper_id: str
    absence_id: str
    kind: AbsenceKind
    evidence_class: str
    basis: str                           # what in the paper licenses the claim
    bears_on: List[str] = field(default_factory=list)
    source: Literal["extraction", "stage4"] = "extraction"


@dataclass
class PaperMeta:
    paper_id: str
    citation: str

    periods: List[str] = field(default_factory=list)   # ordered, coarse, ordinal
    episode_start_period: Optional[str] = None         # defaults to periods[0]
    resolution_period: Optional[str] = None            # where the paper's arc closes
    resolution_basis: Optional[str] = None             # what in the paper marks it
    reports_outcome_after_resolution: Optional[bool] = None

    fieldwork_scale: Optional[str] = None
    printed_fragment_count: Optional[int] = None

    schema_version: int = SCHEMA_VERSION
    claim_layer_status: Literal["extracted", "stub", "absent"] = "absent"
    claim_layer_basis: Optional[str] = None
    second_coder: Optional[str] = None
    double_coded_fields: List[str] = field(default_factory=list)


@dataclass
class Corpus:
    meta: PaperMeta
    fragments: List[Fragment] = field(default_factory=list)
    claims: List[Claim] = field(default_factory=list)
    links: List[ClaimLink] = field(default_factory=list)
    pairs: List[ContrastPair] = field(default_factory=list)
    gaps: List[DeclaredGap] = field(default_factory=list)
    absences: List[Absence] = field(default_factory=list)

    # ---- convenience joins, used by every downstream stage ----
    def fragment(self, fid) -> Optional[Fragment]:
        return {f.fragment_id: f for f in self.fragments}.get(fid)

    def links_by_claim(self, cid) -> List[ClaimLink]:
        return [l for l in self.links if l.claim_id == cid]

    def links_by_fragment(self, fid) -> List[ClaimLink]:
        return [l for l in self.links if l.fragment_id == fid]

    def fragments_under(self, cid) -> List[Fragment]:
        ids = {l.fragment_id for l in self.links_by_claim(cid)}
        return [f for f in self.fragments if f.fragment_id in ids]

    def period_index(self, period) -> Optional[int]:
        try:
            return self.meta.periods.index(period)
        except ValueError:
            return None


# --------------------------------------------------------------- validation
def validate(c: Corpus):
    """Returns (errors, warnings).

    Errors are structural faults. Warnings are findings: an unattached fragment
    and an unsupported claim are both real properties of a paper, and the corpus
    alone cannot say which is an extraction miss.

    v4 change: audit.py refuses to run when errors are present. In v3 validation
    was advisory and nothing called it.
    """
    errs, warns = [], []
    pid = c.meta.paper_id
    periods = set(c.meta.periods)

    seen = set()
    for f in c.fragments:
        if f.fragment_id in seen:
            errs.append(f"duplicate fragment_id {f.fragment_id}")
        seen.add(f.fragment_id)
        if f.paper_id != pid:
            errs.append(f"{f.fragment_id}: paper_id mismatch")
        if f.text_status == "withheld" and f.text:
            errs.append(f"{f.fragment_id}: text_status 'withheld' but text populated")
        if f.text_status == "withheld" and not (f.stub or "").strip():
            errs.append(f"{f.fragment_id}: withheld text needs a stub")
        if not (f.location or "").strip():
            warns.append(f"{f.fragment_id}: no location")
        if f.period and periods and f.period not in periods:
            errs.append(f"{f.fragment_id}: period {f.period!r} not in meta.periods")

    cids = set()
    for cl in c.claims:
        if cl.claim_id in cids:
            errs.append(f"duplicate claim_id {cl.claim_id}")
        cids.add(cl.claim_id)
        if not cl.statement.strip():
            msg = f"{cl.claim_id}: claim with no statement"
            (warns if c.meta.claim_layer_status == "stub" else errs).append(
                msg + (" (stub, not yet extracted)"
                       if c.meta.claim_layer_status == "stub" else ""))
        if cl.outcome and not cl.asserted_direction:
            errs.append(f"{cl.claim_id}: outcome named but asserted_direction "
                        "missing -- uniformity cannot be computed")
        if not cl.location.strip():
            warns.append(f"{cl.claim_id}: claim without location")

    fids = {f.fragment_id for f in c.fragments}
    by_cid = {x.claim_id: x for x in c.claims}
    for l in c.links:
        if l.fragment_id not in fids:
            errs.append(f"link {l.fragment_id}->{l.claim_id}: unknown fragment")
        if cids and l.claim_id not in cids:
            errs.append(f"link {l.fragment_id}->{l.claim_id}: unknown claim")
        if l.direction in ("with", "against") and not l.basis.strip():
            warns.append(f"link {l.fragment_id}->{l.claim_id}: direction coded "
                         "without a stated basis")
        cl = by_cid.get(l.claim_id)
        if cl and l.direction in ("with", "against") and not cl.is_directional():
            errs.append(f"link {l.fragment_id}->{l.claim_id}: direction "
                        f"'{l.direction}' on a claim that is not directional")

    for p in c.pairs:
        unknown = (set(p.fragments_a) | set(p.fragments_b)) - fids
        if unknown:
            errs.append(f"{p.pair_id}: unknown fragment ids {sorted(unknown)}")
        if not p.basis.strip():
            errs.append(f"{p.pair_id}: contrast pair asserted without basis")
        if not (p.fragments_a and p.fragments_b):
            errs.append(f"{p.pair_id}: a pair needs fragments on both sides")

    for g in c.gaps:
        if not g.location.strip():
            errs.append(f"{g.gap_id}: declared gap without location")

    for a in c.absences:
        if not a.basis.strip():
            errs.append(f"{a.absence_id}: absence asserted without basis")

    # ---- ids that point at claims. Added 27 Sep 2026: brief v2 merges claims,
    # and a merge that misses a reference would otherwise pass silently ----
    if cids:
        for f in c.fragments:
            for x in f.citing_claims:
                if x not in cids:
                    errs.append(f"{f.fragment_id}: citing_claims names unknown claim {x}")
        for rec, rid in [(g, g.gap_id) for g in c.gaps] + \
                        [(a, a.absence_id) for a in c.absences]:
            for x in rec.bears_on:
                if x not in cids:
                    errs.append(f"{rid}: bears_on names unknown claim {x}")
    cite = {(f.fragment_id, x) for f in c.fragments for x in f.citing_claims}
    linked = {(l.fragment_id, l.claim_id) for l in c.links}
    if c.links and cite != linked:
        warns.append(f"citing_claims and claim_links disagree on {len(cite ^ linked)} "
                     "fragment-claim pair(s)")

    # ---- the episode's boundaries, which now license a move ----
    m = c.meta
    if m.resolution_period and periods and m.resolution_period not in periods:
        errs.append("meta: resolution_period not in periods")
    if m.episode_start_period and periods and m.episode_start_period not in periods:
        errs.append("meta: episode_start_period not in periods")
    if m.periods and m.periods[0] == "P0" and m.episode_start_period in (None, "P0"):
        errs.append("meta: P0 holds events before the story (brief v2), so "
                    "episode_start_period must name the period where it begins")
    if m.resolution_period and not (m.resolution_basis or "").strip():
        warns.append("meta: resolution_period set with no resolution_basis. It "
                     "licenses boundary_shift, so it needs a stated basis.")

    # ---- claim closure, both ways ----
    linked_claims = {l.claim_id for l in c.links}
    for cl in c.claims:
        if cl.claim_id not in linked_claims:
            warns.append(f"{cl.claim_id}: no fragments beneath this claim -- "
                         "either an extraction miss or an unsupported assertion")
    unattached = sorted(fids - {l.fragment_id for l in c.links})
    if unattached:
        warns.append(f"{len(unattached)} fragments attached to no claim: "
                     f"{', '.join(unattached[:12])}"
                     f"{' ...' if len(unattached) > 12 else ''}")

    # ---- single-coding, now across every hand-set trigger ----
    single = [f for f in HAND_TRIGGER_FIELDS if f not in m.double_coded_fields]
    if single:
        warns.append("single-coded trigger fields: " + ", ".join(single) +
                     ". Each can switch a move on by itself. Report kappa by "
                     "field; no number from a single-coded field should be "
                     "published.")
    return errs, warns


# --------------------------------------------------------------- load / dump
def _pick(cls, raw: dict) -> dict:
    return {k: v for k, v in raw.items() if k in cls.__dataclass_fields__}


def load(path: str) -> Corpus:
    with open(path) as fh:
        raw = json.load(fh)
    ver = raw.get("meta", {}).get("schema_version")
    if ver != SCHEMA_VERSION:
        raise ValueError(
            f"{path} is schema v{ver}; this is v{SCHEMA_VERSION}. "
            f"Run: python3 migrate_v3_v4.py {path} <out.json>")
    c = Corpus(
        meta=PaperMeta(**_pick(PaperMeta, raw["meta"])),
        fragments=[Fragment(**_pick(Fragment, f)) for f in raw.get("fragments", [])],
        claims=[Claim(**_pick(Claim, x)) for x in raw.get("claims", [])],
        links=[ClaimLink(**_pick(ClaimLink, l)) for l in raw.get("claim_links", [])],
        pairs=[ContrastPair(**_pick(ContrastPair, p))
               for p in raw.get("contrast_pairs", [])],
        gaps=[DeclaredGap(**_pick(DeclaredGap, g))
              for g in raw.get("declared_gaps", [])],
        absences=[Absence(**_pick(Absence, a)) for a in raw.get("absences", [])],
    )
    if not c.links:  # cheap attachment, direction not yet coded
        c.links = [ClaimLink(c.meta.paper_id, f.fragment_id, cid,
                             basis="derived from citing_claims", confidence="low")
                   for f in c.fragments for cid in f.citing_claims]
    return c


def dump(c: Corpus, path: str):
    payload = {
        "meta": asdict(c.meta),
        "claims": [asdict(x) for x in c.claims],
        "fragments": [asdict(f) for f in c.fragments],
        "claim_links": [asdict(l) for l in c.links],
        "contrast_pairs": [asdict(p) for p in c.pairs],
        "declared_gaps": [asdict(g) for g in c.gaps],
        "absences": [asdict(a) for a in c.absences],
    }
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=2)


if __name__ == "__main__":
    import sys
    c = load(sys.argv[1])
    errs, warns = validate(c)
    print(f"{c.meta.citation}\n  schema v{c.meta.schema_version}   "
          f"claim layer: {c.meta.claim_layer_status}")
    print(f"  {len(c.fragments)} fragments   {len(c.claims)} claims   "
          f"{len(c.links)} links   {len(c.pairs)} pairs   "
          f"{len(c.gaps)} gaps   {len(c.absences)} absences")
    print(f"  errors {len(errs)}   warnings {len(warns)}")
    for e in errs:
        print("  E", e)
    for w in warns:
        print("  W", w)
