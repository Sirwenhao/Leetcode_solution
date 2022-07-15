"""
    1、用栈实现队列，
    2、复习栈和队列两种数据结构
"""

# class MyQueue:

#     def __init__(self) -> None:
#         self.stack = []
#         self.help_stack = []

#     def push(self, x):
#         """
#         push element to back of queue
#         """
#         while self.stack:
#             self.help_stack.append(self.stack.pop())
#         self.help_stack.append(x)
#         while self.help_stack:
#             self.stack.append(self.help_stack.pop())


#     def pop(self):
#         """
#         remove the element from in front of queue and returns thar element
#         """
#         return self.stack.pop()

#     def peek(self):
#         """
#         get the front element
#         """
#         return self.stack[-1]

#     def empty():
#         """
#         returns whether the queue is empty
#         """
#         return not bool(self.stack)


# 2022/7/1  author:代码随想录
# 栈与队列专题
# 栈是先进后出，队列是先进先出。要用两个栈实现队列实现先进后出，两个栈数据互传
# class MyQueue:
#     def __init__(self):
#         # in主要负责push，out负责pop
#         self.stack_in = [] # 用于push进入元素
#         self.stack_out = [] # 用于pop出去元素

#     def push(self, x):
#         self.stack_in.append(x)

#     def pop(self):
#         # 如果stack_out为空，就不返回任何参数
#         if self.empty():
#             return None

#         # 如果stack_out不为空，就直接pop元素
#         if self.stack_out:
#             return self.stack_out.pop()
#         else: # 如果stack_out为空，就把stack_in中的元素放入到stack_out中用于输出
#             # 通过循环把stack_in中的元素完全放入到stack_in中，刚好又实现了一次先进后出
#             # 两次先进后出的叠加共同实现了先进先出
#             for i in range(len(self.stack_in)):
#                 self.stack_out.append(self.stack_in.pop())
#             return self.stack_out.pop()

#     def peek(self):
#         # 获取队头元素
#         ans = self.pop()
#         self.stack_out.append(ans)
#         return ans

#     def empty(self):
#         # 只要stack_in或者stack_out中有元素就表示不为空
#         # if self.stack_in or self.stack_out:
#         #     return False
#         return not (self.stack_in or self.stack_out)


# 2022/7/6  author:WH
# 使用两个栈实现队列，队列是双端结构，一端进入、一端输出
# 栈是单端结构，只能从一端进入然后从同一端输出，故为先进后出
# class MyQueue:
#     def __init__(self):
#         self.stack_in = []
#         self.stack_out = []

#     def push(self, x):
#         self.stack_in.append(x)

#     def pop(self):
#         # 先判断是否为空
#         if self.empty():
#             return None
#         # 如果不为空，可以直接从out中pop元素
#         if self.stack_out:
#             self.stack_out.pop()
#         else:
#             for i in range(len(self.stack_in)):
#                 self.stack_out.append(self.stack_in.pop())
#             return self.stack_out.pop()

#     def peek(self):
#         # 直接执行pop出栈的是从stack_out中输出的最外侧元素，即stack_in的最内侧元素
#         ans = self.pop()
#         # 还要重新添加回来
#         self.stack_out.append(ans)
#         return ans

#     def empty(self):
#         # 若为空，则stack_in和stack_out均为空
#         return not (self.stack_in or self.stack_out)

# 2022/7/15  author:WH
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if self.empty():
            return None

        # pop之前需要先判断是否为空
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        return (self.stack_in and self.stack_out)