"""
    1、斐波那契数列
    2、严格按照dp五部曲来结题
    3、步骤一：确定dp数组以及下标含义:dp[i]表示第i个斐波那契数值为dp[i]
    4、步骤二：确定状态转移方程dp[i]=dp[i-1]+dp[i-2]
    5、步骤三：确定遍历顺序，从前到后遍历，因为当前值依赖于先前值
"""
# 2022/9/6  author:WH
class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        d0 = 0
        d1 = 1
        d2 = 0
        for i in range(1, n):
            d2 = d0 + d1
            # 更新
            d0, d1 = d1, d2
        return d2

if __name__ == "__main__":
    n = 10
    result = Solution().fib(n)
    print(result)
