#!/usr/bin/env python3
"""
The map test (T39): the scorer. Every measure of MAP_TEST_PLAN.md's part F, described, not tested.

WHY
---
The plan's order (part G, step 4) asks that the scorer be fixed by its sha256 before any reply of round 2 is opened,
and (step 5) that every figure of the results be checked independently, with separate code. It judges nothing: it
counts and compares.

USAGE
-----
    python3 -B score_map_test.py score <out dir>
        MAP_RESULTS.md and map_results.json
    python3 -B score_map_test.py --selftest

It refuses to write over a file, and the same inputs always give the same bytes.

THE INPUTS, all in this folder
------------------------------
Round 1: `map_key.json`; the four map replies (`reply_73_bechky_map_opus.json` to `reply_76_pratt_map_gpt6.json`),
read as `build_map_settle.py` reads them (`build_map_test.py`'s lenient readings applied; refused unless they count
with no quoted span of more than eight words); `map_settle_key_<paper>.json`, `map_settled_<paper>.json` and
`map_closure_<paper>.json`. Round 2: `map_round2_key.json`; the placement replies (`reply_77_bechky_place_argon.json`,
`reply_78_pratt_place_argon.json`), read by `build_map_round2.py`'s check and refused unless they count with no long
quoted span; the openings' checks (`reply_79_bechky_openings_gpt6.json`, `reply_80_pratt_openings_gpt6.json`), read by
its check of them likewise, with `map_openings_key.json`; `map_comparison_key.json` and the PI's answers,
`map_comparison_answers.json`. T37: `relation_key.json` (the planted readings) and `relation_results.json` (both
coders' codes and the PI's worth of the real readings). The PI's times: `map_times.json`,
`{"steps": [{"step", "chat_minutes": {chat: minutes or null}, "pi_minutes", "pi_minutes_at_least"}]}`, each step
with the minutes the PI reported. The frozen
indexes are checked against their hashes. Each file a later one names by its sha256 is checked against it: the
replies of round 1 against their settle keys, the settle keys against the settled maps, the settled maps and T37's
results against the closures and the round 2 key, the round 2 key against the openings' and the comparison's keys,
the placement replies against both, and the comparison's key against the PI's answers.

THE MEASURES
------------
F1, per paper, on the maps as built (map A, the Opus map; map B, the GPT 6 map):
- the listed pairs, an edge or not in each map: both, A only, B only, neither; raw agreement; Cohen's kappa; positive
  agreement (twice both, over twice both plus A only plus B only);
- on the listed pairs both call edges, the type and the strength, each with raw agreement, kappa and the confusion
  table (map A's answer by row, map B's by column);
- the registries, over every unordered pair of two of the sheet's construct names: placed together by map A, by map B
  (each map's groups closed transitively over the sheet's names), and by both; positive and raw agreement;
- where the table applies, the units' outcomes and the paired factors' values in each unit; where the contrasts
  apply, the paired factors' controls in each contrast pair (the factors paired in order by the claim each cites):
  raw agreement on each; and each map's factors that the other's do not pair with;
- the further edges, each map's (a further edge on a listed pair, and a map's second on one pair, left aside), those
  both give, and of those the ones both give with one type and one strength;
- each map's share of edges among the candidate pairs and among the sampled pairs.
F2, per paper: the items of the PI's settling sheet by kind, and the PI's choices (A, B, the PI's own) by kind; the sheet's time
cells as the settled map has them. The PI's minutes, which the PI gave for both papers together, are under F7.
F3, per paper: per reading, the elements it is placed on by kind (a passage given as an element counted as a passage),
the passages of its evidence, whether it has something off the map, and the ties of its opening's two sentences by
kind; the totals; and each planted reading's placement beside the claim and type it was written to, with whether that
claim is among its elements.
F4, per paper: per reading and coder, T37's main claim and type and the labels the closure gives core claims; the PI's worth
of the reading (none for a planted one); the totals of labels on core claims, by label and coder, and the readings with
a label on a core claim besides contested, by coder.
F5, per paper: per reading, whether the openings' check found the opening faithful; the totals.
F6: for each of the PI's two questions, how often the PI picked T37's account, the map's, the same or neither, or left it
unanswered, in all and by paper; the PI's notes, by tab.
F7: each chat's minutes, and the PI's for settling and for the comparison, by `map_times.json`; and the PI's
start and end on the comparison sheet, if the PI typed them.
A rate whose denominator is zero, and a kappa whose expected agreement is one, are given as none; rates and kappas to
three decimals.
"""
import collections
import hashlib
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_map_test as bmt  # noqa: E402
import build_map_settle as bms  # noqa: E402
import build_map_round2 as br2  # noqa: E402

PAPERS = bmt.PAPERS
CODERS = ("gemini", "astra")
LABELS = bms.LABELS
PICKS = ("T37", "map", "the same", "neither", None)
CHATS = {"bechky": {"map": ("reply_73_bechky_map_opus.json", "reply_74_bechky_map_gpt6.json"),
                    "place": "reply_77_bechky_place_argon.json", "check": "reply_79_bechky_openings_gpt6.json"},
         "pratt": {"map": ("reply_75_pratt_map_opus.json", "reply_76_pratt_map_gpt6.json"),
                   "place": "reply_78_pratt_place_argon.json", "check": "reply_80_pratt_openings_gpt6.json"}}
num = bmt.num
sha_bytes = bmt.sha_bytes


def rate(a, b):
    return None if not b else round(a / b, 3)


def kappa(pairs, cats):
    n = len(pairs)
    if not n:
        return None
    po = sum(a == b for a, b in pairs) / n
    ca, cb = collections.Counter(a for a, _ in pairs), collections.Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
    return None if pe == 1 else round((po - pe) / (1 - pe), 3)


