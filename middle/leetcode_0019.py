"""
    1、链表相关
"""
# 官解

# class Solution:
#     def removeNthFromEnd(head, n):
#         def getLength(head):
#             length = 0
#             while head:
#                 length += 1
#                 head = head.next
#             return length

#         dummy = ListNode(0, head)
#         length = getLength(head)
#         cur = dummy
#         for i in range(1, length - n + 1):
#             cur = cur.next
#         cur.next = cur.next.next
#         return dummy.next

# 力扣加加解法

# def removeNthFromEnd(head, n):
