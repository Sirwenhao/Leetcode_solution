"""
    1、整数拆分
    2、动规五步骤：
    2.1、确定dp[i]及i表示的含义：dp[i]表示拆分整数i所得到的最大乘积
    2.2、确定递推公式：dp[i] = max(dp[i], max(j*(i-j)), j*dp[i-j])
    2.3、确定初始状态：dp[2]=1
    2.4、确定遍历顺序：此处要特别注意i>=3,j>=2
"""
# 2022/9/7  author:WH
class Solution:
    def integerBreak(self, n):
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max((j*(i-j)), j*dp[i-j]))
        return dp[n]

if __name__ == "__main__":
    n = 10
    result = Solution().integerBreak(n)
    print(result)