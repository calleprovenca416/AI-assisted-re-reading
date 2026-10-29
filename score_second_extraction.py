"""
Score the second extraction of Bechky (T35), by SECOND_EXTRACTION_PLAN.md. Written
on 15 Oct 2026, before the new return was opened.

    python3 -B score_second_extraction.py selftest
    python3 -B score_second_extraction.py check --key=two_lists_key.json REPLY
    python3 -B score_second_extraction.py score --key=two_lists_key.json --a=REPLY_56 --b=REPLY_57
        --out=DIR

check: whether one matcher's reply counts, as the plan's "Checks on the
replies" says: one JSON object (from its first "{" to its last "}"), with the
keys `claims` and `passages` and no others; `claims` with one entry for every
claim of both lists and `passages` one for every passage, each id exactly once
as a key (a key given twice is a fault) and no other key; each entry a list of
ids, all of them items of the same kind in the other list. Prints the faults,
if any, and exits 1 when there are some. A counterpart named twice in one entry
is not a fault; it is listed.

score: every figure of the plan, written to DIR/SECOND_EXTRACTION_RESULTS.md and
DIR/second_extraction_results.json, from the key built by build_two_lists.py and
the two replies: a, chat 56 (Opus 5.5 at Extra); b, chat 57 (GPT 6 Astra at
max). A reply that fails its check is named, and every figure that needs it is
given as not decided.

A matcher's pairs: every pair of an item of P and an item of Q that it names in
either direction. Pairs named in one direction only are counted and listed. An
item is found when it is in at least one pair: under a matcher, under both
(found by each, not necessarily with the same counterpart) and under either.

Found again: of the first return's items, the share found (f), and of the new
return's items, the share found (s). Claims; the first return's core claims;
passages, all, outside the tables (a passage whose location names no table) and
the table cells; passages by their voice, in each return.

Kappas. Cohen's kappa on two lists of 0s and 1s, not computed (None) only when
both lists are all 0 or both all 1, where chance agreement is 1; when one list
alone holds a single value, kappa is 0 or below. On items: whether each item of both lists is found,
matcher a against matcher b. On pairs: whether each candidate pair is named,
a against b; the candidate pairs are, for claims, every claim of P with every
claim of Q, and for passages every passage of P with every passage of Q that
are in the same table or share a page or have pages next to each other (a
location's pages as the key gives them). Outside the tables: items and
candidate pairs of passages that name no table. Voice: over the passage pairs
both matchers name, the voice code of the pair's passage of the first return
against that of its passage of the new return, compared as raw agreement and
as Cohen's kappa over the codes (None when both lists hold one and the same
code throughout); a passage in two pairs counts once in each.

The bootstrap: 2,000 resamples with the seed 20261018 (random.Random). In each
resample, in this order: the claims of P, the claims of Q, the passages of P
and the passages of Q are each drawn with replacement, as many as there are
(one draw of n indices each); then the voice pairs, as many as there are. The
kappas on items are computed on the drawn items; the kappas on pairs on the
candidate pairs formed among the drawn items (each drawn item of P with each
drawn item of Q; copies of P and Q items are always copies of different items);
voice on the drawn pairs. A kappa that cannot be computed in a resample is left
out of it, and the count left out is given. The 2.5th and 97.5th percentiles
are read from the sorted values by linear interpolation (position q(m - 1)).

The answers, as the plan fixes them, compared with the bars on values rounded
to six places. A case: 1, "repeat", if f and s are both at least 0.80; 2,
"repeat in part", if not, and both are at least 0.50; 3, "do not repeat",
otherwise. Q1 on the claims: the case under each matcher, and the answer the
lower of the two (the larger number); as a second reading the cases under both
and under either; not decided if the pair kappa on claims is below 0.60 or
cannot be computed. Q2 the same on the passages outside the tables, with their
pair kappa; and, as a second reading, on all passages with all candidate pairs.
Q3 on the voice kappa: at least 0.80, "as steady as two codings of one
extraction"; at least 0.60 and under 0.80, "less steady"; under 0.60, "not
steady"; not decided with fewer than 20 pairs, a kappa that cannot be
computed, or Q2 not decided.

Described, not tested: counts of claims (and core), passages, table cells and
voice codes in each return; on the claim pairs both matchers name, whether
stated_as and core agree; on each pair of a claim pair and a passage pair both
matchers name, whether each return links the passage to the claim and with
which direction; passages per page (the first page of each location) in each
return; named passage pairs more than one page apart (their pages known, the
same table or not), with a page unknown, outside the candidate pairs, and of a
table cell with a passage outside the tables.
"""
import collections
import hashlib
import json
import os
import random
import sys

SEED = 20261018
RESAMPLES = 2000
MATCHERS = (("a", "56", "Opus 5.5 at Extra"), ("b", "57", "GPT 6 Astra at max"))
CASES = {1: "repeat", 2: "repeat in part", 3: "do not repeat"}
VOICE_TWO_CODINGS = {"kappa": 0.865, "agree": 161, "n": 172}


# ---------------------------------------------------------------- reading files

def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_reply(path):
    """(object, faults, notes). The object is read from the first "{" to the last "}";
    text outside it is not a fault, and is quoted in a note."""
    text = open(path, encoding="utf-8").read()
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b < a:
        return None, ["no JSON object found"], []
    notes = []
    before, after = text[:a].strip(), text[b + 1:].strip()
    if before or after:
        notes.append(f"text outside the object: before it {before[:80]!r}, after it {after[:80]!r}")
    dups = []

    def hook(items):
        seen = set()
        for k, _ in items:
            if k in seen:
                dups.append(k)
            seen.add(k)
        return dict(items)
    try:
        obj = json.loads(text[a:b + 1], object_pairs_hook=hook)
    except json.JSONDecodeError as e:
        return None, [f"not one JSON object: {e}"], notes
    return obj, [f"the key {k!r} is given more than once" for k in sorted(set(dups))], notes


