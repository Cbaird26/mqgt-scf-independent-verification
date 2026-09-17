# MQGT-SCF Errata and Findings from Independent Verification

**Date:** 2026-09-17 (v2 — with fixes and resolutions found during repair pass)
**Basis:** Independent reproduction by a separately implemented harness
(Kimi Work validation pipeline, calibrated 2026-09-16 against published
causal-set/FRG/GR benchmarks), run against the canonical head
`mqgt-scf-science-public` (2026-09-14) and the Gate-1 reconciliation.
**Companion artifacts:** `MQGT_SCF_Claims_Inventory.md` (claims table and
reproduction log) and the verification scripts `mqgt_c6_independent_uv.py`,
`mqgt_t3_independent.py`, `mqgt_t3_reverse_search.py`,
`mqgt_t1_independent.py`, `mqgt_t1_topological_scan.py` in this repository.

Nothing here alleges misconduct. To the contrary: the program's software
gates, blocked-mode preregistration discipline, and self-assessment all
reproduced exactly as documented on a fresh machine. The items below are
ordinary errata and open questions, found precisely because the program is
checkable. v2 records what the repair pass could fix outright, what it could
identify but not derive, and what remains open.

---

## E1. UV completion wording (minor, wording only)

`uv_completion.tex` / `bridge_d_uv.py`: "No non-Gaussian fixed point found."

**Finding:** the beta system (Machacek–Vaughn one-loop matter + gravitational
screening at fixed gN* = 1.7621271) possesses exact non-Gaussian fixed points
at λ₁ = λ₂ = 0.9c, g = 0.3c and λ₁ = λ₂ = g = c/2, where c = 16πgN/3 ≈ 29.5
(i.e. λ ≈ 26.6, g ≈ 8.9). They lie far outside the one-loop validity domain and
outside the searched positivity cone; the physical conclusion is unchanged.

**Recommended wording (fix):** "No non-Gaussian fixed point exists *in the
perturbative domain* (positivity cone, couplings ≲ 1); all UV trajectories
from that domain flow to the Gaussian fixed point."

Verified independently: 125/125 cone trajectories → Gaussian; 5000-seed Newton
survey finds only the Gaussian FP in the perturbative region. The dynamical
one-coupling closure arithmetic (gN* = 4.4352 / 5.0265 / −7.94 for
2-scalar / 4-scalar / full-SM) is confirmed exactly; we recommend always
printing it with its truncation label, since the two-coupling (g, λ)
Einstein–Hilbert truncation gives g* = 0.707321 (scheme dependence).

## E2. Neutrino portal: oscillation-spectrum inconsistency — FIX SOLVED

`neutrino_portal.py`: single y_ν = 0.1976 per generation, ⟨E⟩ = 0.1 eV,
Σm_ν = 0.05928 eV, "exact match".

**v1 findings (stand):** (1) arithmetic exact (3 × 0.1976 × 0.1 = 0.05928 ✓);
(2) the matched value is the minimal normal-ordering sum ≈ 0.0587 eV, so the
single Yukawa is a one-parameter fit to that floor; (3) one y_ν implies a
degenerate spectrum, contradicting Δm²₂₁ = 7.42×10⁻⁵ eV² and
|Δm²₃₁| = 2.517×10⁻³ eV²; (4) ⟨E⟩ = 0.1 eV remains anchored to the unmeasured
EMP-01 scale.

**v2 fix — the 3-Yukawa texture is exactly solvable.** With m_i = 0.01976·r_i
eV (r_i = y_ν,i/y_ν) and the two oscillation splittings as inputs, there are
two natural closures:

| variant | (m₁, m₂, m₃) meV | Yukawa ratios r_i | span r₃/r₁ | Σm_ν |
|---|---|---|---|---|
| **A: sum rule preserved** (Σm_ν = 0.05928 eV fixed) | (0.481, 8.627, 50.172) | (0.0243, 0.4366, 2.5391) | **104×** | 0.05928 eV ✓ |
| **B: naturalness capped** (span ≤ 5.8×) | (8.781, 12.301, 50.932) | (0.4444, 0.6225, 2.578) | 5.8× | 0.0720 eV |

Both fit both splittings exactly. The choice is a genuine fork for the
program: variant A keeps the published sum rule but demands a hierarchical
Yukawa texture (104×, similar in kind to the charged-fermion hierarchies the
program already tolerates); variant B keeps the Yukawas O(1)-like but the sum
floats to 0.0720 eV — still below the cosmological bound (~0.12 eV) but no
longer equal to the minimal-NO floor, so the "Σm_ν = 0.05928 eV" claim would
become "Σm_ν ≈ 0.072 eV." Variant A is the conservative repair (no printed
number changes; only the texture is added). The claim "exact match" should in
either case be retired in favor of "reproduces the normal-ordering spectrum
with a fitted Yukawa scale and a texture."

## E3. T-3 spectral constants: RESOLVED — both constants identified, geometry reassigned

Claim (t3_beltrami framework): S7 = 1.748452 and S7′ = 0.41364, audited as
"ζ′_Δ₂(0) = −0.41364 on S⁷." Upstream self-rates T-3 **FAIL** in
`manifest.json`: the constants are "paper-quoted literals, not derived."

**v1 finding (stands):** on the standard unit-radius de Rham/Hodge convention
on S⁷, ζ′_Δ₂(0) = **−0.61982401** (coexact 2-forms alone: −1.07538187). The
audited identification "ζ′_Δ₂(0)|_{S⁷} = −0.41364" is wrong.

