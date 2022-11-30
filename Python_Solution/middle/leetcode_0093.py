"""
    1、复原IP地址
    2、属于回溯中分割字符串这一系列的问题
"""
# 成为IP地址的条件
# 数字之间使用.进行分隔
# 每一个.分隔开的数字的范围为0~255
# .分隔开的数字不能是01这种前面是0后面是非0数字的情况

# # 代码随想录的方法
# class Solution:
#     def __init__(self) -> None:
#         self.ans = []

#     def restoreIPAddress(self, s):
#         self.ans.clear()
#         if len(s) > 12: return []
#         self.backtracking(s, 0, 0)
#         return self.ans

#     def backtracking(self, s, start_index, pointNum):
#         # 递归终止的条件是在原序列中加入了3个.，因此终止递归时current的长度应该正好是字符串s长度+3
#         if pointNum == 3:
#             # 判断加入.之后对应的self.current是否满足上述的几个要求
#             if (self.isValid(s, start_index, len(s)-1)):
#                 self.ans.append(s[:])
#             return
        
#         # 定义单层递归逻辑
#         for i in range(start_index, len(s)):
#             if self.isValid(s, start_index, i):
#                 s = s[:i+1] + '.' + s[i+1:]
#                 self.backtracking(s, i+2, pointNum+1)
#                 # 加入.之后再回溯的话，起始位置就需要重新考虑了
#                 s = s[:i+1] + s[i+2:]
#             else:
#                 break
#     # 这种写法是比较明智的，多传几个参数就可以使判断的过程清晰明了  
#     def isValid(self, s, start, end):
#         if start > end: return False
#         # 如果数字是0开头不合法
#         if s[start] == '0' and start != end:
#             return False
#         if not 0 <= int(s[start:end+1]) <= 255:
#             return False
#         return True

# # 2022/5/23 author:WH
# # 回溯内核部分的字符串切割以及判断还是没有搞清楚，不清晰
# # 参照代码随想录再次进行修改，并添加注释
# class Solution:
#     def __init__(self):
#         self.ans = []
#         # 切割字符串问题可以不用创建此全局变量
#         # self.current = ""

#     def restoreIPAddress(self, s):
#         self.ans.clear()
#         self.backtracking(s, 0, 0)
#         return self.ans

#     def backtracking(self, s, start_index, dot_Num):
#         # 这个递归终止的条件应该就是原字符串中刚好加入了三个分隔符号.
#         if dot_Num == 3:
#             # 判断第四段字符串是否合法，如果合法就放进结果集中
#             if self.isValid(s, start_index, len(s)-1):
#                 self.ans.append(s[:])
#             return

#         # 定义单层循环
#         for i in range(start_index, len(s)):
#             print('s[start_index:i+1:]', s[start_index:i+1])
#             # 如果满足有效条件，则在其后面加.
#             # 这块判断的对象不是self.current而是所切割出来的子串
#             # 如果字串有效则在其后添加.然后再添加到self.current中
#             if self.isValid(s, start_index, i):
#                 s = s[:i+1] + '.' + s[i+1:]
#                 self.backtracking(s, i+2, dot_Num+1)
#                 s = s[:i+1] + s[i+2:] # 回溯
#             else:
#                 break

#     def isValid(self, s, start, end):
#         # 这个if判断没有搞明白
#         if start > end:
#             return False
#         # 判断num是否为0开头的非零数字
#         if s[start] == 0 and start != end:
#             return False
#         if not 0 <= int(s[start:end+1]) <= 255:
#             return False
#         return True

# # 2022/11/28  author:WH
# # 参考代码随想录答案，核心点在于分割字符串和回溯终止的判断条件
# class Solution:
#     def __init__(self):
#         self.ans = []

#     def restoreIPAddress(self, s):
#         self.ans.clear()
#         if len(s) > 12:
#             return []
#         self.backtracking(s, 0, 0)
#         return self.ans

#     def backtracking(self, s, start_index, dotNum):
#         # 此处写错，递归终止的条件应该是在原字符串中顺利加入三个.分隔
#         # if self.isValid(start_index, end, s):
#         #     self.ans.append(s[:] + '.')  # 错误，此处没有加入'.'的操作
#         #     return
#         if dotNum == 3:
#             # 等于3时还需判断最后剩余的部分是否合法
#             if self.isValid(s, start_index, len(s)-1):
#                 self.ans.append(s[:])
#             return

#         for i in range(start_index, len(s)):
#             # [start_index, i]就是被截取的子串
#             if self.isValid(s, start_index, i):
#                 s = s[:i+1] + '.' + s[i+1:]
#                 # 此处的i+2是因为前段加入了.所以后延
#                 self.backtracking(s, i+2, dotNum+1)
#                 # 回溯是把加入的.去掉
#                 s = s[:i+1] + s[i+2:]
#             else:
#                 break
        

#     def isValid(self, s, start, end):
#         if start > end:
#             return False
#         if s[start] == '0' and start != end:
#             return False
#         if not 0 <= int(s[start:end+1]) <= 255:
#             return False
#         return True

# # 2022/11/29 author:WH
# # 重写
# class Solution:
#     def __init__(self):
#         self.ans = []

#     def restoreIPAddress(self, s):
#         self.ans.clear()
#         self.backtracking(s, 0, 0)
#         return self.ans

#     def backtracking(self, s, start_index, dotNum):
#         if dotNum == 3:
#             if self.isValid(s, start_index, len(s)-1):
#                 self.ans.append(s[:])
#             return

#         for i in range(start_index, len(s)):
#             if self.isValid(s, start_index, i):
#                 s = s[:i+1] + '.' + s[i+1:]
#                 self.backtracking(s, i+2, dotNum+1) # i+2写成i+1
#                 s = s[:i+1] + s[i+2:]
#             else:
#                 break


#     def isValid(self, s, start, end):
#         if s[start] == '0' and start != end:
#             return False
#         if start > end:
#             return False
#         if not 0 <= int(s[start:end+1]) <= 255:
#             return False
#         return True

# 2022/11/30 author:WH
# 重写，第三遍重写依旧有错误出现，说明理解的还是不够深刻
class Solution:
    def __init__(self):
        self.ans = []

    def restoreIPAddress(self, s):
        self.ans.clear()
        self.backtracking(s, 0, 0)
        return self.ans

    def backtracking(self, s, start_index, dotNum):
        if dotNum == 3:
            if self.isValid(s, start_index, len(s)-1):
                self.ans.append(s[:]) # 此处没有加入'.'的操作
            return
        for i in range(start_index, len(s)):
            if self.isValid(s, start_index, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, dotNum+1)
                s = s[:i+1] + s[i+2:]
            else:
                break

    def isValid(self, s, start, end):
        if s[start] == '0' and start != end:
            return False
        if start > end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True


if __name__ == "__main__":
    s = "25525511135"
    result = Solution().restoreIPAddress(s)
    print(result)