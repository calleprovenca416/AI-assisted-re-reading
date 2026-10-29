"""replay.py: make this repository's results again from the files it holds, and check that each is the file here,
byte for byte.

    python3 -B replay.py                 every step, on a copy of this folder in a temporary folder
    python3 -B replay.py --list          the steps, and what is not replayed here, with the reason
    python3 -B replay.py --only=NAME[,NAME...] [--keep=DIR]

No model is called and nothing is fetched. The replay starts from the records: the models' replies as they were saved,
the PI's filled sheets, the corpora and the keys. Each step runs one of the folder's scripts with the arguments and
seed it was run with, writes into a folder of its own, and sets each file it makes beside the file here. A workbook
is compared part by part, and one whose parts are the same but for the time its properties give for its last save
passes and is reported so. Where a scorer's results file has notes added below its output, after a line "---", the
output must be the file's head. A step that only checks (a self-test, the schema check) must end with exit status 0
and print what it is expected to print. Nothing in this folder is written.

It needs Python 3.12 or later and the packages in requirements.txt: openpyxl, which writes its workbooks through
lxml. Without lxml, openpyxl writes the same cells with other spacing in the XML, so the workbooks it makes are not
the bytes here; and Python before 3.12 sums floats less exactly, so a figure kept to full precision can differ in its
last digits. The replay says at the start what it runs with. The exit status is 0 when every step passes.
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PY = [sys.executable, "-B"]
PAPERS = ("pratt_2000", "bechky_2020")
STAGES = (("A", "A_outcome"), ("A2", "A2_asserted_direction"), ("V", "V_voice"), ("B", "B"))
# the attack's bundles: folder, card; 37 and 38 are calibration copies of 31's card, each with an error planted
ATTACKS = (("28_pratt_CP01", "pratt_2000_construct_inversion_CP01_01"),
           ("29_pratt_CP02", "pratt_2000_construct_inversion_CP02_01"),
           ("30_pratt_CP03", "pratt_2000_construct_inversion_CP03_01"),
           ("31_pratt_C56", "pratt_2000_counterfactual_ending_C56_01"),
           ("32_pratt_unit", "pratt_2000_focalization_shift_current_and_former_distributors_01"),
           ("33_bechky_CP01", "bechky_2020_construct_inversion_from_pair_CP01_01"),
           ("34_bechky_CP02", "bechky_2020_construct_inversion_from_pair_CP02_01"),
           ("35_bechky_DG02", "bechky_2020_counterfactual_ending_DG02_01"),
           ("36_bechky_unit", "bechky_2020_focalization_shift_forensic_biology_DNA_01"))
GENERATION = {"pratt_2000": "stage2/replies/reply_22_pratt_generation_final.json",
              "bechky_2020": "stage2/replies/reply_23_bechky_generation_final.json"}


class Label:
    """The agreement log's line on who the two coders are, as agreement.py takes it; read when the step runs."""

    def __init__(self, p):
        self.p = p

    def __str__(self):
        t = open(os.path.join(HERE, f"{self.p.split('_')[0].upper()}_AGREEMENT_LOG.md"), encoding="utf-8").read()
        m = re.search(r"^- \*\*Who they are:\*\* (Model against model\..*)$", t, re.M)
        return "--label=" + " ".join(m.group(1).split())


def agreement_args(p, log):
    return ["--paper", f"{p}_v1.json", f"--sidecar={p}_v1_voice_gloss.json", f"--key=packs/{p}/key/{p}_pack_key.json",
            f"--log={log}", Label(p), f"--a=returned_{p}_STAGE_A_coder2.xlsx", f"--a2=returned_{p}_STAGE_A2_coder2.xlsx",
            f"--v=returned_{p}_STAGE_V_coder2.xlsx", f"--b=returned_{p}_STAGE_B_coder2.xlsx",
            f"--readings={p}_readings.json", "--against=against_check_results.json"]