def check_reply(obj, key, load_faults=()):
    """(faults, notes, result). result: for claims and passages, the sorted pairs
    (P id, Q id) named in either direction, and those named in one direction only."""
    faults, notes = list(load_faults), []
    if not isinstance(obj, dict):
        return faults + ["not a JSON object"], notes, None
    extra = sorted(set(obj) - {"claims", "passages"})
    if extra:
        faults.append(f"keys other than claims and passages: {extra}")
    result = {}
    for kind in ("claims", "passages"):
        ids = key[kind]
        part = obj.get(kind)
        if not isinstance(part, dict):
            faults.append(f"`{kind}` is missing or not an object")
            continue
        missing = [i for i in sorted(ids) if i not in part]
        if missing:
            faults.append(f"`{kind}` has no entry for {len(missing)} ids: {missing[:12]}")
        unknown = sorted(set(part) - set(ids))
        if unknown:
            faults.append(f"`{kind}` has entries for {len(unknown)} ids not in the lists: {unknown[:12]}")
        from_p, from_q = set(), set()
        for i in sorted(part):
            if i not in ids:
                continue
            v = part[i]
            if not isinstance(v, list) or any(not isinstance(x, str) for x in v):
                faults.append(f"{i}: its entry is not a list of ids")
                continue
            other = "Q" if i[0] == "P" else "P"
            bad = [x for x in v if x not in ids or x[0] != other]
            if bad:
                faults.append(f"{i}: names what is not a {kind[:-1]} of list {other}: {bad[:6]}")
            if len(set(v)) != len(v):
                notes.append(f"{i}: names a counterpart more than once")
            for x in v:
                if x in ids and x[0] == other:
                    (from_p if i[0] == "P" else from_q).add((i, x) if i[0] == "P" else (x, i))
        result[kind] = {"pairs": sorted(from_p | from_q), "one_way": sorted(from_p ^ from_q),
                        "named_from_P": len(from_p), "named_from_Q": len(from_q)}
    if faults:
        return faults, notes, None
    return faults, notes, result


# ---------------------------------------------------------------- measures

def kappa_counts(n11, n10, n01, n00):
    n = n11 + n10 + n01 + n00
    if n == 0:
        return None
    a1, b1 = n11 + n10, n11 + n01          # how many 1s each list holds
    if (a1, b1) in ((0, 0), (n, n)):       # both lists all 0, or both all 1: chance agreement is 1
        return None
    p1, p2 = a1 / n, b1 / n
    po = (n11 + n00) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    return (po - pe) / (1 - pe)


def kappa(x, y):
    if len(x) != len(y):
        return None
    c = collections.Counter(zip(x, y))
    return kappa_counts(c[(1, 1)], c[(1, 0)], c[(0, 1)], c[(0, 0)])


def nominal_kappa(x, y):
    n = len(x)
    if n == 0 or n != len(y):
        return None
    cats = sorted(set(x) | set(y))
    po = sum(1 for a, b in zip(x, y) if a == b) / n
    pe = sum((x.count(c) / n) * (y.count(c) / n) for c in cats)
    if pe >= 1.0:
        return None
    return (po - pe) / (1 - pe)


def percentile(sorted_vals, q):
    if not sorted_vals:
        return None
    pos = q * (len(sorted_vals) - 1)
    lo = int(pos)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (pos - lo)


def r6(x):
    return None if x is None else round(x, 6)


def case_of(f, s):
    if f is None or s is None:
        return None
    if r6(f) >= 0.80 and r6(s) >= 0.80:
        return 1
    if r6(f) >= 0.50 and r6(s) >= 0.50:
        return 2
    return 3


def near(pa, pb):
    return bool(pa) and bool(pb) and any(abs(x - y) <= 1 for x in pa for y in pb)


def is_candidate(p, q):
    if p["table"] is not None and p["table"] == q["table"]:
        return True
    return near(p["pages"], q["pages"])


class Lists:
    """The items of the key, by list, kind and return."""

    def __init__(self, key):
        self.key = key
        self.C, self.F = key["claims"], key["passages"]
        self.PC = [i for i in self.C if i.startswith("PC")]
        self.QC = [i for i in self.C if i.startswith("QC")]
        self.PP = [i for i in self.F if i.startswith("PP")]
        self.QP = [i for i in self.F if i.startswith("QP")]
        self.claim_pairs = [(p, q) for p in self.PC for q in self.QC]
        self.cand_all = [(p, q) for p in self.PP for q in self.QP if is_candidate(self.F[p], self.F[q])]
        self.cand_out = [(p, q) for p, q in self.cand_all
                         if self.F[p]["table"] is None and self.F[q]["table"] is None]
        self.out_items = [i for i in self.PP + self.QP if self.F[i]["table"] is None]

    def of(self, kind, ret, pred=lambda v: True):
        d = self.C if kind == "claims" else self.F
        return [i for i, v in d.items() if v["return"] == ret and pred(v)]


def found_map(ids, pairs):
    f = dict.fromkeys(ids, 0)
    for p, q in pairs:
        if p in f:
            f[p] = 1
        if q in f:
            f[q] = 1
    return f


def share(items, found):
    return None if not items else sum(found[i] for i in items) / len(items)


def shares_for(items, F):
    """Shares under a, b, both and either; F holds each matcher's found map (or None)."""
    out = {"n": len(items)}
    for m in ("a", "b"):
        out[m] = share(items, F[m]) if F.get(m) is not None else None
    if F.get("a") is not None and F.get("b") is not None:
        both = {i: F["a"][i] * F["b"][i] for i in items}
        either = {i: max(F["a"][i], F["b"][i]) for i in items}
        out["both"], out["either"] = share(items, both), share(items, either)
        out["found"] = {m: sum(F[m][i] for i in items) for m in ("a", "b")}
        out["found"]["both"], out["found"]["either"] = sum(both.values()), sum(either.values())
    else:
        out["both"] = out["either"] = None
    return out


