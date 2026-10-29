"""The claims network of a paper's repository entry, for Bechky: one self-contained page (no script, nothing loaded from
outside) that draws the frozen index's claims joined by the settled map's ties, each sized by how many of the paper's
real readings engage it, coloured by its kind and ringed when core; clicking a claim shows its statement, its ties,
the constructs it shares with other claims, and the readings that engage it, with those that reach it only through
its ties apart; clicking a reading's title opens the reading in full, with the claims it engages marked on the map.
Written on 20, 21 and 25 Oct 2026. The labels of a reading that reaches a claim only through its ties are shown by
plain names, the closure's codes named beside them in the intro panel. A note in the page's header says what the
readings are: in the tradition of Black,
Carlile and Repenning (2004), abductive extensions or re-theorizations of the study, not an error-catching audit or a
replication; and that the paper's author is invited as a co-interpreter of what the field material can further support,
and can append a brief commentary to the paper's entry. A second note gives the part of each reading the coders read,
on which the claims each reading engages, the labels and the reach rest, with the rest of each reading marked as not
coded. Each run of six or more of the paper's words
that the quotation check found in a reading (quotation_check_bechky.json, by check_quotations.py) is
highlighted wherever it stands in that reading, with the paper's page; a note in the header says so, and that before any
public version each run is replaced by a note giving its length and page. Reach is shown by a bar, filled to the score
on one gradient fixed along the whole bar, with the score and its level (Marginal 0.00-0.29, Moderate 0.30-0.69, High
0.70-0.89, Max 0.90-1.00); in a claim's lists of readings each reading is given by its title, its bar and the coders who
say so, with no id, model or chat; the table of the readings has the bar and no column "proposed by"; and each reading's
panel says, in a short note, who wrote the reading (a model, in one chat) and who coded it (the two coder models, each
in a chat of its own, not told who wrote it).

A reading engages a claim when a coder's code of the relation test (T37) gives the claim one of the relations
inverts, other_mechanism, rereads_evidence or challenges_premise (the last questions the claim's premise), as the
closure takes it (map_closure_bechky.json); a reading counts when either coder says so. The ties are the settled
map's edges (map_settled_bechky.json): a claim is drawn above the claims it rests on, by the longest chain of ties
beneath it; within a row the order is fixed by a deterministic barycentre sweep. Constructs are merged by the settled
registry, as build_map_settle.py merges them, and listed, never drawn: a shared construct is not dependence.

Each reading is shown first as the coders read it (relation_key.json's text, as RELATION_READINGS_bechky.md gives it:
for the plain and places prompts its wager and evidence; for the cards, its wager statement, the index's ids turned into
places in the paper), then, folded, the rest of it as its model wrote it, from its source reply (matching_key.json
names it): every field but ids and bookkeeping (a card's naming register, and the attack pass's verdicts on the cards
made from the index). In those cards' own words, each fragment and gap id is followed by its place in the paper, in
square brackets, from the index, and each claim id links to its claim.

Inputs, from this folder, each checked by its sha256: the frozen index (through build_map_test.py), the settled map,
the closure, ranking_check.json (reach), reading_titles_bechky.json (the titles), relation_key.json (each reading's
chat and text), matching_key.json (each reading's source), RELATION_READINGS_bechky.md, the six chats' replies and
cards, chats_models_hours.json (each chat's model) and CLAIM_KINDS_bechky.md (the kinds; its statements must equal the
index's). The same inputs always give the same bytes.

usage: python3 -I -B build_claim_network.py build <out dir>     writes CLAIM_NETWORK_bechky.html, never over a file
       python3 -I -B build_claim_network.py check               builds twice in a scratch folder and checks the page
"""
import collections
import hashlib
import html
import json
import math
import os
import re
import sys
import tempfile
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_map_test as bmt  # noqa: E402
import build_map_settle as bms  # noqa: E402

PAPER = "bechky"
OUT_NAME = "CLAIM_NETWORK_bechky.html"
CARDS = "stage2/bechky_2020_cards/"
INPUTS = {"map_settled_bechky.json": "01b7fc1b3045c294af9593573cf9b5ba0f059da901bfd62b1b25998db605380b",
          "map_closure_bechky.json": "7ff976788af4392a40fbe8bd40b0b7b8151690da18b484aa41f19b24680d339f",
          "ranking_check.json": "569a62da4c318a78182291c9aa6d9dece4e8ede12995d5bd29f1aedb7bf08021",
          "reading_titles_bechky.json": "658ff79a9c26535bdda79e38fab39ef3e064410651d6347b4b91627a635337c7",
          "relation_key.json": "b8598261afbe915c4d5c58832c7d4516f7500b7f87493c531cf1682490937ea5",
          "matching_key.json": "faaba978f4d0842a7a98c810b84eb7f2e535a769347efbb353f6a837a23031a1",
          "RELATION_READINGS_bechky.md": "20cadee86efc3d6a29dcc6d4ac29c1006fe6527fb21612a561e7e4d6a378cbf1",
          "chats_models_hours.json": "fe8bebed608792d6e03d54395e8ef2bced876f69045d61fb680d6cd00fa7bcbd",
          "CLAIM_KINDS_bechky.md": "40c953d5fb506a6aa549246b0899a41b624e565221b1fb87f13096e52762b9ab",
          "quotation_check_bechky.json": "144ddf74186df5302ccb6d762a227580e55c8aa89f8f4178ac7a2b96c157efce",
          "stage2/baseline_replies/reply_26_bechky_reading.json":
              "1fbb72c2d5ba296000ee7399c6f2966c892e88493a5fe3883bc6e9dc4d0122d0",
          "stage2/baseline_replies/reply_27_bechky_plain.json":
              "2c66c8dc1f1d01050bcc3ea0128f85ff5124e3f1248b1bf2db57a3ffdff28084",
          "reply_46_bechky_open.json": "4f3bd651333bbdbf4314b9b29ce717adda95ad805bc5e518d2747ca75e2a80f6",
          "reply_49_bechky_plain_astra.json": "8b4e3baf232d2c4865555856f61c20f6aaf76d16814134c65e72af92513f8d93",
          "reply_50_bechky_plain_astra.json": "09859e42db7b6900d930749c2eca594121c278f39dc509fc7b605578c874e293",
          CARDS + "bechky_2020_construct_inversion_from_pair_CP01_01.json":
              "16adf47281a790e70cd86139d7b22600be527b426b79bb31c18921ecab201543",
          CARDS + "bechky_2020_construct_inversion_from_pair_CP02_01.json":
              "4071ca47a50916b408a5717eac3e0271d5cd5e495f3e3d6ab788dcaa8ba5169b",
          CARDS + "bechky_2020_counterfactual_ending_DG02_01.json":
              "47bc4964539dc1595cfe686612641e11718fdaf9d4f3e9b8d78b23a1d2969052",
          CARDS + "bechky_2020_focalization_shift_forensic_biology_DNA_01.json":
              "f0ec5f4b936676deb149680c88afebe742966bbd117e44f177827a315c77c7ac"}
CODERS = ("gemini", "astra")
CODER_NAME = {"gemini": "Gemini 4 Argon", "astra": "GPT 6 Astra"}
# version 7: the closure's labels shown by plain names; the codes stay in the closure's file
LABEL_NAME = {"unsupported": "support in question", "weakened": "support partly in question",
              "idle": "significance in question", "restated": "restated"}
