'''
    1、力扣链表系列习题，反转链表
'''


# def reverseList(head):
#     if not head: return None
#     prev = None
#     cur = head
#     while cur:
#         cur.next, prev, cur = prev, cur, cur.next
#     return prev

# 2022/6/8  author:WH
# 双指针法
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# class Solution:
#     def reverseList(self, head):
#         # 创建两个指针，一个指针指向当前位置，一个指针指向下一个位置
#         cur = head
#         prev = None
#         # 创建临时指针保存节点
#         temp = None
#         while cur:
#             temp = cur.next
#             cur.next, prev = prev, cur
#             cur = temp
#         return prev

# 递归法
class Solution:
    def reverseList(self, head):

        def reverse(pre, cur):
            if not cur:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(cur, temp)

        return reverse(None, head)

