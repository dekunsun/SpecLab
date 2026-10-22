"""Generate items/xrd_public.json (+ answers) and a local held-out set (not committed)."""
import json, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import data, spec as specmod, xrd

sp = specmod.load("high_k_gate_dielectric")
data.download()
pool = [e for e in data.load() if specmod.composition_ok(sp, e.elements)[0] and specmod.stability_ok(sp, e.e_above_hull)]
print("pool", len(pool))
cache = {}
def structure_of(e):
    if e.material_id not in cache:
        cache[e.material_id] = data.structure(e)
    return cache[e.material_id]

def build(seed, per_tier, prefix):
    rng = random.Random(seed)
    items, answers = [], {}
    idx = 0
    for tier in ("T1", "T2", "T3"):
        for _ in range(per_tier):
            it, ans = xrd.make_item(idx, tier, pool, rng, structure_of)
            it["id"] = ans["id"] = f"{prefix}-{idx:03d}"
            ans["tier"] = tier
            items.append(it); answers[it["id"]] = ans; idx += 1
    return items, answers

items, answers = build(20261021, 40, "xrd")
Path("items").mkdir(exist_ok=True)
Path("items/xrd_public.json").write_text(json.dumps(items))
Path("items/xrd_public_answers.json").write_text(json.dumps(answers, indent=1))
h_items, h_answers = build(int(sys.argv[1]) if len(sys.argv) > 1 else 0, 20, "xrdh")
Path("data/heldout").mkdir(parents=True, exist_ok=True)
Path("data/heldout/xrd_heldout.json").write_text(json.dumps(h_items))
Path("data/heldout/xrd_heldout_answers.json").write_text(json.dumps(h_answers, indent=1))
# items/README.md is maintained by hand (it carries the history of the held-out set); print the
# hashes for the record instead of overwriting it.
print("held-out items sha256:", xrd.sha256(h_items)); print("held-out answers sha256:", xrd.sha256(h_answers))
print("public", len(items), "heldout", len(h_items))