KINDS = ("theoretical", "empirical", "method")
# each chat's form of reading and prompt, checked against chats_models_hours.json
CHATS = {"23": ("system", "Fable 5.1", "T29 generation", "no PDF", "the index's files, without the paper"),
         "26": ("middle", "Fable 5.1", "T29 baseline middle", "READING_PROMPT.md and the PDF",
                "READING_PROMPT.md, with the paper"),
         "27": ("plain", "Fable 5.1", "T29 baseline plain", "ALTERNATIVE_READINGS.md and the PDF",
                "the plain prompt, with the paper"),
         "46": ("places", "Fable 5.1", "T32 readings", "OPEN_PLACES.md and the PDF", "the places prompt, with the paper"),
         "49": ("plain", "GPT 6 Astra", "T33 plain second vendor", "the PDF and ALTERNATIVE_READINGS.md",
                "the plain prompt, with the paper"),
         "50": ("plain", "GPT 6 Astra", "T33 plain second vendor", "the PDF and ALTERNATIVE_READINGS.md",
                "the plain prompt, with the paper")}
W, MARGIN = 940, 60
ROW_Y0, ROW_GAP, BAND_GAP = 62, 150, 132


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def num(c):
    return int(c[1:])


def esc(s):
    return html.escape(s, quote=True)


def load(folder):
    """Every input, its hash checked against INPUTS (and the index's against build_map_test's table)."""
    got = {}
    for name, want in INPUTS.items():
        p = os.path.join(folder, name)
        h = sha(p)
        if h != want:
            raise SystemExit(f"{name}: sha256 {h}, not {want}")
        got[name] = open(p, "rb").read()
    index, index_sha = bmt.load_index(PAPER, None if os.path.abspath(folder) == HERE else folder)
    if index_sha != bmt.SHA[bmt.INDEX[PAPER]]:
        raise SystemExit("the index is not the frozen one")
    return index, index_sha, got


def json_of(data):
    t = data.decode("utf-8")
    return json.loads(t[t.index("{"):t.rindex("}") + 1])


def kinds_of(md, claims):
    kind, out = None, {}
    for line in md.split("\n"):
        m = re.match(r"## (Empirical|Theoretical|Method): \d+$", line.strip())
        if m:
            kind = m.group(1).lower()
            continue
        m = re.match(r"- \*\*(C\d\d)\*\* \(((?:not )?core)(?:; [^)]*)?\)\. (.+)$", line)
        if m:
            c = m.group(1)
            assert kind and c not in out, c
            assert m.group(3) == claims[c]["statement"], f"{c}: the kinds file's statement is not the index's"
            assert (m.group(2) == "core") == (claims[c].get("core") is True), c
            out[c] = kind
    assert sorted(out) == sorted(claims), sorted(set(out) ^ set(claims))
    return out


def sources_of(got, key, rows):
    """{reading: (its form, its source object)}, each relation text checked against the matching key and the file."""
    mk = {x["reading"]: x for x in json.loads(got["matching_key.json"])["readings"]}
    rel_md = got["RELATION_READINGS_bechky.md"].decode("utf-8")
    out, texts = {}, {}
    for x in key["readings"]:
        if x["paper"] != PAPER or x["r"] not in rows:
            continue
        m = mk[x["source"]]
        assert m["chat"] == x["chat"] and m["text"] == x["text"], x["r"]
        assert x["text"] in rel_md, x["r"]
        form = CHATS[x["chat"]][0]
        src = m["source"]
        d = json_of(got[src])
        if form == "system":
            assert src.startswith(CARDS) and d["card_id"] == m["source_id"], x["r"]
            obj = d
        elif form == "middle":
            obj = [c for c in d["cards"] if c["card_id"] == m["source_id"]]
            assert len(obj) == 1, x["r"]
            obj = obj[0]
        else:
            obj = [c for c in d["readings"] if c["reading_id"] == m["source_id"]]
            assert len(obj) == 1, x["r"]
            obj = obj[0]
            assert ("place" in obj) == (form == "places"), x["r"]
        out[x["r"]] = (form, obj)
        texts[x["r"]] = x["text"]
    assert sorted(out) == sorted(rows)
    return out, texts


def model_data(index, got):
    claims, _, _, _, core = bmt.structure(index)
    ids = sorted(claims, key=num)
    kinds = kinds_of(got["CLAIM_KINDS_bechky.md"].decode("utf-8"), claims)
    settled = json.loads(got["map_settled_bechky.json"])
    closure = json.loads(got["map_closure_bechky.json"])
    ranking = json.loads(got["ranking_check.json"])["papers"][PAPER]
    titles = json.loads(got["reading_titles_bechky.json"])
    key = json.loads(got["relation_key.json"])
    chats = {str(c["chat_number"]): c for c in json.loads(got["chats_models_hours.json"])["chats"]
             if c.get("chat_number") is not None}
    assert settled["paper"] == PAPER and closure["paper"] == PAPER
    assert sorted(closure["core"]) == core
    planted = {r["reading"] for r in ranking["rows"] if r["planted"]}
    rows = {r["reading"]: r for r in ranking["rows"] if not r["planted"]}
    assert sorted(titles) == sorted(rows), "titles and readings differ"
    chat = {x["r"]: x["chat"] for x in key["readings"] if x["paper"] == PAPER}
    for ch, (_, model, test, setting, _) in CHATS.items():
        c = chats[ch]
        assert c["paper"] == "bechky_2020" and c["model"] == model and c["test"] == test and setting in c["setting"], c
    model = {r: CHATS[chat[r]][1] for r in rows}
    edges = [{"claim": e["claim"], "base": e["base"], "type": e["type"], "strength": e["strength"]}
             for e in settled["edges"]]
    for e in edges:
        assert e["claim"] in claims and e["base"] in claims and e["strength"] in ("necessary", "contributing"), e
    hits = {r: {} for r in rows}
    labels = {r: {} for r in rows}
    seen = set()
    for x in closure["readings"]:
        r = x["reading"]
        if r in planted:
            continue
        assert r in rows and set(x["coders"]) == set(CODERS), r
        seen.add(r)
        for cd in CODERS:
            hits[r][cd] = set(x["coders"][cd]["hits"])
            labels[r][cd] = dict(x["coders"][cd]["labels"])
            for c in hits[r][cd]:
                assert labels[r][cd].get(c) == "contested", (r, cd, c)
    assert seen == set(rows)
    cmap = bms.canon_map(settled, index)
    uses = collections.defaultdict(set)
    for c in claims.values():
        for n in c.get("constructs") or []:
            uses[cmap[n]].add(c["claim_id"])
    cons = {}
    for c in ids:
        out = []
        for n in claims[c].get("constructs") or []:
            k = cmap[n]
            if k not in [y[0] for y in out]:
                out.append((k, sorted(uses[k] - {c}, key=num)))
        cons[c] = out
    loc = {}
    for f in index["fragments"]:
        loc[f["fragment_id"]] = f["location"]
    for g in index.get("declared_gaps", []):
        loc[g["gap_id"]] = g["location"].replace(";", ",")
    srcs, texts = sources_of(got, key, rows)
    return {"claims": claims, "ids": ids, "core": set(core), "kinds": kinds, "edges": edges, "rows": rows,
            "titles": titles, "chat": chat, "model": model, "hits": hits, "labels": labels, "cons": cons,
            "citation": index["meta"]["citation"], "loc": loc, "srcs": srcs, "texts": texts,
            "quotes": quote_runs(got), "marked": {}}


