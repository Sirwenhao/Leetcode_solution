"""
    1、字符最短距离
"""

# 解法一：创建一个列表存储所有字符与c相等的索引
# 遍历给定的列表，把索引值与上述列表做差取绝对值中的最小值存入列表作为最终的返回值
# 时间复杂度O(N),空间复杂度O(N)
# def shortestToChar(s, c):
#     list1 = []
#     for i in range(len(s)):
#         if s[i]==c:
#             list1.append(i)
#     list3 = []
#     for j in range(len(s)):
#         list2 = [j-i for i in list1]
#         list2 = [abs(i) for i in list2]
#         list3.append(min(list2))     

#     return list3


# # 解法二：力扣加加
# 时间复杂度：O(N^2),空间复杂度：O(1)
# def shortestToChar(S, C):
#     ans = []
#     for i in range(len(S)):
#         # 从i向左向右拓展
#         l = r = i
#         # 向左找到第一个C
#         while l > -1:
#             if S[l] == C: break
#             l -= 1
#         # 向右找到第一个C
#         while r < len(S):
#             if S[r] == C: break
#             r += 1
#         if l == -1: l = -10000
#         if r == len(S): r = 10000
#         # 选较近的即可
#         ans.append(min(r - i, i- l))
#     return ans

# 解法三：力扣加加（与官解基本一样）
def shortestToChar(s, c):
    pre = -10000
    ans = []

    for i in range(len(s)):
        if s[i] == c: pre = i
        ans.append(i - pre)
    print(ans)
    pre = 20000
    for i in range(len(s)-1, -1, -1):
        if s[i] == c: pre = i
        ans[i] = min(ans[i], pre - i)
    return ans 

# # 官解
# def shortestToChar(s, c):
#     prev = float('-inf')
#     ans = []
#     for i, x in enumerate(s):
#         if x==c: prev = i
#         ans.append(i - prev)
#         print(ans)

#     prev = float('inf')
#     for i in range(len(s)-1, -1, -1):
#         if s[i] == c: prev = i
#         ans[i] = min(ans[i], prev - i)
#     return ans

# 2022/4/19 出现在力扣每日一题中，重新从头写一遍
# 重新写的想法：把所有的e的index存到一个列表lst1中，遍历S的index与lst1中的元素做差取最小值
# def shortestToChar(S, C):
#     lst1 = []
#     for i in range(len(S)):
#         if S[i] == C:
#             lst1.append(i)
#     print(lst1)
#     lst3 = []
#     for j in range(len(S)):
#         lst2 = [j - k for k in lst1]
#         lst2 = [abs(i) for i in lst2]
#         lst3.append(min(lst2))
#     return lst3


s = "loveleetcode"
c = "e"
result = shortestToChar(s, c)
print(result)

# list1 = []
# for i in range(len(s)):
#     if s[i]==c:
#         list1.append(i)
# print(list1)

# list1 = [3,5,6,11]
# # for i in range(len(list1)):
# list2 = [5-list1[i] for i in range(len(list1))]
# list2 = [abs(i) for i in list2]
# print(list2)