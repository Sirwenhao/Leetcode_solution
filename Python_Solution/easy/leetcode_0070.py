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

# # 空间复杂度为O(1)的情况
# class Solution:
#     def climbStairs(self, n):
#         dp = [0] * (n+1)
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(2, n+1):
#             temp = dp[0] + dp[1]
#             dp[0] = dp[1]
#             dp[1] = temp
#         return dp[1]

# 2022/11/16 author:WH
# 动态规划专题,动态规划五部曲
# 1、dp[i]表示有dp[i]种方法到达第i层,确定dp数组
# 2、dp[i]取决于dp[i-1]和dp[i-2]，因为到第i层可以是一步到达、也可以是两步到达.递推公式为：dp[i] = dp[i-1]+dp[i-2]
# 3、dp数组的初始化, dp[1] = 1, dp[2] = 2
# 4、由递推公式可知顺序为从前往后,dp[i]=dp[i-1]+dp[i-2]
# 5、举例推导，n=5时，dp[1]=1,dp[2]=2,dp[3]=3,dp[4]=5,dp[5]=8

class Solution:
    def climbStairs(self, n):
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]



if __name__ == "__main__":
    n = 5
    result = Solution().climbStairs(n)
    print(result)