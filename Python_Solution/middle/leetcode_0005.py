"""
    1、最大回文数子串
    2、涉及知识点：动态规划，需要找到状态转移方程
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
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1

    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]



# 2022/5/1 review
# 核心思想：从当前字符往左右两个方向进行拓展判断是否满足回文
# 遍历字符串进行拓展,但此处存在两种情况：中心值为单个数和中心值为双个数的情况
# 中心值是单个数比较好考虑，中心值是双个数的还需要考虑是与左边数成对还是与右边数成对
# 即对称中心是一个数或者两个数之间的位置
# class Solution:
#     def longestPalindrome(self, s):
#     #     # 首先定义回文字符串判断函数
#     #     def isPilndrome(s):
#     #         if s == s[::-1]:
#     #             return True
#     #         else:
#     #             return False
# # 核心函数在此部分：直接对比给进来的左右位置数字是否相等，然后改变位置即可实现两种情况的考虑
#         def extend(left, right, s):
#             while left>=0 and right<len(s) and s[left]==s[right]:
#                 left -= 1
#                 right += 1
#             return s[left+1:right] # 左边界是不满足条件才到此位置，因此需要+1
#         n = len(s)
#         if n==0:
#             return ""
#         res = s[0]

#         for left in range(n-1):
#             p1 = extend(left, left, s)
#             p2 = extend(left, left+1, s)
#             if max(len(p1), len(p2)) > len(res):
#                 res = p1 if len(p1)>len(p2) else p2
#         return res


# python中双等号"=="返回值为布尔类型
# 动态规划解法
# 设dp[i][j]表示字符串s[i...j]是否为回文串
# 当j-i<2,即字符串的长度为2时，只要s[i]==s[j],dp[i][j]就为True
# 当j-i>=2时，dp[i][j]= dp[i+1][j-1] && s[i] == s[j]才可以
# class Solution:
#     def longestPalindrome(self, s):
#         n = len(s)
#         dp = [[False]*n for _ in range(n)]
#         # print('dp:', dp)
#         start, mx = 0, 1
#         for j in range(n):
#             for i in range(j+1):
#                 if j-i < 2:
#                     dp[i][j] = s[i] == s[j]
#                 else:
#                     dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
#                 if dp[i][j] and mx < j-i+1:
#                     start, mx = i, j-i+1
#         return s[start:start + mx]

# 2022/9/3  author:github
# 动态规划解法，重点在于找到状态转移方程
# 当j-i<2时,如果s[i]==s[j], dp[i][j]=True
# 当j-i>=2时,dp[i][j]=dp[i+1][j-1] && s[i]==s[j] 才为True

# class Solution:
#     def longestPalindrome(self, s):
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         # 变量maxLen用于记录回文串的最大长度
#         start, maxLen = 0, 1
#         for j in range(n):
#             for i in range(j+1):
#                 if j - i < 2:
#                     # s[i] == s[j]是个判断语句
#                     dp[i][j] = s[i] == s[j]
#                 else:
#                     dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
#                 if dp[i][j] and maxLen < j-i+1:
#                     maxLen = j - i + 1
#                     start = i
#         return s[start:start + maxLen]


# # 2022/11/12 author:WH
# class Solution:
#     def expand(self, s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left+1, right-1


#     def longestPalindrome(self, s):
#         start, end = 0, 0
#         for i in range(len(s)):
#             left1, right1 = self.expand(s, i, i)
#             left2, right2 = self.expand(s, i, i+1)
#             if right1 - left1 > end - start:
#                 start, end = left1, right1
#             if right2 - left2 > end - start:
#                 start, end = right2, left2
#         return s[start:end+1]

# 2022/11/13  author:WH
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    
    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i+1)
            if right1-left1 > end-start:
                end, start = right1, left1
            if right2-left2 > end-start:
                right2, left2 = end, start
        return s[start:end+1]




if __name__ == "__main__":
    s = 'abcbabb'
    result = Solution().longestPalindrome(s)
    print(result)

if __name__ == '__main__':
    s = "babad"
    result = Solution().longestPalindrome(s)
    print(result)


# # 判断回文字符串
# def isPilndrome(s):
#     print(s[::1])
#     if s[::1] == s[::-1]:
#         return True
#     else:
#         return False
# s = 'abcba'
# result = isPilndrome(s)
# print(result)