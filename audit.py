"""
Stage 1: the coupling audit. Version 4.

WHAT CHANGED FROM V3
--------------------
A move now fires because something in THIS PAPER'S OWN RECORD licenses it. In
v3 four of the eight moves were gated on whether some canonical plot in the
library had the right shape, which asked the question of the wrong object: you
cannot tell whether an episode has a definite ending by inspecting Selznick.
The library is no longer consulted here at all. It has become a register of
distinctions, opened after a split is written, to supply candidate names.

WHAT IS SCORED
--------------
One measure: coupling_uniformity, the seam detector. It is the only place the
instrument produces a number about a paper, and it is the only computed trigger.

WHAT IS COMPUTED BUT NOT SCORED
-------------------------------
coupling_asymmetry, kept and demoted: fragments under no claim, claims under no
fragment. A weak signal that flags candidates rather than locating theory.

voice facts: which units are load-bearing beneath core claims and which speak in
the paper but beneath none. v3 scored this as an averaged concentration index
over, in the one real case, eight speech fragments, with three guessed bands
attached. The fact routes the move perfectly well without the number.

WHAT IS ROUTED FROM STAGE 0
---------------------------
contrast pairs -> construct_inversion (NOT boundary_shift: a pair licenses
causal re-attribution, which is inversion. It says nothing about where the
episode starts or ends. In v3 both moves were emitted under one combined label
that matched no operator name, so contrast pairs reached neither.)

ventured claims + unresolved-question gaps -> counterfactual_ending
absences -> research questions, never moves

WHAT IS COMPUTED FROM THE PAPER'S OWN BOUNDARIES
------------------------------------------------
printed evidence outside the episode as the paper bounds it -> boundary_shift.
This is what makes Fragment.period worth keeping after coupling_temporal was cut.

REMOVED
-------
coupling_temporal, channel_loss, script_inversions, generation triage, and the
plot-shape licensing gate. temporal_stratification, actantial_permutation and
scale_shift go with them and are recorded in CUT_MOVES rather than deleted.

CHANGED 27 SEP 2026: THE VOICE RULE, APPLIED BEFORE V5
------------------------------------------------------
SCHEMA_v5.md settles that a fragment coded voice `author_insight` never counts
as `with` or `against`: otherwise the author's own interpretation counts as
evidence for the author's own claim. v5 is not implemented and voice is not a
corpus field, so the audit reads it from the voice sidecar
(<paper_id>_voice_gloss.json), given with --voice=. With a sidecar, uniformity
and the sensitivity grid count links from `reported` fragments only, and every
directional link from an author-voice fragment is listed separately in
`voice_rule` and on its claim's row. Extraction still codes direction on every
fragment: where the author's own sentences supply the support is a finding.

Without a sidecar the audit counts every link, as before, and the report says
the rule was not applied. Only uniformity changes. Asymmetry, voice facts and
the episode's boundaries are computed as before. See AUDIT_VOICE_RULE_LOG.md.
"""

from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict
import itertools
import json

from schema import Corpus, validate, HAND_TRIGGER_FIELDS

# ---------------------------------------------------------------- thresholds
# Every hand-set number in the instrument, in one place, because there are more
# of them than first appears, and a reviewer will ask about all of them.
# sensitivity() recomputes the candidate set across a grid of the first three.
MIN_LINKS_FOR_UNIFORMITY = 4     # below this, a split looks inconsistent by chance
UNIFORMITY_FLOOR = 0.85          # majority share below this is non-uniform
MIN_MINORITY = 2                 # and at least this many must run the other way
MIN_COVERAGE = 0.60              # below this the paper-level RATE is not reported

THRESHOLDS = {
    "MIN_LINKS_FOR_UNIFORMITY": MIN_LINKS_FOR_UNIFORMITY,
    "UNIFORMITY_FLOOR": UNIFORMITY_FLOOR,
    "MIN_MINORITY": MIN_MINORITY,
    "MIN_COVERAGE": MIN_COVERAGE,
}

