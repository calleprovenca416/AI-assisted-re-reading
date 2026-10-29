"""
Build the markers' readings files for the wager test (T29), in one command.

    python3 build_marker_packs.py <out_dir> [--seed=20261011]

For each paper it puts every reading of every arm into one form, prose that
cites the paper by page in parentheses, so that a marker can check, sentence
by sentence, what each asserts about the paper:

    the system's cards     stage2/<paper>_cards/*_01.json, the wager statement.
                           Every fragment, claim and gap id becomes the place in
                           the paper that the frozen corpus gives for it. Inside
                           parentheses: the place alone for a fragment, "the
                           paper's claim at" or "the paper's open question at"
                           the place for a claim or a gap. In the running text:
                           "the passage on" the place (ids that run together are
                           named once, "the passages on" their places), "the
                           paper's claim" or "the paper's open question" with
                           the place in parentheses after it, and "claims in"
                           a claim becomes "claims" with the place. A fragment's
                           gloss becomes the author's characterisation on the
                           place. The record's words become the paper's: stub
                           and fragment become passage, the corpus becomes the
                           paper, a sentence's opening "The record" becomes "The
                           paper", and "This unit speaks" (the group a retelling
                           follows) becomes "This group speaks". A sentence that
                           opened on an id opens on a capital.
    the middle arm         stage2/baseline_replies/reply_24 and reply_26, the
                           wager statement.
    the plain arm          stage2/baseline_replies/reply_25 and reply_27, the
                           wager, then each piece of evidence's job with its page
                           in parentheses at the end of the job's first sentence,
                           since this arm's prompt keeps its evidence out of the
                           statement.

In all three arms the pages are then made alike: lettered pages (p. 480a) plain
(p. 480), a range as pp. 477–478, and a page repeated next to itself in a list
named once. Nothing else of a reading goes in: no move, trigger, rival, grounds,
strains, attack status or field names. The readings of a paper are shuffled with
a fixed seed and numbered P01 or B01 onward, and each is split into sentences,
P01-01 onward. Writes READINGS_pratt.md and READINGS_bechky.md, which go to the
markers, and KEY.json, which says which reading came from where and goes to
nobody.
"""
import glob
import json
import os
import random
import re
import sys

PAPERS = {
    "pratt": {"corpus": "pratt_2000_v1.json", "cards": "stage2/pratt_2000_cards",
              "middle": "stage2/baseline_replies/reply_24_pratt_reading.json",
              "plain": "stage2/baseline_replies/reply_25_pratt_plain.json",
              "prefix": "P"},
    "bechky": {"corpus": "bechky_2020_v1.json", "cards": "stage2/bechky_2020_cards",
               "middle": "stage2/baseline_replies/reply_26_bechky_reading.json",
               "plain": "stage2/baseline_replies/reply_27_bechky_plain.json",
               "prefix": "B"},
}

ABBREV = ("p", "pp", "n", "nn", "e.g", "i.e", "cf", "vs", "Fig", "al", "St", "Dr",
          "Mr", "Ms", "No", "Vol", "U.S", "ca")
QUOTES = "'\"\u2019\u201d"
DASH = "\u2013"


def sentences(text):
    """Split prose into sentences without breaking on page or note abbreviations."""
    t = " ".join(text.split())
    for a in ABBREV:
        t = re.sub(r"\b" + re.escape(a) + r"\.", a.replace(".", "\u00a7") + "\u00a7", t)
    t = re.sub(r"(\d)\.(\d)", "\\1\u00a7\\2", t)
    parts = re.split(r"(?<=[.?!])\s+(?=[A-Z\"'\u2018\u201c(])"
                     r"|(?<=[.?!][\"'\u2019\u201d])\s+(?=[A-Z\"'\u2018\u201c(])", t)
    return [p.replace("\u00a7", ".").strip() for p in parts if p.strip()]


