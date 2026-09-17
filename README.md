# MQGT-SCF Independent Verification Packet

Independent, third-party-style re-verification of selected computational claims from the
**MQGT-SCF** (Multi-Quantum Geometric Theory / Self-Consistent Field) program by
Christopher Baird.

- Canonical upstream repository: [`Cbaird26/mqgt-scf-science-public`](https://github.com/Cbaird26/mqgt-scf-science-public)
- This packet was produced on 2026-09-16/17 against the September 2026 GitHub head of that
  repository. It is a verification layer, **not** a fork: nothing here modifies the upstream
  claims; disagreements are recorded as errata for the author to adjudicate.
- **v2 (2026-09-17):** repair pass. Errata E2 and E3 are now **solved/resolved**; E4 is
  sharpened to a no-go result for fitted corrections.

## Contents

| File | What it is |
|---|---|
| `MQGT_SCF_Claims_Inventory.md` | Full claims inventory with per-claim verification status, including Stage-3 results (C6a/C6b/C7/C8/C9) and v2 resolutions |
| `MQGT_SCF_ERRATA_2026-09-17.md` | Errata E1–E5 with fixes: E2 solved (3-Yukawa texture), E3 resolved (both T-3 constants identified), E4 sharpened (58 gate-passing coincidences), E5 minor |
| `mqgt_c6_independent_uv.py` | Independent implementation of the Bridge-D UV fixed-point / stability analysis |
| `mqgt_t3_independent.py` | Independent spectral-zeta computation on the unit S⁷ (de Rham/Hodge towers) |
| `mqgt_t3_reverse_search.py` | Pre-declared reverse-engineering scan that identifies the T-3 constants: coexact p-form ζ′(0) on round S^n, n = 1,3,5,7,9,11, with Killing/Λ^p anchors and stabilized Hurwitz numerics |
| `mqgt_t1_independent.py` | Independent check of the T-1 inverse-fine-structure identity and a pre-declared, bounded correction search |
| `mqgt_t1_topological_scan.py` | Disciplined topological-coefficient scan proving fitted α³-order corrections are uncertifiable (58 pre-declared gate-passers) |

## One-line verdicts (v2)

- **Gate-1 (EMP-01 harness):** reproduces — 15/15 unit tests pass, blocked mode exits correctly, manifest hashes verify.
- **C6a (UV completion):** holds in the perturbative region; two non-perturbative NGFPs exist → wording errata E1.
- **C6b (dynamical g_N\*):** arithmetic confirmed exactly (4.4352 / 5.0265 / −7.94).
- **C7 (neutrino portal):** arithmetic exact; single-Yukawa texture contradicts oscillations → **fix solved**: Variant A (sum rule preserved, span 104×) or Variant B (span 5.8×, Σm_ν = 0.0720 eV). See E2.
- **C8 (T-3):** **resolved.** S7 = ½ζ′(0) of coexact 3-forms on S⁷ = 1.74845220445 (all 7 quoted digits); S7′ = −ζ′(0) of coexact 2-forms on S⁹ = 0.41364465819 (all 5 quoted digits). The audit's "ζ′_Δ₂(0) on S⁷" assignment is wrong (that value is −0.61982401). The constants are no longer quoted literals — they are identified spectral determinants on the two spheres of the program's Hopf structure. See E3.
- **C9 (T-1 α⁻¹ gate):** FAIL stands (6.08×10⁻⁷). Required coefficient c = 1.563718224; a pre-declared 13,057-expression topological family contains **58 gate-passing coincidences**, so no fitted correction is citable — structural derivation required. See E4.

## Re-running

Requires Python 3 with `mpmath` and `numpy` (no other dependencies):

```bash
python3 mqgt_c6_independent_uv.py
python3 mqgt_t3_independent.py
python3 mqgt_t3_reverse_search.py
python3 mqgt_t1_independent.py
python3 mqgt_t1_topological_scan.py
```

Each script prints its own PASS/FAIL verdicts and the intermediate values needed to audit it.
Numerics note: sphere-zeta computations that subtract a finite head from ζ_R(w) are
catastrophically unstable for w ≳ dps/0.301; `mqgt_t3_reverse_search.py` documents and
fixes this (hybrid direct-sum Hurwitz for w > 40).

## Honest scope note

Claims were taken from the September 2026 GitHub head of the canonical repository and public
search/index records. The Zenodo PDF series (concept DOI 10.5281/zenodo.14019809) was not
re-read in full for this packet; where the GitHub head and a Zenodo record disagree, the
GitHub head was treated as the claim under test.
