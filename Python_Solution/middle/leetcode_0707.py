"""
    1、设计链表
    2、链表专题系列
"""
# 2022/6/7  author:WH
# 单链表
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class MyLinkedList:
#     def __init__(self):
#         self._head = Node(0) # 虚拟头部节点
#         self._count = 0 # 添加的节点数

#     def get(self, index):
#         if 0 <= index <= self._count:
#             node = self._head
#             for _ in range(index + 1):
#                 node = node.next
#             return node.val
#         else:
#             return -1

#     def addAtHead(self, val):
#         self.addAtIndex(0, val)

#     def addAtTail(self, val):
#         self.addAtIndex(self._count, val)

#     def addAtIndex(self, index, val):
#         if index < 0:
#             index = 0
#         elif index > self._count:
#             return

#         # 链表长度+1
#         self._count += 1
#         add_node = Node(val)
#         prev_node, current_node = None, self._head
#         for _ in range(index + 1):
#             prev_node, current_node = current_node, current_node.next
#         else:
#             prev_node.next, add_node.next = add_node, current_node

#     def deleteAtIndex(self, index):
#         if 0 <= index < self._count:
#             self._count -= 1
#             prev_node, current_node = None, self._head
#             for _ in range(index + 1):
#                 prev_node, current_node = current_node, current_node.next
#             else:
#                 prev_node.next, current_node.next = current_node.next, None


2022/6/8  author:WH
双链表
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self._head, self._tail = Node(0), Node(0)
        self._head.next, self._tail.prev = self._tail, self._head
        self._count = 0

    def _get_node(self, index):
        # 当index小于_count//2时，使用_head查找更快，反之_tail更快
        if index >= self._count // 2:
            # 使用prev往前查找
            node = self._tail
            for _ in range(self._count - index):
                node = node.prev
        else:
            # 使用next往后找
            node = self._head
            for _ in range(index + 1):
                node = node.next
        return node

    def get(self, index):
        if 0 <= index < self._count:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        self._update(self._head, self._head.next, val)

    def addAtTail(self, val):
        self._update(self._tail.prev, self._tail, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._update(node.prev, node, val)

    def _update(self, prev, next, val):
        self._count += 1
        node = Node(val)
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def deleteAtIndex(self, index):
        if 0 <= index < self._count:
            node = self._get_node(index)
            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev

# 2022/09/21 author:WH
# 设计链表
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class MyLinkedList:
#     def __init__(self):
#         # 添加虚拟头节点
#         self._head = ListNode()
#         # 链表节点数
#         self.count = 0

#     def get(self, index):
#         if 0 <= index < self.count:
#             node = self._head
#             for _ in range(index+1):
#                 node = node.next
#             return node.val
#         else:
#             return -1

#     def addAtHead(self, val):
#         self.addAtIndex(0, val)


#     def addAtTail(self, val):
#         self.addAtIndex(self.count, val)
        

#     def addAtIndex(self, index, val):
#         # 要对index进行判断，以免超出了链表的范围
#         if index < 0:
#             index = 0
#         elif index > self.count:
#             return

#         # 符合条件插入元素时，链表长需加一
#         self.count += 1
#         pre = self._head
#         for _ in range(index):
#             pre = pre.next
#         pre.next = ListNode(val, pre.next)


#     def deleteAtIndex(self, index):
#         if 0 > index or index >= self.count:
#             return
#         pre = self._head
#         for _ in range(index):
#             pre = pre.next
#         pre.next = pre.next.next
#         self.count -= 1
        