def layout(ids, edges):
    """Rows by the longest chain of ties beneath a claim; the order in each row by a fixed barycentre sweep."""
    bases = {c: sorted({e["base"] for e in edges if e["claim"] == c}, key=num) for c in ids}
    deps = {c: sorted({e["claim"] for e in edges if e["base"] == c}, key=num) for c in ids}
    tied = sorted({e["claim"] for e in edges} | {e["base"] for e in edges}, key=num)
    lev = {}

    def level(c, path=()):
        if c in lev:
            return lev[c]
        assert c not in path, f"a cycle of ties through {c}"
        lev[c] = 0 if not bases[c] else 1 + max(level(b, path + (c,)) for b in bases[c])
        return lev[c]

    for c in tied:
        level(c)
    top = max(lev.values())
    rows = {l: sorted([c for c in tied if lev[c] == l], key=num) for l in range(top + 1)}
    band = [c for c in ids if c not in tied]

    def spread(row):
        n = len(row)
        step = min((W - 2 * MARGIN) / max(n - 1, 1), 128)
        x0 = W / 2 - step * (n - 1) / 2
        return {c: x0 + i * step for i, c in enumerate(row)}

    x = {}
    for l in rows:
        x.update(spread(rows[l]))
    for _ in range(4):
        for l in range(1, top + 1):
            rows[l].sort(key=lambda c: (sum(x[b] for b in bases[c]) / len(bases[c]), x[c], num(c)))
            x.update(spread(rows[l]))
        for l in range(top - 1, -1, -1):
            rows[l].sort(key=lambda c: ((sum(x[d] for d in deps[c]) / len(deps[c])) if deps[c] else x[c], x[c],
                                        num(c)))
            x.update(spread(rows[l]))
    y = {}
    for l in rows:
        for c in rows[l]:
            y[c] = ROW_Y0 + (top - l) * ROW_GAP
    band_y = ROW_Y0 + top * ROW_GAP + BAND_GAP
    x.update(spread(band))
    for c in band:
        y[c] = band_y
    return x, y, rows, band, band_y, lev


def radius(n):
    return 9 + 3.1 * math.sqrt(n)


def f1(v):
    return f"{v:.1f}"


def round2(frac):
    q = Fraction(frac) * 100
    return Fraction(int(q) + (1 if q - int(q) >= Fraction(1, 2) else 0), 100)


def reach_of(row):
    return f"{float(round2(row['score']['fraction'])):.2f}"


# the reach bar (version 5): the entry example's bar, drawn in CSS: one gradient fixed along the whole track (each of
# the PI's four colours at the middle of its level's range, as in the entry's pictures), revealed up to the score; the
# track is 120 pixels in the table and 90 in a claim's lists, where the panel is narrow; the level is that of the
# score as printed, on the PI's table's names and ranges
LEVELS = [("Marginal", Fraction(0), Fraction(29, 100)), ("Moderate", Fraction(30, 100), Fraction(69, 100)),
          ("High", Fraction(70, 100), Fraction(89, 100)), ("Max", Fraction(90, 100), Fraction(1))]


def level(v):
    hit = [name for name, lo, hi in LEVELS if lo <= v <= hi]
    assert len(hit) == 1, v
    return hit[0]


def reach_bar(row):
    v = round2(row["score"]["fraction"])
    assert (v * 100).denominator == 1 and 0 <= v <= 1, v
    fill = f'<i style="width:{int(v * 100)}%"></i>' if v else ""
    return (f'<span class="bar" aria-hidden="true">{fill}</span><span class="rv"><b>{float(v):.2f}</b>&nbsp;'
            f'({level(v)})</span>')


# ---------------------------------------------------------------- the readings in full

def ids_marked(text, loc, claim_ids):
    """The text escaped; in a card made from the index, each fragment or gap id followed by its place in square
    brackets, and each claim id linked to its claim."""
    t = esc(text)

    def one(m):
        i = m.group(0)
        if i in claim_ids:
            return f'<a href="#claim-{i}">{i}</a>'
        if i in loc:
            return f"{i} [{esc(loc[i])}]"
        return i
    return re.sub(r"\b(?:F\d+|DG\d+|C\d\d)\b", one, t)


def humane(word):
    return word.replace("_", " ")


def rest_of_reading(form, obj, loc, claim_ids):
    """The fields of a reading not in the text the coders read, as its model wrote them, labelled."""
    sys_ = form == "system"

    def tx(s):
        return ids_marked(s, loc, claim_ids) if sys_ else esc(s)

    def li(items):
        return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

    def pages(ps):
        return ", ".join(tx(p) for p in ps)

    def in_paper(printed, ps):
        if printed:
            return "yes" + (f" ({pages(ps)})" if ps else "")
        return "no" + (f"; pages it gives: {pages(ps)}" if ps else "")

    B = []

    def part(label, body):
        B.append(f"<h4>{label}</h4>{body}")

    if form in ("plain", "places"):
        if form == "places":
            p = obj["place"]
            part(f"The place ({esc(p['page'])})", f"<p><em>One reading:</em> {esc(p['reading_one'])}</p>"
                 f"<p><em>The other:</em> {esc(p['reading_two'])}</p>")
        w = obj["what_it_would_take_to_cohere"]
        printed = in_paper(w["printed"], w["pages"])
        part("What it would take to cohere", f"<p>{esc(w['observation'])}</p><p><em>In the paper:</em> {printed}</p>")
        part("Strains against it", li(f"{esc(s['page'])}: {esc(s['why'])}" for s in obj["strains_against"]))
        part("Who could complete it", f"<p>{esc(obj['who_could_complete_it'])}</p>")
        return "".join(B)
    # the cards: the middle prompt's (chat 26) and those made from the index (chat 23)
    if sys_:
        part("The wager, as the model wrote it", f"<p>{tx(obj['wager']['statement'])}</p>")
    part("Move", f"<p>{esc(humane(obj['move']))}</p>")
    part("Starting material", f"<p>{tx(obj['trigger'])}</p>")
    part("The paper's claim it bears on most directly", f"<p>{tx(obj['claim'])}</p>")
    part("The paper's reading", f"<p>{tx(obj['incumbent_reading'])}</p>")
    wg = obj["wager"]
    seeds = wg.get("seed_fragments") if sys_ else wg.get("seed_pages")
    if seeds:
        part("Seed passages", f"<p>{pages(seeds)}</p>")
    jobs = obj["fragment_jobs"] if sys_ else obj["passage_jobs"]
    part("Evidence, passage by passage", li(f"{tx(k)}: {tx(v)}" for k, v in jobs.items()))
    w = wg["what_it_would_take_to_cohere"]
    shown = w.get("printed_fragments") if sys_ else w.get("printed_pages")
    printed = in_paper(w["printed"], shown)
    part("What it would take to cohere", f"<p>{tx(w['observation'])}</p><p><em>In the paper:</em> {printed}</p>"
         f"<p><em>Where the model looked:</em> {tx(w['basis'])}</p>")
    part("Strains against it", li(tx(s) for s in wg["strains_against"]))
    part("Who could complete it", f"<p>{tx(wg['who_could_complete_it'])}</p>")
    g = []
    for it in obj["grounded_in"]:
        if it["kind"] == "missing_fact":
            g.append(f"<em>A missing fact:</em> {tx(it['question'])} <em>Bears on:</em> {tx(it['bears_on'])}. "
                     f"<em>If one way:</em> {tx(it['if_one_way'])} <em>If the other:</em> {tx(it['if_the_other'])}")
        elif it["kind"] == "divergence":
            g.append(f"<em>A divergence</em> between {'; '.join(tx(i) for i in it['items'])}: {tx(it['how'])}")
        else:
            raise SystemExit(f"grounded_in kind {it['kind']}")
    part("Grounded in", li(g))
    rc = obj["reach"]
    names = (("same_construct", "Claims on the same construct"), ("same_outcome", "Claims on the same outcome"),
             ("feature_elsewhere", "Where the feature recurs"), ("orphans_used", "Passages tied to no claim"))
    rl = [f"<em>{lab}:</em> {pages(rc[k])}" for k, lab in names if rc.get(k)]
    if rl:
        part("What else reads differently", li(rl))
    part("The rival reading", f"<p>{tx(obj['rival'])}</p>")
    sp = obj.get("split")
    if sp:
        part("The split", li([f"<em>{esc(sp['side_x']['label'])}</em> ({pages(sp['side_x']['pages'])})",
                               f"<em>{esc(sp['side_y']['label'])}</em> ({pages(sp['side_y']['pages'])})",
                               f"<em>Separating feature:</em> {esc(sp['separating_feature'])}",
                               f"<em>Independent of the outcome:</em> {esc(sp['independent_of_outcome'])}",
                               f"<em>Sorts correctly:</em> {esc(sp['sorts_correctly'])}"]
                              + [f"<em>Confound:</em> {esc(c)}" for c in sp["confounds"]]))
    return "".join(B)