def confusion(pairs, cats):
    c = collections.Counter(pairs)
    return {a: {b: c[(a, b)] for b in cats} for a in cats}


def agreement(pairs, cats):
    return {"n": len(pairs), "agree": sum(a == b for a, b in pairs), "raw": rate(sum(a == b for a, b in pairs),
                                                                                    len(pairs)),
            "kappa": kappa(pairs, cats), "confusion": confusion(pairs, cats)}


# ---------------------------------------------------------------- F1

def f1(paper, mkey, index, ra, rb):
    kp = mkey["papers"][paper]
    order, ap = kp["order"], kp["applies"]
    A, B = ({p["pair"]: p for p in r["pairs"]} for r in (ra, rb))
    yes = [(A[o["id"]]["rests_on"], B[o["id"]]["rests_on"]) for o in order]
    both = sum(a and b for a, b in yes)
    neither = sum(not a and not b for a, b in yes)
    only_a = sum(a and not b for a, b in yes)
    only_b = sum(b and not a for a, b in yes)
    out = {"listed": {"n": len(order), "both": both, "a_only": only_a, "b_only": only_b, "neither": neither,
                      "raw": rate(both + neither, len(order)), "kappa": kappa(yes, (True, False)),
                      "positive": rate(2 * both, 2 * both + only_a + only_b)}}
    on_both = [o["id"] for o in order if A[o["id"]]["rests_on"] and B[o["id"]]["rests_on"]]
    out["type"] = agreement([(A[i]["type"], B[i]["type"]) for i in on_both], bmt.TYPES)
    out["strength"] = agreement([(A[i]["strength"], B[i]["strength"]) for i in on_both], bmt.STRENGTHS)
    names = set(bmt.construct_names(index))
    ta, tb = (bms.together(bms.groups_of(r["registry"], names)[0]) for r in (ra, rb))
    allp = len(names) * (len(names) - 1) // 2
    out["registry"] = {"names": len(names), "pairs": allp, "together_a": len(ta), "together_b": len(tb),
                       "together_both": len(ta & tb), "positive": rate(2 * len(ta & tb), len(ta) + len(tb)),
                       "raw": rate(allp - len(ta ^ tb), allp)}
    pairs_f, ua, ub = bms.align(ra["factors"], rb["factors"])
    fac = {"a": len(ra["factors"]), "b": len(rb["factors"]), "paired": len(pairs_f),
           "a_unpaired": [ra["factors"][i]["claim"] for i in ua], "b_unpaired": [rb["factors"][j]["claim"] for j in ub]}
    sign = bmt.SIGNS
    if ap["table"]:
        UA, UB = ({u["unit"]: u for u in r["units"]} for r in (ra, rb))
        units = [u["unit"] for u in ap["units"]]
        oc = [(sign[UA[u]["outcome"]], sign[UB[u]["outcome"]]) for u in units]
        vals = [(sign[UA[u]["values"][ra["factors"][i]["id"]]], sign[UB[u]["values"][rb["factors"][j]["id"]]])
                for u in units for i, j in pairs_f]
        fac["outcomes"] = {"n": len(oc), "agree": sum(a == b for a, b in oc), "raw": rate(sum(a == b for a, b in oc),
                                                                                            len(oc))}
        fac["values"] = {"n": len(vals), "agree": sum(a == b for a, b in vals),
                         "raw": rate(sum(a == b for a, b in vals), len(vals))}
    if ap["contrasts"]:
        CA, CB = ({c["contrast"]: c for c in r["contrasts"]} for r in (ra, rb))
        ctl = [(CA[c]["controls"][ra["factors"][i]["id"]], CB[c]["controls"][rb["factors"][j]["id"]])
               for c in ap["contrasts"] for i, j in pairs_f]
        fac["controls"] = {"n": len(ctl), "agree": sum(a == b for a, b in ctl),
                           "raw": rate(sum(a == b for a, b in ctl), len(ctl))}
    out["factors"] = fac
    listed = {(o["base"], o["claim"]) for o in order}
    fa, fb = bms.further_of(ra, listed), bms.further_of(rb, listed)
    common = sorted(set(fa) & set(fb), key=lambda k: (num(k[1]), num(k[0])))
    same = [k for k in common if (fa[k]["type"], fa[k]["strength"]) == (fb[k]["type"], fb[k]["strength"])]
    out["further"] = {"a": len(fa), "b": len(fb), "both": len(common), "both_alike": len(same),
                      "both_pairs": [f"{c} on {b}" for b, c in common]}
    share = {}
    for m, R in (("a", A), ("b", B)):
        for src in ("candidate", "sample"):
            ids = [o["id"] for o in order if o["source"] == src]
            e = sum(R[i]["rests_on"] for i in ids)
            share[f"{m}_{src}"] = {"pairs": len(ids), "edges": e, "share": rate(e, len(ids))}
    out["share"] = share
    return out


# ---------------------------------------------------------------- F2 to F6

def f2(skey, settled):
    kinds = collections.Counter(it["kind"] for it in skey["items"])
    by = collections.defaultdict(collections.Counter)
    for it in skey["items"]:
        by[it["kind"]][settled["choices"][it["id"]]["choice"]] += 1
    total = collections.Counter(settled["choices"][it["id"]]["choice"] for it in skey["items"])
    return {"items": len(skey["items"]), "by_kind": dict(sorted(kinds.items())),
            "choices": {k: dict(sorted(v.items())) for k, v in sorted(by.items())}, "choices_total": dict(sorted(
                total.items())), "sheet_times": settled.get("times")}


