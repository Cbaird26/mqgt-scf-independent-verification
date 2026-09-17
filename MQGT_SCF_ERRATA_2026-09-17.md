# MQGT-SCF Errata and Findings from Independent Verification

**Date:** 2026-09-17
**Basis:** Independent reproduction by a separately implemented harness
(Kimi Work validation pipeline, calibrated 2026-09-16 against published
causal-set/FRG/GR benchmarks), run against the canonical head
`mqgt-scf-science-public` (2026-09-14) and the Gate-1 reconciliation.
**Companion artifacts:** `MQGT_SCF_Claims_Inventory.md` (claims table and
reproduction log) and the verification scripts `mqgt_c6_independent_uv.py`,
`mqgt_t3_independent.py`, `mqgt_t1_independent.py` in this repository.

Nothing here alleges misconduct. To the contrary: the program's software
gates, blocked-mode preregistration discipline, and self-assessment all
reproduced exactly as documented on a fresh machine. The items below are
ordinary errata and open questions, found precisely because the program is
checkable.

---

## E1. UV completion wording (minor, wording only)

`uv_completion.tex` / `bridge_d_uv.py`: "No non-Gaussian fixed point found."

**Finding:** the beta system (Machacek–Vaughn one-loop matter + gravitational
screening at fixed gN\* = 1.7621271) possesses exact non-Gaussian fixed points
at λ₁ = λ₂ = 0.9c, g = 0.3c and λ₁ = λ₂ = g = c/2, where c = 16πgN/3 ≈ 29.5
(i.e. λ ≈ 26.6, g ≈ 8.9). They lie far outside the one-loop validity domain and
outside the searched positivity cone; the physical conclusion is unchanged.

**Recommended wording:** "No non-Gaussian fixed point exists *in the
perturbative domain* (positivity cone, couplings ≲ 1); all UV trajectories
from that domain flow to the Gaussian fixed point."

Verified independently: 125/125 cone trajectories → Gaussian; 5000-seed Newton
survey finds only the Gaussian FP in the perturbative region. The dynamical
one-coupling closure arithmetic (gN\* = 4.4352 / 5.0265 / −7.94 for
2-scalar / 4-scalar / full-SM) is confirmed exactly; we recommend always
printing it with its truncation label, since the two-coupling (g, λ)
Einstein–Hilbert truncation gives g\* = 0.707321 (scheme dependence).

## E2. Neutrino portal: oscillation-spectrum inconsistency (substantive)

`neutrino_portal.py`: single y_ν = 0.1976 per generation, ⟨E⟩ = 0.1 eV,
Σm_ν = 0.05928 eV, "exact match".

**Findings:**

1. The arithmetic chain is exact: 3 × 0.1976 × 0.1 = 0.05928 eV. ✓
2. The matched value is the **minimal normal-ordering sum**
   (√Δm²₂₁ + √|Δm²₃₁| ≈ 0.0587 eV from oscillation data), so y_ν = 0.1976 is a
   one-parameter fit to that floor, not an independent prediction. The
   documentation should say this.
3. **A single y_ν per generation implies a degenerate spectrum** (all Δm² = 0),
   contradicting measured Δm²₂₁ = 7.4×10⁻⁵ eV² and |Δm²₃₁| = 2.5×10⁻³ eV².
   Consistency requires generation-dependent Yukawas spanning a factor ~5.8
   (e.g. y_ν,i ∝ (0, 0.0086, 0.0501) up to normalization for minimal NO).
4. ⟨E⟩ = DETAE = 0.1 eV is anchored to the EMP-01 monitor-switching scale,
   which is itself unmeasured; the VEV is internally frozen but externally
   unanchored until EMP-01 runs. (This is already the program's stated
   dependency; flagging for reviewer visibility.)

**Recommended fix:** promote to three Yukawas y_ν,i with the oscillation
splittings as inputs; this converts the portal from a sum-fit into a
three-observable structure and strengthens testability. The claim "exact
match" should be retired in favor of "reproduces the minimal normal-ordering
sum with one fitted Yukawa scale."

## E3. T-3 spectral constant: value does not reproduce (needs convention statement)

Claim (t3_beltrami framework / CRITICAL_ASSESSMENT): ζ′_Δ₂(0) = −0.41364 on S⁷.

**Finding:** a fully independent computation — degeneracies from the SO(8)
Weyl dimension formula (validated against the scalar closed form, the
8-dimensional first harmonic, the 28 Killing vectors, and Λ^p dimensions at
k=0), eigenvalues from the quadratic Casimir (validated by the
Weyitzenböck/Killing identity Δ_H K = 2(n−1)K = 12 on S⁷), zeta machinery
validated to 61 digits against the exact massive-circle result and by direct
summation of ζ(4) on the scalar tower — gives, for the unit-radius de Rham /
Hodge Laplacian on S⁷:

| tower | ζ′(0) |
|---|---|
| scalars | −0.35076811 |
| coexact 1-forms | +0.45555786 |
| coexact 2-forms | −1.07538187 |
| **Hodge Δ₂ (coexact 2 ⊕ coexact 1)** | **−0.61982401** |

The claimed −0.41364 matches none of these, and the level-shifted tower
variant is mathematically inconsistent (breaks the degeneracy polynomial's
evenness, producing a Hurwitz pole).

**Requested resolution:** state the precise operator and spectrum convention
behind −0.41364 (de Rham/Hodge vs Branson conformal operator vs the
Dowker–Kirsten "modified" ζ-function; eigenvalue indexing; treatment of exact
vs coexact sectors). Under the standard de Rham convention the value is
−0.619824. If S7' = 0.41364 enters any downstream identity, those identities
inherit this discrepancy.

## E4. T-1 (α⁻¹ identity): FAIL confirmed; numerological-coincidence warning

The known failure reproduces exactly: formula value 137.036082448164 vs
CODATA 137.035999178, rel.dev 6.077×10⁻⁷, gate < 10⁻⁸. A pre-declared bounded
repair search (14,431 candidates across four correction families) found **no**
simple topological repair. One family produced an in-gate hit,
×(1 − (π/2)α³), residual 2.8×10⁻⁹ — but ~1.3 such hits were statistically
expected by accident in that family. **It is a coincidence and must not be
cited as support for the identity in any venue.** The repair path remains a
genuine derivation of the topological prefactor (χ(CP⁴) = 5, Pontryagin
classes, Nielsen Eq. 11 corrections), as the program's own notes indicate.

---

## What passed without qualification

- Gate-1 EMP-01 software suite: 15/15 tests pass on a fresh clone; production
  correctly blocked pending preregistration (exit 1); manifest hash
  verification passes; corrected estimand reproduces its printed table.
- The QRNG/fifth-force/neutrino channels are correctly excluded from the
  EMP-01 estimand in the current code.
- The UV-completion trajectory and fixed-point claims (E1 modulo wording).
- The neutrino-portal arithmetic (E2 modulo structure).
- CRITICAL_ASSESSMENT.md's solid/open split matches independent observation,
  including the honest T-1 FAIL.

*Prepared by the Kimi Work validation pipeline. All numbers in this document
are rerunnable from the scripts in this repository.*
