'''
    1、python中的链表操作还是不熟悉
    2、不熟悉的是具体的表示方法以及链表相应的语法
'''

# class ListNode:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next

# def removeElements(head:ListNode, val:int):
#     prev = ListNode(0)
#     prev.next = head
#     cur = prev
#     while cur.next:
#         if cur.next.val == val:
#             cur.next = cur.next.next
#         else:
#             cur = cur.next
#     return prev.next


# head = ListNode(1,0)
# val = 6
# result = removeElements(head, val)

# 2022/6/7 author:WH
# 此处关于链表的习题有个直接经验是在头部添加虚拟节点dummy
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head, val):
#         dummy_head = ListNode(next=head)
#         cur = dummy_head
#         while(cur.next != None):
#             if cur.next.val == val:
#                 cur.next = cur.next.next # 删除节点cur.next
#             else:
#                 cur = cur.next
#         return dummy_head.next

# 2022/09/21 author:WH
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

if __name__ == "__main__":
    head = [1,2,3,4,5,6,7]
    val = 6
    result = Solution().removeElements(head, val)
    print(result)
