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

class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None