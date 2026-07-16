from math import gcd

# 改为保存当前最大值，复杂度降为 O(n log n)：
nums = [3, 6, 2, 8]
prefixGcd = []
max_num = 0
for num in nums:
    max_num = max(max_num, num)
    prefixGcd.append(gcd(num, max_num))
prefixGcd.sort()
result = sum(
    gcd(prefixGcd[i], prefixGcd[-i - 1])
    for i in range(len(prefixGcd) // 2)
)

# 超出时间限制 双重循环计算前缀最大值，时间复杂度是 O(n²)
# nums = [3, 6, 2, 8]
# prefixGcd = []
# for i in range(len(nums)):
# 	max_num = max(nums[:i + 1])
# 	prefixGcd.append(gcd(nums[i], max_num))
# prefixGcd.sort()
# pairs = [
# 	(prefixGcd[i], prefixGcd[-i - 1])
# 	for i in range(len(prefixGcd) // 2)
# ]
# result = sum(gcd(a, b) for a, b in pairs)
