"""
    1、链表相关
"""
# # 官解,方法一：添加哑节点(dummy node)在头部，可以避免对头节点进行特殊判断
# 时间复杂度O(L),空间复杂度O(1),L为链表长度
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def getLength(head):
#             length = 0
#             while head:
#                 length += 1
#                 head = head.next
#             return length

#         dummy = ListNode(0, head)
#         length = getLength(head)
#         cur = dummy
#         for i in range(1, length - n + 1):
#             cur = cur.next
#         cur.next = cur.next.next
#         return dummy.next # dummy是指向链表表头的哑节点，其后面的节点才是真正要返回的值

# # 官解，方法二：栈，将链表的节点依次入栈，在指定位置出pop出栈顶元素即可。主要是利用栈的删除操作
# 时间复杂度O(L),空间复杂度O(L),L为链表长度
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0, head)
#         stack = list()
#         cur = dummy
#         while cur:
#             stack.append(cur) # 先入栈的元素，后出栈
#             cur = cur.next

#         for i in range(n):
#             stack.pop()

#         prev = stack[-1] # 这时的stack[-1]即为倒数第n个元素
#         prev.next = prev.next.next
#         return dummy.next

# 官解，方法三：双指针
# 使用快慢指针，快指针比慢指针超前n个节点，这样当快指针指向链表尾部时，慢指针指向倒数第n个节点
# 时间复杂度O(L),空间复杂度O(1),L为链表长度
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0, head)
#         first = head
#         second = dummy
#         for i in range(n):
#             first = first.next

#         while first:
#             first = first.next
#             second = second.next

#         second.next = second.next.next
#         return dummy.next
        
# 总结：
# 添加哑节点的好处：
# 1、一般在头结点之前添加哑节点，这样子可以避免因头节点不存在前驱节点而导致对头结点的单独讨论
# 2、其返回值部分直接使用return dummy.next，其中的dummy.next刚好就是操作之后的链表
# 3、栈需要牺牲一点空间，来换取删除操作的便利性
# 4、上述三种操作均默认不释放被删除节点对应的空间

# # 2022/4/23 review
# # 需要删除的位置是倒数第n个节点
# class Solution:
#     def removeNthFromEnd(head, n):
#         def getLength(head):
#             l = 0
#             while head:
#                 head = head.next
#                 l += 1
#             return l

#         dummy = ListNode(0, head) # 指定位置0为头结点位置
#         length = getLength(head)
#         cur = dummy
#         for i in range(1, length-n+1):
#             cur = cur.next
#         cur.next = cur.next.next
#         return 

# 2022/6/8  author:WH
# class ListNode:
#     def __init__(self, val=0, next = None):
#         self.val = val
#         self.next = None
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         # 添加虚拟头节点
#         dummy_node = ListNode(0)
#         dummy_node.next = head

#         # 设置快慢两个指针，其间距为n，则当快指针走到尾部时，慢指针所在位置即为需要删除的位置
#         slow, fast = dummy_node, dummy_node
#         while(n!=0):
#             fast = fast.next
#             n -= 1
#         while(fast != None):
#             slow = slow.next
#             fast = fast.next

#         # fast走到最后时，slow刚好在倒数第n个节点
#         slow.next = slow.next.next # 删除倒数第n个节点
#         return dummy_node.next

# 2022/7/3  author:WH
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         dummyNode = ListNode()
#         dummyNode.next = head
#         cur = head
#         while n != 0:
#             cur = cur.next
#             n -= 1
#         while cur != None:
#             dummyNode = dumyNode.next
#             cur = cur.next
#         dummyNode.next = dumyNode.next.next
#         return dummyNode.next

# # 2022/9/20  author:WH
# # 这个题目初始化部分有个坑，如果初始化快慢指针为头节点时，对于单个元素的用例可能不能AC
# class ListNode:
#     def __init__(self, val=0, next=None) -> None:
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         dummyNode = ListNode()
#         dummyNode.next = head
#         slow = fast = dummyNode
#         while n:
#             fast = fast.next
#             n -= 1
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
#         slow.next = slow.next.next
#         return dummyNode.next

# 2022/11/12 author:WH
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

