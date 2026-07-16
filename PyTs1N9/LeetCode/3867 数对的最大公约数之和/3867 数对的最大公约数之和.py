from math import gcd

nums = [3, 6, 2, 8]
prefixGcd = []
for i in range(len(nums)):
	max_num = max(nums[:i + 1])
	prefixGcd.append(gcd(nums[i], max_num))
prefixGcd.sort()
pairs = [
	(prefixGcd[i], prefixGcd[-i - 1])
	for i in range(len(prefixGcd) // 2)
]
result = sum(gcd(a, b) for a, b in pairs)
