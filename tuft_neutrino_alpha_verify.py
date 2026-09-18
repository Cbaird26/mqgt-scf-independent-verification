#!/usr/bin/env python3
"""
Independent verification of Nielsen TUFT v5 (preprints202604.0315.v5):
  [A] Theorem 48 fine-structure constant formula (p. 92 of PDF)
  [B] Eq. (136) three-generation neutrino mass spectrum (pp. 78-80 of PDF)
  [C] Spectral zeta inputs re-derived independently from the stated spectra:
      - S^9 coexact 2-form Laplacian tower, zeta'_D2(0) = -0.41364...
      - S^7 coexact 3-form Beltrami tower, zeta'_B7(0) = +1.74845...
Method for [C]: exact polynomial expansion against Hurwitz zeta (no cutoff
ambiguity): for d(j) polynomial in j and eigenvalue j,
    sum_j d(j) j^{-s} = sum_p c_p zeta_H(s - p, a),
and for the S^9 tower d is a polynomial in x = K+5 with lambda = x^2 - 4:
    (x^2-4)^{-s} = x^{-2s} sum_m binom(-s,m) (-4)^m x^{-2m},
    d/ds binom(-s,m)|_{s=0} = (-1)^m / m  (m>=1),
so zeta'(0) is a rapidly convergent series in (4/25)^m of Hurwitz values and
derivatives. 80-digit precision. No fitting anywhere.
Run: python3 tuft_neutrino_alpha_verify.py
"""
from mpmath import mp, mpf, pi, zeta, sqrt, exp, log, gamma

mp.dps = 80

def volS(d):  # unit d-sphere surface volume
    return 2 * pi ** ((d + 1) / 2) / gamma((d + 1) / 2)

print("=" * 74)
print("[A] Theorem 48: alpha from S^1 -> S^9 -> CP^4 spectral geometry")
print("=" * 74)
V2, V4, V9 = volS(2), volS(4), volS(9)
NB = (V9 / (2**5 * 5)) ** mpf("0.25")          # Step 3 normalization, n = 5
alpha_pred = (2 * V2) / (V4**2 * pi) * NB       # Vol(RP^1) = pi
wyler = (mpf(9) / (8 * pi**4)) * (pi**5 / 1920) ** mpf("0.25")
print(f"  alpha^-1 predicted = {mp.nstr(1/alpha_pred, 20)}")
print(f"  alpha^-1 experiment = 137.0359991(2)")
print(f"  relative deviation  = {float(abs(1/alpha_pred - mpf('137.0359991'))/mpf('137.0359991')):.3e}")
print(f"  Wyler closed-form identity check: |diff| = {float(abs(alpha_pred - wyler)):.3e}")

print()
print("=" * 74)
print("[C] Independent spectral zeta inputs (analytic Hurwitz method)")
print("=" * 74)

def zH(q, a):  return zeta(q, a)
def zHp(q, a): return zeta(q, a, 1)   # d/dq

# ---- S^9: Delta_2 coexact 2-forms; lambda_k=(k+2)(k+6), k>=1
# d(k) = k(k+1)(k+3)(k+4)^2(k+5)(k+7)(k+8)/720.
# Substitute k = K+1, x = K+5: d = x^2 (x^2-1)(x^2-9)(x^2-16)/720,
# lambda = x^2 - 4.  Expand y(y-1)(y-9)(y-16), y = x^2:
#   = y^4 - 26 y^3 + 169 y^2 - 144 y
POLY_S9 = {4: mpf(1), 3: mpf(-26), 2: mpf(169), 1: mpf(-144)}  # powers of y=x^2
def zeta_prime_s9(M=60):
    tot = mpf(0)
    for p, cp in POLY_S9.items():
        c = cp / 720
        # m = 0 term: 2 * zeta_H'(-2p, 5)
        t = 2 * zHp(-2*p, 5)
        # m >= 1 terms: (4^m / m) * zeta_H(2m - 2p, 5)
        for m in range(1, M + 1):
            t += (mpf(4)**m / m) * zH(2*m - 2*p, 5)
        tot += c * t
    return tot

