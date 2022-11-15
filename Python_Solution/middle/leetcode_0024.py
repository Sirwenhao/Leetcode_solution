"""
    1、链表相关，两两交换节点
    2、链表技巧——初始化指向链表表头的哑节点
"""

# 力扣加加解法同力扣官解解法一递归
# class Solution:
#     def swapPairs(self, head):
#         dummy = ListNode(0, head)

#         if not head or not head.next:
#             return head
#         _next = head.next
#         head.next = self.swapPairs(_next.next)
#         _next.next = head
#         return _next

# 力扣官解解法二：迭代
# 创建哑节点dummy指向头节点，令dummy.next=heaad，每次交换dummy后面的两个节点
# 交换前：dummy->node1->node2，交换后：dummy->node2->node1
# 具体操作为：temp.next = node2,node1.next=node2.next,node2.next = node1


# class Solution:
#     def swapPairs(self, head):
#         dummy = ListNode(0)
#         dummy.next = head
#         temp = dummy

#         while temp.next and temp.next.next:
#             node1 = temp.next
#             node2 = temp.next.next
#             temp.next = node2
#             node1.next = node2.next
#             node2.next = node1
#             temp = node1
#         return dummy.next


# 2022/11/14 author:WH
class SOlution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummy.next