def f3(paper, kp, rep, planted):
    E, passages = kp["elements"], kp["passages"]
    by = {p["reading"]: p for p in rep["placements"]}
    rows, totals, ties = [], collections.Counter(), collections.Counter()
    for r in kp["readings"]:
        p = by[r]
        kinds = collections.Counter(br2.kind_of(b["element"], kp) for b in p["bears_on"])
        tk = [br2.OFF if o["tie"] == br2.OFF else br2.kind_of(o["tie"], kp) for o in p["opening"]]
        ties.update(tk)
        totals.update(kinds)
        rows.append({"reading": r, "elements": [b["element"] for b in p["bears_on"]],
                     "by_kind": dict(sorted(kinds.items())), "evidence": list(p["evidence"]),
                     "off_map": not br2.is_none(p["off_map"]), "ties": tk})
    pl = []
    for x in planted:
        if x["paper"] != paper:
            continue
        els = [b["element"] for b in by[x["r"]]["bears_on"]]
        pl.append({"reading": x["r"], "written_to": {"claim": x["claim"], "type": x["type"]}, "elements": els,
                   "claim_placed": x["claim"] in els})
    return {"readings": rows, "elements_by_kind": dict(sorted(totals.items())),
            "elements": sum(totals.values()), "with_off_map": sum(r["off_map"] for r in rows),
            "with_evidence": sum(bool(r["evidence"]) for r in rows), "ties_by_kind": dict(sorted(ties.items())),
            "planted": pl}


def f4(paper, closure, codes, worth, core, planted):
    plant = {x["r"] for x in planted if x["paper"] == paper}
    core = set(core)
    rows = []
    tot = {c: collections.Counter() for c in CODERS}
    beyond = collections.Counter()
    for x in closure["readings"]:
        r = x["reading"]
        row = {"reading": r, "planted": r in plant, "worth": None if r in plant else worth.get(f"{paper}|{r}")}
        for c in CODERS:
            code = codes[c][f"{paper}|{r}"]
            labels = {k: v for k, v in x["coders"][c]["labels"].items() if k in core}
            row[c] = {"main_claim": code["main_claim"], "main_type": code["main_type"],
                      "core_labels": dict(sorted(labels.items(), key=lambda kv: num(kv[0])))}
            tot[c].update(labels.values())
            beyond[c] += any(v != "contested" for v in labels.values())
        rows.append(row)
    return {"readings": rows, "labels_on_core": {c: {l: tot[c][l] for l in LABELS} for c in CODERS},
            "readings_with_a_label_besides_contested": dict(beyond)}


def f5(rep):
    rows = [{"reading": c["reading"], "faithful": c["faithful"]} for c in rep["checks"]]
    return {"readings": rows, "faithful": sum(r["faithful"] for r in rows),
            "not": sum(not r["faithful"] for r in rows)}


def f6(answers):
    out = {}
    for q in ("q1", "q2"):
        allc = collections.Counter(t[q + "_pick"] for t in answers["tabs"])
        per = {p: collections.Counter(t[q + "_pick"] for t in answers["tabs"] if t["paper"] == p) for p in PAPERS}
        key = (lambda k: "unanswered" if k is None else k)
        out[q] = {"all": {key(k): allc[k] for k in PICKS},
                  "by_paper": {p: {key(k): per[p][k] for k in PICKS} for p in PAPERS}}
    out["notes"] = [{"tab": t["tab"], "note": t["note"]} for t in answers["tabs"] if t["note"]]
    out["tabs"] = [{"tab": t["tab"], "q1": t["q1_pick"], "q2": t["q2_pick"]} for t in answers["tabs"]]
    return out


def minutes(start, end):
    """hh:mm to hh:mm, in minutes, or None."""
    try:
        h1, m1 = (int(x) for x in str(start).strip().split(":")[:2])
        h2, m2 = (int(x) for x in str(end).strip().split(":")[:2])
    except (ValueError, AttributeError):
        return None
    d = (h2 * 60 + m2) - (h1 * 60 + m1)
    return d if d >= 0 else d + 24 * 60


def f7(times, answers):
    steps = [{"step": s["step"], "chat_minutes": s.get("chat_minutes") or {},
              "pi_minutes": s.get("pi_minutes"), "pi_minutes_at_least": s.get("pi_minutes_at_least")}
             for s in times["steps"]]
    return {"steps": steps, "comparison_sheet": {"start": answers.get("start"), "end": answers.get("end"),
                                                 "minutes": minutes(answers.get("start"), answers.get("end"))}}


# ---------------------------------------------------------------- the inputs

def read(name, folder):
    data = open(os.path.join(folder, name), "rb").read()
    return data, json.loads(data)


def need(cond, what):
    if not cond:
        raise SystemExit(f"refused: {what}")