MOVES = ("construct_fission", "construct_inversion", "boundary_shift",
         "counterfactual_ending", "focalization_shift")

VOICE_CODES = ("reported", "author_insight")
VOICE_RULE = ("a fragment coded voice author_insight never counts as with or "
              "against (SCHEMA_v5.md; applied before v5, "
              "from 27 Sep 2026)")

CUT_MOVES = {
    "temporal_stratification": "trigger was coupling_temporal, cut: on the one "
                               "real paper it returned 1.000 as an extraction "
                               "artifact with nearly everything coded P1",
    "actantial_permutation": "trigger was script_inversions, cut with "
                             "script_type; fired only on a fixture built "
                             "knowing the answer",
    "scale_shift": "never had a detector in any version",
}


@dataclass
class Measure:
    name: str
    scored: bool
    score: Optional[float]
    coverage: float
    detail: dict
    reading: str

    def line(self) -> str:
        if not self.scored:
            return (f"  {self.name:<22} RATE NOT REPORTED   "
                    f"coverage {self.coverage:.2f}   {self.reading}")
        return (f"  {self.name:<22} {self.score:>6.3f}   "
                f"coverage {self.coverage:.2f}   {self.reading}")


# ------------------------------------------------------------- 0. voice rule
def load_voice(path: str, c: Corpus) -> dict:
    """{fragment_id: voice code} from a voice sidecar.

    Refuses rather than guesses when the sidecar is for another paper, holds a
    code outside the two values, codes a fragment twice, or leaves a fragment of
    the corpus uncoded. An uncoded fragment would be counted, and counting an
    author's interpretation is what the rule exists to prevent."""
    if not path:
        raise ValueError("voice sidecar refused: --voice= names no file")
    try:
        with open(path) as fh:
            raw = json.load(fh)
    except (OSError, ValueError) as e:     # missing file, or not JSON
        raise ValueError(f"voice sidecar refused: cannot read {path}: {e}")
    if not isinstance(raw, dict) or not isinstance(raw.get("voice"), list):
        raise ValueError("voice sidecar refused: expected an object with a "
                         "'voice' list, as EXTRACTION_BRIEF.md defines")
    problems, voice = [], {}
    if raw.get("paper_id") != c.meta.paper_id:
        problems.append(f"sidecar is for {raw.get('paper_id')!r}; "
                        f"the corpus is {c.meta.paper_id!r}")
    for v in raw["voice"]:
        if not isinstance(v, dict):
            problems.append(f"a voice entry is not an object: {v!r}")
            continue
        fid, code = v.get("fragment_id"), v.get("code")
        if not isinstance(fid, str) or not fid:
            problems.append(f"a voice entry has no fragment_id string: {v}")
            continue
        if code not in VOICE_CODES:
            problems.append(f"{fid}: voice {code!r} is not one of {VOICE_CODES}")
        if fid in voice:
            problems.append(f"{fid}: voice coded twice")
        voice[fid] = code
    fids = {f.fragment_id for f in c.fragments}
    missing, unknown = sorted(fids - set(voice)), sorted(set(voice) - fids)
    if missing:
        problems.append(f"no voice code for {len(missing)} fragment(s): "
                        + ", ".join(missing[:12]) + (" ..." if len(missing) > 12 else ""))
    if unknown:
        problems.append(f"voice coded for {len(unknown)} fragment(s) not in the "
                        "corpus: " + ", ".join(unknown[:12]))
    if problems:
        raise ValueError("voice sidecar refused:\n  " + "\n  ".join(problems))
    return voice


