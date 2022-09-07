"""
    1、二维动态规划
"""
# 2022/09/07  author:WH
class Solution:
    def uniquePaths(self, m, n):
        # 创建二维数组
        dp = [[1 for i in range(n)] for j in range(m)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

if __name__ == "__main__":
    m = 3
    n = 7
    result = Solution().uniquePaths(m, n)
    print(result)