def pair_kappa(cands, sa, sb, wp=None, wq=None):
    c = collections.Counter()
    for p, q in cands:
        w = 1 if wp is None else wp.get(p, 0) * wq.get(q, 0)
        if w:
            c[(int((p, q) in sa), int((p, q) in sb))] += w
    return kappa_counts(c[(1, 1)], c[(1, 0)], c[(0, 1)], c[(0, 0)])


def item_kappa(items, fa, fb, weights=None):
    c = collections.Counter()
    for i in items:
        w = 1 if weights is None else weights.get(i, 0)
        if w:
            c[(fa[i], fb[i])] += w
    return kappa_counts(c[(1, 1)], c[(1, 0)], c[(0, 1)], c[(0, 0)])


KAPPAS = ("claims_items", "claims_pairs", "passages_out_items", "passages_out_pairs",
          "passages_all_items", "passages_all_pairs", "voice")


def all_kappas(L, R, vpairs, w=None, vdraw=None):
    """Every kappa of the plan on the lists (w None) or on one resample (w: weights by id)."""
    sa = {k: set(map(tuple, R["a"][k]["pairs"])) for k in ("claims", "passages")}
    sb = {k: set(map(tuple, R["b"][k]["pairs"])) for k in ("claims", "passages")}
    fa = {**found_map(L.PC + L.QC, sa["claims"]), **found_map(L.PP + L.QP, sa["passages"])}
    fb = {**found_map(L.PC + L.QC, sb["claims"]), **found_map(L.PP + L.QP, sb["passages"])}
    wp = wq = w
    out = {"claims_items": item_kappa(L.PC + L.QC, fa, fb, w),
           "claims_pairs": pair_kappa(L.claim_pairs, sa["claims"], sb["claims"], wp, wq),
           "passages_out_items": item_kappa(L.out_items, fa, fb, w),
           "passages_out_pairs": pair_kappa(L.cand_out, sa["passages"], sb["passages"], wp, wq),
           "passages_all_items": item_kappa(L.PP + L.QP, fa, fb, w),
           "passages_all_pairs": pair_kappa(L.cand_all, sa["passages"], sb["passages"], wp, wq)}
    vp = vpairs if vdraw is None else vdraw
    out["voice"] = nominal_kappa([x for x, _ in vp], [y for _, y in vp]) if vp else None
    return out


def bootstrap(L, R, vpairs, seed=SEED, resamples=RESAMPLES):
    rng = random.Random(seed)
    vals = {k: [] for k in KAPPAS}
    left = dict.fromkeys(KAPPAS, 0)
    for _ in range(resamples):
        w = collections.Counter()
        for group in (L.PC, L.QC, L.PP, L.QP):
            n = len(group)
            for _ in range(n):
                w[group[rng.randrange(n)]] += 1
        nv = len(vpairs)
        vdraw = [vpairs[rng.randrange(nv)] for _ in range(nv)] if nv else []
        k = all_kappas(L, R, vpairs, w, vdraw)
        for name in KAPPAS:
            if k[name] is None:
                left[name] += 1
            else:
                vals[name].append(k[name])
    out = {}
    for name in KAPPAS:
        s = sorted(vals[name])
        out[name] = {"low": percentile(s, 0.025), "high": percentile(s, 0.975), "left_out": left[name],
                     "resamples": resamples}
    return out


def voice_pairs(L, both_pairs):
    """(first-return code, new-return code) for each passage pair both matchers name."""
    out = []
    for p, q in both_pairs:
        a, b = L.F[p], L.F[q]
        first, new = (a, b) if a["return"] == "first" else (b, a)
        out.append((first["voice"], new["voice"]))
    return out


def answer(f_s_a, f_s_b, f_s_both, f_s_either, pk, name):
    ca, cb = case_of(*f_s_a), case_of(*f_s_b)
    res = {"case_a": ca, "case_b": cb, "case_both": case_of(*f_s_both), "case_either": case_of(*f_s_either),
           "pair_kappa": pk}
    if ca is None or cb is None:
        res["answer"], res["why"] = "not decided", f"a share on {name} cannot be computed: a return has none"
    elif pk is None:
        res["answer"], res["why"] = "not decided", f"the pair kappa on {name} cannot be computed"
    elif r6(pk) < 0.60:
        res["answer"], res["why"] = "not decided", f"the pair kappa on {name} is below 0.60"
    else:
        c = max(ca, cb)
        res["answer"], res["why"] = CASES[c], ("both matchers give this case" if ca == cb else
                                               "the lower of the two matchers' cases")
    return res