def voice_rule(c: Corpus, voice: Optional[dict], source: Optional[str]) -> dict:
    """What the voice rule took out of uniformity, listed link by link."""
    if voice is None:
        return {"applied": False, "source": None, "rule": VOICE_RULE,
                "note": "no voice sidecar given; links from author-voice "
                        "fragments are counted"}
    directional = {x.claim_id for x in c.claims if x.is_directional()}
    out = [{"fragment_id": l.fragment_id, "claim_id": l.claim_id,
            "direction": l.direction} for l in c.links
           if l.direction in ("with", "against") and l.claim_id in directional
           and voice.get(l.fragment_id) == "author_insight"]
    return {"applied": True, "source": source, "rule": VOICE_RULE,
            "fragments": dict(Counter(voice.values())),
            "excluded_with": sum(1 for x in out if x["direction"] == "with"),
            "excluded_against": sum(1 for x in out if x["direction"] == "against"),
            "excluded_links": out}


# ------------------------------------------------------------- 1. uniformity
def _uniformity_rows(c: Corpus, min_links, floor, min_minority, voice=None):
    rows = []
    for cl in [x for x in c.claims if x.is_directional()]:
        coded = [l for l in c.links_by_claim(cl.claim_id)
                 if l.direction in ("with", "against")]
        # The voice rule: links from author-voice fragments are listed on
        # the row and left out of every count below.
        excluded = [l for l in coded if voice is not None
                    and voice.get(l.fragment_id) == "author_insight"]
        ls = [l for l in coded if voice is None
              or voice.get(l.fragment_id) != "author_insight"]
        n_with = sum(1 for l in ls if l.direction == "with")
        n_against = sum(1 for l in ls if l.direction == "against")
        n = n_with + n_against
        row = {"claim_id": cl.claim_id, "construct": ", ".join(cl.constructs),
               "core": cl.core, "n_directional": n, "with": n_with,
               "against": n_against,
               "against_ids": [l.fragment_id for l in ls
                               if l.direction == "against"],
               "with_ids": [l.fragment_id for l in ls if l.direction == "with"]}
        if voice is not None:
            row["author_voice_excluded"] = {
                "with": [l.fragment_id for l in excluded if l.direction == "with"],
                "against": [l.fragment_id for l in excluded
                            if l.direction == "against"]}
        if n >= min_links:
            share = max(n_with, n_against) / n
            row["majority_share"] = round(share, 3)
            row["assessed"] = True
            row["seam"] = bool(share < floor and min(n_with, n_against) >= min_minority)
        else:
            row.update(majority_share=None, assessed=False, seam=False,
                       note=f"fewer than {min_links} directionally coded "
                            "fragments; not assessed")
        rows.append(row)
    return rows


def coupling_uniformity(c: Corpus, voice: Optional[dict] = None) -> Measure:
    """THE SEAM DETECTOR, and the only scored measure.

    Per claim: of the fragments coded with or against, what share run the way
    the claim asserts? A claim whose fragments split is a claim whose construct
    is doing more than one job.

    Two things are separated here that v3 confused. Detection is PER CLAIM and
    depends only on that claim clearing MIN_LINKS. The paper-level RATE (what
    share of assessed claims are seams) depends on coverage. v3 suppressed the
    seams from the dossier whenever the rate was unreportable, printed
    "fission candidates: 0", and then passed those same seams to Stage 2 -- so
    the reader was told there was nothing there while the pipeline acted on it.
    v4 always reports detected seams and withholds only the rate.

    It does not name the sub-types. Naming is the scholar's, after the split is
    written; the register is opened afterwards to offer candidate names.
    """
    directional = [x for x in c.claims if x.is_directional()]
    if not directional:
        why = ("no claim layer" if not c.claims else
               "no claim carries both an outcome and an asserted direction")
        return Measure("coupling_uniformity", False, None, 0.0,
                       {"directional_claims": 0, "claims": [], "seams": []}, why)

    rows = _uniformity_rows(c, MIN_LINKS_FOR_UNIFORMITY, UNIFORMITY_FLOOR,
                            MIN_MINORITY, voice)
    assessed = [r for r in rows if r["assessed"]]
    seams = [r for r in assessed if r["seam"]]
    coverage = len(assessed) / len(directional)
    scored = bool(assessed) and coverage >= MIN_COVERAGE
    score = (len(seams) / len(assessed)) if assessed else None

    if not assessed:
        reading = "no directional claim carries enough coded fragments"
    elif seams:
        reading = (f"{len(seams)} seam(s) detected"
                   + ("" if scored else "; paper-level rate withheld on coverage"))
    else:
        reading = "no seam in the assessed claims"

    return Measure("coupling_uniformity", scored,
                   round(score, 3) if (scored and score is not None) else None,
                   round(coverage, 3),
                   {"claims": rows, "directional_claims": len(directional),
                    "assessed_claims": len(assessed),
                    "seams": [r["claim_id"] for r in seams],
                    "seam_detail": seams}, reading)