def load(folder=None):
    folder = folder or HERE
    raw, j = {}, {}
    names = ["map_key.json", "relation_key.json", "relation_results.json", "map_round2_key.json",
             "map_openings_key.json", "map_comparison_key.json", "map_comparison_answers.json", "map_times.json"]
    for p in PAPERS:
        names += [f"map_settle_key_{p}.json", f"map_settled_{p}.json", f"map_closure_{p}.json", *CHATS[p]["map"],
                  CHATS[p]["place"], CHATS[p]["check"]]
    for n in names:
        raw[n], j[n] = read(n, folder)
    h = {n: sha_bytes(d) for n, d in raw.items()}
    r2 = j["map_round2_key.json"]
    for p in PAPERS:
        sk, se, cl = j[f"map_settle_key_{p}.json"], j[f"map_settled_{p}.json"], j[f"map_closure_{p}.json"]
        a, b = CHATS[p]["map"]
        need(sk["inputs"]["reply_a"] == h[a] and sk["inputs"]["reply_b"] == h[b], f"{p}: the map replies are not the "
                                                                                    f"settle key's")
        need(sk["inputs"]["map_key"] == h["map_key.json"], f"{p}: map_key.json is not the settle key's")
        need(se["inputs"]["settle_key"] == h[f"map_settle_key_{p}.json"], f"{p}: the settle key is not the settled "
                                                                             f"map's")
        need(cl["inputs"]["settled"] == h[f"map_settled_{p}.json"] and cl["inputs"]["results"] ==
             h["relation_results.json"], f"{p}: the closure is not of the settled map and T37's results")
        need(r2["inputs"][f"map_settled_{p}.json"] == h[f"map_settled_{p}.json"] and
             r2["inputs"][f"map_closure_{p}.json"] == h[f"map_closure_{p}.json"], f"{p}: not the round 2 key's maps")
        need(j["map_openings_key.json"]["papers"][p]["reply_sha256"] == h[CHATS[p]["place"]] and
             j["map_comparison_key.json"]["replies"][p] == h[CHATS[p]["place"]], f"{p}: the placement reply is not "
                                                                                   f"the one the openings and the "
                                                                                   f"comparison were built from")
    for n in ("relation_key.json", "relation_results.json"):
        need(r2["inputs"][n] == h[n], f"{n} is not the round 2 key's")
    need(j["map_openings_key.json"]["round2_key_sha256"] == h["map_round2_key.json"] and
         j["map_comparison_key.json"]["round2_key_sha256"] == h["map_round2_key.json"],
         "the openings' or the comparison's key is not of this round 2 key")
    need(j["map_comparison_answers.json"]["comparison_key_sha256"] == h["map_comparison_key.json"],
         "the PI's answers are not of this comparison key")
    return folder, raw, j, h


def reply_of(folder, check, *args):
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code, rep = check(*args)
    if code != 0:
        raise SystemExit(f"refused: {args[-1]} does not count with no long quoted span (exit {code})")
    return rep


def score(outdir, folder=None):
    real = folder is None
    folder, raw, j, h = load(folder)
    bms.refuse_existing(outdir, ["MAP_RESULTS.md", "map_results.json"])
    mkey, r2 = j["map_key.json"], j["map_round2_key.json"]
    codes, worth = j["relation_results.json"]["codes"], j["relation_results.json"]["worth"]
    planted = j["relation_key.json"]["planted"]
    res = {"what": "The results of the map test (T39), by score_map_test.py: every measure of MAP_TEST_PLAN.md's part "
                   "F, described, not tested.",
           "scorer_sha256": sha_bytes(open(os.path.abspath(__file__), "rb").read()),
           "inputs": dict(sorted(h.items())), "papers": {}}
    for p in PAPERS:
        index = bmt.load_index(p, None if real else folder)[0]
        a, b = CHATS[p]["map"]
        ra = bms.read_reply(p, mkey, os.path.join(folder, a), index)
        rb = bms.read_reply(p, mkey, os.path.join(folder, b), index)
        place = reply_of(folder, br2.check_placement, p, os.path.join(folder, "map_round2_key.json"),
                         os.path.join(folder, CHATS[p]["place"]))
        chk = reply_of(folder, br2.check_openings, p, os.path.join(folder, "map_openings_key.json"),
                       os.path.join(folder, CHATS[p]["check"]))
        kp = r2["papers"][p]
        res["papers"][p] = {"F1": f1(p, mkey, index, ra, rb),
                            "F2": f2(j[f"map_settle_key_{p}.json"], j[f"map_settled_{p}.json"]),
                            "F3": f3(p, kp, place, planted),
                            "F4": f4(p, j[f"map_closure_{p}.json"], codes, worth, kp["core"], planted),
                            "F5": f5(chk)}
    res["F6"] = f6(j["map_comparison_answers.json"])
    res["F7"] = f7(j["map_times.json"], j["map_comparison_answers.json"])
    data = bms.dumps(res)
    bmt.write_new(os.path.join(outdir, "map_results.json"), data)
    bmt.write_new(os.path.join(outdir, "MAP_RESULTS.md"), results_md(res))
    return res


# ---------------------------------------------------------------- the page

def fmt(x):
    return "none" if x is None else str(x)


