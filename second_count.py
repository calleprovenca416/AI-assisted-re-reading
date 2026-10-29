"""
second_count.py: a cold paper's agreement figures, given a second time with
some records left out.

WHY
---
Pratt's coverage chat ran on another model than Pratt's extraction, so what
it added is counted apart, and so is F109, whose stub that chat rewrote. The
paper's agreement figures are given as they stand, by `agreement.py --paper`,
and a second time without those records. This script gives the second time.

HOW
---
It runs `agreement.py --paper` itself, with every check that script makes on
the whole files, and leaves rows out only after those checks and before any
figure is computed:
  - a claim's row (Stages A and A2, core, stated_as) when its claim is left out;
  - a fragment's row (voice, gloss relation) when its fragment is left out;
  - a link's row (direction) when its fragment or its claim is left out.
Coder 1's codes and the reading calls are left out the same way. The audit
runs on a copy of the corpus without the left-out records, written to a
temporary file that is removed. The log names what is left out and why, says
how many fragments, claims and links are kept, and lists this script and the
list of what is left out among its files.

With an empty list it changes nothing, and its log is the paper's agreement
log byte for byte. That is its check, and it is run before every use.

USAGE
-----
    python3 -B second_count.py --leave-out=<list.json> <the arguments of agreement.py --paper>

<list.json>: {"paper_id": "...", "why": "...", "fragments": [...], "claims": [...]}
--log= names the second count's own file. With a list that is not empty, the
script refuses to write over a log that does not carry the second count's
heading, so that the paper's own agreement log is never written over.
"""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import agreement as A  # noqa: E402

MARK = "**The second count.**"


def touches(ids, frags, claims):
    """Whether a row's ids name a left-out record."""
    return any(i in frags or i in claims for i in ids)


def filtered_corpus(corpus, frags, claims):
    c = json.loads(json.dumps(corpus))
    c["fragments"] = [f for f in c["fragments"] if f["fragment_id"] not in frags]
    for f in c["fragments"]:
        f["citing_claims"] = [x for x in f.get("citing_claims") or [] if x not in claims]
    c["claims"] = [x for x in c["claims"] if x["claim_id"] not in claims]
    for x in c["claims"]:
        if isinstance(x.get("decomposed_into"), list):
            x["decomposed_into"] = [y for y in x["decomposed_into"] if y not in claims]
    c["claim_links"] = [l for l in c["claim_links"]
                        if l["fragment_id"] not in frags and l["claim_id"] not in claims]
    return c