def cards_and_attacks(p):
    """The intake of the generation chat's cards, the attack's bundles from the cards as they were then, and the
    attack's verdicts recorded on the cards."""
    mine = [(f, c) for f, c in ATTACKS if c.startswith(p)]
    cmds = [PY + ["intake_stage2.py", GENERATION[p], f"{p}_v1.json", "{OUT}/cards"]]
    cmds += [PY + ["prepare_attack.py", f"{{OUT}}/cards/{c}.json", f"{p}_v1.json", f"{{OUT}}/attack/{f}"] for f, c in mine]
    if p == "pratt_2000":
        cmds += [PY + ["prepare_attack.py", "{OUT}/cards/pratt_2000_counterfactual_ending_C56_01.json",
                       "pratt_2000_v1.json", f"{{OUT}}/attack/{f}"] for f in ("37_x", "38_y")]
    cmds += [PY + ["record_attack.py", f"{{OUT}}/cards/{c}.json", f"stage2/attack_replies/reply_{f[:2]}_attack.json"]
             for f, c in mine]
    outs = [("dir:cards", f"stage2/{p}_cards")] + [(f"dir:attack/{f}", f"stage2/attack/{f}") for f, _ in mine]
    if p == "pratt_2000":
        outs += [(f"attack/{f}/{x}", f"stage2/attack/{f}/{x}") for f in ("37_x", "38_y")
                 for x in ("corpus_for_attack.json", "attack.md")]
    return cmds, outs