def results_md(res):
    L = ["# The map test (T39): results", "",
         "Every measure of `MAP_TEST_PLAN.md`'s part F, described, not tested, as `score_map_test.py` wrote them "
         "(its sha256 opens " + res["scorer_sha256"][:8] + "). Map A is the Opus map, map B the GPT 6 map; the first "
         "coder is T37's Google coder, the second its OpenAI coder.", ""]
    for p in PAPERS:
        x = res["papers"][p]
        F1 = x["F1"]
        li = F1["listed"]
        L += [f"## {p.capitalize()}", "", "### F1, the maps' agreement, on the maps as built", "",
              f"- **Listed pairs ({li['n']}):** an edge in both {li['both']}, in A only {li['a_only']}, in B only "
              f"{li['b_only']}, in neither {li['neither']}; raw agreement {fmt(li['raw'])}, kappa {fmt(li['kappa'])}, "
              f"positive agreement {fmt(li['positive'])}."]
        for part in ("type", "strength"):
            a = F1[part]
            L.append(f"- **The {part}, on the {a['n']} pairs both call edges:** agree {a['agree']}, raw "
                     f"{fmt(a['raw'])}, kappa {fmt(a['kappa'])}.")
            cats = list(a["confusion"])
            L += ["", "| map A \\ map B | " + " | ".join(cats) + " |", "|---|" + "---|" * len(cats)]
            L += [f"| {r} | " + " | ".join(str(a["confusion"][r][c]) for c in cats) + " |" for r in cats]
            L.append("")
        g = F1["registry"]
        L.append(f"- **The registries,** over the {g['pairs']} pairs of the {g['names']} construct names: together in "
                 f"A {g['together_a']}, in B {g['together_b']}, in both {g['together_both']}; positive agreement "
                 f"{fmt(g['positive'])}, raw {fmt(g['raw'])}.")
        f = F1["factors"]
        s = (f"- **The factors:** A {f['a']}, B {f['b']}, paired by their claims {f['paired']}; A's unpaired "
             f"{', '.join(f['a_unpaired']) or 'none'}, B's {', '.join(f['b_unpaired']) or 'none'}")
        for k in ("outcomes", "values", "controls"):
            if k in f:
                s += f"; {k.replace('values', 'unit values').replace('outcomes', 'unit outcomes')}, agree " \
                     f"{f[k]['agree']} of {f[k]['n']} ({fmt(f[k]['raw'])})"
        L.append(s + ".")
        fu = F1["further"]
        L.append(f"- **Further edges:** A {fu['a']}, B {fu['b']}, both {fu['both']} "
                 f"({', '.join(fu['both_pairs']) or 'none'}), of which alike in type and strength {fu['both_alike']}.")
        sh = F1["share"]
        L.append(f"- **Edges among the candidates and the sampled pairs:** A {sh['a_candidate']['edges']} of "
                 f"{sh['a_candidate']['pairs']} ({fmt(sh['a_candidate']['share'])}) and {sh['a_sample']['edges']} of "
                 f"{sh['a_sample']['pairs']} ({fmt(sh['a_sample']['share'])}); B {sh['b_candidate']['edges']} of "
                 f"{sh['b_candidate']['pairs']} ({fmt(sh['b_candidate']['share'])}) and {sh['b_sample']['edges']} of "
                 f"{sh['b_sample']['pairs']} ({fmt(sh['b_sample']['share'])}).")
        F2 = x["F2"]
        L += ["", "### F2, the PI's settling", "",
              f"- **{F2['items']} items:** " + "; ".join(f"{k} {v}" for k, v in F2["by_kind"].items()) + ".",
              "- **The PI's choices:** " + "; ".join(f"{k}: " + ", ".join(f"{c} {n}" for c, n in v.items())
                                               for k, v in F2["choices"].items()) +
              f"; in all " + ", ".join(f"{c} {n}" for c, n in F2["choices_total"].items()) + ".", ""]
        F3 = x["F3"]
        L += ["### F3, the placement", "",
              f"- **Elements placed:** {F3['elements']}, by kind " +
              "; ".join(f"{k} {v}" for k, v in F3["elements_by_kind"].items()) +
              f"; readings with something off the map {F3['with_off_map']} of {len(F3['readings'])}; with evidence "
              f"{F3['with_evidence']}; the openings' ties, by kind " +
              "; ".join(f"{k} {v}" for k, v in F3["ties_by_kind"].items()) + "."]
        for pl in F3["planted"]:
            L.append(f"- **Planted {pl['reading']}** (written to {pl['written_to']['claim']}, "
                     f"{pl['written_to']['type']}): placed on {', '.join(pl['elements']) or 'nothing'}; its claim "
                     f"{'among them' if pl['claim_placed'] else 'not among them'}.")
        L += ["", "| reading | elements | evidence | off the map | ties |", "|---|---|---|---|---|"]
        for r in F3["readings"]:
            L.append(f"| {r['reading']} | {', '.join(r['elements']) or 'none'} | {', '.join(r['evidence']) or 'none'} |"
                     f" {'yes' if r['off_map'] else 'no'} | {', '.join(r['ties'])} |")
        F4 = x["F4"]
        L += ["", "### F4, the typed effects", ""]
        for c in CODERS:
            who = "the first coder" if c == "gemini" else "the second coder"
            L.append(f"- **Labels on core claims, under {who}'s codes:** " +
                     "; ".join(f"{l} {n}" for l, n in F4["labels_on_core"][c].items()) +
                     f"; readings with a label on a core claim besides contested "
                     f"{F4['readings_with_a_label_besides_contested'].get(c, 0)}.")
        L += ["", "| reading | worth | first coder: main | labels | second coder: main | labels |",
              "|---|---|---|---|---|---|"]
        for r in F4["readings"]:
            cells = []
            for c in CODERS:
                cells.append(f"{r[c]['main_claim']} {r[c]['main_type']}")
                cells.append(", ".join(f"{k} {v}" for k, v in r[c]["core_labels"].items()) or "none")
            L.append(f"| {r['reading']}{' (planted)' if r['planted'] else ''} | {fmt(r['worth'])} | " +
                     " | ".join(cells) + " |")
        F5 = x["F5"]
        L += ["", "### F5, the openings' check", "",
              f"- **Faithful** {F5['faithful']}, **not** {F5['not']}: not faithful " +
              (", ".join(r["reading"] for r in F5["readings"] if not r["faithful"]) or "none") + ".", ""]
    F6 = res["F6"]
    L += ["## F6, the PI's comparison", ""]
    for q, text in zip(("q1", "q2"), br2.QUESTIONS):
        a = F6[q]["all"]
        L.append(f"- **{text}** " + "; ".join(f"{k} {v}" for k, v in a.items()) + " (" + "; ".join(
            f"{p.capitalize()}: " + ", ".join(f"{k} {v}" for k, v in F6[q]["by_paper"][p].items()) for p in PAPERS)
                 + ").")
    L += ["", "| tab | question 1 | question 2 |", "|---|---|---|"]
    L += [f"| {t['tab']} | {t['q1'] or 'unanswered'} | {t['q2'] or 'unanswered'} |" for t in F6["tabs"]]
    if F6["notes"]:
        L += ["", "The PI's notes:", ""] + [f"- **{n['tab']}:** {n['note']}" for n in F6["notes"]]
    F7 = res["F7"]
    L += ["", "## F7, the cost", ""]
    for s in F7["steps"]:
        bits = []
        if s["chat_minutes"]:
            bits.append("chats " + ", ".join(f"{k} {fmt(v)}" for k, v in s["chat_minutes"].items()) + " minutes")
        if s["pi_minutes"] is not None:
            bits.append(f"the PI's minutes {s['pi_minutes']}")
        if s["pi_minutes_at_least"] is not None:
            bits.append(f"the PI's minutes at least {s['pi_minutes_at_least']}")
        L.append(f"- **{s['step']}:** {'; '.join(bits) or 'no minutes'}.")
    cs = F7["comparison_sheet"]
    L.append(f"- **The PI's comparison sheet's cells:** start {fmt(cs['start'])}, end {fmt(cs['end'])}, minutes "
             f"{fmt(cs['minutes'])}.")
    L += ["", "## The inputs", ""] + [f"- `{n}`: {s[:16]}…" for n, s in res["inputs"].items()] + [""]
    return "\n".join(L).encode("utf-8")


