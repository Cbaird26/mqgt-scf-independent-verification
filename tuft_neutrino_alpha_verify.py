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

print()
print("=" * 74)
print("[D] Eqs. (144)-(148): anomalous magnetic moments (g-2)")
print("=" * 74)

ell, l7, l9 = 6, 56, 16
sig3 = z3 / (4 * pi**2)
zpB7 = mpf("1.74845220444776")   # verified in [C]
zpD2 = mpf("-0.413644658189679") # verified in [C]
alpha_exp = 1 / mpf("137.0359991")
alpha_thm = 1 / mpf("137.03608244816433744")  # Theorem 48 value, verified [A]

m_e = mpf("0.51099895000")   # MeV
m_mu = mpf("105.6583755")    # MeV
m_tau = mpf("1776.86")       # MeV

def gminus2(alp, L):
    phi = alp * exp(-alp*z3*(2*ell+1)/(4*pi*ell)
                    - alp**2*z5/(4*pi**2)
                    - alp**3*abs(zpB7)/l7
                    - alp**4*abs(zpD2)/l9)
    Cdet = -(mpf("0.5") - 4*sig3)
    dphi4 = (alp/(2*pi))**2 * (pi/12) * (1 - alp*z3/(4*pi*ell)) * L*(L-2)
    dphi5 = (alp/(2*pi))**3 * Cdet * L
    dphi6 = -(alp/(2*pi))**4 * (1-sig3) * L**2*(L-2)
    return phi/(2*pi) + dphi4 + dphi5 + dphi6

cases = [("electron", m_e, "1.159652180e-3"),
         ("muon",     m_mu, "1.165920747e-3"),
         ("tau",      m_tau, "1.177365e-3")]
for aname, aa in (("alpha = experiment (137.0359991)", alpha_exp),
                  ("alpha = Theorem 48 (137.0360824)", alpha_thm)):
    print(f"\n  convention: {aname}")
    for name, mass, pr in cases:
        L = log(mass/m_e)
        a = gminus2(aa, L)
        pv = mpf(pr.replace("e-3", "")) * 1e-3
        print(f"    a_{name:8s} = {mp.nstr(a, 13)}   printed {pr}"
              f"   rel diff {float(abs(a-pv)/pv):.2e}")

print()
print("  Pulls vs experiment (using alpha = experiment):")
# electron: PDG 1.159652181(13)e-3 -> sigma 1.3e-11 ; muon: 1.165920715(146)e-3 -> sigma 1.46e-9
a_e = gminus2(alpha_exp, mpf(0)); a_mu = gminus2(alpha_exp, log(m_mu/m_e))
print(f"    electron: pred {mp.nstr(a_e,13)} vs PDG 1.159652181e-3 +/- 1.3e-11"
      f"  -> pull {float((a_e - mpf('1.159652181e-3'))/mpf('1.3e-11')):+.2f} sigma")
print(f"    muon:     pred {mp.nstr(a_mu,13)} vs PDG 1.165920715e-3 +/- 1.46e-9"
      f"  -> pull {float((a_mu - mpf('1.165920715e-3'))/mpf('1.46e-9')):+.2f} sigma")
print(f"    LQCD WP25 comparison: pred - LQCD(1.16592033e-3) = "
      f"{float(a_mu - mpf('1.16592033e-3')):.3e}")

print()
print("=" * 74)
print("[E] Eq. (78): charged lepton masses on S^3 (Theorem 34)")
print("=" * 74)

alpha_th = alpha_thm
kappa3 = exp(z3/(24*pi**2)) / (4*pi**2)
Lam_hopf = sqrt(2*pi) * v * kappa3**6      # ell/p = 6/1
a_hel = 6*sqrt(2) * exp(z3/(24*pi**2))
D_printed = {1: mpf("1.203011392"), 2: mpf("4.806545406"), 3: mpf("10.818228646")}
tau3 = {1: mpf(1), 2: mpf(1), 3: sqrt(3)}

print(f"  kappa   = {mp.nstr(kappa3, 12)}  (printed: (4pi^2)^-1 exp(zeta(3)/24pi^2))")
print(f"  Lambda_Hopf = {mp.nstr(Lam_hopf, 12)} MeV")
print(f"  a = {mp.nstr(a_hel, 12)}  (printed 8.5284)")

# Verify the sector zeta values, Eq. (79)-(81)
zH0 = lambda a_: zeta(0, a_)
zp1 = zeta(-2, 2, 1) - zeta(0, 2, 1)   # zeta'_1(0)
print(f"\n  zeta'_1(0) = {mp.nstr(zp1, 12)}   (printed 0.888490076)")
def zp_sector(n):
    return zp1 + sum(j*(j+2)*log(j+1) for j in range(1, n))
