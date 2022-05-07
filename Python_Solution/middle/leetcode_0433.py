"""
    1、深度优先搜索和广度优先搜索相关
    2、注意：每次基因序列的变化必须为有效变化，基因库中所给的都属于有效变化
"""

# 当前所给的start默认是有效基因,start每次变化之后都必须是有效变化，即为bank的子集但不一定是最终解
# 返回的条件是当前变化所需要变动的字符最少

# # 此解法是错误的，忽略了一个重要问题，应该是每次变换只能变换一个字符
# from cmath import inf
# class Solution:
#     def minMutation(self, start, end, bank):
#         if not bank:
#             return -1

#         # 写个函数传入两个等长字符串判断对应位置元素是否不同
#         def isNotEqual(str1, str2):
#             val = 0
#             for i in range(min(len(str1), len(str2))):
#                 if str1[i] != str2[i]:
#                     val += 1
#             return val

#         # 先创建一个字典，存储bank中所有字符变为end所需要的字符变化次数
#         dic1 = {}
#         for i in bank:
#             val1 = isNotEqual(start, i)
#             dic1[i] = val1
#         print('dic1:', dic1)
#         # 再创建一个字典存储bank中所有元素变换为end是所需要的步数，两个步数之和最小值即为所求
#         dic2 = {}
#         for j in bank:
#             val2 = isNotEqual(end, j)
#             dic2[j] = val2
#         print('dic2:', dic2)
#         min_v = inf
#         for m,n in zip(dic1, dic2):
#             print('int(dic1[m]):', int(dic1[m]))
#             print('int(dic2[n]):', int(dic2[n]))
#             min_v = min(min_v, (int(dic1[m]) + int(dic2[n])))
#         return min_v

# 力扣官解
from collections import deque

class Solution:
    def minMutation(self, start, end, bank):
        if start == end:
            return 0

        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i+1:]
                        if nxt in bank:
                            if nxt == end:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step+1))
        return -1



if __name__ == '__main__':
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    result = Solution().minMutation(start, end, bank)
    print(result)

# 判断两个等长字符串对应位置元素是否相同
# s1 = "AACCGGTT"
# s2 = "ABCCGGAA"
# val = 0
# print('s1[::1]:', s1[::1])
# if s1[::1] != s2[::1]:
#     val += 1
# def isNotEqual(str1, str2):
#     val = 0
#     for i in range(min(len(str1), len(str2))):
#         if str1[i] != str2[i]:
#             val += 1
#     return val

# result = isNotEqual(s1, s2)
# print('result:', result)