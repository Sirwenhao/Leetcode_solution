"""
    1、两数相加：涉及知识点为链表
    2、难点：链表这种数据结构自己还是不知道如何写
"""
# leetcode加加
class Solution():
    def addTwoNubmers(l1, l2):
        """
        type l1: ListNode
        type l2: ListNode
        rtype: ListNode
        """
        res = ListNode(0)
        head = res
        carry = 0
        while l1 or l2 or carry != 0:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            if sum <= 9:
                res.val = sum
                carry = 0
            else:
                res.val = sum % 10
                carry = sum // 10

            # creat new node
            if l1 or l2 or carry != 0:
                res.next = ListNode(0)
                res = res.next
        return head
