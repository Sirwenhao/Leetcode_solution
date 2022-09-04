"""
    1、反转链表II
    2、差异：被反转的链表指定了起始点
"""
# # 2022/9/3  author:github
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

# class Solution:
#     def reverseBetween(self, head, left, right):
#         if head is None or head.next is None or left == right:
#             return head
#         dummy = ListNode(0, head)
#         pre = dummy
#         if pre.val != left:
#             pre = pre.next
#         p, q = pre, pre.next
#         cur = q
#         for _ in range(right-left+1):
#             temp = cur.next
#             cur.next = pre
#             pre, cur = cur, temp
#         p.next = pre
#         q.next = cur
#         return dummy.next

# 2022/9/3  author:WH
# 把起始点位置中间那段单独取出来，然后按照206的方法进行翻转，然后再重新链接
class Solution:
    def reverseBetween(self, head, left, right): 
        # 定义反转链表函数体
        def reverseLinkedlist(head):
            pre=None
            cur=head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 把pre移动到left的前一个位置处
        for _ in range(left-1):
            pre = pre.next

        rightNode = pre
        for _ in range(right-left+1):
            rightNode = rightNode.next
        # 切断出一个子链表
        leftNode = pre.next
        curr = rightNode.next
        # 切断原链表的链接
        pre.next = None
        rightNode.next = None
        # 翻转切出来的链表
        reverseLinkedlist(leftNode)
        # 接回到原来的链表中
        pre.next = rightNode
        leftNode.next = curr
        return dummy.next


if __name__ == "__main__":
    head = [1,2,3,4,5]
    left = 2
    right = 4
    result = Solution().reverseBetween(head, left, right)
    print(result)