for n in (2, 3):
    print(f"  zeta'_{n}(0) = {mp.nstr(zp_sector(n), 12)}")

# Masses with printed D(n)
pdg = {1: (mpf("0.51099895000"), mpf("1.5e-7")),
       2: (mpf("105.6583755"), mpf("2.3e-6")),
       3: (mpf("1776.86"), mpf("0.12"))}
names = {1: "e", 2: "mu", 3: "tau"}
print()
for n in (1, 2, 3):
    m = Lam_hopf*(n+1)*exp(a_hel*n - D_printed[n] + n*alpha_th/6 + sig3*log(tau3[n]))
    mpdg, sig = pdg[n]
    print(f"  m_{names[n]:4s} pred = {mp.nstr(m, 12)} MeV  PDG = {mpdg}"
          f"  pull = {float((m-mpdg)/sig):+.2f} sigma")
    # D required to hit PDG exactly
    D_req = a_hel*n + n*alpha_th/6 + sig3*log(tau3[n]) - log(mpdg/(Lam_hopf*(n+1)))
    print(f"         D({n}) printed = {D_printed[n]},  D required by PDG = {mp.nstr(D_req, 12)},"
          f"  diff = {mp.nstr(D_printed[n]-D_req, 6)}")

# Compare: what does -zeta'_n(0) look like vs D(n)? (extraction audit)
print()
print("  Extraction audit: -zeta'_n(0) vs D(n), and zeta(3)n^2 asymptotic")
for n in (1, 2, 3):
    print(f"    n={n}: -zeta'_n(0) = {mp.nstr(-zp_sector(n), 12)}   D(n) = {D_printed[n]}"
          f"   D(n)-zeta(3)n^2 = {mp.nstr(D_printed[n]-z3*n**2, 6)}")

print()
print("=" * 74)
print("[F] Eq. (112): quark masses on S^5 (Theorem 37)")
print("=" * 74)

spectral5 = (3*z5 + 5*pi**2*z3) / (8*pi**4)
kappa5 = exp(spectral5/6) / (8*pi**3)
Lam5 = (2*pi/sqrt(3)) * v * kappa5**3
a5 = exp(spectral5/6) * sqrt(3) * (2 + z3/(4*pi**2))
C5 = z3/12
b5 = z5/(8*pi**4)
sig5 = z3/(16*pi**2)
tauK = {1: mpf(1), 2: mpf(4), 3: mpf(3)}

print(f"  spectral5 = {mp.nstr(spectral5, 12)}")
print(f"  kappa5 = {mp.nstr(kappa5, 12)}")
print(f"  Lambda5 = {mp.nstr(Lam5, 12)} MeV  (printed 6.09144e-2)")
print(f"  a5 = {mp.nstr(a5, 12)}  (printed 3.564112)")
print(f"  C5 = {mp.nstr(C5, 12)}  (printed 0.100171)")

def lamT(n):
    if n == 1:
        return mpf(2)/(3*sqrt(3))
    return 2/pi + (z3/(12*pi))*(mpf("2.5") - n)

def quark_mass(n, sign):
    expo = (a5 + sign*lamT(n))*n + C5*n**2 + b5*n*(n+1)/2 + sig5*log(tauK[n])
    m = Lam5*(n+1)*exp(expo)
    if n == 1:
        m *= mpf(2)/3
    return m

# assignment: n=1 -> u = -lamT, d = +lamT ; n=2 -> s = -, c = + ; n=3 -> b = -, t = +
quarks = [("u", 1, -1, "2.16", "0.07"), ("d", 1, +1, "4.67", "0.09"),
          ("s", 2, -1, "93.4", "0.8"),  ("c", 2, +1, "1270", "20"),
          ("b", 3, -1, "4180", "30"),   ("t", 3, +1, "172760", "300")]
printed_pred = {"u": "2.160005", "d": "4.66418", "s": "93.5650",
                "c": "1272.714", "b": "4172.22", "t": "172864.95"}
print()
for name, n, sgn, pdgv, pdgs in quarks:
    m = quark_mass(n, sgn)
    pp = mpf(printed_pred[name]); pv, ps = mpf(pdgv), mpf(pdgs)
    print(f"  {name}: pred {mp.nstr(m, 10)} MeV | printed {pp} (rel {float(abs(m-pp)/pp):.1e})"
          f" | PDG {pv}+/-{ps} | rel err {float((m-pv)/pv):+.4%} | pull {float((m-pv)/ps):+.2f} sigma")
print()
print(f"  lambdaT(1) = {mp.nstr(lamT(1), 10)} (2/(3 sqrt 3)); d/u ratio pred"
      f" {float(quark_mass(1,1)/quark_mass(1,-1)):.6f} vs printed {4.66418/2.160005:.6f}")
