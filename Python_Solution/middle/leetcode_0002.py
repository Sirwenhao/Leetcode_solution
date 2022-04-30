"""
    1、两数相加：涉及知识点为链表
    2、难点：链表这种数据结构自己还是不知道如何写
"""
# # 力扣加加
# class ListNode:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next

# class Solution():
#     def addTwoNubmers(self, l1: ListNode, l2: ListNode):
#         """
#         type l1: ListNode
#         type l2: ListNode
#         rtype: ListNode
#         """
#         res = ListNode(0)
#         head = res
#         carry = 0
#         while l1 or l2 or carry != 0:
#             sum = carry
#             if l1:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum += l2.val
#                 l2 = l2.next

#             if sum <= 9:
#                 res.val = sum
#                 carry = 0
#             else:
#                 res.val = sum % 10
#                 carry = sum // 10

#             # creat new node
#             if l1 or l2 or carry != 0:
#                 res.next = ListNode(0)
#                 res = res.next
#         return head

# if __name__ == '__main__':
#     l1 = ListNode[2,3,4]
#     l2 = ListNode[4,5,6]
#     result = Solution().addTwoNubmers(l1, l2)
#     print(result)


# # 2022/4/30 review
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         carry, cur = 0, dummy
#         while l1 or l2 or carry != 0:
#             if not l1:
#                 sum = carry
#             else:
#                 sum = l1.val + carry

#             if not l2:
#                 sum = carry
#             else:
#                 sum = l2.val + carry

#             carry, val = divmod(sum, 10)
#             cur.next = ListNode(val)
#             cur = cur.next
#             l1 = None if not l1 else l1.next
#             l2 = None if not l2 else l2.next
#         return dummy.next


# # 爱学习的饲养员解法
# # 解法一：迭代法，容易超时,但这一版能够看得很明白
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         total = 0
#         carry = 0
#         dummy = ListNode()
#         cur = dummy
#         while(l1 != None and l2 != None):
#             total = l1.val + l2.val + carry
#             cur.next = ListNode(total % 10)
#             carry = total // 10
#             cur = cur.next
#             l1 = l1.next
#             l2 = l2.next

#         while l1 != None:
#             total = l1.val + carry
#             cur.next = ListNode(total % 10)
#             carry = total // 10
#             cur = cur.next
#             l1 = l1.next

#         while l2 != None:
#             total = l2.val + carry
#             cur.next = ListNode(total % 10)
#             carry = total // 10
#             cur = cur.next
#             l2 = l2.next

#         if carry != 0:
#             cur.next = ListNode(carry)
#         return dummy.next

# 爱学习的饲养员解法二：递归法
class Solution:
    def addTwoNumbers(self, l1, l2):
        total = l1.val + l2.val
        carry = total // 10
        dummy = ListNode(total % 10)
        if(l1.next or l2.next or carry):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += carry # 这一步是防止上一步的及位置丢失
            carry.next = self.addTwoNumbers(l1, l2)
        return dummy