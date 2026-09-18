# MQGT-SCF Errata and Findings from Independent Verification

**Date:** 2026-09-17 (v3 — source manuscript located; E3 closed end-to-end,
E2 revised, T-1 source derivation verified)
**Basis:** Independent reproduction by a separately implemented harness
(Kimi Work validation pipeline, calibrated 2026-09-16 against published
causal-set/FRG/GR benchmarks), run against the canonical head
`mqgt-scf-science-public` (2026-09-14) and the Gate-1 reconciliation.
v3 additionally uses the source text: J. L. Nielsen, "The Complex Hopf
Fibration as the Canonical Space for Gauge–Gravity Unification",
Preprints.org 202604.0315.v5 (posted 2026-07-17, CC BY 4.0), 116 pp.
**Companion artifacts:** `MQGT_SCF_Claims_Inventory.md` (claims table and
reproduction log) and the verification scripts `mqgt_c6_independent_uv.py`,
`mqgt_t3_independent.py`, `mqgt_t3_reverse_search.py`,
`mqgt_t1_independent.py`, `mqgt_t1_topological_scan.py`,
`tuft_neutrino_alpha_verify.py` in this repository.

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

## E2. Neutrino portal: oscillation-spectrum inconsistency — FIX SOLVED (v3: source spectrum located)

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

**v3 revision — the source spectrum is non-degenerate; import it.** The
portal's 0.05928 eV is inherited from the Nielsen TUFT neutrino formula
(v5 preprint Eq. (136)–(142)), which predicts a **non-degenerate**
three-generation spectrum with no free parameters beyond v = 246220 MeV:
m = (0.000970, 0.008708, 0.049604) eV, Σm_ν = 0.059282 eV,
Δm²₂₁ = 7.489×10⁻⁵ eV² and Δm²₃₁ = 2.460×10⁻³ eV², at −0.2σ and +0.2σ
from the PDG central values. We re-derived the formula's spectral inputs
independently and reproduced every printed number (see E3 v3 and
`tuft_neutrino_alpha_verify.py`). The degeneracy critique in v1 therefore
applies **only to the simplified portal script** (single y_ν), not to the
underlying TUFT claim. Recommended fix, superseding variants A/B: replace
the single Yukawa with the TUFT mass vector (equivalently Yukawa ratios
(0.049, 0.441, 2.510) on the 0.01976 eV base, span 51×) and cite Eq. (136)
as the source. The portal then has a genuine three-generation prediction,
not a one-parameter fit to the normal-ordering floor.

## E3. T-3 spectral constants: RESOLVED (v3: closed end-to-end against the source derivation)

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

**E3 addendum (2026-09-17, normalization-derivation diagnosis).** We attempted
to close the remaining gap — why the constants enter Δφ_univ as α³S7/56 and
α⁴S7′/16 — and report three concrete findings:

1. **The upstream derivation skeleton is structurally incapable of producing
   the constants.** `t3_beltrami_exact.py` models the E-coupled endomorphism as
   E_p(E) = (n−p) + ηE, which makes a₄(E) *quadratic* in E, so W‴(0) and
   W⁗(0) vanish identically; it also identifies a₄ (a local heat-kernel
   coefficient) with W = log det (a spectral invariant), and its two a₄
   functions disagree on the rank factor. This is why the T-3 gate stalled at
   "BLOCKED," not lack of computing power.
2. **The sphere pattern in the phase is now structurally confirmed.** The
   exponent reads as a sum over odd spheres: α·ζ(3) (S³ sector), α²·ζ(5)
   (S⁵), α³·(S⁷ Beltrami determinant), α⁴·(S⁹ determinant). Our
   identification of S7′ on S⁹ is therefore not a foreign assignment — it is
   exactly the next entry in the program's own pattern. A naive single-coupling
   determinant-shift completion fails (κ₃ ≈ −0.78 vs κ₄ ≈ 2.82 on different
   spheres), so the α-dependence enters differently than a constant spectral
   shift; the precise entry point is defined in the Nielsen TUFT manuscript
   (Eq. 17), which is not in the public repository — that text is the missing
   input for closing the 56 = C(8,3) and 16 = 2⁴ normalizations.