def sensitivity(c: Corpus, voice: Optional[dict] = None) -> dict:
    """How the detected seam set moves across the three numbers that constitute
    the detector. Reported rather than tuned: the point is to show a reader what
    the guesses are worth on this paper, not to pick the setting that flatters
    it."""
    out = []
    for ml, fl, mm in itertools.product((3, 4, 5), (0.80, 0.85, 0.90), (1, 2)):
        rows = _uniformity_rows(c, ml, fl, mm, voice)
        assessed = [r for r in rows if r["assessed"]]
        seams = sorted(r["claim_id"] for r in assessed if r["seam"])
        out.append({"min_links": ml, "floor": fl, "min_minority": mm,
                    "assessed": len(assessed), "seams": seams})
    base = [r for r in out
            if (r["min_links"], r["floor"], r["min_minority"])
            == (MIN_LINKS_FOR_UNIFORMITY, UNIFORMITY_FLOOR, MIN_MINORITY)][0]
    stable = sum(1 for r in out if r["seams"] == base["seams"])
    return {"grid": out, "at_current_settings": base["seams"],
            "settings_agreeing_with_current": f"{stable}/{len(out)}"}


# ------------------------------------------------------------- 2. asymmetry
def coupling_asymmetry(c: Corpus) -> Measure:
    """Fragments printed but under no claim; claims with nothing beneath them.

    Kept and demoted: computed, reported, not in the headline. An unattached
    fragment is a seed for a reading the incumbent had no use for. An
    unsupported claim is either an extraction miss or an assertion the paper
    does not evidence, and the corpus alone cannot say which.
    """
    usable = [f for f in c.fragments
              if f.extraction_confidence in ("high", "medium")]
    coverage = len(usable) / len(c.fragments) if c.fragments else 0.0
    if not usable:
        return Measure("coupling_asymmetry", False, None, coverage, {},
                       "no usable fragments")
    attached = {l.fragment_id for l in c.links}
    unattached = [f.fragment_id for f in usable if f.fragment_id not in attached]
    unsupported = [x.claim_id for x in c.claims
                   if not c.links_by_claim(x.claim_id)]
    load = Counter(l.fragment_id for l in c.links)
    score = len(unattached) / len(usable)
    return Measure("coupling_asymmetry", coverage >= MIN_COVERAGE,
                   round(score, 3), round(coverage, 3),
                   {"usable_fragments": len(usable),
                    "unattached_ids": unattached,
                    "unsupported_claims": unsupported,
                    "most_cited": [f"{k} ({v})" for k, v in load.most_common(5)]},
                   "high" if score > 0.35 else
                   "moderate" if score > 0.15 else "low")


