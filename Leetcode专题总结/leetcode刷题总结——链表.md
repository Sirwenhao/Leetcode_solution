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

#### 2.2. 0707

重点题目：实现链表的基本操作

```python
# 2022/6/10  author:代码随想录
# 单链表
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
                
           
# 2022/6/11   author:代码随想录
# 双链表
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0
        
    def get_node(self, index):
        # 如果是双向链表，就存在查找效率的问题，需要考虑index和链表中间位置的相对位置
        # 如果index小于count//2，使用head查找更快，反之使用tail查找更快（核心意思是：相对于两个端点那个更近就用那个）
        if index >= self.count // 2:
            # 使用prev往前找
            node = self.tail
            for _ in range(self.count - index):
                node = node.prev
        else:
            # 使用next往后找
            node = self.head
            for _ in range(index + 1):
                node = node.next
        return node
    
    def get(self, index):
        """Get the value of the index-th node in the linked list. If the index is invalid, return -1."""
        if 0 <= index < self.count:
            node = self.get_node(index)
            return node.val
        else:
            return -1
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        """
        self.update(self.head, self.head.next, val)
        
    def addAtTail(self, val):
        self.update(self.tail.prev, self.tail, val)
        
    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self.count:
            return
        
        node = self.get_node(index)
        self.update(node.prev, node, val)
        
    def update(self, prev, next, val):
        """
        更新节点：
        :param prev：相对于更新的前一个节点
        :param next：相对于更新的后一个节点
        :param val：需要添加的节点值
        """
        # 计数累加
        self.count += 1
        node = Node(val)
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next
        
    def deleteAtIndex(self, index):
        if 0 <= index < self.count:
            node = self.get_node(index)
            self.count -= 1
            node.prev.next, node.next.prev = node.next, node.prev
            

# 2022/09/21 author:WH
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.count = 0
        
    def get(self, index):
        if index < 0 or index >= self.count:
            return -1
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val
    
    def addAtHead(self, val):
        
        
    def addAtTail(self, val):
        
        
    def addAtIndex(self, index, val):
        if index > self.count:
            return
        pre = self.cummy
        for _ in range(index):
            pre = pre.next
        pre.next = ListNode(val, pre.next)
        self.count += 1
        
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.count:
            return
        pre = self.dummy
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next
        self.count -= 1
```

#### 2.3. 0206

```python
# 2022/6/10  author:WH
# 使用双指针完成交换操作（参考代码随想录）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev = None # 参考
        cur = head # 参考
        while cur != None:
            temp = cur.next
           	cur.next = prev # 保存cur的下一个节点，因为接下来要改变cur.next
            # 更新pre，cur指针
            prev = cur
            cur = temp
        return pre
 # 递归法
class Solution:
    def reverseList(self, head):
        def reverse(pre, cur):
            if not cur:
                return pre
            
            temp = cur.next
            cur.next = pre
            return reverse(cur, temp)
    return reverse(None, head)
```

#### 2.4. 0019

- 双指针的妙用：同时设置给定相对距离的两个指针（快慢指针），当快指针指向链表尾部的时候，慢指针刚好指向要删除的地方

```python
# 2022/6/11   author:WH
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
       	self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode()
        dummy_head.next = head
        slow, fast = dummy_head, dummy_head
        for _ in range(n):
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_head.next
```

#### 2.5. 0142

难点问题，具体难点如下：

1. 如何确定是不是有环链表，考察快慢指针
2. 如何确定快慢指针相交的位置
3. 如何确定链表开始入环的第一个节点

分析：此处使用的双指针与前述方法较为不同，具体为fast指针每次移动的步长。此处fast指针每次走两步，slow指针每次走一步，因此相对于slow指针，fast指针是在一步一步靠近slow指针的且最终一定会重合。

相遇节点部分的逻辑为：当快慢指针相遇时，在相遇节点处定义一个指针index1，在头节点处定义一个指针index2，让index1和index2同事移动，每次移动一个节点，那么他们相遇的地方就是环的入口节点。具体推理过程可见代码随想录P66.

```python
# 2022/6/11  author:WH
class ListNode:
    def __init__(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
            # 下面那部分代码还不是特别明白
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                return p
         return None
```

