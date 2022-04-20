"""
    1、最大回文数子串
    2、设计知识点：动态规划，需要找到状态转移方程
"""

# 力扣加加解法：时间复杂度：O(N^2),空间复杂度：O(N^2),对应于力扣官解方法2中心拓展法
# def longestPalindrome(s):
#     n = len(s)
#     if n == 0:
#         return ""
#     res = s[0]
#     def extend(i, j ,s):
#         while(i >= 0 and j < len(s) and s[i] == s[j]):
#             i -= 1
#             j += 1
#         return s[i+1:j]

#     for i in range(n-1):
#         e1 = extend(i, i, s)
#         e2 = extend(i, i+1, s)
#         if max(len(e1), len(e2)) > len(res):
#             res = e1 if len(e1) > len(e2) else e2
#     return res

# 力扣官解
# 时间复杂度O(N^2),空间复杂度O(1)

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left+1, right-1

def longestPalindrome(s):
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        print('left1:', left1)
        print('right1:', right1)
        left2, right2 = expandAroundCenter(s, i, i+1)
        print('left2:', left2)
        print('right2:', right2)
        if right1-left1 > end-start:
            start, end = left1, right1
        if right2-left2 > end-start:
            start, end = left2, right2
    return s[start: end+1]


s = "babad"
result = longestPalindrome(s)
print(result)