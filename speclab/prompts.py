"""Frozen prompts for the XRD qualification runs. Changing any text here is a new registration."""

SYSTEM_XRD = """You are identifying crystalline phases in a simulated powder X-ray diffraction pattern (Cu K-alpha, 10-80 degrees two-theta, 0.05 degree grid, intensities normalised to 100).

You receive the observed pattern and nine candidate structures as CIF files. One or two of the candidates are present. Decide which, from the pattern and the structures alone.

Rules:
- Answer with JSON only, on the last line, in exactly this form: {"present": ["<candidate id>", ...], "confidence": <0 to 1>, "note": "<one sentence>"}
- "present" lists one or two candidate ids from the list given. Never more than two, never an id outside the list.
- If you cannot decide between candidates, choose the most likely one and say so in the note; do not leave "present" empty.
- Keep any reasoning before the JSON short."""

SYSTEM_XRD_TOOL = SYSTEM_XRD + """

You also have a tool, simulate_pattern, that returns the simulated clean pattern of any candidate id on the same grid. Use it as you see fit; the final answer must still be the JSON line."""


def user_xrd(item: dict) -> str:
    cands = "\n\n".join(f"### Candidate {c['id']} ({c['formula']}, space group {c['spacegroup']})\n{c['cif']}" for c in item["candidates"])
    tt = ", ".join(f"{x:g}" for x in item["two_theta"])
    ii = ", ".join(f"{x:g}" for x in item["intensity"])
    return f"""Item {item['id']} (tier {item['tier']}).

Observed pattern.
two_theta: [{tt}]
intensity: [{ii}]

Candidates (nine; one or two present):

{cands}

{item['question']}"""
