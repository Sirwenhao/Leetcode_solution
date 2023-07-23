# 2023/7/21
# 两数相加

# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(0)
        head = ans
        carry = 0
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(sum, 10)
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next


# if __name__ == "__main__":
#     a1 = [2,4,3]
#     a2 = [5,6,4]
#     l1 = ListNode(a1)
#     l2 = ListNode(a2)
#     result = Solution().addTwoNumbers(l1, l2)
#     print(result)