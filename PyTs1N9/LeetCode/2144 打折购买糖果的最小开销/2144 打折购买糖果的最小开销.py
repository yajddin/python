# C语言运行消耗内存9MB Python语言运行消耗内存19MB 消耗内存差异原因如下：
# C 的 int 数组：
#  1. 一块连续内存，直接存整数
#  2. 原地排序，额外内存很少
# Python 的 list：
#  1. 一块指针数组，每个指针再指向一个 Python int 对象，存的是对象
#  2. 带解释器运行

def minimumCost(cost) -> int:
	cost.sort()
	cost.reverse()
	sums = 0
	length = len(cost)

	for i in range(length):
		if i % 3 != 2:
			sums += cost[i]

	return sums

print(minimumCost([6, 5, 7, 9, 2, 2]))

# for _ in range(2, length, 3):
# 	print(_)
# 	print(cost[_])
# 	cost[_] = 0
# for _ in range(length):
# 	sums += cost[_]
