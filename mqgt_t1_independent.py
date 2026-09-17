"""T-1 INDEPENDENT ANALYSIS: alpha^-1 volume-ratio identity gate.

Claim under test (mqgt-scf-science-public, t1_hopf_complete.py / Theorem 66):
    alpha^-1 = (9/(8 pi^4)) * (pi^5/1920)^(1/4) = 137.03608245
    CODATA 2022: 137.035999177(21)   -> rel.dev 6.077e-7, gate needs < 1e-8.

This file:
  1. Re-verifies the arithmetic.
  2. Computes the exact needed correction delta = CODATA / current.
  3. Runs a PRE-DECLARED, bounded correction search over four families, with
     explicit candidate counts and expected accidental-hit rates, so that any
     "match" comes with its multiple-comparison context. A numerological hit
     is NOT a derivation and does not pass the gate; the gate additionally
     requires topological derivation. Families:
       F1: multiply by (1 +/- 1/n), n = 2..5000            (9998 candidates)
       F2: multiply by (1 +/- 1/n)^(1/4) style root/pow variants, p in
           {1/4, 1/2, 2, 4}, n = 2..500                    (3992 candidates)
       F3: additive log-correction delta ~= q * alpha^m for q in a declared
           20-constant set, m = 1..6                        (240 candidates)
       F4: modify the integer 1920 -> 1920 + k, k = -100..100 (201 candidates)
     Hit criterion: |rel.dev after correction| < 1e-8 (the gate itself).
"""

from mpmath import mp, mpf, nstr, pi, log, zeta, e, euler, sqrt, phi

mp.dps = 60

CODATA = mpf("137.035999178")     # CODATA 2022 central value
CODATA_ERR = mpf("0.000000035")   # (21) -> ~3.5e-8 abs -> 2.6e-10 relative


def current_alpha_inv():
    # NOTE: the published expression (9/(8pi^4))(pi^5/1920)^(1/4) = 0.0072973
    # is alpha itself; alpha^-1 is its reciprocal (mirrors their script's
    # CURRENT = 1/alpha_inv_original()).
    return 1 / ((mpf(9) / (8 * pi ** 4)) * (pi ** 5 / 1920) ** (mpf(1) / 4))


def reldev(v):
    return abs(v - CODATA) / CODATA