# ---------------------------------------------------------------- the paper's words, highlighted

V3_PAGE = "84582d04d5d8b69f16c916249f45a2cec9f2b40cd1eb4d0b5c0e37c1cceff450"


def quote_runs(got):
    """{reading: [(words, pages label), ...]}, longest first, from the quotation check of version 3."""
    q = json.loads(got["quotation_check_bechky.json"])
    assert q["rule"]["run"] == 6 and q["page_sha256"] == V3_PAGE, "not the check of version 3"
    out = collections.defaultdict(list)
    for f in q["runs"]:
        if f["class"] != "a reading":
            assert f["class"] == "the paper's citation", f["class"]
            continue
        r = f["where"][len("reading-"):]
        ps = f["paper_pages"]
        label = ("p. " if len(ps) == 1 else "pp. ") + ", ".join(str(p) for p in ps)
        out[r].append((f["words"], label))
    for r in out:
        out[r].sort(key=lambda x: -len(x[0].split()))
    return dict(out)


def run_pattern(words):
    """A run's words, as check_quotations.py takes them, found in text: letters and digits as they stand, any other
    characters between them, the case and the apostrophe's form free."""
    tp = [re.escape(w).replace("'", "['\u2019]") for w in words.split()]
    return re.compile(r"(?<![A-Za-z0-9])" + r"[^A-Za-z0-9]+".join(tp) + r"(?![A-Za-z0-9])", re.I)


def mark_quotes(panel, runs):
    """Highlight every occurrence of each run in a reading's panel, in the reading's own text (the text the coders
    read and the fold), longest run first and never inside another; returns the panel and the count of each run."""
    parts = re.split(r"(<[^>]+>)", panel)
    stack, counts = [], collections.Counter()
    for k, part in enumerate(parts):
        if part.startswith("<"):
            m = re.match(r"<(/?)([a-z0-9]+)([^>]*)>", part)
            closing, name, attrs = m.group(1), m.group(2), m.group(3)
            if closing:
                while stack and stack.pop()[0] != name:
                    pass
            elif not attrs.endswith("/"):
                cm = re.search(r'class="([^"]*)"', attrs)
                stack.append((name, cm.group(1) if cm else ""))
            continue
        if not part:
            continue
        inside = any((n == "p" and c == "rtext") or (n == "details" and c == "rest") for n, c in stack)
        if not inside or any(n in ("h2", "h3", "h4", "summary") for n, _ in stack):
            continue
        raw = html.unescape(part)
        spans = []
        for words, label in runs:
            for m in run_pattern(words).finditer(raw):
                if all(m.end() <= a or m.start() >= b for a, b, _, _ in spans):
                    spans.append((m.start(), m.end(), words, label))
        if not spans:
            continue
        assert esc(raw) == part, "a text node that does not escape back to itself"
        spans.sort()
        out, at = [], 0
        for a, b, words, label in spans:
            out.append(esc(raw[at:a]))
            out.append(f'<mark class="pw" data-p="{esc(label)}" title="The paper\'s own words, {esc(label)}">'
                       f"{esc(raw[a:b])}</mark>")
            counts[words] += 1
            at = b
        out.append(esc(raw[at:]))
        parts[k] = "".join(out)
    return "".join(parts), counts