3. **Bonus value for the lepton sector.** The TUFT lepton winding action
   S[A] = ½∫_{S³} A∧⋆BA (audit p. 6408) needs the S³ Beltrami determinant:
   ζ′_ce1(S³)(0) = 3.5539603045851, so det′|B| = exp(−½ζ′) = 0.169148178512
   and the Gaussian factor (det′|B|)^(−1/2) = 2.43145556544 — now computed to
   full precision whenever the sector is revisited.

**E3 v3 closure (2026-09-17).** The Nielsen manuscript (v5 preprint,
doi:10.20944/preprints202604.0315.v5) is now in hand and resolves every
open sub-item:

1. **The spheres and operators are confirmed at source.** The manuscript's
   shell table (v5 p. 80) assigns S³ → leptons (B = ⋆d on 1-forms), S⁵ →
   quarks (B on 2-forms), S⁷ → gluons, S⁹ → neutrinos (Δ₂ on coexact
   2-forms). The S⁷ misassignment was introduced in the audit layer, not in
   the source: the source has the sphere and operator right throughout.
2. **Both towers and both ζ′ values are confirmed at source** (full ms
   Eqs. (134)–(136), (143)–(154); v5 Eq. (138)). We additionally re-derived
   both values by a third, analytically exact method (polynomial expansion
   against Hurwitz ζ and ζ′ at 80-digit precision, in
   `tuft_neutrino_alpha_verify.py`): ζ′_Δ₂(S⁹)(0) = −0.413644658189679 and
   ζ′_B₇(S⁷)(0) = 1.74845220444776 — matching the printed −0.41364 and
   +1.748452 to every quoted digit. The degeneracy polynomial the
   manuscript prints for S⁹, d(k) = k(k+1)(k+3)(k+4)²(k+5)(k+7)(k+8)/720
   from the SO(10) representation [k−1,0,1,0,0], is *identical* (after
   k = K+1, x = K+5) to the polynomial we derived independently in v2 —
   two fully independent paths to the same spectrum.
3. **The framing numbers 56 and 16 are defined at source** (full ms
   Eq. (154)): ℓ₇ = dim Λ³(R⁸) = C(8,3) = 56 and ℓ₉ = 2^(10−2)/2 = 16
   (Spin(10) contact-chirality subsectors), entering Δφ_univ as
   α³|ζ′_B₇(0)|/ℓ₇ and α⁴|ζ′_Δ₂(0)|/ℓ₉ alongside ℓ = 6 (Hopf self-linking
   of the trefoil) for the α¹ coefficient 13/(24π) = (2ℓ+1)/(4πℓ) ✓.
   What remains a *postulate* rather than a theorem is the uniform
   distribution of the spectral weight over those ℓ subsectors — the
   manuscript asserts the equipartition; it does not derive it. That is
   now the precisely stated remaining gap for T-3, and it is a much
   narrower gap than before.
4. **Convention note (S⁵ shell).** The manuscript's `spectral5` =
   (3ζ(5)+5π²ζ(3))/(8π⁴) = +0.080119 omits the 2ζ′_R(0) = −ln(2π) head term
   that the full Beltrami tower on S⁵ carries (our ζ′ = −1.757764). This
   affects the quark-sector coefficient a₅, not Δφ_univ. Worth one line in
   any future edition, since an independent recomputation of the S⁵ tower
   will land on the full-tower value.

**Status: E3 closed.** What the constants are (identified, v2), that the
source derives them on the correct spheres (v3), and how the framings enter
(defined, v3) are all resolved; only the equipartition postulate remains
open, and it is now named precisely.

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

**E4 v3 note — the source derivation is Theorem 48 of the v5 preprint.**
The 137.0360824 value is produced in the source by
α = [2·Vol(S²)/(Vol(S⁴)²·Vol(RP¹))]·[Vol(S⁹)/(2⁵·5)]^{1/4} on the
S¹ → S⁹ → CP⁴ bundle, which we verified is *numerically identical* to
Wyler's bounded-symmetric-domain formula (9/8π⁴)(π⁵/1920)^{1/4}
(difference < 10⁻⁸³ at our working precision) and reproduces the printed
137.03608244816433 exactly (`tuft_neutrino_alpha_verify.py` [A]). The
manuscript labels the theorem "Derived, with one physical identification"
and supplies a uniqueness lemma (Lemma 6: any SO(10)-invariant
dimensionless fiber/gauge ratio satisfying its four conditions equals α).
This substantially strengthens the provenance of the number — it is no
longer an unmotivated literal — but our gate assessment is unchanged:
(1) the identity still misses the program's own pre-registered 10⁻⁸ gate
(6.08×10⁻⁷ off CODATA); (2) the uniqueness lemma proves uniqueness *within
the chosen ingredient set* (sphere volumes, spectral volumes, Hua
volumes); the selection of that set is where physical judgment enters, so
"not reverse-engineered" is argued, not proven; (3) none of the 58
gate-passing α³ corrections from the v2 scan may be cited as support. The
honest statement is now: "α is computed from Hopf-bundle spectral geometry
(Theorem 48) to 6 significant figures; the remaining 6×10⁻⁷ deviation is
outside the program's own gate and no certified correction exists."

