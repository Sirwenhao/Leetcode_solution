"""
    1、链表专题
    2、环形链表II
"""
# 2022/6/9  author:WH 
# 判断是是否有环可以使用快慢指针，fast指针先进环，slow指针后进环
# 若有环，则两者一定会相遇。fast指针每次走走两个节点，slow指针每次走一个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def detectCycle(self, head):
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             # 如果相遇
#             if slow == fast:
#                 p = head
#                 q = slow
#                 while p != q:
#                     p = p.next
#                     q = q.next
#                 return p
#         return None


# 2022/09/20  author:WH
# 难点一是否有环可以判断出，难点二何处重叠判断不出来
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                index1 = slow
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None