"""
    1、746使用最小花费爬楼梯
    2、重新考虑动规五部曲
"""
# 2022/9/6  author:WH
class Solution:
    def minCostClimbingStairs(self, cost):
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # print(i)
        return min(dp[len(cost)-2], dp[len(cost)-1])

if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    # cost = [10, 15, 20]
    result = Solution().minCostClimbingStairs(cost)
    print(result)