## E6. Anomalous magnetic moments (new v3): formula verified — and a hidden cancellation found

The g−2 prediction (v5 Eqs. (144)–(148)) uses Δφ_univ plus three
mass-dependent holonomy terms in L = ln(m_lepton/m_e), with
σ₃ = ζ(3)/(4π²) (Lemma 4). We implemented the full system independently
(`tuft_neutrino_alpha_verify.py` [D]).

**Verified — internal consistency.** With α taken as the theory's own
Theorem 48 value (1/137.0360824), the formulas reproduce every printed
digit: a_e = 1.159652179949×10⁻³ (printed 1.159652180×10⁻³, rel diff
4×10⁻¹¹), a_μ = 1.165920746967×10⁻³ (printed …747, rel diff 3×10⁻¹¹),
a_τ = 1.177364662×10⁻³ (printed 1.177365×10⁻³, consistent at the printed
7 digits). The published σ-pull claims (0.08σ electron, 0.22σ muon) also
reproduce exactly. The formulas are implemented correctly in the source
and the comparison table is arithmetically honest.

**Found — the electron agreement depends on a cancellation.**
a_e = Δφ_univ/(2π) is essentially linear in α. If one instead inserts the
*measured* α (1/137.0359991), the same formula gives
a_e = 1.1596528842×10⁻³ — a **+54σ** deviation from experiment. In other
words the attenuated-Schwinger formula, evaluated at the true α, carries a
~6×10⁻⁷-relative residual against the full QED series; the theory's own
α is smaller than CODATA by 6.08×10⁻⁷ (the E4 gap), and that offset
cancels the residual to land on experiment at 0.08σ. One of three readings
must hold: (a) the cancellation is meaningful — α and a_e are joint
predictions of one geometry, and the 6×10⁻⁷ "error" in α is precisely the
missing higher-order content of the phase series, in which case the theory
must explain why the *independent* recoil measurements of α point the
other way; (b) the cancellation is coincidence at the 6×10⁻⁷ level — the
same magnitude as the uncertified E4 correction class, which the program's
own scan showed is densely populated by accidental gate-passers; or
(c) the phase series is an approximation good to ~10⁻⁶ relative, and the
sub-σ agreements are partly fortuitous. The muon claim is insensitive to
this (0.22σ with α_thm, 0.51σ with α_exp — both sub-σ, and the "12× closer
than LQCD WP25" comparison survives either convention, since the LQCD pull
is 2.6σ). The electron claim and the a_τ "true prediction"
(1.177365×10⁻³) both stand or fall with the α question. A clean
discriminating test: the theory's a_τ differs between the two α
conventions by ~3×10⁻¹⁰, within reach of the Belle II / CLIC sensitivities
the manuscript itself names.

## E7. Charged-lepton masses (new v3): generation structure exact; printed normalization misses PDG by one constant factor

Theorem 34 (v5 Eq. (78)) predicts the charged-lepton masses from
m_n = Λ_Hopf·(n+1)·exp(a·n − D(n) + nα/6 + σ₃lnτ₃(K_n)) with all
coefficients derived on S³: a = 6√2·exp(ζ(3)/24π²) = 8.52845144101,
κ = (4π²)⁻¹exp(ζ(3)/24π²), Λ_Hopf = √(2π)·v·κ⁶, σ₃ = ζ(3)/4π²,
τ₃ = (1, 1, √3), and D(n) "extracted from the Hurwitz evaluation" of the
sector zeta (Eq. (79)–(82)). We implemented the full system independently
(`tuft_neutrino_alpha_verify.py` [E]).