def main(argv):
    leave = [a for a in argv if a.startswith("--leave-out=")]
    rest = [a for a in argv if not a.startswith("--leave-out=")]
    if len(leave) != 1:
        print("REFUSED: give --leave-out=<list.json> once")
        print(__doc__.split("USAGE")[1])
        return 2
    path = leave[0].split("=", 1)[1]
    try:
        spec = json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(f"REFUSED: {path} is not a JSON file that can be read")
        return 1
    frags, claims = set(spec.get("fragments") or []), set(spec.get("claims") or [])
    corpus_args = [a for a in rest if not a.startswith("--")]
    if len(corpus_args) != 1:
        print("REFUSED: one corpus file is expected")
        return 2
    corpus = json.load(open(corpus_args[0], encoding="utf-8"))
    pid = corpus["meta"]["paper_id"]
    if spec.get("paper_id") != pid:
        print(f"REFUSED: the list is for {spec.get('paper_id')!r}, and the corpus is {pid!r}")
        return 1
    known_f = {f["fragment_id"] for f in corpus["fragments"]}
    known_c = {x["claim_id"] for x in corpus["claims"]}
    wrong = sorted((frags - known_f) | (claims - known_c))
    if wrong:
        print(f"REFUSED: the list names records that are not in the corpus: {wrong}")
        return 1
    active = bool(frags or claims)
    opt = {a.split("=", 1)[0]: a.split("=", 1)[1] for a in rest if a.startswith("--") and "=" in a}
    log_path = opt.get("--log")
    if active and log_path and os.path.isfile(log_path):
        head = open(log_path, encoding="utf-8", errors="replace").read(4000)
        if MARK not in head:
            print(f"REFUSED: {log_path} is not a second count's log. The second count is written "
                  "to a file of its own, and never over the paper's agreement log")
            return 1

    orig = {n: getattr(A, n) for n in ("read_returned", "from_corpus", "load_readings",
                                       "audit_under", "paper_results", "paper_log")}

    def read_returned(p, stage, corp, key):
        out = orig["read_returned"](p, stage, corp, key)       # every check, on the whole workbook
        return {tab: [r for r in recs if not touches(r[1], frags, claims)]
                for tab, recs in out.items()}

    def from_corpus(corp, sidecar=None):
        out = orig["from_corpus"](corp, sidecar)
        return {fld: {k: v for k, v in d.items() if not touches(k, frags, claims)}
                for fld, d in out.items()}

    def load_readings(p, rpid, rclaims, digests=None):
        out = orig["load_readings"](p, rpid, rclaims, digests)  # every check, on the whole file
        for part in ("outcome_wording", "direction_sign"):
            out[part] = {cid: v for cid, v in out[part].items() if cid not in claims}
        return out

    temp = []

    def audit_under(corpus_path, voice, coding=None, flagged=()):
        corp = json.load(open(corpus_path, encoding="utf-8"))
        fd, tmp = tempfile.mkstemp(suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(filtered_corpus(corp, frags, claims), fh)
        temp.append(tmp)
        kept_voice = {f: v for f, v in voice.items() if f not in frags}
        return orig["audit_under"](tmp, kept_voice, coding, flagged)

    def paper_results(corpus_path, *a, **k):
        res = orig["paper_results"](corpus_path, *a, **k)
        kept = filtered_corpus(json.load(open(corpus_path, encoding="utf-8")), frags, claims)
        res["counts"] = {"fragments": len(kept["fragments"]), "claims": len(kept["claims"]),
                         "links": len(kept["claim_links"]),
                         "directional": len(A.directional_claims(kept))}
        if res.get("V"):
            res["V"]["removed"] = [f for f in res["V"]["removed"] if f not in frags]
        res["files"] = res["files"] + [
            ("the second count: what is left out", os.path.basename(path), A.sha(path)),
            ("the second count, written by", os.path.basename(__file__),
             A.sha(os.path.abspath(__file__)))]
        return res

    def paper_log(res, label=None):
        text = orig["paper_log"](res, label)
        first, rest_ = text.split("\n", 1)
        out_links = [(l["fragment_id"], l["claim_id"]) for l in corpus["claim_links"]
                     if l["fragment_id"] in frags or l["claim_id"] in claims]
        nat = lambda s: A.natural(s)
        head = (f"{MARK} This log gives the paper's agreement figures a second time, with these "
                f"records left out of every field: fragments {', '.join(sorted(frags, key=nat)) or 'none'}; "
                f"claims {', '.join(sorted(claims, key=nat)) or 'none'}; and every link of a left-out "
                f"fragment or to a left-out claim, {len(out_links)} links. A row is left out when "
                f"any id it names is left out, and only after every check of `agreement.py` has run "
                f"on the whole files. The audit below runs on the corpus without them. "
                f"Why: {' '.join((spec.get('why') or 'not given').split())} "
                f"The figures with every record are in the paper's own agreement log.\n")
        return first + "\n\n" + head + rest_

    if active:
        for n, f in (("read_returned", read_returned), ("from_corpus", from_corpus),
                     ("load_readings", load_readings), ("audit_under", audit_under),
                     ("paper_results", paper_results), ("paper_log", paper_log)):
            setattr(A, n, f)
    try:
        return A.paper(rest)
    finally:
        for n, f in orig.items():
            setattr(A, n, f)
        for t in temp:
            try:
                os.remove(t)
            except OSError:
                pass


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