# ----------------------------------------------------------- 3. voice facts
def voice_facts(c: Corpus) -> dict:
    """Which units are load-bearing beneath the core claims, and which speak in
    the paper but beneath none. A routed fact, not a score.

    The second list parameterises focalization_shift. Retelling from a unit's
    own printed fragments imports no theory, which is why the move survives the
    cut even though its number did not.
    """
    core = [x for x in c.claims if x.core]
    speech = [f for f in c.fragments if f.is_speech()]
    corpus_units = sorted({f.unit for f in speech if f.has_unit()})
    per_claim, core_units = {}, set()
    for cl in core:
        fs = [f for f in c.fragments_under(cl.claim_id) if f.is_speech()]
        units = Counter(f.unit for f in fs if f.has_unit())
        per_claim[cl.claim_id] = {"speech_fragments": len(fs),
                                  "identified": sum(units.values()),
                                  "units": dict(units.most_common())}
        core_units |= set(units)
    # With no core claim marked, every unit is trivially "never load-bearing",
    # which is an artifact of the missing judgement rather than a fact about the
    # paper. Report nothing rather than route a move off it.
    never = sorted(set(corpus_units) - core_units) if core else []
    return {"core_claims": [x.claim_id for x in core],
            "computable": bool(core),
            "speech_fragments_in_corpus": len(speech),
            "units_in_corpus": corpus_units,
            "per_core_claim": per_claim,
            "present_but_never_load_bearing": never,
            "basis": ("no core claim marked" if not core else
                      "units beneath core claims, counted over speech fragments "
                      "only; unattributed speech is excluded, not imputed")}


# ------------------------------------------- 4. the episode's own boundaries
def outside_episode(c: Corpus) -> dict:
    """Printed evidence sitting outside the episode as the paper bounds it.

    Strictly before episode_start_period, or strictly after resolution_period.
    Evidence AT the resolution is inside the paper's own arc and is reported as
    context rather than as a licence: counting it would fire on nearly every
    paper and the trigger would stop meaning anything.
    """
    m = c.meta
    if not m.periods:
        return {"computable": False,
                "why": "no ordered periods declared", "before": [], "after": [],
                "at_resolution": []}
    start = m.episode_start_period or m.periods[0]
    si = c.period_index(start)
    ri = c.period_index(m.resolution_period) if m.resolution_period else None
    before, after, at = [], [], []
    for f in c.fragments:
        if not f.period:
            continue
        i = c.period_index(f.period)
        if i is None:
            continue
        if si is not None and i < si:
            before.append(f.fragment_id)
        elif ri is not None and i > ri:
            after.append(f.fragment_id)
        elif ri is not None and i == ri:
            at.append(f.fragment_id)
    return {"computable": ri is not None or si is not None,
            "episode_start_period": start, "resolution_period": m.resolution_period,
            "resolution_basis": m.resolution_basis,
            "reports_outcome_after_resolution": m.reports_outcome_after_resolution,
            "before": before, "after": after, "at_resolution": at,
            "why": ("no resolution_period declared; only the start boundary is "
                    "testable" if ri is None else "")}


# ------------------------------------------------------- the cheap route in
def straddling_pairs(c: Corpus, seam: dict) -> List[dict]:
    """Contrast pairs with one of a seam's sides on each side of the pair.

    This is the cheap route to a separating feature. Where it fires, the pair's
    own `differs_in` note is a ready-made candidate for what tells the two
    halves of a split apart, already stated in the paper's own words and coded
    before anyone was looking for a split. Where it does not fire, the feature
    has to be found by reading the fragment descriptions, which is Stage 2's job.
    """
    out = []
    against, withs = set(seam["against_ids"]), set(seam["with_ids"])
    for p in c.pairs:
        a, b = set(p.fragments_a), set(p.fragments_b)
        if (against & a and withs & b) or (against & b and withs & a):
            out.append({"pair_id": p.pair_id, "differs_in": p.differs_in,
                        "drawn_by_authors": p.drawn_by_authors,
                        "against_side": sorted(against & (a | b)),
                        "with_side": sorted(withs & (a | b))})
    return out


