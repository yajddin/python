cost = [6, 5, 7, 9, 2, 2]
cost.sort()
cost.reverse()
sums = 0
length = len(cost)

for _ in range(2, length, 3):
	print(_)
	print(cost[_])
	cost[_] = 0
for _ in range(length):
	sums += cost[_]