zp_s9 = zeta_prime_s9()
print(f"  zeta'_D2(S^9)(0) independent = {mp.nstr(zp_s9, 15)}")
print(f"  Nielsen printed value        = -0.41364")

# ---- S^7: B = *d coexact 3-forms; eigenvalue j, j>=4,
# d(j) = (j^2-1)(j^2-4)(j^2-9)/18 = (j^6 - 14 j^4 + 49 j^2 - 36)/18
def zeta_prime_b7():
    return (zHp(-6, 4) - 14*zHp(-4, 4) + 49*zHp(-2, 4) - 36*zHp(0, 4)) / 18

zp_b7 = zeta_prime_b7()
print(f"  zeta'_B7(S^7)(0) independent = {mp.nstr(zp_b7, 15)}")
print(f"  Nielsen printed value        = +1.748452")

print()
print("=" * 74)
print("[B] Eq. (136)-(142): three-generation neutrino spectrum")
print("=" * 74)

z3, z5 = zeta(3), zeta(5)
v = mpf(246220)  # MeV, electroweak VEV (sole unit-conversion input)

def spectrum(zp9):
    kappa9 = exp(zp9/16) / (32 * pi**5)
    Lam9 = sqrt(2*pi) * v * kappa9**4     # MeV
    a9 = sqrt(5)
    C9 = -z3/8 * (1 + z3/28)
    b9 = z5 / (8 * pi**4)
    s9 = z3 / (8 * pi**2)
    tau = {1: mpf(1), 2: mpf(4), 3: mpf(3)}
    out = {}
    for n in (1, 2, 3):
        m = Lam9 * (n+1) * exp(a9*n + C9*n**2 + b9*n*(n+1)/2 + s9*log(tau[n]))
        out[n] = m * 1e6                  # MeV -> eV
    return Lam9, out

printed = {1: mpf("0.000970"), 2: mpf("0.008708"), 3: mpf("0.049604")}
for label, zp in (("printed zeta' = -0.41364", mpf("-0.41364")),
                  ("full-precision zeta'", zp_s9)):
    Lam9, m = spectrum(zp)
    ssum = sum(m.values())
    dm21 = float(m[2]**2 - m[1]**2)
    dm31 = float(m[3]**2 - m[1]**2)
    print(f"\n  convention: {label}")
    print(f"    Lambda9 = {float(Lam9):.6e} MeV   (v5 prints 6.052e-11)")
    for n in (1, 2, 3):
        print(f"    m_{n} = {float(m[n]):.9f} eV   (printed {printed[n]}, "
              f"rel diff {float(abs(m[n]-printed[n])/printed[n]):.2e})")
    print(f"    sum m_nu = {float(ssum):.6f} eV   (v5: ~0.059; Planck bound < 0.12)")
    print(f"    Dm^2_21 = {dm21:.4e} eV^2   (printed 7.489e-5; PDG 7.53+/-0.18 e-5)")
    print(f"    Dm^2_31 = {dm31:.4e} eV^2   (printed 2.460e-3; PDG 2.453+/-0.033 e-3)")
    print(f"    pulls: Dm^2_21 {(dm21-7.53e-5)/0.18e-5:+.2f} sigma,"
          f" Dm^2_31 {(dm31-2.453e-3)/0.033e-3:+.2f} sigma")

print()
print("Implied Yukawa ratios vs a single-scale seesaw base of 0.01976 eV")
Lam9, m = spectrum(mpf("-0.41364"))
base = mpf("0.01976")
print("  y_n = m_n / 0.01976 eV:",
      {n: float(m[n]/base) for n in (1, 2, 3)})
print(f"  span y_3/y_1 = {float(m[3]/m[1]):.1f}x")
