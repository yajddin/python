# 思路1： 统计目标字母数量
def maxNumberOfBalloons_01(text):
	count = {}
	for ch in text:
		count[ch] = count.get(ch, 0) + 1
	return min(
		count.get('b',0),
		count.get('a',0),
		count.get('l',0) // 2,
		count.get('o',0) // 2,
		count.get('n',0),
	)

if __name__ == '__main__':
    print(maxNumberOfBalloons_01("loonbalxballpoon"))
