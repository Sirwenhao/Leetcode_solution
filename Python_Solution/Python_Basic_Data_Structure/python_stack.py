"""
    1、使用python实现基本数据结构——栈，源自《Python数据结构与算法分析》
    2、示例：匹配括号，对应leetcode_0020——有效的括号
"""

# 基本数据结构——栈
# 用列表实现栈，列表尾为栈顶


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# # 使用列表尾作为栈顶，此种情况下无法直接使用pop和append方法
# # 必须要用pop方法和insert方法显示的访问下标为0的元素

# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         return self.items.insert(0, item)  # 使用insert方法指定位置插入元素

#     def pop(self):
#         return self.items.pop(0) # 指定要pop的元素的索引

#     def peek(self):
#         return self.items[0]

#     def size(self):
#         return len(self.items)

# 调用，实例化

# s = Stack()

# print(s.isEmpty())
# print(s.push(4))
# print(s.push('dog'))
# print(s.pop())
# print(s.peek())
# print(s.size())


# # 栈应用1：匹配括号，只有一种括号

# def parChecker(str):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(str) and balanced:
#         symbol = str[index]
#         if symbol == '(':
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False # balanced用于控制
#             else:
#                 s.pop()

#         index += 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False

# # 测试

# str = '((()))'
# result = parChecker(str)
# print(result)


# 栈应用2：匹配括号，三种括号{[()]}

def parChecker(str):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str) and balanced:
        symbol = str[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open, close):
    opens = '{[('
    closers = '}])'

    return opens.index(open) == closers.index(close)

# 测试

str = '([{}]))'
result = parChecker(str)
print(result)