# MQGT-SCF Claims Inventory — Pipeline Stage 1–2 Output

**Date:** 2026-09-17 · **Built by:** Kimi Work (Zora workspace) against the canonical head
**Canonical chain (by date, per owner instruction):**
1. `mqgt-scf-science-public` (GitHub, pushed 2026-09-14) — **canonical software head**
2. `ToE-MQGT-SCF` closeout `toe-closeout-v1` (2026-09-12) — gates repo
3. Rxiv/Zenodo anchor paper (2026-09-12) — "MQGT-SCF as a Minimal Scalar-Singlet EFT:
   Specification-Level Closure, Local GKSL Measurement Dynamics, and an H2
   Interferometric Exclusion Observable" — most conservative theoretical statement
4. Zenodo corpus v1.0.4 (record 22736998); version family DOI 10.5281/zenodo.14019809
5. Local corpus editions v1.0.1–v1.0.3 (July 2026) — **superseded**, retained as provenance;
   `claim_status_matrix_v1_0_3` useful as historical index

**Framework in one line:** GR + SM extended by two real scalar singlets — Φ_c
(consciousness) and E (ethical) — with local GKSL measurement dynamics, an
asymptotic-safety UV completion attempt, an E-scalar Dirac neutrino mass portal,
and a preregistered interferometric exclusion observable (EMP-01).

---

## A. Claims table (status = program's own assessment; ✓/✗ = tonight's independent run)

| # | Claim | Their status | Independent check 2026-09-17 |
|---|-------|--------------|------------------------------|
| C1 | EMP-01 Gate-1 software: corrected N0 sign, absolute-visibility estimator, η inversion per block | Implemented | ✓ **15/15 unit tests pass** on fresh clone |
| C2 | Analyzer blocks production without preregistration | Documented | ✓ Confirmed: historical CSV → `BLOCKED: preregistration_incomplete`, exit 1 |
| C3 | Gate-1 manifest hash integrity (13 files) | Implemented | ✓ Verified, exit 0 |
| C4 | Corrected estimand α_on/off formulas with N1 common-mode null | Documented in GATE1_RECONCILIATION | ✓ `falsifiable_predictions.py` reproduces printed table; honestly labeled "illustrative only" |
| C5 | QRNG/fifth-force/neutrino claims are **separate channels**, not EMP-01 | Corrected 2026-09-14 | ✓ Confirmed in current code (earlier QRNG misidentification retracted) |
| C6 | UV completion: gN\* ≈ 4.435 (2 scalars), ≈ 5.03 (4 scalars); SM matter → no physical UV FP; matter → Gaussian | "Solid" | ☐ Not yet independently run (`bridge_d_uv*.py`, `uv_dynamical_gn_complete.py`) |
| C7 | Neutrino portal: Σm_ν = 0.05928 eV "exact match"; y_ν = 0.1976/gen; ⟨E⟩ = DETAE = 0.1 eV from emp01 | "Solid" (VEV no longer ad hoc) | ⚠ Arithmetic exact; single-y_ν contradicts oscillations; **3-Yukawa fix solved** (variants A/B, §E-C7, errata E2) |
| C8 | T-3: S7 = 1.748452, S7' = 0.41364; ζ′_Δ2(0) = −0.41364 | "Solid" (framework) | ✓ **RESOLVED**: S7 = ½ζ′_ce3(S⁷) = 1.74845220445 (7 digits); S7′ = −ζ′_ce2(S⁹) = 0.41364465819 (5 digits); audit's S⁷-Δ₂ assignment wrong (errata E3) |
| C9 | T-1: α⁻¹ = 137.03608245 via Hopf volume ratio (Theorem 66) | **Known FAIL** (6 digits vs 8+ target) | ✗ **Independently reproduced the failure**: rel.dev 6.077×10⁻⁷ vs CODATA 137.035999178; v2: 58 pre-declared candidates pass gate ⇒ corrections uncertifiable, derivation required (errata E4) |
| C10 | Φ_c/E experimental signatures (interferometry V/V₀ = e^(−ΓTΔX²), fifth force, QRNG bias) | Untested; blocked pending lab preregistration | ☐ Correctly blocked; no experimental claims to verify |

## B. What tonight's independent run establishes

