def minimumCost(cost) -> int:
	cost.sort()
	cost.reverse()
	sums = 0
	length = len(cost)

	for i in range(length):
		if i >= 2 and (i - 2) % 3 == 0:
			cost[i] = 0
		sums += cost[i]

	return sums

print(minimumCost([6,5,7,9,2,2]))

# for _ in range(2, length, 3):
# 	print(_)
# 	print(cost[_])
# 	cost[_] = 0
# for _ in range(length):
# 	sums += cost[_]