**Verified.** (a) The sector zeta chain reproduces exactly:
ζ′₁(0) = ½ln(2π) − ζ(3)/(4π²) = 0.888490076146 vs printed 0.888490076 ✓,
and Eq. (81)'s finite-sum extension ✓. (b) a, κ, σ₃ all reproduce to every
printed digit. (c) Most importantly, the *generation-to-generation*
content is exact: the required D(n) values (back-solved from PDG masses)
differ from the printed D(n) by a **constant** −3.4115×10⁻⁵ for all three
generations (drift across n: 1.7×10⁻⁹). A constant exponent offset is
absorbed entirely by the overall scale, so the n-dependent structure —
helicity a, Casimir spread D(3)−D(1) = 9.615217254, knot torsion
σ₃ln√3 — is verified to ~10⁻⁹ relative against both mass ratios.

**Found — a one-constant normalization gap.** Evaluated literally as
printed (Λ_Hopf = √(2π)vκ⁶ with κ as printed, D(n) as printed), the
formula gives m = (0.5110164, 105.66198, 1776.921) MeV vs PDG
(0.51099895, 105.6583755, 1776.86): every mass high by the *same* factor
e^{3.4115×10⁻⁵} ≈ 1.0000341, i.e. +116σ (e), +1567σ (μ), +0.51σ (τ) —
not the printed "0.00σ" table. Because the offset is n-independent, a
single missing constant factor in Λ_Hopf as printed (the text states a
constant piece of −ζ′_n(0) is "absorbed into Λ_Hopf", but the printed
Λ_Hopf formula does not produce it) explains everything; the printed mass
table was evidently generated with that factor included. Two concrete
repairs, either suffices: (i) print the full Λ_Hopf including the absorbed
constant, Λ_Hopf → Λ_Hopf·e^{−3.4115×10⁻⁵}; or (ii) give the explicit
extraction formula mapping Eq. (79)–(81) to the printed D(n) values, which
is currently not derivable from the printed text (we verified D(n) is not
ζ(3)n² + linear + constant, nor −ζ′_n(0) + quadratic). Until one of these
is printed, "0.00σ on all three leptons" should read "all three leptons
match after a single normalization constant whose printed formula is
incomplete." The physics content (the n-dependent spectrum) is unaffected.

## E9. Gauge boson and Higgs masses (new v3): structure verified; same single-constant assembly gap as E7, plus two printed-value slips

Theorem 35 (v5 Eq. (87)–(90)): m_B = ΛB·(n+1)·e^{nα/6}·T_B(n) with
ΛB = v·√(2/r)sin(π/r)·e^{−2α}, r = 8. We implemented the full chain
(`tuft_neutrino_alpha_verify.py` [G]).

**Verified.** Z_CS(S³) = √(2/8)sin(π/8) = 0.19134172, v·Z_CS = 47112.16
(printed 47112) ✓, ΛB = 46429.56 (printed 46429) ✓, the Wilson-loop
dressings T_W, T_Z (with shifted r_f = r + √3α/2π), T_H all evaluate as
printed ✓. sin²θ_W^top = 3/(4π) = 0.238732 vs PDG Thomson
0.23867 ± 0.00016 → +0.39σ ✓ (printed "0.4σ" ✓); the on-shell value from
the predicted masses 1 − m_W²/m_Z² = 0.223201 ✓ (printed 0.22320).

**Found — the E7 pattern repeats.** Evaluated literally, Eq. (87) gives
(W, Z, H) = (80413.77, 91238.07, 125294.13) MeV — every one uniformly
high by the *same* factor 1.0005504 (+3.4σ W, +24σ Z, +0.9σ H), while the
printed table (80369.5, 91187.8, 125225) sits at +0.04/+0.11/+0.23σ
(χ² = 0.067 vs printed 0.066 ✓). So the printed table is internally
consistent, but the printed formula chain is missing one constant factor
e^{−5.504×10⁻⁴} — same documentation class as E7 (leptons,
e^{−3.41×10⁻⁵}), different magnitude. Three shells, two with a missing
assembly constant (S³ leptons, S³ bosons), one complete (S⁵ quarks, E8).
Repair: print the missing factor's origin (most likely an
O(α²)-order determinant correction to ΛB — the text itself says "the
residual is O(α²)", and α² = 5.3×10⁻⁵ is the right order but the exact
value 5.504×10⁻⁴ = 10.3·α² is not derived).

