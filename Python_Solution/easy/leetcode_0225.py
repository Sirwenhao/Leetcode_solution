"""
    1、使用队列实现栈
    2、包含两个版本：使用一个队列实现和使用两个队列实现
    3、使用两个队列的版本原理类似于汉诺塔
"""
# # 2022/7/7  author:代码随想录
# """
#     Python中的queue没有类似于peek的功能，也无法用索引访问
#     具有popleft()和append()的功能
# """
# class MyStack:
#     def __init__(self):
#         self.queue_in = deque()
#         self.queue_out = deque()

#     def push(self, x):
#         # 直接append
#         self.queue_in.append()

#     def pop(self):
#         """
#         pop的步骤（原理类似于汉诺塔）
#         1、首先确认非空
#         2、队列特点FIFO，只有在pop()的时候使用queue_out
#         3、先把queue_in中的所有元素（除了最后一个）依次放入到queue_out中
#         4、交换in和out，此时out中只有一个元素，pop即可
#         5、把out中的pop出来即可，即原队列中的最后一个元素
#         """
#         if self.empty():
#             return None

#         for i in range(len(self.queue_in)-1):
#             self.queue_out.append(self.queue_in.popleft())
#         # 交换in和out
#         self.queue_in, self.queue_out = self.queue_out, self.queue_in
#         return self.queue_out.popleft()
        
#     def top(self):
#         """
#         1、首先确认不空
#         2、仅in会存放数据，返回第一个即可
#         """
#         if self.empty():
#             return None
#         return self.queue_in[-1]

#     def empty(self):
#         # 只有in存放数据，只要判断in是否为空即可
#         return len(self.queue_in) == 0

# 2022/7/7 author:WH  单队列版本
# class MyStack:
#     def __init__(self):
#         self.queue = deque()

#     def push(self, x):
#         self.queue.append(x)

#     def pop(self):
#         if self.empty():
#             return None
#         for i in range(len(self.queue)-1):
#             self.queue.append(self.queue.popleft())
#         return self.queue.popleft()
    
#     def top(self):
#         if self.empty():
#             return None
#         return self.queue[-1]

#     def empty(self):
#         return len(self.queue) == 0
#         # 或者使用
#         # return not self.queue 

# 2022/7/15  author:WH
# class MyStack:
#     def __init__(self):
#         self.que = deque()

#     def push(self, x):
#         self.que.append(x)

#     def pop(self):
#         # 先判断是否为空，不为空弹出最后一个进入deque的元素
#         if self.empty():
#             return None
#         # 这一步牛，通过最内层的self.que.popleft()先把最左边元素移除掉一个
#         # 然后在此基础上再把这个元素给添加到最右端，一直循环到原最右侧元素迭换至最左端
#         for i in range(len(self.que)-1):
#             self.que.append(self.que.popleft())
#         return self.que.popleft()

#     def top(self):
#         if self.empty():
#             return None
#         else:
#             return self.que[-1]

#     def empty(self):
#         return len(self.que) == 0

# 2022/7/16  author:WH
# from collections import deque
# class MyStack:
#     def __init__(self):
#         self.que_in = deque()
#         self.que_out = deque()

#     def push(self, x):
#         self.que_in.append(x)

#     def pop(self):
#         if self.empty():
#             return None
#         for i in range(len(self.que_in)-1):
#             self.que_out.append(self.que_in.popleft())
#         self.que_in, self.que_out = self.que_out, self.que_in
#         return self.que_out.popleft()

#     def top(self):
#         if self.empty():
#             return None    
#         return self.que_in[-1]

#     def empty(self):
#         return len(self.que_in) == 0

# 2022/10/04  author:WH
# 使用两个队列实现栈的操作
# Python双端队列的pop操作默认弹出右侧元素，popleft才是弹出左侧元素
from collections import deque
class MyStack:
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        self.queue_in.append(x)

    def pop(self):
        if self.empty():
            return None
        # 此处使用self.queue_out的作用就只是为了输出第一个进栈的元素
        # 把第一个进栈的元素与其后续的元素分开，
        if self.queue_in:
            for i in range(len(self.queue_in)-1):
                self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self):
        return self.queue_in[-1]

    def empty(self):
        return not self.queue_in

# 使用一个deque的写法
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.empty():
            return None
        return self.queue.popleft()

    def top(self):
        return self.queue[-1]

    def empty(self):
        return not self.queue