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

# 23/10/18 author:WH
# 还是沿用之前的逻辑
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = 0
        l3 = ListNode(0) # l3指向一个空结点
        head = l3 # 用一个头结点指向l3，用于维护下属计算
        carry = 0
        while l1 or l2 or carry:
            sum = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry) # 此处l1和l2为0时的判断忘记了
            carry, ans = divmod(sum, 10) # divmod用法忘记了
            head.next = ListNode(ans)  # ListNode(ans)把ans转换成结点值
            l1 = l1.next if l1 else None # 这两处的判断逻辑忘记
            l2 = l2.next if l2 else None 
            head = head.next # 结点后移，继续维护运算
        return l3.next
        
            



# if __name__ == "__main__":
#     a1 = [2,4,3]
#     a2 = [5,6,4]
#     l1 = ListNode(a1)
#     l2 = ListNode(a2)
#     result = Solution().addTwoNumbers(l1, l2)
#     print(result)