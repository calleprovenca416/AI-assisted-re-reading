"""
Rule 2 check: does any text field in a corpus repeat the paper's wording?

WHY
---
Corpora are shareable only because they carry no verbatim text: every stub,
statement, gloss and basis is written in the extractor's own words. The Carlile
pilot's session checked this by reading and missed near-copies, mostly in claim
statements, where theoretical sentences are hard to paraphrase. This script is
the mechanical check. Run it on every corpus before it is frozen; reword each
field it flags, and log each rewording.

USAGE
-----
    python3 wording_check.py <paper.txt> <corpus.json> [<voice_gloss.json>] [<n_to_list>]

<paper.txt> is the paper's text in reading order, made locally from the PDF and
never committed (the text is copyrighted). For a single-column PDF:
    pdftotext paper.pdf paper.txt
For a two-column PDF, crop each column so no run is broken at a line end, e.g.
for each page p and each half: pdftotext -f p -l p -x <x> -y 0 -W <half width>
-H <height> paper.pdf -   (this is how the Carlile text was made).

OUTPUT
------
A histogram of each field's longest run of words shared with the paper, then the
fields at 7 words or more, longest first. Runs are matched on lower-cased word
tokens, with line-break hyphens rejoined, starting from 5-word seeds.

Carlile, 26 Sep: the pilot has 8 of 674 fields at 9 or more words, longest 16
(C63); v4.4 has 10 of 207, longest 15 (F38). Names, pseudonyms and the paper's
own construct and code labels are allowed by the rule; runs longer than a label
are not.
"""
import json, re, sys, collections
def toks(s):
    s = s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s = re.sub(r'-\s*\n\s*', '', s)            # de-hyphenate line breaks
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", s.lower())
paper = toks(open(sys.argv[1]).read())
N=5
grams = collections.defaultdict(set)
for i in range(len(paper)-N+1):
    grams[tuple(paper[i:i+N])].add(i)
pset = set(grams)
def longest(text):
    t = toks(text); best=(0,'')
    i=0
    while i < len(t)-N+1:
        if tuple(t[i:i+N]) in pset:
            j=i+N
            # extend while the run stays contiguous in the paper
            starts = grams[tuple(t[i:i+N])]
            cur = set(starts)
            while j < len(t):
                nxt = {s for s in cur if s+(j-i) < len(paper) and paper[s+(j-i)]==t[j]}
                if not nxt: break
                cur = nxt; j+=1
            if j-i > best[0]: best=(j-i,' '.join(t[i:j]))
            i = j
        else: i+=1
    return best
def fields(path, side=None):
    d=json.load(open(path)); out=[]
    m=d['meta']
    for k in ('fieldwork_scale','resolution_basis'):
        if m.get(k): out.append((f'meta.{k}', m[k]))
    for f in d['fragments']:
        for k in ('stub','author_gloss','notes'):
            if f.get(k): out.append((f"{f['fragment_id']}.{k}", f[k]))
    for c in d['claims']:
        for k in ('statement','outcome','asserted_direction','notes'):
            if c.get(k): out.append((f"{c['claim_id']}.{k}", c[k]))
    for l in d['claim_links']:
        if l.get('basis'): out.append((f"{l['fragment_id']}>{l['claim_id']}.basis", l['basis']))
    for p in d['contrast_pairs']:
        for k in ('episode_a','episode_b','held_comparable','differs_in','basis'):
            out.append((f"{p['pair_id']}.{k}", p[k]))
    for g in d['declared_gaps']: out.append((f"{g['gap_id']}.statement", g['statement']))
    for a in d['absences']:
        for k in ('evidence_class','basis'): out.append((f"{a['absence_id']}.{k}", a[k]))
    if side:
        s=json.load(open(side))
        for v in s['voice']+s['gloss_relation']: out.append((f"{v['fragment_id']}.reason", v['reason']))
    return out
path=sys.argv[2]; side=sys.argv[3] if len(sys.argv)>3 else None
res=[(k,)+longest(v) for k,v in fields(path, side)]
hist=collections.Counter(min(n,12) for _,n,_ in res)
print("fields checked:", len(res), " longest-run histogram (words):", sorted(hist.items()))
for k,n,s in sorted(res, key=lambda r:-r[1])[:int(sys.argv[4]) if len(sys.argv)>4 else 25]:
    if n>=7: print(f"  {n:2d}  {k:28s} | {s}")