1. **The software discipline is real.** Tests, blocked mode, manifest hashing, and
   the retracted QRNG misidentification all behave exactly as documented on a
   fresh machine. This is not common in independent-theory repos and should be
   said publicly.
2. **The self-assessment is accurate.** CRITICAL_ASSESSMENT.md's "solid vs open"
   split matches what an independent runner observes, including the honest T-1 FAIL.
3. **The live frontier is exactly where they say it is:**
   - **T-1** — α⁻¹ to 8+ digits; current identity is 6.077×10⁻⁷ off (6 digits);
     needs corrected Hopf S¹→S⁹→CP⁴ volume ratio with topological prefactors
     (χ(CP⁴)=5, Pontryagin classes, Nielsen Eq. 11 correction).
   - **T-3** — first-principles Beltrami spectral determinant on S⁷ (Gilkey a₄,
     η-invariant) to *derive* S7/S7′ rather than fit them.
   - **UV** — beyond Gaussian FP with matter: R²/R_μν² operators, full SM content
     (currently gN\* goes negative with SM), momentum-dependent FRG beyond LPA.
   - **EMP-01** — lab preregistration decisions (all null in the draft JSON).

## C. What the validated pipeline (built 2026-09-16) can attack next

| Target | Pipeline asset | Expected value |
|---|---|---|
| C6 UV completion | Independently-built FRG integrator (`frg_eh_truncation.py`, validated to Reuter's 6 decimals) | Reproduce gN\* ≈ 4.435/5.03 from scratch; test R² extension; cross-check the "SM → no FP" claim — this is the single most decision-relevant claim in the program |
| C7 neutrino portal | Direct arithmetic + literature values | Verify 0.05928 eV chain end-to-end; check what "exact match" depends on (normal ordering? current PDG central values?) |
| C8 T-3 spectral | sympy + numeric zeta evaluation | Independent ζ′_Δ2(0) on S⁷; then the Gilkey a₄ derivation attempt |
| C9 T-1 (the open gate) | Topological volume-ratio computation + Lean formalization | The honest hard problem; a Lean-checked volume identity would settle whether the 6-digit match is structural or coincidental |
| C10 EMP-01 | Already-gated analyzer | Nothing to compute until preregistration; pipeline role is reviewing the preregistration draft decisions |

## D. Guardrails (carried from the program's own documents, endorsed)

- PASS_SYNTHETIC is software validation on labeled simulated input, not an experiment.
- The Φ_c/E sector is **untested**; every empirical claim routes through EMP-01
  preregistration or the separate (retracted-from-EMP-01) QRNG channel.
- "Exact match" claims (C7) must state their dependence on input oscillation
  parameters and ordering assumptions before external reviewers will credit them.
- Hash agreement = byte identity, not scientific validity (their words; correct).

---

*Next action queued: independent reproduction of C6 (`bridge_d_uv_4scalar.py` vs
the pipeline's own FRG integrator), then C7 arithmetic audit.*

---

## E. Stage-3 independent verification results (2026-09-17, this machine)

### C6a — Bridge-D UV claim (fixed gN\* = 1.7621271): **VERIFIED, with a scoping nuance**
Independent implementation from the printed equations (`mqgt_c6_independent_uv.py`:
closed-form fixed-point solve + analytic-Jacobian Newton + own RK4, 125-IC cone,
t_max = 20):
- **125/125 trajectories flow to the Gaussian FP** (worst endpoint 1.4×10⁻⁵) —
  their "matter → Gaussian in the UV" claim reproduces exactly.
- 5000-seed Newton survey of the perturbative region (λ ≤ 2, g ≤ 1) finds **only**
  the Gaussian FP.
- **Nuance found by the exact analysis:** the quadratic system possesses two
  non-Gaussian FPs at λ = 0.9c ≈ 26.6, g = 0.3c ≈ 8.86 and a degenerate one at
  λ = g = c/2 ≈ 14.8 (c = 16πg_N/3). Both lie far outside the one-loop
  Machacek–Vaughn validity domain, so the physical conclusion stands — but the
  paper's wording "no non-Gaussian fixed point found" should read "**none in the
  perturbative domain**". Recommend the errata file.

### C6b — Dynamical gN\* closure: **arithmetic CONFIRMED; scheme caveat noted**
β_gN = 2gN + (a_matter − 19/12π)gN² gives gN\* = 2/(a_grav − a_matter):
2 scalars → **4.4352** (claimed 4.435 ✓); 4 scalars → **5.0265** (claimed 5.03 ✓);
full SM (N_s=2, N_f=45, N_v=12) → **−7.94** (claimed negative ✓).
Caveat for external review: this is a one-coupling closure; the validated
two-coupling (g, λ) Einstein–Hilbert truncation gives g\* = 0.707321
(pipeline Phase 2). The 4.435 value is truncation- and scheme-dependent and
should always be printed with that label.

### C7 — Neutrino portal: **arithmetic CONFIRMED; "exact match" claim must be narrowed**
- Chain arithmetic: m_ν = 0.1976 × 0.1 eV = 0.01976 eV/gen, Σm_ν = 0.05928 eV ✓.
- **Finding 1 (what the match IS):** 0.05928 eV ≈ the minimal normal-ordering sum
  from oscillation data (√Δm²₂₁ + √|Δm²₃₁| ≈ 0.0587 eV). The y_ν = 0.1976 is a
  one-parameter fit to that floor — "exact match to the NO minimal sum," not an
  independent prediction.
- **Finding 2 (a genuine problem):** a single y_ν per generation gives a
  *degenerate* spectrum (Δm² = 0), contradicting measured Δm²₂₁ = 7.4×10⁻⁵ eV²
  and |Δm²₃₁| = 2.5×10⁻³ eV². Consistency requires generation-dependent y_ν
  spanning a ~5.8× ratio. As written, the portal fits Σm_ν but violates
  oscillation splittings — recommend errata + a 3-yukawa version (which would
  also make it testable).
- **Finding 3 (circularity risk):** ⟨E⟩ = DETAE = 0.1 eV is anchored to the
  EMP-01 monitor-switching scale, which is itself unmeasured. The VEV is
  internally frozen (good) but externally unanchored until EMP-01 runs.
- **RESOLUTION (2026-09-17 v2):** the 3-Yukawa repair is exactly solved.
  Variant A (sum rule preserved, Σm_ν = 0.05928 eV): (m₁,m₂,m₃) =
  (0.481, 8.627, 50.172) meV, Yukawa ratios (0.0243, 0.4366, 2.5391), span
  104×. Variant B (span capped at 5.8×): (8.781, 12.301, 50.932) meV, ratios
  (0.4444, 0.6225, 2.578), Σm_ν floats to 0.0720 eV (still below the ~0.12 eV
  cosmological bound). Both fit Δm²₂₁ and |Δm²₃₁| exactly. The program must
  choose: keep the printed sum (A, hierarchical texture) or keep O(1) Yukawas
  (B, sum becomes ≈0.072 eV). See errata E2.

### Pipeline self-note
This session again validated the harness pattern: a naive trajectory-threshold
bug in *my own* first C6a run (1e-3 cut at t_max=10 vs the κ-decay timescale)
was caught by comparing against their published endpoint values before any
claim was written. Controls first, conclusions second.

### C8 — T-3 spectral constant: **claim does NOT reproduce under standard conventions**
Fully independent computation (`mqgt_t3_independent.py`): degeneracies derived
from the SO(8) Weyl dimension formula for the hook irreps (validated: scalar
tower matches closed form; first harmonic = 8; coexact 1-form k=0 = 28 = Killing
vectors; degeneracy polynomials come out even in the level variable as symmetry
demands, and equal x²(x²−1)(x²−4)/360, x²(x²−1)(x²−9)/60, x²(x²−4)(x²−9)/24 —
checking to C(8,p+1) at k=0); eigenvalues derived from the quadratic Casimir,
validated by the Weitzenböck/Killing identity Δ_H K = 2(n−1)K = 12 on S⁷;
zeta machinery validated to 61 digits on the massive circle and by direct
summation of ζ(4) on the S⁷ scalar tower (agreement to the tail bound).
Results (unit S⁷, de Rham/Hodge Laplacian):
- scalar tower: ζ′(0) = **−0.35076811**
- coexact 1-forms: ζ′(0) = **+0.45555786**
- coexact 2-forms: ζ′(0) = **−1.07538187**
- **Hodge Δ₂ (coexact 2 + coexact 1): ζ′(0) = −0.61982401**
The claimed **ζ′_Δ₂(0) = −0.41364 matches none of these**. A misindexed-tower
variant (shifting the level origin by one) was tested and is mathematically
inconsistent (degeneracy polynomial loses evenness → Hurwitz pole at w=1).
Open question for the program: state the exact operator and spectrum
convention behind −0.41364 (Gilkey/Dowker–Kirsten "modified" ζ? Branson
conformal operator? different shift?), because under the standard de Rham
convention the value is −0.619824. Errata item.

- **RESOLUTION (2026-09-17 v2, `mqgt_t3_reverse_search.py`):** both quoted
  constants are now *identified* as spectral determinants, on the spheres of
  the program's own Hopf structure:
  - **S7 = 1.748452 = ½ ζ′(0) of coexact 3-forms on S⁷** (computed
    1.74845220444776; all 7 digits). The ce3 tower is pure-square,
    λ_k = (k+4)², deg = (x²−1)(x²−4)(x²−9)/18, x = k+4 (k=0 anchor = C(8,4) =
    70 ✓). The ½ is the |B| vs B² relation for the Beltrami operator B = ⋆d on
    S⁷ 3-forms — the program's stated operator.
  - **S7′ = 0.41364 = −ζ′(0) of coexact 2-forms on S⁹** (computed
    0.41364465819; all 5 digits; x₀-shift consistent to 3.9×10⁻⁴⁷). S⁹ is the
    sphere of the S¹ → S⁹ → CP⁴ fibration in the program's own
    compactification map — the same fibration behind T-1.
  The audit's assignment "ζ′_Δ₂(0) on S⁷" is wrong (that value is −0.619824);
  the constants convert from quoted literals into identified spectral
  determinants. What remains open is the *derivation* of their α³/56, α⁴/16
  normalizations via the Gilkey a₄ E-coupling expansion. Numerics caution:
  ζ_R(w)−head subtraction is catastrophically unstable for w ≳ dps/0.301
  (harmonic ghost tail); the scan uses hybrid direct-sum Hurwitz for w > 40.

### C9 — T-1 α⁻¹ identity: **FAIL confirmed; no simple repair; one flagged coincidence**
`mqgt_t1_independent.py`:
- Arithmetic verified: formula gives 137.036082448164 vs CODATA
  137.035999178 → rel.dev 6.077×10⁻⁷, exactly their documented failure.
  Needed correction: ×(1 − 6.07651×10⁻⁷).
- Pre-declared bounded search (14,431 candidates across four families, hit =
  residual rel.dev < 10⁻⁸): F1 (1±1/n, n≤5000): 0 hits; F2 (root/power
  variants): 0; F4 (integer 1920 ± k, |k|≤100): 0.
- **F3 produced one in-gate hit:** correction (1 − (π/2)α³), residual 2.8×10⁻⁹.
  However the pre-declared family density implies ~1.3 accidental in-gate hits
  were *expected* — the hit is consistent with pure coincidence, carries no
  topological motivation, and **must not be cited as support**. The gate is a
  derivation, not a fit.
- Verdict: Theorem 66 remains FAIL at the 8-digit gate; the repair requires an
  actual topological derivation (χ(CP⁴)=5 / Pontryagin / Nielsen Eq. 11 route
  noted in their code comments), not a search. A Lean-checked volume identity
  remains the right eventual tool.
- **SHARPENED (2026-09-17 v2, `mqgt_t1_topological_scan.py`):** writing the
  required correction as c·α³ needs c = 1.563718224. A pre-declared family of
  13,057 expressions from the program's own topological integers (χ=5,
  Pontryagin coefficients, 9, 8, 1920, 4) and π contains **58 distinct values
  that pass the 1e-8 gate** (π/2 at 2.8×10⁻⁹; χ²/2⁴ = 25/16 at 4.7×10⁻¹⁰;
  56 others). Gate-passing in this class is therefore vacuous as evidence; no
  α³-order correction is citable without a structural derivation. Also noted:
  `t1_hopf_final.py` misprints p₁(CP⁴) = 10h², p₂ = 35h⁴; correct values are
  p₁ = 5h², p₂ = 10h⁴ (errata E5).
