"""
    1、分饼干，首先第一步排序，这个没有考虑到其实，这个要重点记一下
"""

# 解法一，有参考力扣加加
# class Solution:
#     def findContentChildren(g: list, s: list):
#         g.sort()
#         s.sort()
#         cnt = 0
#         student = biscuits = 0
#         while student < len(g) and biscuits < len(s):
#             if s[biscuits] >= g[student]:
#                 student+=1
#                 cnt += 1
#             biscuits += 1
#         return cnt

# 2022/7/29  author:WH
# 优先考虑饼干
# class Solution:
#     def findContentChildren(self, g, s):
#         g.sort()
#         s.sort()
#         res = 0
#         for i in range(len(s)):
#             if res < len(g) and s[i] >= g[res]:
#                 res += 1
#         return res

# 优先考虑胃口大小
# class Solution:
#     def findContentChildren(self, g, s):
#         g.sort()
#         s.sort()
#         start, res = len(s)-1, 0
#         for i in range(len(g)-1, -1, -1):
#             if start >= 0 and g[i] <= s[start]:
#                 start -= 1
#                 res += 1
#         return res


# 2022/8/4  author:WH
# 优先考虑饼干:胃口值小于等于饼干大小
# class Solution:
#     def findContentChildren(self, g, s):
#         ans = start = 0
#         g.sort()
#         s.sort()
#         for i in range(len(s)):
#             if s[i] >= g[start]:
#                 start += 1
#                 ans += 1
#             else:
#                 continue
#         return ans


if __name__ == "__main__":
    g = [1,4,3,5,3]
    s = [1,2,2]
    result = Solution().findContentChildren(g, s)
    print(result)