# ------------------------------------------------------------------- moves
def parameterise(c: Corpus, uni: Measure, asy: Measure, voice: dict,
                 bounds: dict) -> dict:
    """What Stage 1 hands to Stage 2: per move, the material in THIS paper that
    licenses it. No plot is consulted and no shape is required."""
    p: Dict[str, object] = {}

    seams = uni.detail.get("seam_detail", [])
    if seams:
        p["construct_fission"] = [{
            "claim": s["claim_id"], "construct": s["construct"],
            "core": s["core"], "majority_share": s["majority_share"],
            "side_a_fragments": s["with_ids"],
            "side_b_fragments": s["against_ids"],
            "candidate_separating_features": straddling_pairs(c, s),
            "admissibility": [
                "both sides non-empty: satisfied by construction",
                "at least one side-B fragment must be one the incumbent claim "
                "leaves unexplained -- a person checks this",
                "a separating feature, independent of the outcome, must sort "
                "the fragments; report how cleanly it sorts, do not set a pass mark",
            ]} for s in seams]

        # The same seam licenses a second move: either the construct is doing
        # two jobs, or the arrow runs the other way. Tagged by trigger so the
        # two sources can be compared later.
        p.setdefault("construct_inversion", []).extend([{
            "trigger": "from_seam", "claim": s["claim_id"],
            "construct": s["construct"], "outcome_fragments": s["against_ids"]}
            for s in seams])

    if c.pairs:
        p.setdefault("construct_inversion", []).extend([{
            "trigger": "from_pair", "pair": x.pair_id,
            "drawn_by_authors": x.drawn_by_authors, "differs_in": x.differs_in,
            "fragments": x.fragments_a + x.fragments_b,
            "note": ("analyst-constructed pair: a weaker licence than one the "
                     "authors drew" if not x.drawn_by_authors else "")}
            for x in c.pairs])

    out = bounds.get("before", []) + bounds.get("after", [])
    if out:
        p["boundary_shift"] = {
            "fragments_outside_episode": out,
            "before_start": bounds["before"], "after_resolution": bounds["after"],
            "episode": [bounds.get("episode_start_period"),
                        bounds.get("resolution_period")],
            "basis": bounds.get("resolution_basis")}

    ventured = [x.claim_id for x in c.claims if x.stated_as == "ventured"]
    unresolved = [g.gap_id for g in c.gaps if g.kind == "unresolved_question"]
    if ventured or unresolved:
        p["counterfactual_ending"] = {"ventured_claims": ventured,
                                      "unresolved_question_gaps": unresolved}

    nlb = voice.get("present_but_never_load_bearing", [])
    if nlb:
        p["focalization_shift"] = {
            "units": nlb,
            "fragments_by_unit": {u: [f.fragment_id for f in c.fragments
                                      if f.unit == u] for u in nlb}}

    if asy.detail.get("unattached_ids"):
        p["seed_fragments"] = asy.detail["unattached_ids"]   # not a move
    if c.absences:
        p["research_questions_only"] = [a.absence_id for a in c.absences]
    return p


def readiness(params: dict) -> dict:
    """Mechanical sufficiency, no threshold: Stage 2 has work iff at least one
    move was parameterised. Grades nothing, and an empty result is a finding
    about this paper's record, not a verdict on the paper."""
    ops = [k for k in params if k in MOVES]
    return {"moves_parameterised": sorted(ops),
            "has_seed_fragments": bool(params.get("seed_fragments")),
            "ready": bool(ops),
            "reason": (f"{len(ops)} move(s) parameterised" if ops else
                       "no move has material in this paper's record; Stage 2 "
                       "has nothing to instantiate")}


