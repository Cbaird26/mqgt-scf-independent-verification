"""T-3 INDEPENDENT VERIFICATION v2 (analytic): zeta'_Delta2(0) on S^7.

Claim under test (mqgt-scf-science-public): zeta'_{Delta_2}(0) = -0.41364.

Method (no shared code):
  Degeneracies: Weyl dimension formula for SO(8) hook irreps
    scalars (k,0,0,0); coexact 1-forms (k+1,1,0,0); coexact 2-forms (k+1,1,1,0)
    dim = prod_{i<j} (l_i^2 - l_j^2)/(m_i^2 - m_j^2), l_i = lam_i + 3 - i ... (m=(3,2,1,0))
  Eigenvalues: lam_k = (k+p)(k+6-p) = (k+3)^2 - a^2, a = 3-p.
  Towers: scalar k>=1 (x=k+3>=4), coexact p>=1: k>=0 (x>=3).
  Degeneracy polys are fit in x=k+3 from 9 exact Weyl values and must come
  out EVEN (symmetry control) -- then no Hurwitz pole at w=1 occurs.

  Exact zeta'(0): with (x^2-a^2)^{-s} = sum_j (s)_j/j! a^{2j} x^{-2s-2j},
  zeta(s) = sum_m c_m [ zeta_H(2s-m, x0) + sum_{j>=1} (s)_j/j! a^{2j} zeta_H(2s+2j-m, x0) ]
  => zeta'(0) = sum_m c_m [ 2 zeta_H'(-m, x0) + sum_{j>=1} (a^{2j}/j) zeta_H(2j-m, x0) ]
  with zeta_H(w, x0) = zeta_R(w) - sum_{n<x0} n^{-w}  (finite subtraction).

CONTROLS first:
  A. Weyl scalar tower == (2k+6)(k+5)!/(720 k!); first harmonic = 8;
     coexact 1-form k=0 == SO(8) adjoint = 28 (Killing vectors).
  B. Massive scalar on circle: same machinery gives -2 ln(2 sinh(pi m)) exactly.
"""

from mpmath import (mp, mpf, nstr, zeta, log, sinh, pi, factorial, binomial)

mp.dps = 60


def weyl_so8(lam):
    m = [3, 2, 1, 0]
    l = [lam[i] + m[i] for i in range(4)]
    d = mpf(1)
    for i in range(4):
        for j in range(i + 1, 4):
            d *= mpf(l[i] ** 2 - l[j] ** 2) / (m[i] ** 2 - m[j] ** 2)
    return d


def deg_coexact(p, k):
    if p == 0:
        return weyl_so8([k, 0, 0, 0])
    lam = [k + 1] + [1] * p + [0] * (3 - p)
    return weyl_so8(lam)


def zetaR(w, x0, der=0):
    """zeta_H^{(der)}(w, x0) = zeta_R^{(der)}(w) - d/dw^der sum_{n<x0} n^{-w}."""
    val = zeta(w, derivative=der)
    for n in range(1, x0):
        if der == 0:
            val -= mpf(n) ** (-w)
        else:
            val += log(n) * mpf(n) ** (-w)
    return val


def zeta_prime0(deg_poly_x, a, x0, jmax=80):
    """deg_poly_x: dict {power m: coeff} in x; spectrum x^2 - a^2 from x0."""
    total = mpf(0)
    for m_, c in deg_poly_x.items():
        if abs(c) < mpf("1e-50"):
            continue
        total += c * 2 * zetaR(-m_, x0, der=1)
        for j in range(1, jmax + 1):
            total += c * a ** (2 * j) / j * zetaR(2 * j - m_, x0)
    return total


def control_A():
    print("[A] Weyl-dimension control")
    ok = True
    for k in range(6):
        exact = mpf(2 * k + 6) * factorial(k + 5) / (720 * factorial(k))
        ok &= abs(deg_coexact(0, k) - exact) < mpf("1e-40")
    v = deg_coexact(0, 1)
    k0 = deg_coexact(1, 0)
    tol = mpf("1e-40")
    print(f"    scalar tower k=0..5 matches closed form: {ok}")
    print(f"    first scalar harmonic = {nstr(v,5)} (need 8): {abs(v-8) < tol}")
    print(f"    coexact 1-form k=0 = {nstr(k0,5)} (SO(8) adjoint, need 28): {abs(k0-28) < tol}")
    return ok and abs(v - 8) < tol and abs(k0 - 28) < tol


