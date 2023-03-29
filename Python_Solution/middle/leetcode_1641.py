# 2023/3/29  author:WH

class Solution:
    def countVowelStrings(self, n):
        dp = [1] * 5
        for _ in range(n-1):
            s = 0
            for j in range(5):
                s += dp[j]
                dp[j] = s
        return sum(dp)

# leetcode官解：等价于从n+4个选择中选取四种不同的
from math import comb
class Solution:
    def countVowelStrings(self, n):
        return comb(n+4, 4)    

if __name__ == "__main__":
    n = 3
    result = Solution().countVowelStrings(n)
    print(result)