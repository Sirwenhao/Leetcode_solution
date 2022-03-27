"""
    1、leetcode0021合并两个有序链表
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(None)
        cur = head
        while l1 and l2:
            if not l1:
                cur.next = l2
                break
            if not l2:
                cur.next = l1
                break
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        return head.next


if __name__ == '__main__':
    l1 = [1, 3, 4, 6]
    l2 = [2,3,4,5,6,7]

    result = Solution(l1, l2)
    print(result)


# 2022/3/26 复习

# def mergeTwoLists(l1, l2):
#     if l1 is None:
#         return l2
#     elif l2 is None:
#         return l1
#     elif l1.val < l2.val:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = self.mergeTwoLists(l2.next, l1)
#         return l2