def score(key, R, plan_sha=None, reply_info=None, seed=SEED, resamples=RESAMPLES):
    """R: {"a": result or None, "b": result or None}. Returns the results object."""
    L = Lists(key)
    ok = R.get("a") is not None and R.get("b") is not None
    F = {}
    for m in ("a", "b"):
        if R.get(m) is None:
            F[m] = None
            continue
        F[m] = {**found_map(L.PC + L.QC, map(tuple, R[m]["claims"]["pairs"])),
                **found_map(L.PP + L.QP, map(tuple, R[m]["passages"]["pairs"]))}
    first_c, new_c = L.of("claims", "first"), L.of("claims", "new")
    first_p, new_p = L.of("passages", "first"), L.of("passages", "new")
    out_t = lambda v: v["table"] is None                       # noqa: E731
    in_t = lambda v: v["table"] is not None                    # noqa: E731
    found = {
        "claims": {"first": shares_for(first_c, F), "new": shares_for(new_c, F),
                   "first_core": shares_for(L.of("claims", "first", lambda v: v.get("core") is True), F),
                   "new_core": shares_for(L.of("claims", "new", lambda v: v.get("core") is True), F)},
        "passages_all": {"first": shares_for(first_p, F), "new": shares_for(new_p, F)},
        "passages_out": {"first": shares_for(L.of("passages", "first", out_t), F),
                         "new": shares_for(L.of("passages", "new", out_t), F)},
        "passages_tables": {"first": shares_for(L.of("passages", "first", in_t), F),
                            "new": shares_for(L.of("passages", "new", in_t), F)},
        "passages_by_voice": {}}
    codes = sorted({v["voice"] for v in L.F.values()})
    for ret in ("first", "new"):
        for c in codes:
            found["passages_by_voice"][f"{ret} {c}"] = shares_for(
                L.of("passages", ret, lambda v, c=c: v["voice"] == c), F)

    def fs(group, m):
        return (found[group]["first"][m], found[group]["new"][m])
    res = {"plan_sha256": plan_sha, "key_lists_sha256": key.get("lists_sha256"), "P": key["P"],
           "Q": key["Q"], "seed": seed, "resamples": resamples, "replies": reply_info or {},
           "counts": {}, "found": found}
    for ret in ("first", "new"):
        cl = L.of("claims", ret)
        ps = L.of("passages", ret)
        res["counts"][ret] = {
            "claims": len(cl), "core": sum(1 for i in cl if L.C[i].get("core") is True),
            "stated_as": dict(sorted(collections.Counter(str(L.C[i].get("stated_as")) for i in cl).items())),
            "passages": len(ps), "table_cells": sum(1 for i in ps if L.F[i]["table"] is not None),
            "voice": dict(sorted(collections.Counter(L.F[i]["voice"] for i in ps).items())),
            "per_page": {str(k): v for k, v in sorted(collections.Counter(
                L.F[i]["first_page"] if L.F[i]["first_page"] is not None else -1 for i in ps).items())}}
    res["candidates"] = {"claim_pairs": len(L.claim_pairs), "passage_pairs_all": len(L.cand_all),
                         "passage_pairs_outside_tables": len(L.cand_out)}
    res["pairs"] = {}
    for m, chat, model in MATCHERS:
        if R.get(m) is None:
            res["pairs"][m] = None
            continue
        pp = [tuple(x) for x in R[m]["passages"]["pairs"]]
        cand = set(L.cand_all)

        def known(x):
            return bool(L.F[x[0]]["pages"]) and bool(L.F[x[1]]["pages"])
        far = [x for x in pp if known(x) and not near(L.F[x[0]]["pages"], L.F[x[1]]["pages"])]
        unknown = [x for x in pp if not known(x)]
        mixed = [x for x in pp if (L.F[x[0]]["table"] is None) != (L.F[x[1]]["table"] is None)]
        res["pairs"][m] = {
            "chat": chat, "model": model,
            "claims": len(R[m]["claims"]["pairs"]), "claims_one_way": R[m]["claims"]["one_way"],
            "passages": len(pp), "passages_one_way": R[m]["passages"]["one_way"],
            "passages_more_than_one_page_apart": far, "passages_page_unknown": unknown,
            "passages_not_candidates": [x for x in pp if x not in cand],
            "passages_table_cell_with_passage_outside_tables": mixed}
    if not ok:
        res["kappas"], res["intervals"], res["voice"] = None, None, None
        nd = {"answer": "not decided", "why": "a reply does not count"}
        res["answers"] = {"Q1": nd, "Q2": nd, "Q2_with_tables": nd, "Q3": nd}
        res["described"] = None
        return res
    sa = {k: set(map(tuple, R["a"][k]["pairs"])) for k in ("claims", "passages")}
    sb = {k: set(map(tuple, R["b"][k]["pairs"])) for k in ("claims", "passages")}
    both_p = sorted(sa["passages"] & sb["passages"])
    both_c = sorted(sa["claims"] & sb["claims"])
    vp = voice_pairs(L, both_p)
    K = all_kappas(L, R, vp)
    res["kappas"] = K
    res["intervals"] = bootstrap(L, R, vp, seed, resamples)
    agree = sum(1 for x, y in vp if x == y)
    res["voice"] = {"pairs_both_name": len(vp), "agree": agree, "raw": (agree / len(vp)) if vp else None,
                    "kappa": K["voice"], "table": {f"{x} / {y}": n for (x, y), n in
                                                   sorted(collections.Counter(vp).items())},
                    "two_codings_of_the_first_extraction": VOICE_TWO_CODINGS}
    q1 = answer(fs("claims", "a"), fs("claims", "b"), fs("claims", "both"), fs("claims", "either"),
                K["claims_pairs"], "claims")
    q1["item_kappa"] = K["claims_items"]
    q2 = answer(fs("passages_out", "a"), fs("passages_out", "b"), fs("passages_out", "both"),
                fs("passages_out", "either"), K["passages_out_pairs"], "the passages outside the tables")
    q2["item_kappa"] = K["passages_out_items"]
    q2t = answer(fs("passages_all", "a"), fs("passages_all", "b"), fs("passages_all", "both"),
                 fs("passages_all", "either"), K["passages_all_pairs"], "all passages")
    q2t["item_kappa"] = K["passages_all_items"]
    vk = K["voice"]
    if q2["answer"] == "not decided":
        q3 = {"answer": "not decided", "why": "Q2 is not decided"}
    elif len(vp) < 20:
        q3 = {"answer": "not decided", "why": f"fewer than 20 passage pairs both matchers name ({len(vp)})"}
    elif vk is None:
        q3 = {"answer": "not decided", "why": "the voice kappa cannot be computed"}
    elif r6(vk) >= 0.80:
        q3 = {"answer": "as steady as two codings of one extraction", "why": "the voice kappa is at least 0.80"}
    elif r6(vk) >= 0.60:
        q3 = {"answer": "less steady", "why": "the voice kappa is at least 0.60 and under 0.80"}
    else:
        q3 = {"answer": "not steady", "why": "the voice kappa is under 0.60"}
    q3["kappa"], q3["pairs"] = vk, len(vp)
    res["answers"] = {"Q1": q1, "Q2": q2, "Q2_with_tables": q2t, "Q3": q3}
    # described
    sa_agree = sum(1 for p, q in both_c if L.C[p].get("stated_as") == L.C[q].get("stated_as"))
    core_agree = sum(1 for p, q in both_c if bool(L.C[p].get("core")) == bool(L.C[q].get("core")))
    links = {}
    for ret in ("first", "new"):
        d = collections.defaultdict(list)
        for c_id, f_id, direction in key["links"][ret]:
            d[(c_id, f_id)].append(direction)
        links[ret] = d
    lc = collections.Counter()
    dup = 0
    for cp in both_c:
        cf, cn = (cp if L.C[cp[0]]["return"] == "first" else (cp[1], cp[0]))
        for fp in both_p:
            ff, fn = (fp if L.F[fp[0]]["return"] == "first" else (fp[1], fp[0]))
            a_ = links["first"].get((L.C[cf]["id"], L.F[ff]["id"]))
            b_ = links["new"].get((L.C[cn]["id"], L.F[fn]["id"]))
            dup += int(bool(a_ and len(a_) > 1)) + int(bool(b_ and len(b_) > 1))
            if a_ and b_:
                lc["both link, same direction" if a_[0] == b_[0] else "both link, different direction"] += 1
                lc[f"both link: {a_[0]} / {b_[0]}"] += 1
            elif a_:
                lc["first return only"] += 1
            elif b_:
                lc["new return only"] += 1
            else:
                lc["neither"] += 1
    res["described"] = {"claim_pairs_both_name": len(both_c), "stated_as_agree": sa_agree,
                        "core_agree": core_agree, "passage_pairs_both_name": len(both_p),
                        "links_on_matched_pairs": dict(sorted(lc.items())),
                        "links_given_twice": dup}
    return res


