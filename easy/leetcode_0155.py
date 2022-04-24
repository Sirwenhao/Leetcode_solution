"""
    1、题目一开始没有看明白
    2、以一下输入为例：
        输入：
            ["MinStack","push","push","push","getMin","pop","top","getMin"]
            [[],[-2],[0],[-3],[],[],[],[]]

            输出：
            [null,null,null,null,-3,null,0,-2]
    3、上述的前两行一个代表对目前对象执行的操作，一个代表目前的对象
"""

class MinStack:
    def __init__(self):
        """initialize data structure here"""
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]



# 力扣官解
# 思路：当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前值进行比较，取二者中的最小值放入辅助栈
# 当一个元素要出栈时，把辅助栈元素也一并弹出
# 在任意时刻，栈内元素的最小值就存储在辅助栈的栈顶

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x):
        self.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

