# MQGT-SCF Independent Verification Packet

Independent, third-party-style re-verification of selected computational claims from the
**MQGT-SCF** (Multi-Quantum Geometric Theory / Self-Consistent Field) program by
Christopher Baird.

- Canonical upstream repository: [`Cbaird26/mqgt-scf-science-public`](https://github.com/Cbaird26/mqgt-scf-science-public)
- This packet was produced on 2026-09-16/17 against the September 2026 GitHub head of that
  repository. It is a verification layer, **not** a fork: nothing here modifies the upstream
  claims; disagreements are recorded as errata for the author to adjudicate.

## Contents

| File | What it is |
|---|---|
| `MQGT_SCF_Claims_Inventory.md` | Full claims inventory with per-claim verification status, including the Stage-3 results (C6a/C6b/C7/C8/C9) |
| `MQGT_SCF_ERRATA_2026-09-17.md` | Four errata (E1–E4) found by independent recomputation |
| `mqgt_c6_independent_uv.py` | Independent implementation of the Bridge-D UV fixed-point / stability analysis |
| `mqgt_t3_independent.py` | Independent spectral-zeta computation on the unit S⁷ (de Rham/Hodge towers) for claim T-3 |
| `mqgt_t1_independent.py` | Independent check of the T-1 inverse-fine-structure identity and a pre-declared, bounded correction search |

## One-line verdicts

- **Gate-1 (EMP-01 harness):** reproduces — 15/15 unit tests pass, blocked mode exits correctly, manifest hashes verify.
- **C6a (UV completion):** claim holds in the perturbative region (125/125 cone trajectories Gaussian; 5000-seed Newton survey), **but** two non-perturbative NGFPs exist (λ≈26.6, g≈8.86 and degenerate λ=g≈14.76) → wording errata E1.
- **C6b (dynamical g_N\*):** arithmetic confirmed exactly (4.4352 / 5.0265 / −7.94).
- **C7 (neutrino portal):** arithmetic exact (0.05928 eV ≈ minimal normal-ordering sum), **but** a single y_ν cannot fit the oscillation Δm² splittings → errata E2.
- **C8 (T-3 spectral identity):** does **not** reproduce — independent ζ′(0) towers on unit S⁷ give Hodge Δ₂ = −0.61982401 vs claimed −0.41364; claimed value matches no standard tower convention → errata E3.
- **C9 (T-1 α⁻¹ gate):** formula gives 137.036082448164 vs CODATA 137.035999178 (rel. dev. 6.08×10⁻⁷, **FAIL** by the program's own gate). A pre-declared bounded search found one correction ×(1−(π/2)α³) at residual 2.8×10⁻⁹, but with ~1.3 accidental hits expected it is flagged as a coincidence and must not be cited → errata E4.

## Re-running

Requires Python 3 with `mpmath` and `numpy` (no other dependencies):

```bash
python3 mqgt_c6_independent_uv.py
python3 mqgt_t3_independent.py
python3 mqgt_t1_independent.py
```

Each script prints its own PASS/FAIL verdicts and the intermediate values needed to audit it.

## Honest scope note

Claims were taken from the September 2026 GitHub head of the canonical repository and public
search/index records. The Zenodo PDF series (concept DOI 10.5281/zenodo.14019809) was not
re-read in full for this packet; where the GitHub head and a Zenodo record disagree, the
GitHub head was treated as the claim under test.
