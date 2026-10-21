import json, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import xrd

ROOT = Path(__file__).resolve().parent.parent
ITEMS = json.loads((ROOT / "items/xrd_public.json").read_text())
ANS = json.loads((ROOT / "items/xrd_public_answers.json").read_text())


def test_payload_has_no_answer_and_candidates_cover_truth():
    for it in ITEMS:
        p = xrd.prompt_payload(it)
        assert "present" not in p and "answer" not in p and "weights" not in p
        ids = {c["id"] for c in it["candidates"]}
        assert set(ANS[it["id"]]["present"]) <= ids


def test_answer_position_is_not_a_leak():
    first = sum(1 for it in ITEMS if it["candidates"][0]["id"] in ANS[it["id"]]["present"])
    # 120 items, nine candidates, 1-2 present: expected ~ 1/9 to 2/9 of items; fail above 35 %
    assert first / len(ITEMS) < 0.35, first


def test_tiers_and_phase_counts():
    for it in ITEMS:
        n = len(ANS[it["id"]]["present"])
        assert (it["tier"] == "T3") == (n == 2)


def test_scorer_handles_silence_as_coverage():
    answers = {"a": {"present": ["x"], "tier": "T1"}, "b": {"present": ["y"], "tier": "T1"}}
    per = xrd.score(answers, {"a": ["x"]})
    assert per["T1"]["coverage"] == 0.5 and per["T1"]["exact_rate"] == 1.0


def test_oracle_and_random_agents_shape():
    it = ITEMS[0]
    assert xrd.agent_oracle(it, ANS) == ANS[it["id"]]["present"]
    r = xrd.agent_random(it, random.Random(0))
    assert 1 <= len(r) <= 2 and all(x in {c["id"] for c in it["candidates"]} for x in r)