def control_B():
    print("[B] massive circle: zeta'(0) vs -2 ln(2 sinh(pi m))")
    ok = True
    # binomial series converges only for m < k_min = 1, so test m <= 0.9
    for m_ in (mpf("0.3"), mpf("0.5"), mpf("0.8")):
        # lambda_k = k^2 + m^2, k in ZZ\{0} deg 2, plus zero-shift mode m^{-2s}
        # x = k >= 1, spectrum x^2 - a^2 with a = i m  -> a^{2j} = (-1)^j m^{2j}
        a = m_  # keep real; inject (-1)^j explicitly
        comp = -2 * log(m_)                      # zero mode derivative
        comp += 2 * (2 * zeta(0, derivative=1))  # deg-2 tower, j=0 term
        for j in range(1, 81):
            comp += 2 * ((-1) ** j) * a ** (2 * j) / j * zeta(2 * j)
        exact = -2 * log(2 * sinh(pi * m_))
        err = abs(comp - exact)
        ok &= err < mpf("1e-10")
        print(f"    m={nstr(m_,3)}: computed {nstr(comp,12)} exact {nstr(exact,12)} "
              f"|err|={nstr(err,2)} {'PASS' if err < mpf('1e-10') else 'FAIL'}")
    return ok


def fit_x_poly(p, xshift):
    """Fit degeneracy as polynomial in x = k + xshift (degree <= 8) from 9
    exact Weyl values. Symmetry control: odd coefficients must vanish."""
    import mpmath
    ks = list(range(9))
    ys = [deg_coexact(p, k) for k in ks]
    M = mpmath.matrix([[mpf(k + xshift) ** i for i in range(9)] for k in ks])
    c = mpmath.lu_solve(M, mpmath.matrix(ys))
    poly = {i: mpf(c[i]) for i in range(9)}
    odd = max(abs(poly.get(i, 0)) for i in (1, 3, 5, 7))
    even_max = max(abs(poly.get(i, 0)) for i in (0, 2, 4, 6, 8))
    print(f"    p={p}: |odd coefs|/|even| = {nstr(odd / even_max, 2)} "
          f"(must be ~0)")
    return {i: v for i, v in poly.items() if abs(v) > even_max * mpf("1e-30")}


def main():
    print("=" * 76)
    print("T-3 INDEPENDENT VERIFICATION: zeta'_{Delta_2}(0) on S^7")
    print("=" * 76)
    okA, okB = control_A(), control_B()
    print(f"\n    CONTROLS: A {'PASS' if okA else 'FAIL'}, B {'PASS' if okB else 'FAIL'}")
    if not (okA and okB):
        print("    CONTROL FAILURE -- target not reported.")
        return

    # Spectra from the SO(8) Casimir derivation (Delta_H = C2 on the sphere):
    #   scalars  (k,0,0,0),   k>=1: lam = (k+3)^2 - 9,  x = k+3 >= 4, a=3
    #   coexact1 (k+1,1,0,0), k>=0: lam = (k+4)^2 - 4,  x = k+4 >= 4, a=2
    #   coexact2 (k+1,1,1,0), k>=0: lam = (k+4)^2 - 1,  x = k+4 >= 4, a=1
    shift_for = {0: 3, 1: 4, 2: 4}
    print("\n[*] Degeneracy polynomials in x = k + shift (from Weyl formula)")
    polys = {p: fit_x_poly(p, shift_for[p]) for p in (0, 1, 2)}
    for p, poly in polys.items():
        print(f"    p={p}: " + " + ".join(f"{nstr(v,6)} x^{i}" for i, v in sorted(poly.items())))

    print("\n[*] zeta'(0) per tower")
    a_for = {0: mpf(3), 1: mpf(2), 2: mpf(1)}
    x0_for = {0: 4, 1: 4, 2: 4}
    z = {}
    for p in (0, 1, 2):
        z[p] = zeta_prime0(polys[p], a_for[p], x0_for[p])
        print(f"    coexact {p}-forms (x0={x0_for[p]}, a={a_for[p]}): "
              f"zeta'(0) = {nstr(z[p], 12)}")

    z_hodge2 = z[2] + z[1]
    claimed = mpf("-0.41364")
    print(f"\n    Hodge Delta_2 = coexact(2) + coexact(1):")
    print(f"    zeta'_Delta2(0) = {nstr(z_hodge2, 12)}   claimed -0.41364")
    print(f"    |diff| = {nstr(abs(z_hodge2 - claimed), 3)}")
    print(f"    VERDICT: {'MATCHES claim' if abs(z_hodge2 - claimed) < mpf('1e-4') else 'DISAGREES'}")
    print(f"    (also: coexact-2 only = {nstr(z[2], 12)}, in case their Delta_2 "
          f"meant the coexact tower alone)")


if __name__ == "__main__":
    main()
