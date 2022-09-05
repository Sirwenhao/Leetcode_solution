"""
    1、单调递增的数字
"""
# 2022/8/3  author:WH
class Solution:
    def monotoneIncreasingDigits(self, n):
        numStr = list(str(n))
        for i in range(len(numStr)-1, 0, -1):
            if int(numStr[i]) < int(numStr[i-1]):
                numStr[i-1] = str(int(numStr[i-1])-1)
                numStr[i:] = '9' * (len(numStr) - i)
        return int("".join(numStr))

# 2022/9/4  author:github
# class Solution:
#     def monotoneIncreasingDigits(self, n):
#         s = list(str(n))
#         i = 1
#         while i < len(s) and s[i-1] <= s[i]:
#             i += 1
#         if i < len(s):
#             while i and s[i-1] > s[i]:
#                 s[i-1] = str(int(s[i-1]) - 1)
#                 i -= 1
#             i += 1
#             while i < len(s):
#                 s[i] = '9'
#                 i += 1
#         return int("".join(s))

if __name__ == "__main__":
    # n = 10
    n = 3324
    result = Solution().monotoneIncreasingDigits(n)
    print(result)