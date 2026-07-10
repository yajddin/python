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

# 思路2： 利用python set()集合，通过集合元素唯一性进行统计
def maxNumberOfBalloons_02(text):
	target = "balloon"
	return min(text.count(c) // target.count(c) for c in set(target))

if __name__ == '__main__':
    print(maxNumberOfBalloons_01("loonbalxballpoon"))
    print(maxNumberOfBalloons_02("nlaebolko"))