def main():
    print("=" * 76)
    print("T-1 INDEPENDENT ANALYSIS: alpha^-1 identity gate")
    print("=" * 76)

    cur = current_alpha_inv()
    print(f"\n[0] arithmetic re-verification")
    print(f"    formula value : {nstr(cur, 15)}")
    print(f"    CODATA 2022   : {nstr(CODATA, 15)} +/- {nstr(CODATA_ERR, 3)}")
    print(f"    rel.dev       : {nstr(reldev(cur), 4)}  (gate: < 1e-8 -> FAIL, as they report)")
    delta = CODATA / cur
    print(f"    needed multiplicative correction: 1 + ({nstr(delta - 1, 6)})")
    print(f"    needed log correction: {nstr(log(delta), 12)}")

    GATE = mpf("1e-8")

    # ----------------------------------------------------------- F1
    print(f"\n[F1] (1 +/- 1/n), n = 2..5000   [9998 candidates]")
    hits = []
    for n in range(2, 5001):
        for sgn in (1, -1):
            v = cur * (1 + mpf(sgn) / n)
            if reldev(v) < GATE:
                hits.append((n, sgn, reldev(v)))
    exp_hits = 9998 * 2 * GATE * CODATA / 1  # window 2e-8 rel around target vs spacing 1/n^2-scale
    print(f"    hits: {len(hits)}")
    for n, sgn, rd in hits[:10]:
        print(f"      n={n}, sign={'+' if sgn>0 else '-'}, residual rel.dev {nstr(rd,2)}")
    # honest expectation: spacing of successive 1/n values near the target
    # n ~ 1646 is 1/n^2 ~ 3.7e-7, ~18x wider than the gate window 2e-8, so an
    # accidental hit would occur with probability ~5%; 0 observed is
    # unremarkable either way.

    # ----------------------------------------------------------- F2
    print(f"\n[F2] (1 +/- 1/n)^p, p in (1/4, 1/2, 2, 4), n = 2..500   [3992]")
    hits2 = []
    for n in range(2, 501):
        for sgn in (1, -1):
            for p in (mpf(1) / 4, mpf(1) / 2, mpf(2), mpf(4)):
                v = cur * (1 + mpf(sgn) / n) ** p
                if reldev(v) < GATE:
                    hits2.append((n, sgn, p, reldev(v)))
    print(f"    hits: {len(hits2)}")
    for n, sgn, p, rd in hits2[:10]:
        print(f"      n={n}, sign={'+' if sgn>0 else '-'}, p={nstr(p,3)}, "
              f"residual {nstr(rd,2)}")

    # ----------------------------------------------------------- F3
    print(f"\n[F3] delta = 1 + q * alpha^m, 20 declared constants, m = 1..6 [240]")
    consts = {
        "pi/2": pi / 2, "pi": pi, "pi^2": pi ** 2, "zeta(3)": zeta(3),
        "zeta(5)": zeta(5), "ln2": log(2), "euler_gamma": euler, "e": e,
        "sqrt2": sqrt(2), "phi": phi, "1/2": mpf("0.5"), "1/pi": 1 / pi,
        "2/pi": 2 / pi, "pi/4": pi / 4, "3/2": mpf("1.5"), "2": mpf(2),
        "1": mpf(1), "pi^2/6": pi ** 2 / 6, "6/pi^2": 6 / pi ** 2,
        "zeta(3)/(4pi^2)": zeta(3) / (4 * pi ** 2),
    }
    alpha = 1 / CODATA
    hits3 = []
    need = delta - 1
    for name, q in consts.items():
        for m_ in range(1, 7):
            for sgn in (1, -1):
                v = cur * (1 + sgn * q * alpha ** m_)
                if reldev(v) < GATE:
                    hits3.append((name, m_, sgn, reldev(v)))
    print(f"    hits: {len(hits3)}")
    for name, m_, sgn, rd in hits3:
        print(f"      q={name}, m={m_}, sign={'+' if sgn>0 else '-'}, "
              f"residual {nstr(rd,2)}")
    # expected accidents: count family members within 10% of the needed
    # correction, then scale by (gate window)/(10% window).
    near = sum(1 for name, q in consts.items() for m_ in range(1, 7)
               for sgn in (1, -1)
               if abs(log(abs(sgn * q * alpha ** m_) / abs(need))) < log(mpf("1.1")))
    print(f"    family density near target (within 10%): {near}/480; "
          f"expected in-gate accidents ~= {near} * 1e-8/(0.1*|delta-1|) "
          f"= {nstr(near * GATE / (mpf('0.1') * abs(need)), 3)}")

    # ----------------------------------------------------------- F4
    print(f"\n[F4] 1920 -> 1920 + k, k = -100..100   [201]")
    hits4 = []
    for k in range(-100, 101):
        v = 1 / ((mpf(9) / (8 * pi ** 4)) * (pi ** 5 / (1920 + k)) ** (mpf(1) / 4))
        if reldev(v) < GATE:
            hits4.append((k, reldev(v)))
    print(f"    hits: {len(hits4)} (spacing per k-step ~ delta(1/4k/1920) "
          f"~ 8e-8 rel -> expect ~0-1 accidental)")
    for k, rd in hits4:
        print(f"      k={k}, residual {nstr(rd,2)}")

    print("\n" + "=" * 76)
    print("INTERPRETATION")
    print("=" * 76)
    print("  The gate is a derivation, not a fit: even a residual < 1e-8 from F1-F4")
    print("  would be numerology unless the factor is derived from the Hopf/")
    print("  topological structure. In this run, the single F3 hit")
    print("  (1 - (pi/2) alpha^3, residual 2.8e-9) sits in a family where ~1.3")
    print("  accidental in-gate hits were EXPECTED -- it is consistent with pure")
    print("  coincidence and must not be cited as support for the identity.")
    print("  Absent a derived prefactor, Theorem 66 as stated remains FAIL at the")
    print("  8-digit gate, exactly as the program's own CI reports.")


if __name__ == "__main__":
    main()
