"""T-1 TOPOLOGICAL-CORRECTION SCAN (disciplined, pre-declared).

Claim under test: TUFT Eq. (11)  alpha^-1 = (9/(8 pi^4)) (pi^5/1920)^(1/4)
= 137.036082448164, vs CODATA 137.035999178 -> rel dev 6.077e-7, gate FAIL
(needs < 1e-8). Upstream (t1_hopf_final.py) itself states the correction
needs "topological factors": chi(CP^4)=5, Pontryagin classes, 4 pi^2 volumes.

Required: alpha^-1 -> alpha^-1 (1 - delta), delta = 6.0766e-7.
Since alpha^3 = 3.88776e-7, any correction of order alpha^3 needs a
coefficient c = delta/alpha^3 ~ 1.563.

DISCIPLINE: the coefficient must come from a PRE-DECLARED family built only
from the topological integers the program itself names
  {chi=5, p1 coeff (5 correct / 10 as printed upstream), p2 coeff
   (10 correct / 35 as printed upstream), 9, 8, 1920 = 2^7*3*5, 4}
and pi. Family:
  c = A/B, A*pi/B, A/(B*pi), A*pi^2/B, A/(B*pi^2),  A,B in 1..64
Gate: |c - c_req| small enough that the corrected alpha^-1 passes rel.dev<1e-8.
ACCIDENT TEST: count how many DISTINCT family values pass. If >~1 passes,
the gate cannot certify any single one -> correction must be derived
structurally, not fitted. Also note: upstream prints p1=10h^2, p2=35h^4 for
CP^4; the correct values are p1=5h^2, p2=10h^4  (p(TCP^n)=(1+h^2)^{n+1}).
"""

from mpmath import mp, mpf, pi, nstr

mp.dps = 60

CODATA = mpf("137.035999178")
FORMULA = mpf("137.036082448164")

ALPHA = 1 / CODATA
DELTA = (FORMULA - CODATA) / FORMULA
C_REQ = DELTA / ALPHA ** 3

print("=" * 74)
print("T-1 TOPOLOGICAL-CORRECTION SCAN")
print("=" * 74)
print(f"delta required        = {nstr(DELTA, 10)}")
print(f"alpha^3 (CODATA)      = {nstr(ALPHA**3, 10)}")
print(f"c_req = delta/alpha^3 = {nstr(C_REQ, 10)}")

# coefficient tolerance: corrected value passes rel.dev < 1e-8
# residual = FORMULA*(1 - c*alpha^3) vs CODATA
def residual(c):
    return abs(FORMULA * (1 - c * ALPHA ** 3) - CODATA) / CODATA

# pre-declared family
vals = {}
for A in range(1, 65):
    for B in range(1, 65):
        vals[A / B] = f"{A}/{B}"
        vals[A * pi / B] = f"{A}pi/{B}"
        vals[A / (B * pi)] = f"{A}/({B}pi)"
        vals[A * pi ** 2 / B] = f"{A}pi^2/{B}"
        vals[A / (B * pi ** 2)] = f"{A}/({B}pi^2)"

near = [(abs(v - C_REQ), v, name) for v, name in vals.items()
        if abs(v - C_REQ) < mpf("0.05")]
near.sort()
print(f"\nfamily size: {len(vals)} expressions; distinct values within 0.05 of c_req: {len(near)}")
print("\nnearest candidates (residual rel.dev after applying correction):")
npass = 0
for d, v, name in near[:15]:
    r = residual(v)
    ok = r < mpf("1e-8")
    npass += ok
    print(f"    c = {name:12s} = {nstr(v, 10)}  |c-c_req|={nstr(d, 4)}  "
          f"residual={nstr(r, 3)}  {'GATE-PASS' if ok else 'fail'}")
total_pass = sum(1 for d, v, name in near if residual(v) < mpf("1e-8"))
print(f"\nDISTINCT family values passing the 1e-8 gate: {total_pass}")
print("accident interpretation: with ~%d values within 0.05 and gate width "
      "~0.05," % len(near))
print("multiple passes are expected by construction -> no single correction")
print("can be certified without a structural derivation.")

# the two named candidates
for label, c in [("pi/2", pi / 2), ("chi^2/2^4 = 25/16", mpf(25) / 16),
                 ("chi/pi", 5 / pi), ("p1/pi (correct p1=5)", 5 / pi)]:
    print(f"    named: c={label:24s} {nstr(c, 10)} residual={nstr(residual(c), 3)}")

print("\nrequired correction factor T =", nstr(1 - DELTA, 12))
print("conclusion: T-1 remains OPEN pending structural derivation of c.")
