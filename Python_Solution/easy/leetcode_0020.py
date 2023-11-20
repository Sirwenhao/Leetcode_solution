# """
#     1、20题有效的括号
#     2、这个一开始不会，后面也不是很明白
#     3、python中()表示创建元组，[]表示创建列表，{}表示创建字典
# """



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

# def isValid(s):
#     stack = []
#     dic = {
#         '{':'}',
#         '[':']',
#         '(':')',
#     }
#     for i in s:
#         if i in dic:
#             stack.append(dic[i])
#         else:
#             if len(stack) != 0:
#                 top_element = stack.pop()
#                 if i == top_element:
#                     continue
#                 else:
#                     return False
#             else:
#                 return False
#     return len(stack) == 0


# # 2022/6/6 author:WH
# class Solution:
#     def isValid(self, s):
#         dict = {
#             "{":"}",
#             "[":"]",
#             "(":")",
#         }
#         strList = []
#         for i in s:
#             if i in dict:
#                 strList.append(dict[i])
#             else:
#                 if len(strList) != 0:
#                     top_element = strList.pop()
#                     if i != top_element:
#                         return False
#                     else:
#                         continue
#                 else:
#                     return False
#         return len(strList) == 0

# 2022/7/8  author:WH
# class Solution:
#     def isValid(self, s):
#         dict = {
#             "{": "}",
#             "(": ")",
#             "[": "]",
#         }
#         stack = []
#         for i in s:
#             if i in dict:
#                 stack.append(i)
#             else:
#                 if len(stack) != 0:
#                     if dict[stack.pop()] != i:
#                         return False
#                     else:
#                         continue
#                 else:
#                     return False
#         return len(stack) == 0

# 2022/7/16  author:WH
# class Solution:
#     def isValid(self, s):
#         dict = {
#             "(": ")",
#             "{": "}",
#             "[": "]",
#         }
#         stack = []
#         if len(s) == 0:
#             return False
#         for i in s:
#             if i in dict:
#                 stack.append(i)
#             else:
#                 if i != dict[stack.pop()]:
#                     return False
#                 else:
#                     continue

#         return len(stack) == 0

# 2022/10/05  author:WH
# class Solution:
#     def isValid(self, s):
#         if len(s) % 2 != 0:
#             return False
#         l = []
#         dic = {
#             '(':')',
#             '[':']',
#             '{':'}'}
#         for i in s:
#             if i in dic:
#                 l.append(i)
#             else:
#                 if i != dic[l.pop()]:
#                     return False
#         return len(l) == 0


# 23/11/16 author:WH
# 出错

class Solution:
    def isValid(self, s):
        ans = []
        brace_dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in brace_dic:
                ans.append(c)   
            else:
                if len(ans) != 0:
                    if c != brace_dic[ans.pop()]:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(ans) == 0

if __name__ == "__main__":
    s = "{[()]}"
    # s = "[["
    s = "){"
    s = "]"
    result = Solution().isValid(s)
    print(result)