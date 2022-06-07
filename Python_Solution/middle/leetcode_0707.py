"""
    1、设计链表
    2、链表专题系列
"""
# 2022/6/7  author:WH
# 单链表
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self._head = Node(0) # 虚拟头部节点
        self._count = 0 # 添加的节点数

    def get(self, index):
        if 0 <= index <= self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        self.addAtHead(0, val)

    def addAtTail(self, val):
        self.addAtTail(self._count, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return

        # 链表长度+1
        self._count += 1
        add_node = Node(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node

    def deleteAtIndex(self, index):
        if 0 <= index < self._count:
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None
