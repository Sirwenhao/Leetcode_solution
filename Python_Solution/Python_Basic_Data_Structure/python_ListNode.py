"""
    1、python实现基本数据结构——链表
"""

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class LinkedList:
#     def __init__(self):
#         self.size = 0
#         self.head = None
#         self.last = None
    
#     def get(self, index):
#         if index < 0 or index >= self.size:
#             raise Exception('超出链表节点范围!')
#         p = self.head
#         for i in range(index):
#             p = p.next
#         return p

#     def insert(self, data, index):
#         if index < 0 or index > self.size:
#             raise Exception('超出链表节点范围!')
#         node = Node(data)
#         if self.size == 0:
#             # 空链表
#             self.head = node
#             self.last = node
#         elif index == 0:
#             # 插入头部
#             node.index = self.head
#             self.node = node
#         elif self.size == index:
#             # 插入尾部
#             self.last.next = node
#             self.last = node;
#         else:
#             # 插入中间
#             prev_node = self.get(index-1)
#             node.next = prev_node.next
#             prev_node.next = node
#         self.size += 1

#     def remove(self, index):
#         if index < 0 or index >= self.size:
#             raise Exception('超出链表节点范围')
#         # 暂存被删除的节点，用于返回
#         if index == 0:
#             # 删除头节点
#             remove_node = self.head
#             self.head = self.head.next
#         elif index == self.size - 1:
#             # 删除尾节点
#             prev_node = self.get(index-1)
#             remove_node = prev_node.next
#             prev_node.next = None
#             self.last = prev_node
#         else:
#             # 删除中间节点
#             prev_node = self.get(index-1)
#             next_node = prev_node.next.next
#             remove_node = prev_node.next
#             prev_node.next = next_node
#             self.size -= 1
#             return remove_node

#         def output(self):
#             p = self.head
#             while p is not None:
#                 print(p.data)
#                 p = p.next

# # 无序链表实现

# 节点类

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 指向空值，初始化节点next
    
    def getData(self):
        return self.data # 返回当前数据

    def getNext(self):
        return self.next # 返回当前指向下一个节点的引用

    def setData(self, newData):
        self.data = newData # 添加新的数据，需要传入参数newData

    def setNext(self, newNext):
        self.next = newNext # 添加新的指向引用，需要传入参数newNext

# # 无序列表类

# class UnorderedList():
#     def __init__(self):
#         self.head = None # 无序列表的头结点不指向任何节点

#     def isEmpty(self):
#         return self.head == None  # 检查无序列表是否为空，返回值为bool类型

#     def add(self, item):  # 这个操作是向表头添加元素
#         temp = Node(item) # 通过节点类Node()的构造方法添加新的元素temp
#         temp.setNext(self.head) # 通过节点类的方法setNode()传入新的指向引用，将其指向链表的头部
#         self.head = temp # 修改列表的头节点，使其指向新创建的节点

#     def length(self):
#         current = self.head # 定义中间变量current，列表的头节点赋值给该变量，标记当前位置
#         count = 0
#         while current != None: # 列表遍历
#             count += 1 # 每指向一个新的非空节点，累加
#             current = current.getNext() # 更新节点，返回当前指向下一个节点的引用
#         return count

#     def search(self, item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.getData() == item: # 中间变量的值等于所要寻找的值，更新found状态
#                 found = True
#             else:
#                 current = current.getNext() # 如果没找到，更新当前节点到下一节点
#         return found

#     def remove(self, item): # 从列表中删除元素item，需要传入参数item
#         current = self.head
#         previous = None  # 定义外部引用previous指向current上一次访问的节点
#         found = False
#         while not found:
#             if current.getData() == item:
#                 found = True
#             else:
#                 previous = current # 将列表的头节点赋值给变量previous
#                 current = current.getNext() # 返回当前指向下一个节点的引用并复制给current

#         if previous == None: # 如果要删除的元素怒是列表中的头节点时，需要改变列表的头结点
#             self.head = current.getNext()
#         else:
#             previous.setNext(current.getNext())

#     def append(self, item): # 向链表的尾端append元素
#         temp = Node(item)
#         current = self.head
#         if self.isEmpty():
#             self.head = temp
#         else:
#             while current.next != None:
#                 current = current.next
#             current.next = temp


#     def insert(self, pos, item):
#         temp = Node(item)
#         current = self.head
#         if pos <= 0:  # 小于0的情况插入的表头
#             # # 可以重写
#             # temp.setNext(current)
#             # self.head = temp

#             # 也可以直接用写好的接口
#             self.add(item)

#         elif pos >= self.length(): # 大于表长的情况插入到尾端
#             self.append(item)
#         else:
#             cnt = 1
#             while cnt < pos:
#                 current = current.next
#                 cnt += 1
#             next = current.next # next指向pos位置下一位的引用
#             current.next = temp # 把下一位置的引用用新加入的节点替换并接到当前的引用之后
#             temp.next = next # 在当前的引用之后在加入原来剩下的节点

        
#     def pop(self):
#         if self.isEmpty():
#             print("SingleLinkList is empty")
#         else:
#             current = self.head
#             cnt = 1
#             while cnt < self.length():
#                 current = current.getNext()
#                 cnt += 1
#             self.remove(current.getData())
#             return current.getData()


#     def printLinklist(self):
#         l = self.length()
#         ls = []
#         temp = self.head
#         while l > 0:
#             ls.append(temp.getData())
#             temp = temp.getNext()
#             l -= 1
#         print(ls)

# if __name__ == '__main__':
#     LinkList = UnorderedList() # 实例化链表对象
#     # 判断链表是否为空
#     print(LinkList.isEmpty())
#     # 链表插入元素
#     LinkList.add(1)
#     LinkList.add(2)
#     LinkList.add(3)
#     LinkList.add(4)
#     # 打印链表
#     LinkList.printLinklist()
#     # 查看链表长度
#     print(LinkList.length())
#     # 在链表中搜索元素
#     print(LinkList.search(3))
#     # 移除链表中的指定元素
#     LinkList.remove(3)
#     LinkList.printLinklist()
#     # 在链表尾部append元素
#     LinkList.append(7)
#     LinkList.append(8)
#     LinkList.append(9)
#     LinkList.printLinklist()
#     # 在指定位置处插入元素
#     LinkList.insert(4, 10)
#     LinkList.printLinklist()
#     # pop元素
#     print(LinkList.pop())
#     LinkList.printLinklist()

# python实现有序列表

class OrderedList:
    def __init__(self):
        self.head = None
    
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.next
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)