def page(d, inputs_note):
    ids, claims, kinds, core, edges = d["ids"], d["claims"], d["kinds"], d["core"], d["edges"]
    rows, titles, chat, model, hits, labels = d["rows"], d["titles"], d["chat"], d["model"], d["hits"], d["labels"]
    n_read = len(rows)
    forms = collections.Counter(d["srcs"][r][0] for r in rows)
    assert set(forms) == {"system", "middle", "plain", "places"}, forms
    n_cards = forms["system"] + forms["middle"]  # the wager statement alone was coded
    n_full = forms["plain"] + forms["places"]  # the wager and its evidence were coded
    assert n_cards + n_full == n_read
    either = {c: sorted([r for r in rows if any(c in hits[r][cd] for cd in CODERS)], key=num) for c in ids}
    both = {c: [r for r in either[c] if all(c in hits[r][cd] for cd in CODERS)] for c in ids}
    reached = {c: sorted([r for r in rows if r not in either[c] and any(labels[r][cd].get(c) for cd in CODERS)],
                         key=num) for c in ids}
    score = {r: Fraction(rows[r]["score"]["fraction"]) for r in rows}

    def by_reach(rs):
        return sorted(rs, key=lambda r: (-score[r], num(r)))

    def through_labels(r, c):
        labs = [labels[r][cd].get(c) for cd in CODERS]
        if labs[0] == labs[1]:
            return f"{esc(LABEL_NAME[labs[0]] if labs[0] else 'no effect')}, both coders"
        return "; ".join(f"{CODER_NAME[cd]}: {esc(LABEL_NAME[lb] if lb else 'no effect')}"
                         for cd, lb in zip(CODERS, labs))

    x, y, lrows, band, band_y, lev = layout(ids, edges)
    H = int(band_y + 64)
    nb = collections.defaultdict(set)
    for e in edges:
        nb[e["claim"]].add(e["base"])
        nb[e["base"]].add(e["claim"])
    S = [f'<svg viewBox="0 0 {W} {H}" role="group" aria-label="the claims and the ties between them">']
    S.append(f'<rect class="band" x="16" y="{f1(band_y - 58)}" width="{W - 32}" height="{f1(H - band_y + 40)}" '
             'rx="10"/>')
    S.append(f'<text class="bandlabel" x="30" y="{f1(band_y - 38)}">No ties in the settled map</text>')
    for e in sorted(edges, key=lambda e: (num(e["claim"]), num(e["base"]))):
        a, b = e["base"], e["claim"]
        x1, y1, x2, y2 = x[a], y[a], x[b], y[b]
        ym = (y1 + y2) / 2
        cls = f'edge {"nec" if e["strength"] == "necessary" else "con"} e-{a} e-{b}'
        S.append(f'<path class="{cls}" d="M{f1(x1)},{f1(y1)} C{f1(x1)},{f1(ym)} {f1(x2)},{f1(ym)} {f1(x2)},{f1(y2)}">'
                 f'<title>{b} rests on {a}: {esc(e["type"])}, {esc(e["strength"])}</title></path>')
    for c in ids:
        n = len(either[c])
        r = radius(n)
        cls = " ".join(["node", kinds[c]] + [f"nb-{o}" for o in sorted(nb[c], key=num)])
        tip = (f"{c} ({kinds[c]}{', core' if c in core else ''}): {claims[c]['statement']} Engaged by {n} of the "
               f"{n_read} readings.")
        S.append(f'<a href="#claim-{c}" id="node-{c}" class="{cls}" aria-label="{esc(c)}, {kinds[c]}'
                 f'{", core" if c in core else ""}, engaged by {n} readings"><title>{esc(tip)}</title>')
        if c in core:
            S.append(f'<circle class="ring" cx="{f1(x[c])}" cy="{f1(y[c])}" r="{f1(r + 4.5)}"/>')
        S.append(f'<circle class="dot" cx="{f1(x[c])}" cy="{f1(y[c])}" r="{f1(r)}"/>')
        if n:
            S.append(f'<text class="count" x="{f1(x[c])}" y="{f1(y[c] + 4.2)}">{n}</text>')
        S.append(f'<text class="id" x="{f1(x[c])}" y="{f1(y[c] + r + (4.5 if c in core else 0) + 17)}">{c}</text>')
        S.append("</a>")
    S.append("</svg>")

    def clink(c):
        return f'<a href="#claim-{c}">{c}</a>'

    def tops(kind_):
        cs = [c for c in ids if kinds[c] == kind_]
        return sorted(cs, key=lambda c: (-len(either[c]), -len(both[c]), num(c)))[:3]

    def reading_li(r, extra, short):
        # the coders who say so kept on one line when short (both coders, or one coder only); the labels of a
        # reading that reaches the claim through its ties may wrap; the dot stays with the score, so that a line
        # that wraps never starts with it
        return (f'<li><a class="rt" href="#reading-{r}">{esc(titles[r])}</a><span class="rm">{reach_bar(rows[r])}'
                f'&nbsp;· <span class="{"cw" if short else "cl"}">{extra}</span></span></li>')

    P = []
    for c in ids:
        ins = [e for e in edges if e["claim"] == c]
        outs = [e for e in edges if e["base"] == c]
        tags = [f'<span class="tag {kinds[c]}">{kinds[c]}</span>']
        if c in core:
            tags.append('<span class="tag core">core</span>')
        if claims[c].get("stated_as") == "ventured":
            tags.append('<span class="tag">ventured</span>')
        rest = "; ".join(f"{clink(e['base'])} ({esc(e['type'])}, {esc(e['strength'])})"
                         for e in sorted(ins, key=lambda e: num(e["base"]))) or "no other claim"
        sup = "; ".join(f"{clink(e['claim'])} ({esc(e['type'])}, {esc(e['strength'])})"
                        for e in sorted(outs, key=lambda e: num(e["claim"]))) or "no other claim"
        con = "; ".join(f"{esc(k)}" + (f" (also {', '.join(clink(o) for o in others)})" if others else "")
                        for k, others in d["cons"][c]) or "none"
        L = [f'<section class="panel" id="claim-{c}" aria-labelledby="h-{c}">',
             '<p class="back"><a href="#network">Close</a></p>',
             f'<h2 id="h-{c}">{c} {"".join(tags)}</h2>', f'<p class="stmt">{esc(claims[c]["statement"])}</p>',
             f'<dl><dt>Rests on</dt><dd>{rest}</dd><dt>Supports</dt><dd>{sup}</dd>'
             f'<dt>Constructs</dt><dd>{con}</dd></dl>']
        e, bth = either[c], both[c]
        if e:
            L.append(f'<h3>Engaged by {len(e)} of the {n_read} readings</h3>')
            L.append(f'<p class="sub">{len(bth)} by both coders. Click a title to read the reading in full.</p>')
            L.append('<ol class="readings">')
            for r in by_reach(e):
                who = [cd for cd in CODERS if c in hits[r][cd]]
                extra = "both coders" if len(who) == 2 else f"{CODER_NAME[who[0]]} only"
                L.append(reading_li(r, extra, True))
            L.append("</ol>")
        else:
            L.append('<h3>No reading engages it directly</h3>')
        if reached[c]:
            L.append(f'<details><summary>Reached only through its ties by {len(reached[c])} more readings'
                     '</summary><ol class="readings">')
            for r in by_reach(reached[c]):
                L.append(reading_li(r, through_labels(r, c), False))
            L.append("</ol></details>")
        L.append("</section>")
        P.append("".join(L))

    # the readings in full
    claim_ids = set(ids)

    def who_note(r):
        """Who wrote the reading and who coded it, for a reader who has not read the protocol (version 5)."""
        twice = ""
        if model[r] in CODER_NAME.values():
            twice = (f" {esc(model[r])} is thus both the writer of this reading, in chat {esc(chat[r])}, and one of "
                     "its coders, in another chat.")
        return (f'<p class="who"><strong>Who wrote it, who coded it.</strong> A language model, {esc(model[r])}, '
                f'wrote this reading in chat {esc(chat[r])}, asked for alternative readings of the paper. The two '
                f'coders are models too, {CODER_NAME["gemini"]} and {CODER_NAME["astra"]}, each working in a chat '
                "of its own and not told who wrote the reading: they read the part of it shown first below and "
                "recorded which of the paper's claims it engages, and how. The claims it engages and its reach come "
                f"from their codes.{twice}</p>")
    R = []
    for r in by_reach(rows):
        form, obj = d["srcs"][r]
        ch = []
        for c in sorted({c for cd in CODERS for c in hits[r][cd]}, key=num):
            who = [cd for cd in CODERS if c in hits[r][cd]]
            ch.append(f"{clink(c)} ({'both coders' if len(who) == 2 else CODER_NAME[who[0]] + ' only'})")
        through = []
        for c in ids:
            if any(c in hits[r][cd] for cd in CODERS):
                continue
            if any(labels[r][cd].get(c) for cd in CODERS):
                through.append(f"{clink(c)} ({through_labels(r, c)})")
        L = [f'<section class="panel rpanel" id="reading-{r}" aria-labelledby="h-{r}">',
             '<p class="back"><a href="#network">Close</a></p>',
             f'<h2 id="h-{r}">{r} <span class="tag">reading</span></h2>',
             f'<p class="rtitle">{esc(titles[r])}</p>',
             f'<p class="sub">Reach {reach_of(rows[r])} · {esc(model[r])}, chat {esc(chat[r])}, '
             f'{esc(CHATS[chat[r]][4])}</p>',
             who_note(r),
             f'<dl><dt>Engages</dt><dd>{"; ".join(ch) or "no claim, by either coder"}</dd>'
             f'<dt>Through ties</dt><dd>{"; ".join(through) or "no other claim"}</dd></dl>',
             '<p class="sub">On the map, a red ring marks the claims it engages; a dashed ring, those it reaches '
             'only through their ties.</p>',
             '<h3>The reading, as the coders read it</h3>',
             f'<p class="rtext">{esc(d["texts"][r])}</p>',
             '<details class="rest"><summary>The rest of the reading, as its model wrote it (not coded)</summary>',
             rest_of_reading(form, obj, d["loc"], claim_ids), "</details></section>"]
        panel = "".join(L)
        if r in d["quotes"]:
            panel, cnt = mark_quotes(panel, d["quotes"][r])
            for words, _ in d["quotes"][r]:
                assert cnt[words] >= 1, (r, words)
            d["marked"][r] = cnt
        R.append(panel)

    theo, emp = tops("theoretical"), tops("empirical")
    methods = [c for c in ids if kinds[c] == "method"]
    intro = ('<section class="intro"><h2>Click a claim</h2><p>Its panel gives the claim as the index states it, the '
             'claims it rests on and supports, the constructs it shares with other claims, and the readings that '
             'engage it, each by title and reach, with the coders who say so. Reach is shown as a bar filled to '
             'the score, with the score\'s level: Marginal (0.00 to 0.29), Moderate (0.30 to 0.69), High (0.70 to '
             '0.89) or Max (0.90 to 1.00). Readings that reach the claim only through its ties are listed apart, each '
             'with what it would mean for the claim if the reading were right: support in question, when the '
             'claim\'s necessary support runs through a claim the reading engages; support partly in question, '
             'when only contributing support does; significance in question, through a tie of significance; '
             'restated, through a comparative tie (the closure\'s file codes these unsupported, weakened, idle '
             'and restated). '
             'Click a reading\'s title to read it in full: its panel says who wrote it and who coded it.</p>'
             '<p><strong>Most often engaged.</strong> Theoretical: '
             + ", ".join(f"{clink(c)} ({len(either[c])})" for c in theo) + ". Empirical: "
             + ", ".join(f"{clink(c)} ({len(either[c])})" for c in emp) + ". Method: "
             + ", ".join(f"{clink(c)} ({len(either[c])})" for c in methods) + ".</p></section>")
    trs = []
    for c in ids:
        ins = sorted({e["base"] for e in edges if e["claim"] == c}, key=num)
        outs = sorted({e["claim"] for e in edges if e["base"] == c}, key=num)
        trs.append(f"<tr><td>{clink(c)}</td><td>{kinds[c]}</td><td>{'core' if c in core else ''}</td>"
                   f"<td class=\"n\">{len(either[c])}</td><td class=\"n\">{len(both[c])}</td>"
                   f"<td>{', '.join(clink(o) for o in ins)}</td><td>{', '.join(clink(o) for o in outs)}</td></tr>")
    rtrs = []
    for r in by_reach(rows):
        cs = sorted({c for cd in CODERS for c in hits[r][cd]}, key=num)
        rtrs.append(f"<tr><td class=\"rch\">{reach_bar(rows[r])}</td><td><a href=\"#reading-{r}\">"
                    f"{esc(titles[r])}</a> ({r})</td><td>{', '.join(clink(c) for c in cs)}</td></tr>")
    css_sel = []
    for c in ids:
        css_sel.append(f"body:has(#claim-{c}:target) #node-{c},body:has(#claim-{c}:target) .nb-{c}{{opacity:1}}")
        css_sel.append(f"body:has(#claim-{c}:target) #node-{c} .dot{{stroke:var(--fg);stroke-width:3}}")
        css_sel.append(f"body:has(#claim-{c}:target) #node-{c} .id{{font-weight:700}}")
        css_sel.append(f"body:has(#claim-{c}:target) .edge.e-{c}{{stroke:var(--fg);opacity:1}}")
    for r in sorted(rows, key=num):
        hit = sorted({c for cd in CODERS for c in hits[r][cd]}, key=num)
        thr = [c for c in ids if c not in hit and any(labels[r][cd].get(c) for cd in CODERS)]
        if hit + thr:
            css_sel.append(",".join(f"body:has(#reading-{r}:target) #node-{c}" for c in hit + thr) + "{opacity:1}")
        if hit:
            css_sel.append(",".join(f"body:has(#reading-{r}:target) #node-{c} .dot" for c in hit)
                           + "{stroke:var(--hit);stroke-width:4}")
        if thr:
            css_sel.append(",".join(f"body:has(#reading-{r}:target) #node-{c} .dot" for c in thr)
                           + "{stroke:var(--fg);stroke-width:2;stroke-dasharray:3 2.5}")
    css = (":root{--bg:#fbfaf7;--fg:#1f2328;--mute:#5f6670;--rule:#e2e0d9;--card:#ffffff;--band:#f1efe9;"
           "--theo:#2f62a3;--emp:#c56a1c;--meth:#8a9099;--edge:#a3abb5;--link:#2f62a3;--hit:#c0262d;--pw:#f9eec5}"
           "@media (prefers-color-scheme: dark){:root{--bg:#141619;--fg:#e9e7e2;--mute:#a4aab2;--rule:#2c3036;"
           "--card:#1b1e22;--band:#1d2025;--theo:#7fa9df;--emp:#efa361;--meth:#9aa1aa;--edge:#5c6570;"
           "--link:#8fb6ea;--hit:#ff6b6b;--pw:#4a3e19}}"
           "*{box-sizing:border-box}html{scroll-behavior:auto}"
           "body{background:var(--bg);color:var(--fg);margin:0;font:15px/1.5 -apple-system,BlinkMacSystemFont,"
           "'Segoe UI',Helvetica,Arial,sans-serif}"
           "a{color:var(--link)}main{max-width:980px;margin:0 auto;padding:20px 16px 40px}"
           "h1{font-size:21px;line-height:1.3;margin:4px 0 6px}p{margin:6px 0 10px}.cite{color:var(--mute);"
           "font-size:13px}.lede{max-width:70ch}.coded{border-left:3px solid var(--rule);padding-left:10px}"
           ".pw,.pwk{background:var(--pw);color:inherit;border-radius:3px;padding:0 2px}"
           ".pw::after{content:attr(data-p);font-size:10.5px;color:var(--mute);margin-left:3px;vertical-align:super;"
           "line-height:0;white-space:nowrap}"
           ".bar{--bw:120px;display:inline-block;position:relative;width:var(--bw);height:12px;border-radius:6px;"
           "background:rgba(148,163,184,.22);vertical-align:-1px;margin-right:7px}.readings .bar{--bw:90px}"
           ".bar>i{position:absolute;left:0;top:0;bottom:0;border-radius:6px;background:linear-gradient(90deg,"
           "#94A3B8 0%,#94A3B8 14.5%,#2563EB 49.5%,#1E40AF 79.5%,#0F172A 95%,#0F172A 100%) 0 0/var(--bw) 100% "
           "no-repeat}"
           ".bar::after{content:\"\";position:absolute;inset:0;border-radius:6px;"
           "box-shadow:inset 0 0 0 1px rgba(148,163,184,.55)}"
           ".rv,.cw{white-space:nowrap}td.rch{white-space:nowrap}"
           ".who{font-size:13px;color:var(--mute);border-left:3px solid var(--rule);padding-left:10px;"
           "margin:8px 0 10px}.who strong{color:var(--fg)}"
           ".legend{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:13px;color:var(--mute);margin:12px 0 6px;"
           "padding:0;list-style:none}.legend li{display:flex;align-items:center;gap:6px}"
           ".sw{display:inline-block;width:12px;height:12px;border-radius:50%}.sw.theoretical{background:var(--theo)}"
           ".sw.empirical{background:var(--emp)}.sw.method{background:var(--meth)}"
           ".sw.core{background:transparent;border:2px solid var(--fg);width:14px;height:14px}"
           ".ln{display:inline-block;width:26px;height:0;border-top:2px solid var(--edge)}"
           ".ln.con{border-top:1.5px dashed var(--edge)}"
           "figure{margin:8px 0 0;background:var(--card);border:1px solid var(--rule);border-radius:12px;"
           "padding:6px;overflow-x:auto}svg{display:block;width:100%;min-width:680px;height:auto}"
           ".band{fill:var(--band)}.bandlabel{fill:var(--mute);font-size:12px}"
           ".edge{fill:none;stroke:var(--edge);stroke-width:2;opacity:.9}.edge.con{stroke-width:1.4;"
           "stroke-dasharray:5 4}"
           ".node .dot{stroke:var(--card);stroke-width:1.5}.node.theoretical .dot{fill:var(--theo)}"
           ".node.empirical .dot{fill:var(--emp)}.node.method .dot{fill:var(--meth)}"
           ".node .ring{fill:none;stroke:var(--fg);stroke-width:2}"
           ".node .count{fill:#fff;font-size:11.5px;font-weight:700;text-anchor:middle;pointer-events:none}"
           ".node .id{fill:var(--fg);font-size:12.5px;text-anchor:middle;paint-order:stroke;stroke:var(--card);"
           "stroke-width:4px;stroke-linejoin:round}"
           ".node:hover .dot,.node:focus .dot{stroke:var(--fg);stroke-width:2.5}"
           "body:has(.panel:target) .edge{opacity:.16}body:has(.panel:target) .node{opacity:.4}"
           + "".join(css_sel) +
           ".panels{margin-top:18px}.panel{display:none}.panel:target{display:block}"
           ".panels:has(.panel:target) .intro{display:none}"
           ".panel,.intro{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:14px 16px}"
           ".panel h2,.intro h2{font-size:17px;margin:2px 0 8px;display:flex;flex-wrap:wrap;align-items:center;"
           "gap:8px}.panel h3{font-size:15px;margin:14px 0 2px}.sub{color:var(--mute);font-size:13px;margin:0 0 6px}"
           ".tag{font-size:11.5px;font-weight:600;border:1px solid var(--rule);border-radius:999px;padding:1px 8px;"
           "color:var(--mute)}.tag.theoretical{color:var(--theo);border-color:var(--theo)}"
           ".tag.empirical{color:var(--emp);border-color:var(--emp)}.tag.method{color:var(--meth);"
           "border-color:var(--meth)}.tag.core{color:var(--fg);border-color:var(--fg)}"
           ".stmt{font-size:15px;margin:0 0 8px}dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 12px;"
           "margin:8px 0;font-size:13.5px}dt{color:var(--mute)}dd{margin:0}"
           ".readings{margin:6px 0 0;padding-left:22px;font-size:13.5px}.readings li{margin:0 0 7px}"
           ".rt{display:block}.rm{display:block;color:var(--mute);font-size:12.5px}"
           ".rtitle{font-size:16px;font-weight:600;margin:0 0 4px}.rtext{font-size:14.5px}"
           ".rest h4{font-size:13.5px;margin:12px 0 2px;color:var(--mute)}.rest p,.rest li{font-size:14px}"
           ".rest ul{margin:4px 0 6px;padding-left:20px}.rest li{margin:0 0 5px}"
           "details{margin-top:12px;font-size:13.5px}summary{cursor:pointer;color:var(--link)}"
           ".back{margin:0 0 4px;font-size:13px}"
           "table{border-collapse:collapse;width:100%;margin-top:22px;font-size:13.5px}"
           "th,td{border-top:1px solid var(--rule);padding:5px 6px;text-align:left;vertical-align:top}"
           "th{color:var(--mute);font-weight:600}td.n,th.n{text-align:right}h2.tablehead{font-size:16px;"
           "margin:26px 0 0}.foot{color:var(--mute);font-size:12.5px;margin-top:18px}.tablewrap{overflow-x:auto}"
           "@media (min-width:1180px){main{max-width:none;margin:0;padding:20px 420px 40px 28px}"
           ".panels{position:fixed;top:0;right:0;width:400px;height:100vh;overflow-y:auto;margin:0;"
           "padding:20px 20px 40px 0}}")
    lede = (f"Each circle is one of the {len(ids)} claims of the paper's index. Its size shows how many of the "
            f"{n_read} alternative readings engage it, as either of two coders ({CODER_NAME['gemini']} and "
            f"{CODER_NAME['astra']}) codes them; the number inside is that count. Colour gives the claim's kind, and "
            "a dark ring marks the paper's core claims. A line joins two claims when the settled map says the upper "
            "one rests on the lower one: solid when the support is necessary, dashed when it contributes. The lines "
            "are the map's ties, not shared constructs; each claim's constructs are listed in its panel. Hover a "
            "claim for its statement; click it for its panel, and a reading's title for the reading in full.")
    about = ("<strong>What these readings are.</strong> Each is an alternative reading of the paper's own "
             "evidence, in the tradition of Black, Carlile and Repenning (2004): an abductive extension or "
             "re-theorization of the study, not an error-catching audit or a replication. A reading engages a "
             "claim when a coder codes it as inverting the claim, offering another mechanism for it, rereading "
             "its evidence or questioning its premise. The paper's author is invited as a co-interpreter of "
             "what the field material can further support, and can append a brief commentary to the paper's "
             "entry.")
    coded = ("<strong>What was coded.</strong> The two coders, whose codes give the claims each reading "
             "engages, the labels and the reach, read only part of each reading:"
             f" for the {n_full} readings of the plain and places prompts, "
             f"the wager and its evidence; for the {n_cards} cards, the wager statement alone. Each reading's panel "
             "shows that part first, word for word; the rest of the reading, shown folded, was never coded.")
    n_runs, n_rdg = sum(len(v) for v in d["quotes"].values()), len(d["quotes"])
    # one run stands twice in its reading (R10, p. 637), so the page has one highlight more than runs; the note says so
    twice = [(r, w) for r, cnt in d["marked"].items() for w, k in cnt.items() if k > 1]
    assert len(twice) == 1 and d["marked"][twice[0][0]][twice[0][1]] == 2, twice
    words_note = ("<strong>The paper's words.</strong> Where a reading repeats six or more of the paper's words in a "
                  "row, they are highlighted <mark class=\"pwk\">like this</mark>, with the paper's page: "
                  f"{n_runs} runs in {n_rdg} readings, one of them standing twice in its reading, found by checking "
                  "every string on this page against the paper. Before any public version, each is replaced by a note "
                  "giving its length and page.")
    doc = ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
           f"<title>Claims network</title><style>{css}</style></head><body><main>"
           f"<h1>The claims and the readings that engage them</h1><p class=\"cite\">{esc(d['citation'])}</p>"
           f"<p class=\"lede coded\">{about}</p>"
           f"<p class=\"lede\">{lede}</p><p class=\"lede coded\">{coded}</p><p class=\"lede coded\">{words_note}</p>"
           "<ul class=\"legend\"><li><span class=\"sw theoretical\"></span>theoretical</li>"
           "<li><span class=\"sw empirical\"></span>empirical</li><li><span class=\"sw method\"></span>method</li>"
           "<li><span class=\"sw core\"></span>core claim</li><li><span class=\"ln\"></span>rests on, necessary</li>"
           "<li><span class=\"ln con\"></span>rests on, contributing</li></ul>"
           f"<figure id=\"network\">{''.join(S)}</figure>"
           f"<div class=\"panels\">{intro}{''.join(P)}{''.join(R)}</div>"
           "<h2 class=\"tablehead\">The claims</h2>"
           "<div class=\"tablewrap\"><table><thead><tr><th>claim</th><th>kind</th><th>core</th>"
           "<th class=\"n\">readings engaging it</th><th class=\"n\">by both coders</th><th>rests on</th>"
           f"<th>supports</th></tr></thead><tbody>{''.join(trs)}</tbody></table></div>"
           f"<h2 class=\"tablehead\">The {n_read} readings, by reach</h2>"
           "<div class=\"tablewrap\"><table><thead><tr><th>reach</th><th>reading</th>"
           f"<th>engages</th></tr></thead><tbody>{''.join(rtrs)}</tbody></table></div>"
           "<p class=\"foot\">An example for the paper's entry in the shared repository, built by "
           "build_claim_network.py from the frozen index, the settled map, the closure of the relation test's codes, "
           "the reach scores, the readings' titles and texts and the claims' kinds; the same inputs give the same page. "
           "The titles were written by a separate model session from each reading's opening and have not been checked "
           "for faithfulness. Each reading is shown first as the coders read it: for the plain and places prompts, "
           "its wager and evidence; for the cards, its wager statement, with the index's ids turned into places in "
           "the paper; one word of one places reading was changed for the tests (place to passage). The rest of each "
           "reading follows, folded, as its model wrote it, leaving out only ids and bookkeeping; in the cards made "
           "from the index, square brackets give the place of each fragment or gap the model names. Reach is how "
           "much of the paper's argument a reading would unsettle if it were right, scored on the core claims "
           "from the lower of the two codings, so a reading that one coder alone says engages a core claim can "
           "have little reach; it is not worth. Its bar is filled to the score on one gradient along the bar, from "
           "slate blue through cobalt and indigo to obsidian, and its level is that of the score: Marginal (0.00 to "
           "0.29), Moderate (0.30 to 0.69), High (0.70 to 0.89) or Max (0.90 to 1.00). No script; nothing is loaded "
           "from outside.</p>"
           f"</main>{inputs_note}</body></html>\n")
    return doc.encode("utf-8")