def locator(corpus):
    loc = {}
    for f in corpus["fragments"]:
        loc[f["fragment_id"]] = f["location"]
    for c in corpus["claims"]:
        loc[c["claim_id"]] = c["location"].replace(";", ",")
    for g in corpus.get("declared_gaps", []):
        loc[g["gap_id"]] = g["location"].replace(";", ",")
    return loc


ID = r"(?:F\d+|C\d+|DG\d+)"
RUN = ID + r"(?:(?:,\s*|;\s*|,?\s+and\s+)" + ID + r")*"


def uniq(items):
    out = []
    for x in items:
        if x not in out:
            out.append(x)
    return out


def listed(items, last=" and "):
    if len(items) == 1:
        return items[0]
    sep = "; " if any("," in x for x in items) else ", "
    return sep.join(items[:-1]) + (last if last else sep) + items[-1]


def opens_sentence(s, i):
    return re.search(r"(?:^|[.?!][" + QUOTES + r"]?\s+)$", s[:i]) is not None


def cap(text, s, i):
    return text[0].upper() + text[1:] if opens_sentence(s, i) else text


def in_parens_name(tok, loc):
    if tok.startswith("F"):
        return loc[tok]
    if tok.startswith("C"):
        return f"the paper's claim at {loc[tok]}"
    return f"the paper's open question at {loc[tok]}"


def bare_name(toks, loc):
    if all(t.startswith("F") for t in toks):
        noun = "passage" if len(toks) == 1 else "passages"
        return f"the {noun} on " + listed(uniq([loc[t] for t in toks]))
    names = []
    for t in toks:
        if t.startswith("F"):
            names.append(f"the passage on {loc[t]}")
        elif t.startswith("C"):
            names.append(f"the paper's claim ({loc[t]})")
        else:
            names.append(f"the paper's open question ({loc[t]})")
    return listed(uniq(names))


def system_text(statement, loc):
    """Replace record ids with places in the paper, and the record's words with the paper's."""
    s = statement
    s = re.sub(r"\((F\d+)'s gloss, the author's\)",
               lambda m: f"(the author's characterisation on {loc[m.group(1)]})", s)
    s = re.sub(r"\b(F\d+)'s gloss\b",
               lambda m: cap(f"the author's characterisation on {loc[m.group(1)]}", s, m.start()), s)
    s = re.sub(r"\bclaims in (C\d+)\b", lambda m: f"claims ({loc[m.group(1)]})", s)
    s = re.sub(r"\b(C\d+)'s ([^,;:.()]+)",
               lambda m: cap(f"the paper's {m.group(2)} ({loc[m.group(1)]})", s, m.start()), s)

    def in_parens(m):
        inner = re.sub(RUN, lambda k: listed(uniq([in_parens_name(t, loc)
                                                   for t in re.findall(ID, k.group(0))]), last=None),
                       m.group(1))
        return "(" + inner + ")"
    s = re.sub(r"\(([^()]*)\)", in_parens, s)
    s = re.sub(r"\b" + RUN + r"\b",
               lambda m: cap(bare_name(re.findall(ID, m.group(0)), loc), s, m.start()), s)
    left = re.findall(r"\b(?:F\d+|C\d+|DG\d+|CP\d+)\b", s)
    if left:
        raise SystemExit(f"ids left in a system statement: {left}")
    for old, new in ((r"\bstubs\b", "passages"), (r"\bstub\b", "passage"),
                     (r"\bfragments\b", "passages"), (r"\bfragment\b", "passage"),
                     (r"\bthe corpus\b", "the paper"), (r"\bThe record\b", "The paper"),
                     (r"\bThis unit speaks\b", "This group speaks")):
        s = re.sub(old, new, s)
    return s


def cite_first(job, page):
    """Put a piece of evidence's page in parentheses at the end of its job's first sentence."""
    ss = sentences(job)
    body, punct, quotes = re.match(r"^(.*?)([.?!]?)([" + QUOTES + r"]*)$", ss[0], re.S).groups()
    ss[0] = f"{body}{quotes} ({page}){punct or '.'}"
    return " ".join(ss)


