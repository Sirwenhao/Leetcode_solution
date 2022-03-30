"""
    1、用栈实现队列，
    2、复习栈和队列两种数据结构
"""

class MyQueue:

    def __init__(self) -> None:
        self.stack = []
        self.help_stack = []

    def push(self, x):
        """
        push element to back of queue
        """
        while self.stack:
            self.help_stack.append(self.stack.pop())
        self.help_stack.append(x)
        while self.help_stack:
            self.stack.append(self.help_stack.pop())


    def pop(self):
        """
        remove the element from in front of queue and returns thar element
        """
        return self.stack.pop()

    def peek(self):
        """
        get the front element
        """
        return self.stack[-1]

    def empty():
        """
        returns whether the queue is empty
        """
        return not bool(self.stack)