def build(folder, outdir):
    index, index_sha, got = load(folder)
    d = model_data(index, got)
    note = "<!-- inputs (sha256): " + "; ".join(
        [f"{bmt.INDEX[PAPER]} {index_sha}"] + [f"{k} {v}" for k, v in INPUTS.items()]) + " -->"
    data = page(d, note)
    text = data.decode("utf-8")
    assert "<script" not in text.lower() and "http:" not in text and "https:" not in text and "@import" not in text
    assert "url(" not in text and "<link" not in text.lower() and "<img" not in text.lower()
    out = os.path.join(outdir, OUT_NAME)
    bmt.write_new(out, data)
    return out, d


def check():
    pages = []
    for _ in range(2):
        tmp = tempfile.mkdtemp()
        out, d = build(HERE, tmp)
        pages.append(open(out, "rb").read())
    assert pages[0] == pages[1], "two builds differ"
    t = pages[0].decode("utf-8")
    assert t.count('<section class="panel" id="claim-') == len(d["ids"]) == 23
    assert t.count('<section class="panel rpanel" id="reading-') == len(d["rows"]) == 28
    for c in d["ids"]:
        assert f'id="claim-{c}"' in t and f'id="node-{c}"' in t and f'href="#claim-{c}"' in t
    for r in d["rows"]:
        assert f'id="reading-{r}"' in t and f'href="#reading-{r}"' in t
    assert t.count('<p class="lede coded"><strong>What was coded.</strong>') == 1
    # version 6: "engages" in the page's own words, and the note on what the readings are
    assert t.count('<p class="lede coded"><strong>What these readings are.</strong>') == 1
    for w in ("hallenged by", "that challenge them", "readings that challenge", "Most often challenged",
              "readings challenging", "<th>challenges</th>", "<dt>Challenges</dt>", "reading challenges it"):
        assert w not in t, w
    # version 7: plain names, not the closure's codes, in the lists and the readings' panels
    shown = re.findall(r'<span class="cl">(.*?)</span>', t) + re.findall(r'<dt>Through ties</dt><dd>(.*?)</dd>', t)
    assert shown and not any(re.search(r"\b(unsupported|weakened|idle|contested)\b", s) for s in shown)
    assert t.count("the closure's file codes these unsupported, weakened, idle and restated") == 1
    assert t.count("<strong>The paper's words.</strong>") == 1 and t.count('<mark class="pwk">') == 1
    marks = re.findall(r'<mark class="pw" data-p="([^"]+)" title="[^"]+">(.*?)</mark>', t)
    n_runs = sum(len(v) for v in d["quotes"].values())
    assert len(marks) == sum(sum(c.values()) for c in d["marked"].values()) == n_runs + 1 == 22, (len(marks), n_runs)
    assert t.count("21 runs in 10 readings, one of them standing twice in its reading") == 1
    assert sorted(d["marked"]) == sorted(d["quotes"]) and len(d["quotes"]) == 10
    assert t.count("(not coded)</summary>") == len(d["rows"]) and "bring down" not in t
    # version 5: the bars, the lists without model or chat, the table without "proposed by", the note in each panel
    assert "proposed by" not in t and t.count('<p class="who"><strong>Who wrote it, who coded it.</strong>') == 28
    n_li = t.count('<li><a class="rt" href="#reading-')
    assert t.count('<span class="bar" aria-hidden="true">') == n_li + 28, (n_li, t.count('class="bar"'))
    for li in re.findall(r'<li><a class="rt" href="#reading-.*?</li>', t):
        assert "chat" not in li and "Fable" not in li and "<span class=\"bar\"" in li, li
    for lab in ("Peripheral", "Substantial"):
        assert lab not in t
    targets = set(re.findall(r'href="#([^"]+)"', t))
    ids_ = set(re.findall(r' id="([^"]+)"', t))
    assert targets <= ids_, sorted(targets - ids_)
    print("check: two builds give the same", len(pages[0]), "bytes; 23 claims, each with its node and panel; 28",
          "readings, each with its panel; every link has its target; no script, nothing loaded from outside;",
          len(marks), "marks of the paper's words, every one of the", n_runs, "runs marked at least once;", n_li + 28,
          "reach bars (", n_li, "in the claims' lists, 28 in the table); 28 notes on who wrote and who coded;",
          "the note on what the readings are, once; no reading said to challenge a claim; the labels by their "
          "plain names")


def main(argv):
    if len(argv) == 2 and argv[0] == "build":
        out, _ = build(HERE, argv[1])
        print("wrote", out)
    elif argv == ["check"]:
        check()
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
