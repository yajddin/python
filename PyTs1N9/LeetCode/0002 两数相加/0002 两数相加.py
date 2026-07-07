def addTwoNumbers(l1,l2):
	num1 = int(''.join(map(str, l1[::-1])))
	num2 = int(''.join(map(str, l2[::-1])))
	num = num1 + num2
	return [int(i) for i in str(num)][::-1]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(addTwoNumbers(l1,l2))

# 石山代码 👇👇👇👇👇👇👇👇👇👇👇👇👇👇
# str_num1 = []
# str_num2 = []
# for i in range(arr1_len, 0, -1):
# 	str_num1.append(arr1[i - 1])
# for i in range(arr2_len, 0, -1):
# 	str_num2.append(arr2[i - 1])
# num1 = int(''.join(map(str, str_num1)))
# num2 = int(''.join(map(str, str_num2)))
# num = num1 + num2
#
# arr = [int(i) for i in str(num)][::-1]
# print("arr ", arr)
