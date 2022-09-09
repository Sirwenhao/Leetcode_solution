"""
    1、不同的二叉搜索树
    2、难：没有推导出递推的过程
"""
# 2022/9/9  author:WH
class Solution:
    def numTrees(self, n):
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]

if __name__ == "__main__":
    n = 5
    result = Solution().numTrees(n)
    print(result)