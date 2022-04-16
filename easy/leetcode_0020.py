# """
#     1、20题有效的括号
#     2、这个一开始不会，后面也不是很明白
#     3、python中()表示创建元组，[]表示创建列表，{}表示创建字典
# """


# def isValid(s):
#     stack = []
#     map = {
#         "{": "}",
#         "[": "]",
#         "(": ")",
#     }
#     for x in s:
#         print('x1:', x)
#         if x in map:
#             stack.append(map[x])  #此处map[x]表示键对应的值
#             print('stack:', stack)
#         else:
#             if len(stack) != 0:
#                 top_element = stack.pop()
#                 if x != top_element:
#                     return False
#                 else:
#                     continue
#             else:
#                 return False
#     return len(stack) == 0

# # def isValid(s: str) -> bool:
# #     if len(s) % 2 == 1:
# #         return False
# #     dic = {
# #         "}": "{",
# #         ")": "(",
# #         "]": "[",
# #     }
# #
# #     stack = list()
# #     for i in s:
# #         if i in dic:
# #             if not stack or stack[-1] != dic[i]:
# #                 return False
# #             stack.pop()
# #         else:
# #             stack.append(i)
# #     return not stack
# #
# #
# # s = "({[]})"


# 2022/3/26 复习

# def isValid(s):
#     stack = []  # 创建空列表做栈
#     dic = {
#         '{':'}',
#         '[':']',
#         '(':')',
#     }
#     for i in s:
#         if i in dic:
#             stack.push(dic.values(i)) # 遍历字符串s如果当前元素即在s中又在字典dic的key中（key只有三种情况，
#                                       # 三种左括号），将对应的值压入栈中
#         else:
#             top_elements = stack.pop() # 如果不在键中，则判断当前的元素与栈顶元素是否相同（原理：先进后出）
#             if i == top_elements:
#                 return True
    

def isValid(s):
    stack = []
    dic = {
        '{':'}',
        '[':']',
        '(':')',
    }
    for i in s:
        if i in dic:
            stack.append(dic[i])
        else:
            if len(stack) != 0:
                top_element = stack.pop()
                if i == top_element:
                    continue
                else:
                    return False
            else:
                return False
    return len(stack) == 0


result = isValid(s)
print(result)