**Minor printed-value slips.** The text prints g ≈ 0.6205 and
g′ ≈ 0.3469; the printed formulas (92)–(93) give g = 4π√(α/3) = 0.6198
and g′ = √(4πα)/√(1−3/4π) = 0.3471. The two printed values are also
mutually inconsistent (they imply sin²θ_W = 0.2382 and 0.2380
respectively, neither equal to 0.23873). Third-digit corrections; no
structural impact.

## E10. CKM/PMNS (new v3): both numerical CKM predictions verify; Vub and PMNS angles are not yet numerical predictions

Theorem 42 (v5 Eqs. (156)–(158)) computed from our independently
generated quark masses: |Vus| = √(m_d/m_s) = 0.223270 (printed 0.2233;
PDG pull −1.54σ vs printed −1.5 ✓) and |Vcb| = (2/3)|√(m_s/m_b) −
√(m_c/m_t)| = 0.042632 (printed 0.0426; +0.66σ vs printed +0.6 ✓). Both
also hold with PDG central masses (0.2236, 0.04249), so the results are
robust to the E8 mass residuals.

**Reviewer notes (honesty, not errors).** (a) |Vus| = √(m_d/m_s) is the
Gatto–Sartori–Tonin relation (1968), which the paper credits; its −1.5σ
residual is the *known* GST ceiling — the neglected up-type rotation
√(m_u/m_c) = 0.041 is 50× the PDG error on |Vus|, so "within 2σ" is the
right claim, not a defect, but the residual is structural to the leading
order, not experimental. (b) |Vub| is *not* numerically predicted: the
text bounds the phase factor 0 ≤ F ≤ 1 and notes PDG requires F ≈ 0.40.
(c) PMNS (Theorem 44) is a qualitative large-angle argument; the only
numeric, Δm²₃₁/Δm²₂₁ = 32.84 (printed 32.8) ✓, follows from the E2
spectrum. No θ₁₂, θ₁₃, θ₂₃ values exist yet to verify.

## E11. Cosmological constant (new v3): verified exactly, insensitive to the E6 α question

Λ = 3·exp(−(2 + ζ(3)/24)/α) in Planck units (Theorem 57/58; the identity
σ₃·ζ(2) = ζ(3)/24 checks algebraically ✓). Evaluated: exponent 280.936,
Λ = 2.940×10⁻¹²² — the printed value, under **both** α conventions
(E4/E6 note: the 6×10⁻⁷ α gap moves Λ by only 0.017%, so this prediction
does not inherit the electron g−2 cancellation problem). The exponential
structure cuts both ways: e^{−281} means a 0.4% exponent error moves Λ by
a factor of 3, so the 3-digit agreement is striking but structurally
fragile — one missing O(1) term in the exponent destroys it. The w = −1
claim is exact *by construction* (Λ defined as a topological invariant);
whether the partition-function evaluation itself is the right vacuum
energy is the assumption a referee will probe. H₀ = 68.5 km/s/Mpc is
printed in the summary table; it follows from Λ through the framework's
Friedmann sector and we did not independently re-derive it.

## E12. Part IV novel predictions (new v3): all arithmetic verifies; two interpretive claims flagged as assertions

The falsifiable forward-looking predictions (v5 Eqs. (188)–(192)) check
out numerically end-to-end (`tuft_neutrino_alpha_verify.py` [J]): both QGT
magnitudes (|Ω| = α/2π = 1.1614×10⁻³, |g| = α²/4π² = 1.3489×10⁻⁶), both
prefactors (α²/4π = 4.2376×10⁻⁶, α³/8π² = 4.9216×10⁻⁹), and **all 15
entries** of the five-configuration interferometer table (lab bench,
piezo-enhanced, ZARM free-fall tower, AION-10, AION-100 × Δφ, δθ, θ_pol)
reproduce the printed values at the printed precision, using g = 9.81 m/s²
and c exactly. The falsification thresholds in the summary table are
internally consistent with the predictions.

**Two interpretive flags (not arithmetic errors).** (a) The statement
"this is the *same* QGT recently measured by Sala et al." in
LaAlO₃/SrTiO₃ is an interpretive identification of the Bloch-band QGT of a
crystal with the spacetime fiber QGT — asserted, not derived; the paper's
own insistence that it "is not an analogy" makes this a load-bearing claim
a referee will probe hardest. (b) The dark-sector structural predictions
(w = −1, flat rotation curves, discrete v₀ clustering, no DM particle)
are qualitative in v5: the velocity-quantization relation
v₀² = 4πGλ²_Ωn (Cor. 13) appears without a numerical λ_Ω, so there is
currently no number to test; the discrete-v₀ clustering prediction needs a
predicted spectrum before it can falsify anything.

