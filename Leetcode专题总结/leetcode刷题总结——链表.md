## Leetcode刷题总结——链表

2022/6/10版本

### 1.相关题目编号：

- 0019删除链表的倒数第n个节点
- 0142环形链表II
- 0203移除链表元素
- 0206反转链表
- 0707设计链表

### 2.代码实现

#### 2.1. 0203

```python
# 2022/6/10  author:WH
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        # 添加虚拟头节点
        dummy_head = ListNode(0)
        cur = dummy_head
        while cur.next != None:
            if(cur.next.val == val):
                cur.next = cur.next.next # 删除cur.next节点
            else:
                cur = cur.next
        return dummy_head.next
```

#### 2.2.0707

重点题目：实现链表的基本操作

```python
# 2022/6/10  author:WH
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next    
class MyLinkedList:
    def __init__(self):
        dummy.head = ListNode(0) # 添加虚拟头节点
        self.count = 0  # 节点计数
        
    def get(self, index):
        """get the value of index-th node in the linked list. If the index is invalid, return -1"""
        if 0 <= index < self.count:
            node = self.head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1
        
    def addAtHead(self, val):
        self.addAtIndex(0, val)
        
    def addAtTail(self, val):
        self.addAtIndex(self.count, val)
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be append to the end of linked list. If index is greater than the length, the node will bot be inserted.
        """
        if index < 0:
            index = 0
        elif index > self.count:
            return
        
        # 新加入节点，总节点数+1
        self.count += 1
        add_node = LinstNode(val)
        prev_node, current_node = None, self.head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node
            
     def deleteAtIndex(self, index):
        """Delete the index-th node in the linked list, if the index is valid"""
        if 0 <= index < self.count:
            # 删除节点，总节点数-1
            self.count -= 1
            prev_node, current_node = None, self.head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, current_node.next = current_node.next, None
```

