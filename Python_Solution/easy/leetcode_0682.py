'''
    1、通过给定操作符记录分数
    2、不用考虑前两个字符是否为数字的情况默认了只有数字、+、C、D这四种字符
    3、想法是创建空栈，遇到数字则入栈，遇到不同情况则执行不同的操作，核心还是栈的先进后出
'''


def calPoints(ops):
    stack = []
    for i in ops:
        if i == 'C':
            stack.pop()
        elif i == 'D':
            stack.append(stack[-1]*2)
        elif i == '+':
            stack.append(stack[-1]+stack[-2])
        else:
            stack.append(int(i))
    return sum(stack)

list = ["5","2","C","D","+"]
result = calPoints(list)
print(result)