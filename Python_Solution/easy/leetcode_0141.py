"""
    1、链表专题
    2、环形链表
"""
# 2022/6/9  author:Leetcode  
# 把所有遍历过的节点记录下来，每次遇到新的节点就在已遍历过的节点中查找，时间复杂度较高
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# class Solution:
#     def hasCycle(self, head):
#         seen = set()
#         while head:
#             if head in seen:
#                 return True
#             seen.add(head)
#             head = head.next
#         return False

# 2022/6/9  author:Leetcode 双指针（快慢指针）
# 快慢指针：如果存在环，则快慢指针必定会相遇
class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
