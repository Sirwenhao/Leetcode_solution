"""
    1、整数拆分
    2、动规五步骤：
    2.1、确定dp[i]及i表示的含义：dp[i]表示拆分整数i所得到的最大乘积
    2.2、确定递推公式：dp[i] = max(dp[i], max(j*(i-j)), j*dp[i-j])
    2.3、确定初始状态：dp[2]=1
    2.4、确定遍历顺序：此处要特别注意i>=3,j>=2
    2.5、关于递推公式的解释：
    假设对正整数i拆分出的第一个正整数是j(1<=j<i)，则有以下两种方案：
    1>将i拆分成j和i-j的和，且i-j不在拆分成多个正整数，此时乘积是j*(i-j)
    2>将i拆分成j和i-j的和，且i-j继续拆分成多个正整数，此时乘积为j*dp[i-j]
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