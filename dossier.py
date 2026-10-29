"""
The Stage 1 dossier. Version 4.

What a scholar reads. The audit's job is to locate; this file's job is to show
what was located, in the order that reflects where re-theorising actually came
from in the one case we can verify: a construct load-bearing in the paper's
THEORETICAL narrative, undecomposed, beneath which the fragments did not all
behave the same way.

Nothing here is an interpretation, a rival reading, or a claim that the authors
were wrong. Non-uniform coupling is not a defect: it usually means a construct
is doing more than one job, which is the normal condition of any useful
abstraction. The dossier ends before the abduction begins.

WHAT CHANGED IN V4
------------------
Seams are printed whenever they are detected. v3 suppressed them whenever the
paper-level rate fell below the coverage floor, printed "fission candidates: 0",
and passed the same seams to Stage 2 anyway. Detection is per claim; the rate is
about the paper. Only the rate is ever withheld.

Validation and coding status come first, because three of the five triggers are
hand-coded and any one of them can switch a move on by itself.

The sensitivity grid is printed next to the seams, so a reader can see what the
guessed numbers are worth on this paper rather than taking them on trust.

An empty handoff is stated as a finding about this paper's printed record. It is
not a verdict on the paper and the wording must not drift into one.
"""

from schema import Corpus, load, validate
from audit import run_audit, MIN_COVERAGE, CUT_MOVES


