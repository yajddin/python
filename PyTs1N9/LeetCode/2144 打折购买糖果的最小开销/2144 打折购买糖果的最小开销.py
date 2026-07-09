arr = [4,2,3,1]
arr.sort()
arr.reverse()
sums = 0
length = len(arr)

for _ in range(2, length, 3):
	print(_)
	print(arr[_])
	arr[_] = 0
for _ in range(length):
	sums += arr[_]