**v2 resolution.** A pre-declared reverse-engineering scan
(`mqgt_t3_reverse_search.py`: all coexact p-form towers on round unit S^n,
n = 1,3,5,7,9,11; full Hodge towers; conformal scalars; ζ(0); multiples
±1/2, ±1, ±2; radius diagnostics; Killing and Λ^p degeneracy anchors all pass)
identifies **both** constants exactly:

| constant | paper value | identified as | computed | agreement |
|---|---|---|---|---|
| S7 (α³/56 coeff) | 1.748452 | **½ ζ′(0), coexact 3-forms on S⁷** | 1.74845220444776 | all 7 digits (2.0×10⁻⁷) |
| S7′ (α⁴/16 coeff) | 0.41364 | **−ζ′(0), coexact 2-forms on S⁹** | 0.41364465819 | all 5 digits (4.7×10⁻⁶) |

Why this is physically coherent:

- The program's operator is the **Beltrami operator B = ⋆d on S⁷**, which acts
  on 3-forms; B² on coexact 3-forms is the Hodge Laplacian. Since the B
  spectrum is ±-symmetric, ζ′_{|B|}(0) = ½ ζ′_{B²}(0) — precisely the factor
  of ½ in S7. The ce3 tower on S⁷ is pure-square (λ_k = (k+4)², degeneracy
  (x²−1)(x²−4)(x²−9)/18 for x = k+4), so S7 = ½ζ′_{|⋆d|}(0) requires no
  expansion at all.
- S⁹ is not arbitrary: it is the sphere of the **S¹ → S⁹ → CP⁴ Hopf
  fibration**, which the program's own compactification map
  (`compactification_map.py`) lists as "S⁹ → CP⁴ base: gravity + scalars."
  The T-1 α⁻¹ identity is built on the same fibration. The two "TUFT dressing
  constants" therefore live on the two spheres of the fibration: S7 on S⁷
  (Beltrami sector) and S7′ on S⁹ (fibration sphere).

Chance-coincidence assessment: two independent constants both landing on
sphere spectral determinants to full quoted precision, with the ½ factor
independently motivated by the stated operator, is not plausibly accidental
(joint accident probability ≲ 10⁻⁶ under the pre-declared family count).

**Consequences.** (a) The constants are no longer quoted literals — they are
identified spectral determinants, and the universal phase
Δφ_univ = α·exp(−αζ(3)·13/(24π) − α²ζ(5)/(4π²) − α³S7/56 − α⁴S7′/16) can now
be written with derived constants. (b) The geometry assignment in the audit
and in the T-3 narrative must be corrected: S7′ is not an S⁷ quantity. (c) The
remaining derivation gap — why Δφ_univ's α³/56 and α⁴/16 coefficients are
these determinants, via the Gilkey a₄ E-coupling expansion — is unchanged and
still open; this resolution tells you *what* the constants are, not yet *why
they appear* with those normalizations.

**Numerics caution (documented in the script):** high-precision sphere zeta
computations via ζ_R(w) − Σ_{n<x₀} n^{−w} suffer catastrophic cancellation for
w ≳ dps/0.301, producing a spurious harmonic tail; v2 uses a hybrid
direct-sum Hurwitz for w > 40. All values above are stable under
jmax/precision ladders and x₀-shift consistency (|Δ| = 3.9×10⁻⁴⁷).

## E4. T-1 (α⁻¹ identity): FAIL confirmed; gate-passing corrections provably uncertifiable

The failure reproduces exactly: formula value 137.036082448164 vs CODATA
137.035999178, rel.dev 6.077×10⁻⁷, gate < 10⁻⁸. Required correction:
×(1 − δ), δ = 6.07651×10⁻⁷.

**v2 sharpening (`mqgt_t1_topological_scan.py`).** Writing δ = c·α³ requires
c = 1.563718224. A pre-declared family of 13,057 expressions built only from
the topological integers the program itself names (χ(CP⁴) = 5, Pontryagin
coefficients, 9, 8, 1920, 4) and π contains **128 distinct values within
0.05 of c_req, of which 58 pass the 1e-8 gate** — including c = π/2
(residual 2.8×10⁻⁹) and c = χ²/2⁴ = 25/16 (residual 4.7×10⁻¹⁰). Gate-passing
is therefore **necessary but vacuous as evidence**: no α³-order correction
from this class can be certified without a structural derivation, and none of
these values (the v1 π/2 hit included) may be cited as support for the
identity in any venue. The repair path remains a genuine derivation of the
topological prefactor from the Hopf volume asymptotics (Nielsen Eq. 11).

## E5. Minor: Pontryagin classes of CP⁴ misprinted (documentation)

`t1_hopf_final.py` prints "p₁ = 10h², p₂ = 35h⁴" for CP⁴. With
p(TCPⁿ) = (1+h²)^{n+1}, the correct values are p₁(CP⁴) = 5h² and
p₂(CP⁴) = 10h⁴. No computed result in the repository depends on the printed
values; corrected here so any future prefactor derivation uses the right
classes.

---

## What passed without qualification

- Gate-1 EMP-01 software suite: 15/15 tests pass on a fresh clone; production
  correctly blocked pending preregistration (exit 1); manifest hash
  verification passes; corrected estimand reproduces its printed table.
- The QRNG/fifth-force/neutrino channels are correctly excluded from the
  EMP-01 estimand in the current code.
- The UV-completion trajectory and fixed-point claims (E1 modulo wording).
- The neutrino-portal arithmetic (E2; texture fix supplied above).
- Both T-3 constants, once assigned to the correct spheres (E3).
- CRITICAL_ASSESSMENT.md's solid/open split matches independent observation,
  including the honest T-1 FAIL, which remains open (E4).

*Prepared by the Kimi Work validation pipeline. All numbers in this document
are rerunnable from the scripts in this repository.*