# ---------------------------------------------------------------- self-test

def selftest():
    import shutil
    import tempfile
    n_ok = n_bad = 0

    def expect(label, cond):
        nonlocal n_ok, n_bad
        if cond:
            n_ok += 1
        else:
            n_bad += 1
            print(f"FAIL: {label}")

    expect("kappa: a worked case", kappa([(True, True), (True, False), (False, False), (False, False)],
                                         (True, False)) == 0.5)
    expect("kappa: none when expected agreement is one", kappa([(True, True), (True, True)], (True, False)) is None)
    expect("kappa: none on no pairs", kappa([], (True, False)) is None)
    expect("rate: none on a zero denominator, three decimals", rate(1, 0) is None and rate(2, 3) == 0.667)
    index = bmt.made_up_index("bechky")
    mkey = {"papers": {"bechky": {
        "order": [{"id": "P001", "base": "C02", "claim": "C01", "source": "candidate"},
                  {"id": "P002", "base": "C03", "claim": "C01", "source": "candidate"},
                  {"id": "P003", "base": "C06", "claim": "C04", "source": "sample"},
                  {"id": "P004", "base": "C02", "claim": "C05", "source": "sample"},
                  {"id": "P005", "base": "C03", "claim": "C04", "source": "sample"}],
        "applies": {"table": True, "units": [{"unit": "ward A", "claim": "C02"}, {"unit": "ward B", "claim": "C03"}],
                    "contrasts": ["CP01"], "factors": True}}}}

    def pr(i, base, claim, t=None, s=None):
        return {"pair": i, "base": base, "claim": claim, "rests_on": t is not None, "type": t, "strength": s}
    fe = {"type": "evidential", "strength": "contributing", "basis": "b", "page": "p. 1", "reason": "r"}
    ra = {"pairs": [pr("P001", "C02", "C01", "evidential", "contributing"),
                    pr("P002", "C03", "C01", "evidential", "necessary"), pr("P003", "C06", "C04"),
                    pr("P004", "C02", "C05", "mechanistic", "contributing"), pr("P005", "C03", "C04")],
          "further_edges": [dict(fe, base="C04", claim="C01"), dict(fe, base="C02", claim="C01"),
                            dict(fe, base="C06", claim="C05", strength="necessary")],
          "registry": [{"canonical": "ward", "names": ["ward A", "ward B"]}],
          "factors": [{"id": "X1", "name": "endorsement", "claim": "C01"}, {"id": "X2", "name": "budget", "claim": "C06"}],
          "units": [{"unit": "ward A", "outcome": "+", "values": {"X1": "+", "X2": "?"}},
                    {"unit": "ward B", "outcome": "-", "values": {"X1": "-", "X2": "?"}}],
          "contrasts": [{"contrast": "CP01", "controls": {"X1": "varies", "X2": "held"}}]}
    rb = {"pairs": [pr("P001", "C02", "C01", "evidential", "contributing"),
                    pr("P002", "C03", "C01", "mechanistic", "necessary"),
                    pr("P003", "C06", "C04", "comparative", "necessary"), pr("P004", "C02", "C05"),
                    pr("P005", "C03", "C04")],
          "further_edges": [dict(fe, base="C04", claim="C01"), dict(fe, base="C06", claim="C05")],
          "registry": [{"canonical": "ward", "names": ["ward A", "ward B", "identity"]}],
          "factors": [{"id": "F1", "name": "endorsement", "claim": "C01"}, {"id": "F2", "name": "identity",
                                                                             "claim": "C05"}],
          "units": [{"unit": "ward A", "outcome": "+", "values": {"F1": "\u2212", "F2": "+"}},
                    {"unit": "ward B", "outcome": "\u2212", "values": {"F1": "\u2013", "F2": "?"}}],
          "contrasts": [{"contrast": "CP01", "controls": {"F1": "varies", "F2": "unclear"}}]}
    x = f1("bechky", mkey, index, ra, rb)
    li = x["listed"]
    expect("F1: the listed pairs", (li["n"], li["both"], li["a_only"], li["b_only"], li["neither"]) == (5, 2, 1, 1, 1)
           and li["raw"] == 0.6 and li["kappa"] == 0.167 and li["positive"] == 0.667)
    expect("F1: the type on the pairs both call edges", x["type"]["n"] == 2 and x["type"]["agree"] == 1 and
           x["type"]["kappa"] == 0.0 and x["type"]["confusion"]["evidential"]["mechanistic"] == 1 and
           x["type"]["confusion"]["evidential"]["evidential"] == 1)
    expect("F1: the strength", x["strength"]["agree"] == 2 and x["strength"]["kappa"] == 1.0)
    g = x["registry"]
    expect("F1: the registries", (g["names"], g["pairs"], g["together_a"], g["together_b"], g["together_both"]) ==
           (6, 15, 1, 3, 1) and g["positive"] == 0.5 and g["raw"] == 0.867)
    f = x["factors"]
    expect("F1: the factors paired by claim", f["paired"] == 1 and f["a_unpaired"] == ["C06"] and
           f["b_unpaired"] == ["C05"])
    expect("F1: the unit outcomes and values, signs read", f["outcomes"] == {"n": 2, "agree": 2, "raw": 1.0} and
           f["values"] == {"n": 2, "agree": 1, "raw": 0.5})
    expect("F1: the controls", f["controls"] == {"n": 1, "agree": 1, "raw": 1.0})
    expect("F1: the further edges, a listed pair left aside", x["further"] == {
        "a": 2, "b": 2, "both": 2, "both_alike": 1, "both_pairs": ["C01 on C04", "C05 on C06"]})
    expect("F1: the shares by source", x["share"]["a_candidate"] == {"pairs": 2, "edges": 2, "share": 1.0} and
           x["share"]["a_sample"] == {"pairs": 3, "edges": 1, "share": 0.333} and
           x["share"]["b_sample"] == {"pairs": 3, "edges": 1, "share": 0.333})
    skey = {"items": [{"id": "S001", "kind": "pair-edge"}, {"id": "S002", "kind": "pair-type"},
                      {"id": "S003", "kind": "constructs"}, {"id": "S004", "kind": "pair-edge"}]}
    settled = {"choices": {"S001": {"choice": "A"}, "S002": {"choice": "own"}, "S003": {"choice": "B"},
                           "S004": {"choice": "A"}}, "times": {"start": None, "end": None}}
    y = f2(skey, settled)
    expect("F2: items and choices by kind", y["items"] == 4 and y["by_kind"] == {"constructs": 1, "pair-edge": 2,
                                                                                 "pair-type": 1} and
           y["choices"]["pair-edge"] == {"A": 2} and y["choices"]["pair-type"] == {"own": 1} and
           y["choices"]["constructs"] == {"B": 1} and y["choices_total"] == {"A": 2, "B": 1, "own": 1})
    kp = {"elements": {"C01": {"kind": "claim"}, "E01": {"kind": "edge"}, "K01": {"kind": "construct"}},
          "passages": {"F01": "p. 1", "F02": None}, "readings": ["R01", "R02"], "core": ["C01"]}
    rep = {"placements": [
        {"reading": "R01", "bears_on": [{"element": "C01", "how": "h"}, {"element": "E01", "how": "h"},
                                        {"element": "F02", "how": "h"}], "evidence": ["F01"], "off_map": "None.",
         "opening": [{"sentence": "s", "tie": "C01"}, {"sentence": "s", "tie": br2.OFF}]},
        {"reading": "R02", "bears_on": [], "evidence": [], "off_map": "the nurses",
         "opening": [{"sentence": "s", "tie": br2.OFF}, {"sentence": "s", "tie": "K01"}]}]}
    planted = [{"paper": "bechky", "r": "R02", "claim": "C01", "type": "inverts"},
               {"paper": "pratt", "r": "R01", "claim": "C02", "type": "restates"}]
    z = f3("bechky", kp, rep, planted + [{"paper": "bechky", "r": "R01", "claim": "C04", "type": "restates"}])
    expect("F3: the totals", z["elements"] == 3 and z["elements_by_kind"] == {"claim": 1, "edge": 1, "passage": 1} and
           z["with_off_map"] == 1 and z["with_evidence"] == 1 and
           z["ties_by_kind"] == {"claim": 1, "construct": 1, br2.OFF: 2})
    expect("F3: a planted reading beside its claim", z["planted"] == [
        {"reading": "R02", "written_to": {"claim": "C01", "type": "inverts"}, "elements": [], "claim_placed": False},
        {"reading": "R01", "written_to": {"claim": "C04", "type": "restates"}, "elements": ["C01", "E01", "F02"],
         "claim_placed": False}])
    closure = {"readings": [{"reading": "R01", "coders": {"gemini": {"labels": {"C01": "contested", "C02": "contested",
                                                                                "C05": "weakened"}},
                                                          "astra": {"labels": {"C01": "idle"}}}},
                            {"reading": "R02", "coders": {"gemini": {"labels": {}},
                                                          "astra": {"labels": {"C04": "unsupported"}}}},
                            {"reading": "R03", "coders": {"gemini": {"labels": {"C01": "contested", "C02": "idle"}},
                                                          "astra": {"labels": {}}}}]}
    codes = {c: {f"bechky|{r}": {"main_claim": "C01", "main_type": "inverts"} for r in ("R01", "R02", "R03")}
             for c in CODERS}
    w = f4("bechky", closure, codes, {"bechky|R01": 2, "bechky|R02": 3}, ["C01", "C04", "C05"], planted)
    expect("F4: the labels on core claims only, by coder, with worth",
           w["readings"][0]["gemini"]["core_labels"] == {"C01": "contested", "C05": "weakened"} and
           w["readings"][0]["worth"] == 2 and w["readings"][1]["worth"] is None and w["readings"][1]["planted"])
    expect("F4: the totals", w["labels_on_core"]["gemini"]["weakened"] == 1 and
           w["labels_on_core"]["gemini"]["contested"] == 2 and w["labels_on_core"]["astra"]["unsupported"] == 1 and
           w["readings_with_a_label_besides_contested"] == {"gemini": 1, "astra": 2})
    v = f5({"checks": [{"reading": "R01", "faithful": True}, {"reading": "R02", "faithful": False}]})
    expect("F5: the counts", v["faithful"] == 1 and v["not"] == 1)
    answers = {"start": "20:00", "end": "21:15",
               "tabs": [{"tab": "Bechky R01", "paper": "bechky", "q1_pick": "map", "q2_pick": "T37", "note": "n"},
                        {"tab": "Pratt R02", "paper": "pratt", "q1_pick": None, "q2_pick": "the same", "note": None}]}
    u = f6(answers)
    expect("F6: the picks, unanswered counted", u["q1"]["all"] == {"T37": 0, "map": 1, "the same": 0, "neither": 0,
                                                                   "unanswered": 1} and
           u["q2"]["by_paper"]["pratt"]["the same"] == 1 and u["notes"] == [{"tab": "Bechky R01", "note": "n"}])
    expect("minutes: across the hour, across midnight, unreadable", minutes("20:00", "21:15") == 75 and
           minutes("23:30", "00:10") == 40 and minutes("", "21:00") is None and minutes(None, None) is None)
    times = {"steps": [{"step": "settling", "pi_minutes_at_least": 120}]}
    s7 = f7(times, answers)
    expect("F7: the steps and the sheet's minutes", s7["steps"][0]["pi_minutes_at_least"] == 120 and
           s7["steps"][0]["chat_minutes"] == {} and s7["comparison_sheet"]["minutes"] == 75)
    res = {"scorer_sha256": "0" * 64, "inputs": {"a.json": "1" * 64},
           "papers": {p: {"F1": x, "F2": y, "F3": z, "F4": w, "F5": v} for p in PAPERS}, "F6": u, "F7": s7}
    page = results_md(res).decode("utf-8")
    expect("the page: F1 to F7 and the inputs", all(s in page for s in (
        "## Bechky", "## Pratt", "an edge in both 2, in A only 1, in B only 1, in neither 1; raw agreement 0.6, kappa "
        "0.167", "| evidential | 1 | 1 | 0 | 0 |", "in both 1; positive agreement 0.5",
        "both 2 (C01 on C04, C05 on C06), of which alike in type and strength 1",
        "**Planted R02** (written to C01, inverts): placed on nothing; its claim not among them",
        "| R02 (planted) | none |", "**Faithful** 1, **not** 1: not faithful R02", "map 1",
        "the PI's minutes at least 120", "minutes 75", "- `a.json`: 1111111111111111", "| Pratt R02 | unanswered | the same |")))
    # the hash chain
    tmp = tempfile.mkdtemp()
    try:
        def put(name, obj):
            data = json.dumps(obj).encode("utf-8")
            open(os.path.join(tmp, name), "wb").write(data)
            return sha_bytes(data)
        h = {}
        for p in PAPERS:
            for n in CHATS[p]["map"] + (CHATS[p]["place"], CHATS[p]["check"]):
                h[n] = put(n, {"reply": n})
        for n in ("map_key.json", "relation_key.json", "relation_results.json", "map_times.json"):
            h[n] = put(n, {"file": n})
        inputs2 = {"relation_key.json": h["relation_key.json"], "relation_results.json": h["relation_results.json"]}
        for p in PAPERS:
            a, b = CHATS[p]["map"]
            h[f"map_settle_key_{p}.json"] = put(f"map_settle_key_{p}.json", {"inputs": {
                "reply_a": h[a], "reply_b": h[b], "map_key": h["map_key.json"]}})
            h[f"map_settled_{p}.json"] = put(f"map_settled_{p}.json", {"inputs": {
                "settle_key": h[f"map_settle_key_{p}.json"]}})
            h[f"map_closure_{p}.json"] = put(f"map_closure_{p}.json", {"inputs": {
                "settled": h[f"map_settled_{p}.json"], "results": h["relation_results.json"]}})
            inputs2[f"map_settled_{p}.json"] = h[f"map_settled_{p}.json"]
            inputs2[f"map_closure_{p}.json"] = h[f"map_closure_{p}.json"]
        h["map_round2_key.json"] = put("map_round2_key.json", {"inputs": inputs2})
        h["map_openings_key.json"] = put("map_openings_key.json", {
            "round2_key_sha256": h["map_round2_key.json"],
            "papers": {p: {"reply_sha256": h[CHATS[p]["place"]]} for p in PAPERS}})
        h["map_comparison_key.json"] = put("map_comparison_key.json", {
            "round2_key_sha256": h["map_round2_key.json"], "replies": {p: h[CHATS[p]["place"]] for p in PAPERS}})
        put("map_comparison_answers.json", {"comparison_key_sha256": h["map_comparison_key.json"]})

        def loads():
            try:
                load(tmp)
                return "ok"
            except SystemExit as e:
                return str(e)
        expect("inputs: a consistent chain loads", loads() == "ok")
        for name, want in (("reply_74_bechky_map_gpt6.json", "bechky: the map replies"),
                           ("map_settle_key_pratt.json", "pratt: the settle key is not"),
                           ("relation_results.json", "the closure is not of"),
                           ("reply_78_pratt_place_argon.json", "pratt: the placement reply"),
                           ("map_round2_key.json", "not of this round 2 key"),
                           ("map_comparison_key.json", "the PI's answers are not"),
                           ("map_key.json", "map_key.json is not the settle key's")):
            keep = open(os.path.join(tmp, name), "rb").read()
            open(os.path.join(tmp, name), "wb").write(keep + b" ")
            expect(f"inputs: a changed {name} is refused", want in loads())
            open(os.path.join(tmp, name), "wb").write(keep)
        expect("inputs: the chain loads again", loads() == "ok")
    finally:
        shutil.rmtree(tmp)
    print(f"self-test: {n_ok} checks pass, {n_bad} fail")
    return 1 if n_bad else 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if argv[:1] == ["score"] and len(argv) == 2:
        score(argv[1])
        return 0
    raise SystemExit(__doc__)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