# --------------------------------------------------------------- run / report
def run_audit(c: Corpus, voice: Optional[dict] = None,
              voice_source: Optional[str] = None) -> dict:
    """`voice`, from load_voice(), applies the voice rule to uniformity and the
    sensitivity grid. None leaves every link counted, as before 27 Sep."""
    uni = coupling_uniformity(c, voice)
    asy = coupling_asymmetry(c)
    vfacts = voice_facts(c)
    bounds = outside_episode(c)
    params = parameterise(c, uni, asy, vfacts, bounds)
    errs, warns = validate(c)
    return {"paper_id": c.meta.paper_id, "citation": c.meta.citation,
            "schema_version": c.meta.schema_version,
            "claim_layer_status": c.meta.claim_layer_status,
            "measures": [uni, asy], "voice_facts": vfacts, "bounds": bounds,
            "voice_rule": voice_rule(c, voice, voice_source),
            "seams_detected": uni.detail.get("seams", []),
            "sensitivity": sensitivity(c, voice),
            "move_parameters": params, "readiness": readiness(params),
            "thresholds": dict(THRESHOLDS),
            "coding_status": {
                "double_coded": list(c.meta.double_coded_fields),
                "single_coded": [f for f in HAND_TRIGGER_FIELDS
                                 if f not in c.meta.double_coded_fields],
                "second_coder": c.meta.second_coder},
            "validation": {"errors": errs, "warnings": warns}}


def to_jsonable(r: dict) -> dict:
    out = dict(r)
    out["measures"] = [asdict(m) for m in r["measures"]]
    return out


def report(r: dict) -> str:
    L = [f"COUPLING AUDIT v4  --  {r['citation']}",
         f"claim layer: {r['claim_layer_status']}", ""]
    for m in r["measures"]:
        L.append(m.line())
    vr = r.get("voice_rule", {})
    if vr.get("applied"):
        L.append(f"  voice rule applied: {vr['excluded_with']} with and "
                 f"{vr['excluded_against']} against from author-voice fragments "
                 f"listed, not counted  ({vr['source']})")
        links = [f"{x['fragment_id']}->{x['claim_id']} {x['direction']}"
                 for x in vr["excluded_links"]]
        line = "    not counted:"
        for s in links:
            if len(line) + len(s) + 2 > 78:
                L.append(line.rstrip(","))
                line = "     "
            line += f" {s},"
        if links:
            L.append(line.rstrip(","))
    else:
        L.append("  voice rule NOT applied: no voice sidecar given (--voice=); "
                 "links from author-voice fragments are counted")
    L += ["", f"  seams detected: {len(r['seams_detected'])} "
              f"{r['seams_detected'] or ''}",
          f"  sensitivity: same seam set under "
          f"{r['sensitivity']['settings_agreeing_with_current']} threshold settings",
          ""]
    rd = r["readiness"]
    L.append(f"  GENERATION READY: {'yes' if rd['ready'] else 'no'}  -- {rd['reason']}")
    if rd["moves_parameterised"]:
        L.append(f"  moves: {', '.join(rd['moves_parameterised'])}")
    if r["coding_status"]["single_coded"]:
        L += ["", "  single-coded triggers: "
                  + ", ".join(r["coding_status"]["single_coded"])]
    L += ["", "  No verdict is issued. The measure is how coupling is arranged,",
          "  not how well it is done."]
    return "\n".join(L)


if __name__ == "__main__":
    import sys
    from schema import load
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    voice_path = next((a.split("=", 1)[1] for a in sys.argv[1:]
                       if a.startswith("--voice=")), None)   # "" if given empty
    c = load(args[0])
    errs, _ = validate(c)
    if errs and not force:
        print(f"REFUSING TO AUDIT: {len(errs)} validation error(s).")
        for e in errs:
            print("  E", e)
        print("Fix them, or re-run with --force.")
        raise SystemExit(1)
    try:
        voice = load_voice(voice_path, c) if voice_path is not None else None
    except ValueError as e:        # a bad sidecar is refused even with --force
        print(f"REFUSING TO AUDIT: {e}")
        raise SystemExit(1)
    result = run_audit(c, voice=voice, voice_source=voice_path)
    print(report(result))
    for a in sys.argv[1:]:
        if a.startswith("--json="):
            with open(a.split("=", 1)[1], "w") as fh:
                json.dump(to_jsonable(result), fh, indent=2)
            print(f"\n  wrote {a.split('=', 1)[1]}")
