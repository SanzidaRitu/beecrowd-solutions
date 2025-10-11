import math

n = float(input())
approx1 = n / math.log(n)
approx2 = 1.25506 * n / math.log(n)

print(f"{approx1:.1f} {approx2:.1f}")