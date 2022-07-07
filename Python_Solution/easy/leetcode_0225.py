"""
    1、使用队列实现栈
    2、包含两个版本：使用一个队列实现和使用两个队列实现
    3、使用两个队列的版本原理类似于汉诺塔
"""
from collections import deque
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
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.empty():
            return None
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
    
    def top(self):
        if self.empty():
            return None
        return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0
        # 或者使用
        # return not self.queue 