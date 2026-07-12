# 双重循环 + 列表
def lengthOfLongestSubstring_1(s):
	max_len = 0
	for i in range(len(s)):
		arr = []
		for j in range(i, len(s)):
			if s[j] in arr:
				break
			arr.append(s[j])
			max_len = max(max_len, len(arr))
	return max_len

# 滑动窗口 + 字典
def lengthOfLongestSubstring_2(s):
	start = -1
	d = {}
	max_len = 0
	for i in range(len(s)):
		if s[i] in d and d[s[i]] > start:
			start = d[s[i]]
			d[s[i]] = i
		else:
			d[s[i]] = i
			if i - start > max_len:
				max_len = i - start
	return max_len

# 如果字符串不包含中文(只有ASCII字符)，可以用固定数组代替字段，空间O(1)
# 最快版本 时间O(n) 空间O(1)
def lengthOfLongestSubstring_3(s: str):
	last = [-1] * 128
	left = 0
	max_len = 0

	for right, char in enumerate(s):
		index = ord(char)
		left = max(left, last[index] + 1)
		last[index] = right
		max_len = max(max_len, right - left + 1)

	return max_len

print(lengthOfLongestSubstring_1("abcabcbb"))
print(lengthOfLongestSubstring_2("abcabcbb"))
print(lengthOfLongestSubstring_3("abcabcbb"))