# ---------------------------------------------------------------- writing

def fmt(x, d=3):
    return "—" if x is None else f"{x:.{d}f}"


def pct(sh, m):
    x = sh.get(m)
    if x is None:
        return "—"
    n = sh["found"][m] if "found" in sh else round(x * sh["n"])
    return f"{x:.2f} ({n} of {sh['n']})"


def write_md(res, path):
    L = []
    w = L.append
    w("# The second extraction of Bechky (T35): the results")
    w("")
    w("Written by `score_second_extraction.py score`, as `SECOND_EXTRACTION_PLAN.md` fixes the figures "
      f"(its sha256 {res['plan_sha256'] or '—'}). List P is the {res['P']} return, list Q the {res['Q']}; "
      f"the lists file's sha256 is {res['key_lists_sha256']}. Matcher a is chat 56 (Opus 5.5 at Extra); "
      "matcher b is chat 57 (GPT 6 Astra at max).")
    w("")
    w("## The replies")
    w("")
    for m, chat, model in MATCHERS:
        info = res["replies"].get(m, {})
        w(f"- **{m}, chat {chat} ({model}):** {info.get('file', '—')}, sha256 {info.get('sha256', '—')}: "
          + ("counts." if not info.get("faults") else "does not count: " + "; ".join(info["faults"]) + "."))
        for n in info.get("notes", []):
            w(f"  - note: {n}")
    w("")
    w("## The answers")
    w("")
    A = res["answers"]
    for q, title in (("Q1", "Q1, the claims"), ("Q2", "Q2, the passages outside the tables"),
                     ("Q2_with_tables", "Q2, second reading: all passages, the table cells included"),
                     ("Q3", "Q3, voice on the passages both matchers pair")):
        x = A[q]
        line = f"- **{title}: {x['answer']}** ({x['why']})."
        if q != "Q3" and "case_a" in x:
            line += (f" Case under a: {x['case_a']}; under b: {x['case_b']}; under both: {x['case_both']}; "
                     f"under either: {x['case_either']}. Pair kappa {fmt(x['pair_kappa'])}; kappa on whether "
                     f"an item is found {fmt(x['item_kappa'])}, which decides nothing.")
        if q == "Q3" and "pairs" in x:
            line += f" Kappa {fmt(x['kappa'])} on {x['pairs']} pairs."
        w(line)
    w("")
    w("Cases: 1, repeat (f and s at least 0.80); 2, repeat in part (both at least 0.50); 3, do not repeat. "
      "f is the share of the first return's items found again, s the share of the new return's found in "
      "the first.")
    w("")
    w("## Found again")
    w("")
    w("| items | n | a | b | both | either |")
    w("|---|---|---|---|---|---|")
    fo = res["found"]
    rows = [("claims of the first return (f)", fo["claims"]["first"]),
            ("claims of the new return (s)", fo["claims"]["new"]),
            ("the first return's core claims", fo["claims"]["first_core"]),
            ("the new return's core claims", fo["claims"]["new_core"]),
            ("passages outside the tables, first return (f)", fo["passages_out"]["first"]),
            ("passages outside the tables, new return (s)", fo["passages_out"]["new"]),
            ("all passages, first return", fo["passages_all"]["first"]),
            ("all passages, new return", fo["passages_all"]["new"]),
            ("table cells, first return", fo["passages_tables"]["first"]),
            ("table cells, new return", fo["passages_tables"]["new"])]
    rows += [(f"passages, {k}", v) for k, v in fo["passages_by_voice"].items()]
    for name, sh in rows:
        w(f"| {name} | {sh['n']} | {pct(sh, 'a')} | {pct(sh, 'b')} | {pct(sh, 'both')} | {pct(sh, 'either')} |")
    w("")
    w("## The matchers' agreement")
    w("")
    if res["kappas"] is None:
        w("Not computed: a reply does not count.")
    else:
        w(f"Cohen's kappa, matcher a against matcher b, with 95% intervals from {res['resamples']:,} bootstrap "
          f"resamples (seed {res['seed']}).")
        w("")
        w("| kappa | over | value | 95% interval | resamples left out |")
        w("|---|---|---|---|---|")
        c = res["candidates"]
        label = {"claims_items": "claims: whether each is found",
                 "claims_pairs": "claims: whether each pair is named",
                 "passages_out_items": "passages outside the tables: whether each is found",
                 "passages_out_pairs": "passages outside the tables: whether each candidate pair is named",
                 "passages_all_items": "all passages: whether each is found",
                 "passages_all_pairs": "all passages: whether each candidate pair is named",
                 "voice": "voice: the first return's code against the new return's"}
        over = {"claims_items": "every claim of both lists",
                "claims_pairs": f"{c['claim_pairs']} pairs of a claim of P and a claim of Q",
                "passages_out_items": "every passage outside the tables, of both lists",
                "passages_out_pairs": f"{c['passage_pairs_outside_tables']} candidate pairs outside the tables",
                "passages_all_items": "every passage of both lists",
                "passages_all_pairs": f"{c['passage_pairs_all']} candidate pairs",
                "voice": "the passage pairs both matchers name"}
        for k in KAPPAS:
            iv = res["intervals"][k]
            w(f"| {label[k]} | {over[k]} | {fmt(res['kappas'][k])} | {fmt(iv['low'])} to "
              f"{fmt(iv['high'])} | {iv['left_out']} |")
    w("")
    w("## Voice on matched passages")
    w("")
    v = res["voice"]
    if v is None:
        w("Not computed: a reply does not count.")
    else:
        t = v["two_codings_of_the_first_extraction"]
        w(f"Over the {v['pairs_both_name']} passage pairs both matchers name: the two returns' codes agree on "
          f"{v['agree']} (raw {fmt(v['raw'])}), kappa {fmt(v['kappa'])}; beside the two codings of the first "
          f"extraction's record, {t['agree']} of {t['n']}, kappa {t['kappa']}.")
        w("")
        for k2, n in v["table"].items():
            w(f"- first / new: {k2}: {n}")
    w("")
    w("## Described, not tested")
    w("")
    for ret in ("first", "new"):
        c = res["counts"][ret]
        w(f"- **The {ret} return:** {c['claims']} claims ({c['core']} core; stated_as {c['stated_as']}); "
          f"{c['passages']} passages, {c['table_cells']} of them table cells; voice {c['voice']}.")
    d = res["described"]
    if d:
        w(f"- **Claim pairs both matchers name:** {d['claim_pairs_both_name']}; stated_as agrees on "
          f"{d['stated_as_agree']}, core on {d['core_agree']}.")
        w(f"- **Links, on each claim pair with each passage pair both name** ({d['passage_pairs_both_name']} "
          f"passage pairs): {d['links_on_matched_pairs']}; links given twice for one pair: "
          f"{d['links_given_twice']}.")
    for m, chat, model in MATCHERS:
        p = res["pairs"].get(m)
        if not p:
            continue
        w(f"- **Matcher {m}'s pairs:** {p['claims']} of claims ({len(p['claims_one_way'])} named one way only), "
          f"{p['passages']} of passages ({len(p['passages_one_way'])} one way only); of the passage pairs, "
          f"{len(p['passages_more_than_one_page_apart'])} more than one page apart, "
          f"{len(p['passages_page_unknown'])} with a page unknown, "
          f"{len(p['passages_not_candidates'])} outside the candidate pairs, and "
          f"{len(p['passages_table_cell_with_passage_outside_tables'])} of a table cell with a passage outside "
          "the tables.")
    for ret in ("first", "new"):
        w(f"- **Passages per page, {ret} return** (-1: no page): {res['counts'][ret]['per_page']}")
    w("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


# ---------------------------------------------------------------- self-test

def toy_key():
    """A made-up key: P is the first return, with 3 claims and 5 passages; Q the new, 2 and 4."""
    C = {"PC01": {"return": "first", "id": "C01", "pages": [606], "core": True, "stated_as": "established"},
         "PC02": {"return": "first", "id": "C02", "pages": [610], "core": False, "stated_as": "ventured"},
         "PC03": {"return": "first", "id": "C03", "pages": [620], "core": True, "stated_as": "established"},
         "QC01": {"return": "new", "id": "C01", "pages": [606], "core": True, "stated_as": "established"},
         "QC02": {"return": "new", "id": "C02", "pages": [612], "core": False, "stated_as": "established"}}

    def p(ret, fid, pages, table, voice):
        return {"return": ret, "id": fid, "location": "x", "pages": pages,
                "first_page": pages[0] if pages else None, "table": table, "voice": voice}
    F = {"PP001": p("first", "F01", [607], None, "reported"),
         "PP002": p("first", "F02", [612], None, "author_insight"),
         "PP003": p("first", "F03", [613], "Table 1", "reported"),
         "PP004": p("first", "F04", [613], "Table 1", "reported"),
         "PP005": p("first", "F05", [630], None, "author_insight"),
         "QP001": p("new", "F01", [607, 608], None, "reported"),
         "QP002": p("new", "F02", [613], "Table 1", "reported"),
         "QP003": p("new", "F03", [612], None, "reported"),
         "QP004": p("new", "F04", [640], None, "author_insight")}
    links = {"first": [["C01", "F01", "with"], ["C02", "F02", "illustrates"]],
             "new": [["C01", "F01", "with"], ["C02", "F03", "with"]]}
    return {"P": "first", "Q": "new", "claims": C, "passages": F, "links": links, "lists_sha256": "toy"}


def toy_reply(claims, passages, key):
    """A reply naming the given pairs from both sides."""
    obj = {"claims": {i: [] for i in key["claims"]}, "passages": {i: [] for i in key["passages"]}}
    for kind, pairs in (("claims", claims), ("passages", passages)):
        for a, b in pairs:
            obj[kind][a].append(b)
            obj[kind][b].append(a)
    return obj


def selftest():
    fails = []

    def check(cond, msg):
        if not cond:
            fails.append(msg)

    def close(a, b):
        return a is not None and b is not None and abs(a - b) < 1e-12

    check(close(kappa([1, 1, 0, 0], [1, 0, 0, 0]), 0.5), "kappa: a known value")
    check(kappa([1, 1, 1], [1, 0, 1]) == 0.0, "kappa: one list all 1 gives 0")
    check(kappa([0, 0, 0], [1, 1, 1]) == 0.0, "kappa: one list all 0, the other all 1, gives 0")
    check(kappa([1, 1], [1, 1]) is None and kappa([0, 0], [0, 0]) is None,
          "kappa: both lists all 1, or all 0, is not computed")
    check(close(kappa([1, 1, 1, 0], [1, 1, 1, 1]), 0.0) and close(kappa([1, 1, 0, 1], [1, 1, 1, 1]), 0.0),
          "kappa: a matcher who finds everything")
    check(close(nominal_kappa(["r", "r", "a", "a"], ["r", "a", "a", "a"]), 0.5), "nominal kappa: a known value")
    check(nominal_kappa(["r", "r"], ["r", "r"]) is None, "nominal kappa: one code throughout")
    rng = random.Random(1)
    for _ in range(50):
        x = [rng.randint(0, 1) for _ in range(30)]
        y = [rng.randint(0, 1) for _ in range(30)]
        wts = [rng.randint(0, 3) for _ in range(30)]
        ex = [a for a, k in zip(x, wts) for _ in range(k)]
        ey = [b for b, k in zip(y, wts) for _ in range(k)]
        c = collections.Counter()
        for a, b, k in zip(x, y, wts):
            c[(a, b)] += k
        k1, k2 = kappa_counts(c[(1, 1)], c[(1, 0)], c[(0, 1)], c[(0, 0)]), kappa(ex, ey)
        check(k1 == k2 or close(k1, k2), "weighted kappa differs from the expanded lists")
    check([case_of(*x) for x in ((0.8, 0.8), (0.7999999, 0.9), (0.79, 0.9), (0.5, 0.5), (0.49, 0.9))] ==
          [1, 1, 2, 2, 3], "cases at the bars")
    check(near([612], [613]) and not near([612], [614]) and not near([], [612]), "pages next to each other")
    key = toy_key()
    L = Lists(key)
    check(L.cand_all == [("PP001", "QP001"), ("PP002", "QP002"), ("PP002", "QP003"), ("PP003", "QP002"),
                         ("PP003", "QP003"), ("PP004", "QP002"), ("PP004", "QP003")], f"candidates: {L.cand_all}")
    check(L.cand_out == [("PP001", "QP001"), ("PP002", "QP003")], f"candidates outside tables: {L.cand_out}")
    # the checks on a reply
    good = toy_reply([("PC01", "QC01")], [("PP001", "QP001")], key)
    f, n, r = check_reply(good, key)
    check(not f and r["claims"]["pairs"] == [("PC01", "QC01")] and not r["claims"]["one_way"], "a good reply")
    bad = json.loads(json.dumps(good))
    del bad["claims"]["PC03"]
    bad["claims"]["XC01"] = []
    bad["passages"]["PP002"] = ["PP001", "QC01", "QP009"]
    bad["passages"]["PP003"] = "QP002"
    bad["notes"] = "x"
    f, n, r = check_reply(bad, key)
    for frag in ("keys other than claims and passages", "no entry for 1 ids: ['PC03']",
                 "ids not in the lists: ['XC01']", "PP002: names what is not a passage of list Q",
                 "PP003: its entry is not a list of ids"):
        check(any(frag in x for x in f), f"a fault not found: {frag}")
    check(r is None, "a failing reply gave pairs")
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        pth = os.path.join(d, "r.txt")
        open(pth, "w").write('Here: {"claims": {"PC01": [], "PC01": ["QC01"]}, "passages": {}} thanks')
        obj, lf, ln = load_reply(pth)
        check(lf == ["the key 'PC01' is given more than once"], f"a key given twice: {lf}")
        check(ln == ["text outside the object: before it 'Here:', after it 'thanks'"], f"outside text: {ln}")
        open(pth, "w").write("no object here")
        check(load_reply(pth)[1] == ["no JSON object found"], "no object")
        open(pth, "w").write('{"claims": {}, "passages": {}}')
        check(load_reply(pth)[1:] == ([], []), "a bare object has no fault and no note")
    one_way = toy_reply([], [], key)
    one_way["passages"]["PP001"] = ["QP001"]
    f, n, r = check_reply(one_way, key)
    check(not f and r["passages"]["pairs"] == [("PP001", "QP001")] and
          r["passages"]["one_way"] == [("PP001", "QP001")], "a pair named one way counts, and is listed")
    twice = toy_reply([], [("PP001", "QP001")], key)
    twice["passages"]["PP001"].append("QP001")
    f, n, r = check_reply(twice, key)
    check(not f and n == ["PP001: names a counterpart more than once"], "a counterpart named twice is a note")
    # a whole score on the toy: matcher a and b
    ra = check_reply(toy_reply([("PC01", "QC01"), ("PC02", "QC02")],
                               [("PP001", "QP001"), ("PP002", "QP003"), ("PP003", "QP002"),
                                ("PP004", "QP002")], key), key)[2]
    rb = check_reply(toy_reply([("PC01", "QC01"), ("PC03", "QC02")],
                               [("PP001", "QP001"), ("PP002", "QP003"), ("PP003", "QP002"),
                                ("PP005", "QP004")], key), key)[2]
    res = score(key, {"a": ra, "b": rb}, resamples=200)
    fo = res["found"]
    check(fo["claims"]["first"]["a"] == 2 / 3 and fo["claims"]["first"]["b"] == 2 / 3, "claims f")
    check(fo["claims"]["first"]["both"] == 1 / 3 and fo["claims"]["first"]["either"] == 1.0, "claims both/either")
    check(fo["claims"]["new"]["a"] == 1.0 and fo["claims"]["new"]["b"] == 1.0, "claims s")
    check(fo["claims"]["first_core"]["a"] == 0.5 and fo["claims"]["first_core"]["b"] == 1.0, "core claims")
    check(fo["passages_out"]["first"]["a"] == 2 / 3 and fo["passages_out"]["first"]["b"] == 1.0,
          "passages outside the tables, f")
    check(fo["passages_out"]["new"]["a"] == 2 / 3 and fo["passages_out"]["new"]["b"] == 1.0,
          "passages outside the tables, s")
    check(fo["passages_tables"]["first"]["a"] == 1.0 and fo["passages_tables"]["first"]["b"] == 0.5,
          "table cells")
    # claims: items PC01 PC02 PC03 QC01 QC02; a: 1 1 0 1 1; b: 1 0 1 1 1
    check(close(res["kappas"]["claims_items"], kappa([1, 1, 0, 1, 1], [1, 0, 1, 1, 1])), "claims item kappa")
    # claim pairs in order PC01-QC01, PC01-QC02, PC02-QC01, PC02-QC02, PC03-QC01, PC03-QC02
    check(close(res["kappas"]["claims_pairs"], kappa([1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 1])),
          "claims pair kappa")
    # passage candidates all: as above; a names 1,2,4,6 ; b names 1,2,4 (PP005-QP004 is no candidate)
    check(close(res["kappas"]["passages_all_pairs"], kappa([1, 0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 0])),
          "passages pair kappa, all")
    check(res["kappas"]["passages_out_pairs"] is None, "outside the tables both name both pairs: None")
    check(res["pairs"]["b"]["passages_more_than_one_page_apart"] == [("PP005", "QP004")],
          "a pair ten pages apart is reported")
    # voice on pairs both name: PP001-QP001 r/r, PP002-QP003 ai/r, PP003-QP002 r/r
    check(res["voice"]["pairs_both_name"] == 3 and res["voice"]["agree"] == 2, "voice pairs")
    check(close(res["kappas"]["voice"], nominal_kappa(["reported", "author_insight", "reported"],
                                                      ["reported", "reported", "reported"])), "voice kappa")
    A = res["answers"]
    check(A["Q1"]["case_a"] == 2 and A["Q1"]["case_b"] == 2 and A["Q1"]["answer"] == "not decided",
          f"Q1 on the toy: {A['Q1']}")
    check(A["Q3"]["answer"] == "not decided", "Q3 not decided with Q2 not decided")
    d = res["described"]
    check(d["claim_pairs_both_name"] == 1 and d["stated_as_agree"] == 1 and d["core_agree"] == 1,
          "described: claims")
    # links: claim pair PC01-QC01 with passage pairs PP001-QP001 (both link, with/with), PP002-QP003, PP003-QP002
    check(d["links_on_matched_pairs"].get("both link, same direction") == 1 and
          d["links_on_matched_pairs"].get("neither") == 2, f"described: links {d['links_on_matched_pairs']}")
    res2 = score(key, {"a": ra, "b": rb}, resamples=200)
    check(json.dumps(res, default=list) == json.dumps(res2, default=list), "two scores differ")
    check(score(key, {"a": ra, "b": None}, resamples=10)["answers"]["Q1"]["answer"] == "not decided",
          "a reply that does not count leaves the answers not decided")
    # answers with clear agreement: a and b alike
    res3 = score(key, {"a": ra, "b": ra}, resamples=50)
    check(res3["answers"]["Q1"]["answer"] == "repeat in part" and res3["kappas"]["claims_pairs"] == 1.0,
          f"Q1 when the matchers agree: {res3['answers']['Q1']}")
    check(res3["intervals"]["claims_pairs"]["left_out"] >= 0, "intervals given")
    if fails:
        print("SELF-TEST FAILED:")
        for x in fails:
            print("  ", x)
        return 1
    print("self-test passed: kappas, weights, cases, candidates, the checks on a reply, a whole score on a "
          "made-up key, the answers, the described figures, two scores alike")
    return 0


def main(argv):
    if not argv or argv[0] not in ("selftest", "check", "score"):
        print(__doc__)
        return 2
    if argv[0] == "selftest":
        return selftest()
    opts = dict(a[2:].split("=", 1) for a in argv[1:] if a.startswith("--") and "=" in a)
    args = [a for a in argv[1:] if not a.startswith("--")]
    key = json.load(open(opts["key"], encoding="utf-8"))
    if argv[0] == "check":
        obj, lf, ln = load_reply(args[0])
        f, n, r = check_reply(obj, key, lf)
        for x in ln + n:
            print("note:", x)
        if f:
            print(f"DOES NOT COUNT ({len(f)} faults):")
            for x in f:
                print("  ", x)
            return 1
        print(f"counts: {len(r['claims']['pairs'])} claim pairs ({len(r['claims']['one_way'])} one way only), "
              f"{len(r['passages']['pairs'])} passage pairs ({len(r['passages']['one_way'])} one way only)")
        return 0
    R, info = {}, {}
    for m, chat, model in MATCHERS:
        path = opts[m]
        obj, lf, ln = load_reply(path)
        f, n, r = check_reply(obj, key, lf)
        R[m] = r
        info[m] = {"file": os.path.basename(path), "sha256": sha(path), "faults": f, "notes": ln + n}
    plan = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SECOND_EXTRACTION_PLAN.md")
    res = score(key, R, sha(plan) if os.path.exists(plan) else None, info,
                int(opts.get("seed", SEED)), int(opts.get("resamples", RESAMPLES)))
    os.makedirs(opts["out"], exist_ok=True)
    write_md(res, os.path.join(opts["out"], "SECOND_EXTRACTION_RESULTS.md"))
    with open(os.path.join(opts["out"], "second_extraction_results.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1, default=list)
        fh.write("\n")
    for q in ("Q1", "Q2", "Q2_with_tables", "Q3"):
        print(f"{q}: {res['answers'][q]['answer']} ({res['answers'][q]['why']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
