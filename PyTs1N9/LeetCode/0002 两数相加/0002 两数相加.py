################# LeetCode环境已经打好 ###############
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
####################################################
class Solution:

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            cur.next = ListNode(total % 10)

            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# 列表思维 👇👇👇链表不支持下标或切片
# def addTwoNumbers(l1,l2):
# 	num1 = int(''.join(map(str, l1[::-1])))
# 	num2 = int(''.join(map(str, l2[::-1])))
# 	num = num1 + num2
# 	return [int(i) for i in str(num)][::-1]
#
# l1 = [2,4,3]
# l2 = [5,6,4]
# print(addTwoNumbers(l1,l2))

# 石山代码 👇👇👇
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