# A step: (name, what it is, the commands, the outputs to check, options). A command is a list; "{OUT}" is the step's
# own folder. An output is (the file made, relative to {OUT}; the file here): "dir:" sets a folder made beside a folder
# here, file by file; "head:" asks only that the file made be the head of the file here. Options: "expect", a pattern
# the step's printed output must hold; "kept", files of a folder here that the step does not make (each a record).
STEPS = [
    # ------------------------------------------------------------------------------------------- the record
    ("schema", "every corpus against the schema, by schema.py: no error",
     [PY + ["schema.py", f] for f in ("pratt_2000_corpus.json", "pratt_2000_coverage_corpus.json", "pratt_2000_v1.json",
                                     "bechky_2020_corpus.json", "bechky_2020_coverage_corpus.json",
                                     "bechky_2020_v1.json", "bechky_2020_x2_corpus.json")],
     [], {"expect": lambda out: out.count("\n  errors 0 ") == 7 and "\n  E " not in out}),
    ("audit", "the audit of each paper's first return and of its frozen corpus, by audit.py",
     [PY + ["audit.py", f"{p}_corpus.json", f"--voice={p}_voice_gloss.json", f"--json={{OUT}}/{p}_audit_first_return.json"]
      for p in PAPERS] + [PY + ["audit.py", f"{p}_v1.json", f"--voice={p}_v1_voice_gloss.json",
                                f"--json={{OUT}}/{p}_v1_audit.json"] for p in PAPERS],
     [(f"{p}_{x}.json", f"{p}_{x}.json") for p in PAPERS for x in ("audit_first_return", "v1_audit")], {}),
    ("coverage_sheets", "the reading sheets of the coverage check, by coverage_sheet.py",
     [PY + ["coverage_sheet.py", f"{p}_corpus.json", f"{{OUT}}/{p}_coverage_reading.md"] for p in PAPERS],
     [(f"{p}_coverage_reading.md",) * 2 for p in PAPERS], {}),
    ("intake", "coder 2's returned workbooks, from the workbooks as sent and the replies, by intake_coder2.py",
     [PY + ["intake_coder2.py", f"packs/{p}/attach/{p}_STAGE_{f}.xlsx", f"--key=packs/{p}/key/{p}_pack_key.json",
            f"--text=reply_{p}_STAGE_{s}.txt", f"--out={{OUT}}/returned_{p}_STAGE_{s}_coder2.xlsx"]
      for p in PAPERS for s, f in STAGES],
     [(f"returned_{p}_STAGE_{s}_coder2.xlsx",) * 2 for p in PAPERS for s, _ in STAGES], {}),
    ("against_check", "the check of the links coded `against` (seed 20261009), by build_against_check.py",
     [PY + ["build_against_check.py", "build", "{OUT}", "--seed=20261009",
            "pratt_2000_v1.json=returned_pratt_2000_STAGE_B_coder2.xlsx",
            "bechky_2020_v1.json=returned_bechky_2020_STAGE_B_coder2.xlsx"],
      PY + ["build_against_check.py", "read", "{OUT}/against_check_key.json", "against_check_answers.txt"]],
     [(f, f) for f in ("against_check_table.md", "against_check_key.json", "against_check_results.json")], {}),
    ("agreement_pratt", "Pratt's agreement log, by agreement.py --paper",
     [PY + ["agreement.py"] + agreement_args("pratt_2000", "{OUT}/PRATT_AGREEMENT_LOG.md")],
     [("PRATT_AGREEMENT_LOG.md",) * 2], {}),
    ("agreement_bechky", "Bechky's agreement log, by agreement.py --paper",
     [PY + ["agreement.py"] + agreement_args("bechky_2020", "{OUT}/BECHKY_AGREEMENT_LOG.md")],
     [("BECHKY_AGREEMENT_LOG.md",) * 2], {}),
    ("second_count", "Pratt's second count, by second_count.py",
     [PY + ["second_count.py", "--leave-out=pratt_2000_second_count.json"]
      + agreement_args("pratt_2000", "{OUT}/PRATT_SECOND_COUNT_LOG.md")[1:]],
     [("PRATT_SECOND_COUNT_LOG.md",) * 2], {}),
    # ------------------------------------------------------------------------------------------- the wager test (T29)
    ("generation_pratt", "Pratt's generation bundle, by prepare_generation.py",
     [PY + ["prepare_generation.py", "pratt_2000_v1.json", "{OUT}/g", "--voice=pratt_2000_v1_voice_gloss.json"]],
     [("dir:g", "stage2/pratt_2000_generation")], {}),
    ("generation_bechky", "Bechky's generation bundle, by prepare_generation.py",
     [PY + ["prepare_generation.py", "bechky_2020_v1.json", "{OUT}/g", "--voice=bechky_2020_v1_voice_gloss.json"]],
     [("dir:g", "stage2/bechky_2020_generation")], {}),
    ("cards_pratt", "Pratt's cards, the attack's bundles and its verdicts, by intake_stage2.py, prepare_attack.py and "
     "record_attack.py", *cards_and_attacks("pratt_2000"), {}),
    ("cards_bechky", "Bechky's cards, the attack's bundles and its verdicts, by intake_stage2.py, prepare_attack.py "
     "and record_attack.py", *cards_and_attacks("bechky_2020"), {"kept": ["stage2/bechky_2020_cards/NOTE.md"]}),
    ("marker_packs", "the markers' packs, by build_marker_packs.py",
     [PY + ["build_marker_packs.py", "{OUT}/m"]], [("dir:m", "stage2/markers")], {}),
    ("marker_results", "the markers' results, by score_markers.py",
     [PY + ["score_markers.py", "{OUT}/r"]], [("dir:r", "stage2/marker_results")], {}),
    ("worth_sheet", "the blank worth sheet, by build_worth_sheet.py",
     [PY + ["build_worth_sheet.py", "{OUT}/worth_sheet.xlsx"]], [("worth_sheet.xlsx", "stage2/worth/worth_sheet.xlsx")],
     {}),
    ("worth", "the worth results, by score_worth.py",
     [PY + ["score_worth.py", "{OUT}/w"]],
     [("w/WORTH_RESULTS.md", "stage2/worth/WORTH_RESULTS.md"), ("w/worth_joined.json", "stage2/worth/worth_joined.json")],
     {}),
    # ------------------------------------------------------------------------------------------- T31, the judges
    ("judge_tables", "the judges' tables and key (seed 20261013), by build_judge_table.py",
     [PY + ["build_judge_table.py", "--seed=20261013", "--out={OUT}", "pratt_2000", "bechky_2020"]],
     [(f, f) for f in ("JUDGE_TABLE_pratt_part1.md", "JUDGE_TABLE_pratt_part2.md", "JUDGE_TABLE_bechky_part1.md",
                       "JUDGE_TABLE_bechky_part2.md", "judge_key.json")], {}),
    ("judge_results", "the judges' answers counted, by read_judge_answers.py",
     [PY + ["read_judge_answers.py", "--key=judge_key.json", "--out={OUT}/JUDGE_RESULTS.md",
            "--json={OUT}/judge_results.json", "pratt_2000:1=reply_43_judge_pratt_part1.json",
            "pratt_2000:2=reply_43_judge_pratt_part2.json", "bechky_2020:1=reply_44_judge_bechky_part1.json",
            "bechky_2020:2=reply_44_judge_bechky_part2.json"]],
     [("JUDGE_RESULTS.md",) * 2, ("judge_results.json",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T32, places
    ("places", "the places (seed 20261014), by build_places.py",
     [PY + ["build_places.py", "--seed=20261014", "--paper=bechky_2020", "--out={OUT}", "F129:C01=qualifies/with",
            "F164:C03=illustrates/with", "F164:C17=illustrates/with", "F98:C01=with/qualifies"]],
     [("PLACES.md",) * 2, ("places_key.json",) * 2], {}),
    ("places_packs", "the markers' pack and the worth sheet (seed 20261015), by build_places_packs.py",
     [PY + ["build_places_packs.py", "--seed=20261015", "--out={OUT}", "--edits=places_pack_edits.json",
            "reply_45_bechky_places.json", "reply_46_bechky_open.json"]],
     [(f, f) for f in ("READINGS_places.md", "places_packs_key.json", "worth_sheet_places.xlsx")], {}),
    ("places_markers", "the markers' scores, by score_places_markers.py",
     [PY + ["score_places_markers.py", "{OUT}"]],
     [(f, f) for f in ("PLACES_MARKER_RESULTS.md", "places_marker_results.json")], {}),
    ("places_results", "the results, by places_results.py",
     [PY + ["places_results.py", "{OUT}"]], [("PLACES_RESULTS.md",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T33, matching
    ("matching_reference", "the reference, by build_matching_pack.py reference",
     [PY + ["build_matching_pack.py", "reference", "--out={OUT}"]], [("REFERENCE_bechky.md",) * 2], {}),
    ("matching_pack", "the matchers' pack and the PI's sheets (seed 20261014), by build_matching_pack.py pack",
     [PY + ["build_matching_pack.py", "pack", "--seed=20261014", "--out={OUT}", "reply_49_bechky_plain_astra.json",
            "reply_50_bechky_plain_astra.json"]],
     [(f, f) for f in ("READINGS_matching.md", "matching_key.json", "grouping_sheet.xlsx", "worth_sheet_matching.xlsx")],
     {}),
    ("matching_score", "the scores, by score_matching.py score",
     [PY + ["score_matching.py", "score", "--key=matching_key.json", "--blank=grouping_sheet.xlsx",
            "--sheet=grouping_sheet_filled.xlsx", "--a1=reply_51_match_a_opus.json", "--a2=reply_52_match_a_astra.json",
            "--b1=reply_53_match_b_opus.json", "--b2=reply_54_match_b_astra.json", "--out={OUT}"]],
     [("matching_results.json",) * 2, ("head:MATCHING_RESULTS.md", "MATCHING_RESULTS.md")], {}),
    ("matching_worth", "the worth beside the groups, by matching_worth.py",
     [PY + ["matching_worth.py", "{OUT}"]], [("MATCHING_WORTH.md",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T35, the second extraction
    ("two_lists", "the two lists and their key (seed 20261018), by build_two_lists.py build",
     [PY + ["build_two_lists.py", "build", "--seed=20261018",
            "--first=bechky_2020_corpus.json,bechky_2020_voice_gloss.json",
            "--new=bechky_2020_x2_corpus.json,bechky_2020_x2_voice_gloss.json", "--out={OUT}"]],
     [("TWO_LISTS_bechky.md",) * 2, ("two_lists_key.json",) * 2], {}),
    ("second_extraction", "the scores, by score_second_extraction.py score",
     [PY + ["score_second_extraction.py", "score", "--key=two_lists_key.json", "--a=reply_56_match_lists_opus.json",
            "--b=reply_57_match_lists_astra.json", "--out={OUT}"]],
     [("head:SECOND_EXTRACTION_RESULTS.md", "SECOND_EXTRACTION_RESULTS.md"),
      ("second_extraction_results.json",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T36, citation only
    ("citation_sheet", "the key and the sheet (seed 20261020), by build_citation_sheet.py build",
     [PY + ["build_citation_sheet.py", "build", "--seed=20261020", "--out={OUT}", "reply_58_bechky_citation_fable.json",
            "reply_59_bechky_citation_astra.json", "reply_60_pratt_citation_fable.json",
            "reply_61_pratt_citation_astra.json"]],
     [(f, f) for f in ("citation_only_key.json", "citation_matching_sheet.xlsx")], {}),
    ("citation_score", "the scores, by score_citation_only.py score",
     [PY + ["score_citation_only.py", "score", "--key=citation_only_key.json", "--blank=citation_matching_sheet.xlsx",
            "--sheet=citation_matching_sheet_filled.xlsx", "--out={OUT}", "reply_58_bechky_citation_fable.json",
            "reply_59_bechky_citation_astra.json", "reply_60_pratt_citation_fable.json",
            "reply_61_pratt_citation_astra.json"]],
     [("head:CITATION_ONLY_RESULTS.md", "CITATION_ONLY_RESULTS.md"), ("citation_only_results.json",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T37, the relation test
    ("relation_specs", "the claims files and the planted readings' specifications, by build_relation_test.py specs",
     [PY + ["build_relation_test.py", "specs", "--out={OUT}"]],
     [(f, f) for f in ("CLAIMS_bechky.md", "CLAIMS_pratt.md", "PLANTED_SPEC_bechky.md", "PLANTED_SPEC_pratt.md")], {}),
    ("relation_pack", "the readings files, the key and the two sheets, by build_relation_test.py pack",
     [PY + ["build_relation_test.py", "pack", "--out={OUT}", "reply_62_bechky_planted_fable_short.json",
            "reply_63_pratt_planted_fable_short.json"]],
     [(f, f) for f in ("RELATION_READINGS_bechky.md", "RELATION_READINGS_pratt.md", "relation_key.json",
                       "relation_sheet.xlsx", "planted_check.xlsx")], {}),
    ("relation_score", "the scores, by score_relation_test.py score",
     [PY + ["score_relation_test.py", "score", "--key=relation_key.json", "--sheet=relation_sheet_filled.xlsx",
            "--check=planted_check_filled.xlsx", "--out={OUT}", "reply_64_bechky_relation_gemini.json",
            "reply_65_bechky_relation_astra.json", "reply_66_pratt_relation_gemini.json",
            "reply_67_pratt_relation_astra.json"]],
     [("head:RELATION_RESULTS.md", "RELATION_RESULTS.md"), ("relation_results.json",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T38, completeness
    ("completeness_files", "the reading sheets and the matcher's file, by build_completeness_test.py files",
     [PY + ["build_completeness_test.py", "files", "{OUT}"]],
     [(f, f) for f in ("CHECK_SHEET_bechky.md", "CHECK_SHEET_pratt.md", "PASSAGES_AND_Q_bechky.md")], {}),
    ("completeness_key", "the key, by build_completeness_test.py key",
     [PY + ["build_completeness_test.py", "key", "{OUT}/completeness_key.json"]], [("completeness_key.json",) * 2], {}),
    ("completeness_lists", "the judges' files and their key, by build_completeness_test.py lists",
     [PY + ["build_completeness_test.py", "lists", "completeness_key.json", "reply_68_bechky_check_opus.json",
            "reply_69_pratt_check_opus.json", "{OUT}"]],
     [(f, f) for f in ("TWO_PASSAGE_LISTS_bechky.md", "TWO_PASSAGE_LISTS_pratt.md", "completeness_lists_key.json")], {}),
    ("completeness_score", "the scores, by score_completeness_test.py score",
     [PY + ["score_completeness_test.py", "score", "--key=completeness_key.json", "--lists=completeness_lists_key.json",
            "--checker-bechky=reply_68_bechky_check_opus.json", "--checker-pratt=reply_69_pratt_check_opus.json",
            "--matcher=reply_70_bechky_ready_test_opus.json", "--judge-bechky=reply_71_bechky_judge_argon.json",
            "--judge-pratt=reply_72_pratt_judge_argon.json", "--out={OUT}"]],
     [("head:COMPLETENESS_RESULTS.md", "COMPLETENESS_RESULTS.md"), ("completeness_results.json",) * 2], {}),
    # ------------------------------------------------------------------------------------------- T39, the map test
    ("map_pairs", "the map sheets and their key (seed 20261025), by build_map_test.py pairs",
     [PY + ["build_map_test.py", "pairs", "--seed=20261025", "{OUT}"]],
     [(f, f) for f in ("MAP_SHEET_bechky.md", "MAP_SHEET_pratt.md", "map_key.json")], {}),
] + [
    step for paper, a, b in (("bechky", "reply_73_bechky_map_opus.json", "reply_74_bechky_map_gpt6.json"),
                             ("pratt", "reply_75_pratt_map_opus.json", "reply_76_pratt_map_gpt6.json"))
    for step in (
        (f"map_settle_sheet_{paper}", f"{paper}: the settling sheet and its key, by build_map_settle.py sheet",
         [PY + ["build_map_settle.py", "sheet", paper, "map_key.json", a, b, "{OUT}"]],
         [(f"MAP_SETTLE_{paper}.xlsx",) * 2, (f"map_settle_key_{paper}.json",) * 2], {}),
        (f"map_settle_{paper}", f"{paper}: the settled map, by build_map_settle.py settle",
         [PY + ["build_map_settle.py", "settle", paper, f"map_settle_key_{paper}.json",
                f"MAP_SETTLE_{paper}_filled.xlsx", "{OUT}"]],
         [(f"map_settled_{paper}.json",) * 2], {}),
        (f"map_closure_{paper}", f"{paper}: the closure, by build_map_settle.py closure",
         [PY + ["build_map_settle.py", "closure", paper, f"map_settled_{paper}.json", "relation_results.json", "{OUT}"]],
         [(f"map_closure_{paper}.json",) * 2], {}),
        (f"map_modules_{paper}", f"{paper}: the modules, by build_map_settle.py modules",
         [PY + ["build_map_settle.py", "modules", paper, f"map_settled_{paper}.json", "{OUT}"]],
         [(f"map_modules_{paper}.json",) * 2], {}),
    )
] + [
    ("map_round2_files", "the settled maps, T37's codes and round 2's key, by build_map_round2.py files",
     [PY + ["build_map_round2.py", "files", "{OUT}"]],
     [(f, f) for f in ("SETTLED_MAP_bechky.md", "SETTLED_MAP_pratt.md", "T37_CODES_bechky.md", "T37_CODES_pratt.md",
                       "map_round2_key.json")], {}),
    ("map_openings", "the openings and their key, by build_map_round2.py openings",
     [PY + ["build_map_round2.py", "openings", "map_round2_key.json", "reply_77_bechky_place_argon.json",
            "reply_78_pratt_place_argon.json", "{OUT}"]],
     [(f, f) for f in ("OPENINGS_bechky.md", "OPENINGS_pratt.md", "map_openings_key.json")], {}),
    ("map_comparison", "the PI's comparison sheet and its key (seed 20261026), by build_map_round2.py comparison",
     [PY + ["build_map_round2.py", "comparison", "--seed=20261026", "map_round2_key.json",
            "reply_77_bechky_place_argon.json", "reply_78_pratt_place_argon.json", "{OUT}"]],
     [(f, f) for f in ("MAP_COMPARISON.xlsx", "map_comparison_key.json")], {}),
    ("map_comparison_answers", "the PI's answers read, by build_map_round2.py read-comparison",
     [PY + ["build_map_round2.py", "read-comparison", "map_comparison_key.json", "MAP_COMPARISON_filled.xlsx", "{OUT}"]],
     [("map_comparison_answers.json",) * 2], {}),
    ("map_results", "the map test's measures, by score_map_test.py score",
     [PY + ["score_map_test.py", "score", "{OUT}"]], [(f, f) for f in ("MAP_RESULTS.md", "map_results.json")], {}),
    ("map_ranking", "the ranking and its check, by rank_map_readings.py run",
     [PY + ["rank_map_readings.py", "run", ".", "{OUT}"]],
     [(f, f) for f in ("RANKING_CHECK.md", "ranking_check.json")], {}),
    # ------------------------------------------------------------------------------------------- the example, the figures
    ("network", "the claims network of Bechky's entry, by build_claim_network.py build",
     [PY + ["build_claim_network.py", "build", "{OUT}"]], [("CLAIM_NETWORK_bechky.html",) * 2], {}),
    ("figures", "the figures, each worked out again from its record, by build_figures.py build",
     [PY + ["build_figures.py", "build", "--out={OUT}"]],
     [(f, f) for f in ("FIGURES_bechky_2020.md", "FIGURES_pratt_2000.md", "FIGURES_across.md", "figures.json")], {}),
] + [
    # ------------------------------------------------------------------------------------------- the scripts' own checks
    (name, what, [PY + [script] + args], [], {"expect": expect})
    for name, script, args, expect, what in (
        ("network_check", "build_claim_network.py", ["check"], r"check: two builds give the same \d+ bytes",
         "the network page built twice alike, every link with its target, by build_claim_network.py check"),
        ("check_must_agree", "check_must_agree.py", [], r"all agree and all clean",
         "the passages that the coders' packs and the `against` check must give alike, and no forbidden term in the "
         "files the chats received, by check_must_agree.py"),
    ) + tuple((f"selftest_{os.path.splitext(s)[0]}", s, a, e, f"{s}'s self-test") for s, a, e in (
        ("coverage_sheet.py", ["--selftest"], r"selftest: all \d+ checks pass"),
        ("build_two_lists.py", ["selftest"], r"self-test passed"),
        ("score_second_extraction.py", ["selftest"], r"self-test passed"),
        ("score_matching.py", ["selftest"], r"SELFTEST PASSES"),
        ("score_citation_only.py", ["selftest"], r"selftest: all checks pass"),
        ("score_relation_test.py", ["selftest"], r"selftest: all checks pass"),
        ("build_completeness_test.py", ["--selftest"], r"SELFTEST PASSES"),
        ("score_completeness_test.py", ["--selftest"], r"SELFTEST PASSES"),
        ("build_map_test.py", ["--selftest"], r"SELFTEST PASSES"),
        ("build_map_settle.py", ["--selftest"], r"SELFTEST PASSES"),
        ("build_map_round2.py", ["--selftest"], r"self-test: \d+ checks pass, 0 fail"),
        ("score_map_test.py", ["--selftest"], r"self-test: \d+ checks pass, 0 fail"),
        ("rank_map_readings.py", ["selftest"], r"ALL PASSED"),
        ("score_author_ratings.py", ["selftest"], r"self-test passed"),
        ("build_figures.py", ["selftest"], r"selftest: all passed"),
    ))
]

# What is not replayed here, and why.
NOT_HERE = [
    ("The models' replies: the extractions, codings, readings, attacks, judgements and matchings",
     "they are the records the replay starts from, kept as each chat gave them; no model is called"),
    ("The PI's filled sheets and the answers typed from them", "records the replay starts from"),
    ("check_quotations.py and wording_check.py",
     "they need the papers' text, which this repository does not hold; their outputs are kept, with the papers' "
     "words in them replaced by notes"),
    ("The packs sent to coder 2 (build_cold_pack.py)",
     "the builder writes the time it built a pack into the pack's key; the packs are kept as sent, and the intake step "
     "checks each workbook against the hash the key records"),
    ("The calibration copies of card 31 that the attack received (stage2/attack/37_x and 38_y)",
     "made from card 31 by a script that is not here, each with one error planted (stage2/calibration/KEY.md says "
     "which); the replay makes their corpus and instructions, not the planted card"),
    ("stage2/attack_results.md", "written by a script not kept here; build_figures.py works its figures out again "
                                 "from the cards"),
    ("The self-tests of agreement.py, build_cold_pack.py, intake_coder2.py, build_against_check.py and the guarded "
     "word's test of check_must_agree.py",
     "they run on a pilot paper's files, which are not here, or need a hash this copy does not keep; each says so "
     "when run"),
    ("The authors' ratings (T34)", "the sheets sent to the authors are not here, and no author's reply came in"),
    ("The two link tests", "reported from their rules, plans, reports and results; the scripts that ran them are not "
                           "here"),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def tree(root):
    out = {}
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x != "__pycache__"]
        for f in fs:
            p = os.path.join(d, f)
            out[os.path.relpath(p, root)] = open(p, "rb").read()
    return out


SAVED = re.compile(rb"(<dcterms:modified\b[^>]*>)[^<]*(</dcterms:modified>)")
PASS = ("same", "same head", "same but for the time it was saved", "kept, not made")


def parts_differ(a, b):
    za, zb = zipfile.ZipFile(io.BytesIO(a)), zipfile.ZipFile(io.BytesIO(b))
    na, nb = za.namelist(), zb.namelist()
    if sorted(na) != sorted(nb):
        return ["the parts' names"], False
    out, saved = [], False
    for n in na:
        x, y = za.read(n), zb.read(n)
        if x != y and n == "docProps/core.xml" and SAVED.sub(rb"\1\2", x) == SAVED.sub(rb"\1\2", y):
            saved = True
        elif x != y:
            out.append(n)
    return out, saved


def compare(made, here):
    if made is None:
        return "not made"
    if made == here:
        return "same"
    if made[:2] == b"PK" and here[:2] == b"PK":
        d, saved = parts_differ(made, here)
        if d:
            return "differs in " + ", ".join(d)
        return "same but for the time it was saved" if saved else "same parts, other bytes"
    return "differs"


def run_step(copy, out, step):
    name, what, cmds, outputs, opt = step
    os.makedirs(out)
    t0, printed, code = time.time(), [], 0
    for cmd in cmds:
        args = [str(a).replace("{OUT}", out) for a in cmd]
        p = subprocess.run(args, cwd=copy, capture_output=True, text=True)
        printed.append(p.stdout)
        code = p.returncode
        if code != 0:
            printed.append(p.stderr)
            break
    text = "".join(printed)
    open(os.path.join(out, "_printed.txt"), "w", encoding="utf-8").write(text)
    res = []
    exp = opt.get("expect")
    if code == 0 and exp and not (exp(text) if callable(exp) else re.search(exp, text)):
        res.append(("its printed output", "not what it should print"))
    for made, here in outputs:
        if made.startswith("dir:"):
            a = tree(os.path.join(out, made[4:])) if os.path.isdir(os.path.join(out, made[4:])) else {}
            b = tree(os.path.join(HERE, here))
            for k in sorted(set(a) | set(b)):
                if k in a and k in b:
                    r = compare(a[k], b[k])
                elif k in b and os.path.join(here, k) in opt.get("kept", []):
                    r = "kept, not made"
                else:
                    r = "made, not here" if k in a else "not made"
                res.append((os.path.join(here, k), r))
        else:
            head = made.startswith("head:")
            made = made[5:] if head else made
            mp = os.path.join(out, made)
            m = open(mp, "rb").read() if os.path.exists(mp) else None
            h = open(os.path.join(HERE, here), "rb").read()
            if head and m is not None and m != h:
                res.append((here, "same head" if h.startswith(m) and h[len(m):].lstrip(b"\n").startswith(b"---\n")
                            else compare(m, h[:len(m)]) + " (head)"))
            else:
                res.append((here, compare(m, h)))
    return code, round(time.time() - t0, 1), res, text.strip().split("\n")[-1:]


def setting():
    """What the replay runs with, and a warning for each thing that will make bytes differ."""
    out = [f"Python {sys.version.split()[0]}"]
    warn = []
    if sys.version_info < (3, 12):
        warn.append("Python before 3.12 sums floats less exactly: a figure kept to full precision may differ in its "
                    "last digits")
    try:
        import openpyxl
        import openpyxl.xml
        out.append(f"openpyxl {openpyxl.__version__}")
        if openpyxl.xml.LXML:
            import lxml
            out.append(f"writing through lxml {lxml.__version__}")
        else:
            warn.append("openpyxl writes without lxml here: the workbooks it makes will differ from those here in their "
                        "XML's spacing (install requirements.txt)")
    except ImportError:
        warn.append("openpyxl is not installed (requirements.txt): the steps that read or write workbooks will fail")
    return "; ".join(out), warn


def main(argv):
    only = [x for a in argv if a.startswith("--only=") for x in a[7:].split(",")]
    keep = [a[7:] for a in argv if a.startswith("--keep=")]
    if "--list" in argv:
        for name, what, cmds, outputs, _ in STEPS:
            print(f"{name}: {what}")
        print("\nNot replayed here:")
        for what, why in NOT_HERE:
            print(f"- {what}: {why}.")
        return 0
    unknown = set(only) - {s[0] for s in STEPS}
    if unknown:
        raise SystemExit(f"no such step: {', '.join(sorted(unknown))} (see --list)")
    steps = [s for s in STEPS if not only or s[0] in only]
    work = keep[0] if keep else tempfile.mkdtemp(prefix="replay_")
    if keep:
        assert not os.path.exists(work), "--keep names a folder that exists: " + work
    copy = os.path.join(work, "copy")
    shutil.copytree(HERE, copy, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    with_what, warn = setting()
    print(with_what)
    for w in warn:
        print("warning:", w)
    bad, files = 0, 0
    for step in steps:
        code, secs, res, last = run_step(copy, os.path.join(work, "out", step[0]), step)
        ok = code == 0 and all(r in PASS for _, r in res)
        bad += not ok
        files += sum(1 for _, r in res if r in PASS and r != "kept, not made")
        print(f"{'ok  ' if ok else 'FAIL'} {step[0]} (exit {code}, {secs} s)")
        for here, r in res:
            if r not in ("same", "same head") or not ok:
                print(f"       {r}: {here}")
        if code != 0:
            print("       last line:", last[0][:300] if last else "")
    print(f"{len(steps) - bad} of {len(steps)} steps pass; {files} files made again and the same"
          + (f"; work kept in {work}" if keep else ""))
    if not keep:
        shutil.rmtree(work, ignore_errors=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
