"""
    1、逆波兰表达式即后缀表达式
    2、三种表达式:前缀表达式、中缀表达式和后缀表达式
    补充知识点：
    1、python中的f-string，其用法为f"{表达式}",可以将表达式中的变量表示为其真正所代表的值
    2、python中的eval()函数，用来执行一个字符串表达式，并返回表达式的值。具体用法如：
    s1 = '3*7'
    s2 = 'pow(2, 3)'
    n = eval(s1)
    m = eval(s2)
    输出结果：n=21,m=6
    """
# 2022/7/9  author:WH
# class Solution:
#     def evalRPN(self, tokens):
#         # 用于遍历元素并将元素压栈
#         stack = []
#         for item in tokens:
#             if item not in {"+", "-", "*", "/"}:
#                 stack.append(item)
#             else:
#                 # 这一步没有想到再把操作之后的元素重新入栈
#                 first_num, second_num = stack.pop(), stack.pop()
#                 stack.append(int(eval(f'{second_num} {item} {first_num}')))
#         return int(stack.pop())

# 2022/7/16  author:WH
# class Solution:
#     def evalRPN(self, tokens):
#         stack = []
#         for i in range(len(tokens)):
#             if tokens[i] not in {"+", "-", "*", "/"}:
#                 stack.append(tokens[i])
#             else:
#                 f_ele, s_ele = stack.pop(), stack.pop()
#                 result = int(eval(f"{s_ele} {tokens[i]} {f_ele}"))
#                 # print(f"{s_ele} {tokens[i]} {f_ele}")
#                 stack.append(result)
#         return int(stack.pop())

# 改进版
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                f_ele, s_ele = stack.pop(), stack.pop()
                stack.append(int(eval(f"{s_ele} {item} {f_ele}")))
        return int(stack.pop())

if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    result = Solution().evalRPN(tokens)
    print(result)