**Falsifiability assessment (the strongest feature of Part IV).** The
phase-wobble row is a genuine, clean, near-term falsifier: Δφ =
4.2×10⁻⁶ rad for a tabletop configuration against a stated
10⁻¹⁰ rad/√Hz sensitivity floor — four orders of magnitude of margin,
with GR predicting identically zero. If the MQGT-SCF program wants one
experiment to champion, this is it; it requires no new facility, only a
Mach–Zehnder with a controlled accelerated arm and Sagnac/redshift
subtraction.

## E8. Quark masses (new v3): fully verified — no erratum, one reviewer note

Theorem 37 (v5 Eq. (112)) and its supporting chain (Eqs. (100)–(111)):
κ5, Λ5 = (2π/√3)vκ5³ = 6.09144×10⁻² MeV, a5 = e^{spectral5/6}√3(2 +
ζ(3)/4π²) = 3.564112, C5 = ζ(3)/12, β5 = ζ(5)/8π⁴, σ5 = ζ(3)/16π²,
τ = (1, 4, 3), and the parity doublet λT(1) = 2/(3√3), λT(n) = 2/π +
(ζ(3)/12π)(5/2 − n) for n = 2, 3 — all reproduce to every printed digit,
and the six quark masses match the printed table to ≤ 10⁻⁶ relative with
all six PDG pulls ≤ 0.35σ (`tuft_neutrino_alpha_verify.py` [F]). The d/u
ratio (2.15934) independently confirms λT(1) = 2/(3√3) rather than
(2/3)√3. **Unlike the lepton shell (E7), the S⁵ normalization is complete
as printed** — Λ5 works exactly with no missing constant — which
strengthens the reading that E7 is an omitted factor in one printed
formula, not a structural problem. This is the strongest single
verification in the program: six masses across five orders of magnitude
(2.16 MeV to 172.9 GeV) from one closed-form system.

**Reviewer note (not an erratum):** the comparison mixes PDG quark-mass
conventions (MSbar at 2 GeV for u/d/s, MSbar at the quark mass for c/b,
direct reconstruction for t) without stating scheme or scale; a referee
will ask. The light-quark agreement (u, d, s) is a weak test at current
errors; c, b, t at 0.14–0.35σ are the substantive ones.

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
- Both T-3 constants, on the correct spheres, now confirmed against the
  source derivation by a third independent method (E3, closed).
- The TUFT neutrino spectrum formula reproduces all printed masses and
  both splittings within quoted rounding (E2 v3).
- The Theorem 48 α formula reproduces its printed value exactly and is
  numerically identical to Wyler's formula (E4 v3).
- The g−2 formula system reproduces every printed value and published
  σ-pull exactly under the theory's own α (E6); the α-dependence caveat
  is documented there.
- The charged-lepton sector zeta chain (Eq. (79)–(82)), helicity
  coefficient, and all generation-dependent content of Theorem 34 verify
  exactly; the printed overall scale is off by one constant factor
  (E7).
- The full quark sector (Theorem 37): all coefficients and all six masses
  reproduce to ≤10⁻⁶ relative, all PDG pulls ≤ 0.35σ, with no missing
  normalization (E8).
- The boson sector structure (Z_CS, Wilson-loop dressings, Weinberg angle
  3/4π at 0.39σ, on-shell sin²θ_W to 10⁻⁵) verifies; the printed boson
  formula misses one constant factor of the E7 class, and g/g′ carry
  third-digit slips (E9).
- CKM |Vus|/|Vcb| verify from independently generated masses (E10); the
  cosmological constant Λ = 2.940×10⁻¹²² reproduces exactly under both α
  conventions (E11).
- All Part IV novel-prediction arithmetic (QGT magnitudes, prefactors,
  the full 15-entry interferometer table) verifies (E12).
- CRITICAL_ASSESSMENT.md's solid/open split matches independent observation,
  including the honest T-1 FAIL, which remains open (E4).

*Prepared by the Kimi Work validation pipeline. All numbers in this document
are rerunnable from the scripts in this repository.*