def _wrap(text, width=74, indent="      "):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(indent + cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(indent + cur)
    return "\n".join(lines)


def build(c: Corpus, for_generation: bool = False, voice=None,
          voice_source=None) -> str:
    """for_generation=True suppresses every coder basis.

    A basis is the coder's rationale for a direction, written for a second coder.
    It is not evidence. A reading that leans on one is importing, and an attack
    pass caught exactly that: the strongest support for a split's second side was
    a basis line, not a printed fragment. Stage 2 sees stubs, claims and
    directions; if the seam is real it is visible in those.

    `voice` (audit.load_voice) applies the voice rule, as `audit.py --voice=`
    does; without it every link is counted and section 0 says so."""
    r = run_audit(c, voice=voice, voice_source=voice_source)
    by_frag = {f.fragment_id: f for f in c.fragments}
    by_claim = {x.claim_id: x for x in c.claims}
    uni, asy = r["measures"]
    L, A = [], None
    A = L.append

    A("=" * 78)
    A("STAGE 1 DOSSIER  --  coupling audit v4")
    A(c.meta.citation)
    A("=" * 78)
    A("")
    A("How this paper's data-theory coupling is ARRANGED. Not how well it is")
    A("coupled, and no claim that the account is wrong. Loss at each stage of")
    A("narrative production is normal, not a defect. What follows is capacity;")
    A("the apparatus is yours.")
    A("")

    # ---------------------------------------------------- 0. status first
    A("-" * 78)
    A("0. STATUS OF THIS EXTRACTION")
    A("-" * 78)
    v = r["validation"]
    A(f"   claim layer: {c.meta.claim_layer_status.upper()}   "
      f"errors {len(v['errors'])}   warnings {len(v['warnings'])}")
    if c.meta.claim_layer_status != "extracted":
        A("   !! Stage 1 is a relation between two layers. Without an extracted")
        A("      theory layer most of what follows cannot be computed.")
    cs = r["coding_status"]
    if cs["single_coded"]:
        A("")
        A("   SINGLE-CODED TRIGGERS -- each can switch a move on by itself:")
        for f in cs["single_coded"]:
            A(f"      {f}")
        A("   Report kappa by field. No number resting on these should be")
        A("   published until a second coder exists.")
    if cs["double_coded"]:
        A(f"   double-coded: {', '.join(cs['double_coded'])}"
          f"   (second coder: {cs['second_coder'] or 'unnamed'})")
    for w in v["warnings"]:
        A(_wrap(f"- {w}", indent="      "))
    vr = r["voice_rule"]
    A("")
    if vr["applied"]:
        A(_wrap(f"VOICE RULE applied ({vr['source']}): {vr['excluded_with']} with "
                f"and {vr['excluded_against']} against from author-voice "
                "fragments are left out of section 1.", indent="   "))
    else:
        A(_wrap("VOICE RULE NOT APPLIED: no voice sidecar given, so links from "
                "author-voice fragments count in section 1.", indent="   "))
    A("")

    # --------------------------------------------------------- 1. seams
    A("-" * 78)
    A("1. SEAMS  (non-uniform coupling)")
    A("-" * 78)
    A("   Claims whose fragments do not all behave the same way. A seam is not")
    A("   an error. It usually means the construct is doing more than one job.")
    A("   The system locates it and stops: it does not name the two sides, and")
    A("   the register of distinctions is not opened until a split is written.")
    A("")
    seams = uni.detail.get("seam_detail", [])
    if not uni.scored and seams:
        A(f"   Paper-level rate withheld: coverage {uni.coverage:.2f} is below")
        A(f"   {MIN_COVERAGE:.2f}. Detection is per claim and is reported in full.")
        A("")
    if not seams:
        A(f"   None detected. {uni.reading}")
    for s in seams:
        cl = by_claim.get(s["claim_id"])
        A(f"   [{s['claim_id']}]  {'core' if s['core'] else 'supporting'}   "
          f"construct: {s['construct'] or '-'}")
        if cl:
            A(_wrap(cl.statement))
            if cl.asserted_direction:
                A(_wrap(f"asserted: {cl.asserted_direction}"))
        A(f"      coupling: {s['with']} with / {s['against']} against   "
          f"majority share {s['majority_share']}")
        A(f"      running against: {', '.join(s['against_ids'])}")
        for fid in s["against_ids"]:
            f = by_frag.get(fid)
            if f:
                A(_wrap(f"{fid}: {f.stub or '(no stub)'}", indent="        "))
            for l in c.links_by_fragment(fid):
                if l.claim_id == s["claim_id"] and l.basis and not for_generation:
                    A(_wrap(f"basis: {l.basis}", indent="          "))
        feats = [x for p in r["move_parameters"].get("construct_fission", [])
                 if p["claim"] == s["claim_id"]
                 for x in p["candidate_separating_features"]]
        A("")
        if feats:
            A("      CANDIDATE SEPARATING FEATURE (a contrast pair straddles this")
            A("      seam, so the feature is already coded, in the paper's words)")
            for x in feats:
                A(_wrap(f"[{x['pair_id']}] {x['differs_in']}"
                        f"  ({'drawn by the authors' if x['drawn_by_authors'] else 'constructed by the analyst'})",
                        indent="        "))
        else:
            A("      No contrast pair straddles this seam. The feature that")
            A("      separates the two sides has to be found by reading the")
            A("      fragment descriptions.")
        A("")

    # --------------------------------------------------- 2. sensitivity
    A("-" * 78)
    A("2. SENSITIVITY OF THE DETECTOR")
    A("-" * 78)
    A("   Three hand-set numbers constitute the seam detector. This is what they")
    A("   are worth on this paper. Reported, never tuned against the paper being")
    A("   measured.")
    A("")
    sens = r["sensitivity"]
    A(f"   at current settings {r['thresholds']}")
    A(f"   seam set holds under {sens['settings_agreeing_with_current']} settings")
    A("")
    seen = {}
    for g in sens["grid"]:
        seen.setdefault(tuple(g["seams"]), []).append(
            f"links>={g['min_links']} floor<{g['floor']} minority>={g['min_minority']}")
    for combo, settings in seen.items():
        A(f"      seams {list(combo) or 'none'}   under {len(settings)} setting(s)")
        A(_wrap("; ".join(settings[:6]) + (" ..." if len(settings) > 6 else ""),
                indent="        "))
    A("")

    # ------------------------------------------------ 3. unattached / unsupported
    A("-" * 78)
    A("3. UNATTACHED EVIDENCE AND UNSUPPORTED CLAIMS  (coupling asymmetry)")
    A("-" * 78)
    A("   Computed and demoted. A weak signal: it flags candidates, it does not")
    A("   locate theory.")
    A("")
    ids = asy.detail.get("unattached_ids", [])
    A(f"   unattached fragments: {asy.score if asy.scored else '-'} "
      f"({len(ids)} of {asy.detail.get('usable_fragments', 0)} usable)")
    for fid in ids:
        f = by_frag[fid]
        A(f"   [{fid}]  {f.unit or 'unattributed'}   {f.location or '-'}")
        A(_wrap(f.stub or "(no stub)"))
    unsup = asy.detail.get("unsupported_claims", [])
    if unsup:
        A("")
        A("   CLAIMS WITH NO FRAGMENTS BENEATH THEM")
        A("   (an extraction miss or an assertion the paper does not evidence;")
        A("   the corpus alone cannot decide which)")
        for cid in unsup:
            cl = by_claim.get(cid)
            A(_wrap(f"[{cid}] {cl.statement if cl else ''}"))
    A("")

    # ---------------------------------------------------------- 4. voice
    A("-" * 78)
    A("4. VOICE BENEATH THE CORE CLAIMS  (a fact, not a score)")
    A("-" * 78)
    A("   Who is load-bearing where the argument is carried, and who speaks in")
    A("   the paper but beneath no core claim. v3 scored this as an averaged")
    A("   concentration index; the number rested on very few speech fragments")
    A("   and carried three guessed bands. The fact routes the move without it.")
    A("")
    vf = r["voice_facts"]
    if not vf.get("computable"):
        A(f"   Not computed: {vf['basis']}")
    else:
        A(f"   speech fragments in corpus: {vf['speech_fragments_in_corpus']}"
          f"   units: {', '.join(vf['units_in_corpus']) or '-'}")
        A("")
        for cid, d in vf["per_core_claim"].items():
            cl = by_claim.get(cid)
            head = (cl.statement[:58] + "...") if cl and len(cl.statement) > 58 else (cl.statement if cl else "")
            A(f"   [{cid}] {head}")
            A(f"      speech {d['speech_fragments']}   identified "
              f"{d['identified']}   units {d['units'] or '-'}")
        nlb = vf["present_but_never_load_bearing"]
        if nlb:
            A("")
            A(f"   PRESENT IN THE CORPUS, LOAD-BEARING ON NO CORE CLAIM:")
            A(f"      {', '.join(nlb)}")
    A("")

    # ------------------------------------------------------ 5. boundaries
    A("-" * 78)
    A("5. THE EPISODE'S OWN BOUNDARIES")
    A("-" * 78)
    A("   Printed evidence outside the episode as the paper bounds it licenses")
    A("   boundary_shift. Evidence AT the resolution is inside the paper's arc")
    A("   and is listed as context, not as a licence.")
    A("")
    b = r["bounds"]
    if not b.get("computable"):
        A(f"   Not computable: {b.get('why')}")
    else:
        A(f"   episode: {b['episode_start_period']} -> "
          f"{b['resolution_period'] or '(no resolution period declared)'}")
        if b.get("resolution_basis"):
            A(_wrap(f"basis: {b['resolution_basis']}"))
        A(f"   before the start:    {', '.join(b['before']) or 'none'}")
        A(f"   after the resolution:{' ' + ', '.join(b['after']) if b['after'] else ' none'}")
        A(f"   at the resolution:   {', '.join(b['at_resolution']) or 'none'}")
        if b.get("reports_outcome_after_resolution"):
            A("   the paper reports an outcome after its resolution point")
    A("")

    # -------------------------------------------------- 6. contrast pairs
    A("-" * 78)
    A("6. CONTRAST PAIRS")
    A("-" * 78)
    A("   Two episodes the paper treats as comparable that came out differently.")
    A("   Licenses causal re-attribution, which is construct_inversion. A pair")
    A("   the authors drew is a stronger licence than one the analyst built.")
    A("")
    if not c.pairs:
        A("   None extracted.")
    for p in c.pairs:
        A(f"   [{p.pair_id}]  ({'drawn by the authors' if p.drawn_by_authors else 'constructed by the analyst'})")
        A(_wrap(f"A: {p.episode_a}"))
        A(_wrap(f"B: {p.episode_b}"))
        A(_wrap(f"held comparable: {p.held_comparable}"))
        A(_wrap(f"differs in: {p.differs_in}"))
        A(f"      fragments A: {', '.join(p.fragments_a) or '-'}")
        A(f"      fragments B: {', '.join(p.fragments_b) or '-'}")
        A("")

    # ----------------------------------------- 7. ventured claims and gaps
    A("-" * 78)
    A("7. VENTURED CLAIMS AND SELF-DECLARED GAPS")
    A("-" * 78)
    A("   Claims the authors themselves mark as provisional, and statements")
    A("   about the limits of their own account. Invitations already in the")
    A("   text, not criticisms imported from outside.")
    A("")
    ventured = [x for x in c.claims if x.stated_as == "ventured"]
    if ventured:
        A("   VENTURED")
        for x in ventured:
            A(_wrap(f"[{x.claim_id}] ({x.location}) {x.statement}"))
        A("")
    if not c.gaps:
        A("   No declared gaps extracted.")
    for g in c.gaps:
        mark = "->" if g.kind == "unresolved_question" else "  "
        A(f"   {mark} [{g.gap_id}]  {g.kind}   ({g.location})")
        A(_wrap(g.statement))
        if g.bears_on:
            A(f"      bears on: {', '.join(g.bears_on)}")
    A("")
    A("   Only an unresolved_question gap parameterises counterfactual_ending.")
    A("   That is a one-person coding decision on a single record: recoding one")
    A("   gap switches the move on. It belongs on the double-coding list.")
    A("")

    # -------------------------------------------------------- 8. absences
    A("-" * 78)
    A("8. ABSENCE REGISTER")
    A("-" * 78)
    A("   Evidence classes that do not appear in print. NOT the same as")
    A("   unattached fragments. No reading can be scored against evidence the")
    A("   design could not have produced, so these bound what any re-reading may")
    A("   claim. They become research questions, never readings. Whether an")
    A("   absent observation is obtainable is the scholar's call, not the")
    A("   instrument's.")
    A("")
    for kind in ("not_collected", "collected_not_printed", "not_ascertainable"):
        sel = [a for a in c.absences if a.kind == kind]
        if not sel:
            continue
        A(f"   {kind.replace('_', ' ').upper()}")
        for a in sel:
            tag = "  [added by Stage 4]" if a.source == "stage4" else ""
            A(f"      - {a.evidence_class}{tag}")
            A(_wrap(f"basis: {a.basis}", indent="        "))
        A("")

    # --------------------------------------------------- 9. the handoff
    A("-" * 78)
    A("9. MOVE PARAMETERS  (handoff to Stage 2)")
    A("-" * 78)
    A("   Each move fires because something in this paper's own record licenses")
    A("   it. No plot is consulted and no story shape is required.")
    A("")
    params = r["move_parameters"]
    if not params:
        A("   Nothing. No move has material in this paper's printed record.")
    for k, val in params.items():
        A(f"   {k}:")
        if isinstance(val, list):
            for item in val[:20]:
                A(_wrap(str(item), indent="        "))
        else:
            A(_wrap(str(val), indent="        "))
        A("")
    A("   CUT MOVES, retained visibly rather than deleted:")
    for k, why in CUT_MOVES.items():
        A(_wrap(f"{k}: {why}", indent="        "))
    A("")

    # ------------------------------------------------------ 10. readiness
    A("-" * 78)
    A("10. GENERATION READINESS")
    A("-" * 78)
    rd = r["readiness"]
    A(f"   READY: {'yes' if rd['ready'] else 'no'}  -- {rd['reason']}")
    if rd["moves_parameterised"]:
        A(f"   moves: {', '.join(rd['moves_parameterised'])}")
    if not rd["ready"]:
        A("")
        A("   This is a finding about what this paper printed, not a verdict on")
        A("   the paper and not a grade. Papers whose coupling is uniform and")
        A("   whose record stays inside its own episode are exactly the papers")
        A("   this instrument should return nothing for.")
    A("")
    A("=" * 78)
    A("END OF DOSSIER. The system stops here. Writing the split, naming its two")
    A("sides, and opening the register all come after, and in that order.")
    A("=" * 78)
    return "\n".join(L)


if __name__ == "__main__":
    import sys
    from audit import load_voice
    c = load(sys.argv[1])
    gen = "--for-generation" in sys.argv
    voice_path = next((a.split("=", 1)[1] for a in sys.argv[1:]
                       if a.startswith("--voice=")), None)
    errs, _ = validate(c)
    if errs and "--force" not in sys.argv:
        print(f"REFUSING: {len(errs)} validation error(s). Re-run with --force.")
        for e in errs:
            print("  E", e)
        raise SystemExit(1)
    try:
        voice = load_voice(voice_path, c) if voice_path is not None else None
    except ValueError as e:
        print(f"REFUSING: {e}")
        raise SystemExit(1)
    print(build(c, for_generation=gen, voice=voice, voice_source=voice_path))
