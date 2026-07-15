from math import gcd

n = 4
sumOdd = 0
sumEven = 0
for _ in range(1, 2 * n, 2):
	sumOdd += _
for _ in range(2, 2 * n + 1, 2):
	sumEven += _
gcd = gcd(sumOdd, sumEven)
print(gcd)

# ??????????????
# n = 5
# gcd = n
