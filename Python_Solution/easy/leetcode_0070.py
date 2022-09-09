"""
    1、爬楼梯
    2、动态规划专题
"""
# 2022/9/6  author:WH
# 计算复杂度为O(n)
# class Solution:
#     def climbStairs(self, n):
#         dp = [0] * (n+1)
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]

# 空间复杂度为O(1)的情况
class Solution:
    def climbStairs(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            temp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = temp
        return dp[1]


if __name__ == "__main__":
    n = 5
    result = Solution().climbStairs(n)
    print(result)