def tidy_pages(text):
    t = re.sub(r"\b(pp?\. \d+)[a-z]\b", r"\1", text)
    t = re.sub(r"\bpp?\. (\d+)\s?[-" + DASH + r"]\s?(\d+)", "pp. \\1" + DASH + "\\2", t)
    t = re.sub(r"\b(pp?\. \d+(?:" + DASH + r"\d+)?)(?:[,;] \1(?![\d" + DASH + r"]))+", r"\1", t)
    return t


def readings_for(paper, cfg):
    corpus = json.load(open(cfg["corpus"]))
    loc = locator(corpus)
    out = []
    for p in sorted(glob.glob(os.path.join(cfg["cards"], "*_01.json"))):
        card = json.load(open(p))
        out.append({"arm": "system", "source": os.path.relpath(p),
                    "source_id": card["card_id"],
                    "text": system_text(card["wager"]["statement"], loc)})
    mid = json.load(open(cfg["middle"]))
    for c in mid["cards"]:
        out.append({"arm": "middle", "source": cfg["middle"], "source_id": c["card_id"],
                    "text": c["wager"]["statement"]})
    pl = json.load(open(cfg["plain"]))
    for r in pl["readings"]:
        ev = " ".join(cite_first(e["job"], e["page"]) for e in r["evidence"])
        out.append({"arm": "plain", "source": cfg["plain"], "source_id": r["reading_id"],
                    "text": r["wager"] + " " + ev})
    for r in out:
        r["text"] = tidy_pages(r["text"])
    return corpus["meta"]["citation"], out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--seed=")]
    seeds = [int(a.split("=", 1)[1]) for a in sys.argv[1:] if a.startswith("--seed=")]
    if len(args) != 1 or len(seeds) > 1:
        raise SystemExit("usage: python3 build_marker_packs.py <out_dir> [--seed=N]")
    out_dir, seed = args[0], (seeds[0] if seeds else 20261011)
    os.makedirs(out_dir, exist_ok=True)
    key = {"seed": seed, "papers": {}}
    for paper, cfg in PAPERS.items():
        citation, rs = readings_for(paper, cfg)
        rng = random.Random(f"{seed}-{paper}")
        rng.shuffle(rs)
        lines = [f"# Readings of {citation}", "",
                 f"{len(rs)} readings of this paper, in no particular order. Each is split",
                 "into numbered sentences. A page in a sentence is a pointer, not a proof.", ""]
        entries = []
        for i, r in enumerate(rs, 1):
            rid = f"{cfg['prefix']}{i:02d}"
            ss = sentences(r["text"])
            lines += [f"## Reading {rid}", ""]
            units = []
            for j, s in enumerate(ss, 1):
                uid = f"{rid}-{j:02d}"
                lines += [f"{uid}  {s}", ""]
                units.append({"unit": uid, "text": s})
            entries.append({"reading": rid, "arm": r["arm"], "source": r["source"],
                            "source_id": r["source_id"], "units": units})
        open(os.path.join(out_dir, f"READINGS_{paper}.md"), "w").write("\n".join(lines))
        key["papers"][paper] = entries
        n_units = sum(len(e["units"]) for e in entries)
        arms = {a: sum(1 for e in entries if e["arm"] == a) for a in ("system", "middle", "plain")}
        print(f"{paper}: {len(entries)} readings {arms}, {n_units} sentences")
    json.dump(key, open(os.path.join(out_dir, "KEY.json"), "w"), indent=1, ensure_ascii=False)
    print(f"wrote READINGS_pratt.md, READINGS_bechky.md and KEY.json in {out_dir}/")
    print("  The readings files go to the markers; KEY.json goes to nobody.")


if __name__ == "__main__":
    main()
