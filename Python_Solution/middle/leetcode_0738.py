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

if __name__ == "__main__":
    # n = 10
    n = 3324
    result = Solution().monotoneIncreasingDigits(n)
    print(result)