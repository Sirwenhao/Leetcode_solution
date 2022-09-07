"""
    1、不同路径II，由障碍
"""
# 2022/9/7  author:WH
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # print('m:', m)
        # print('n:', n)
        # 这个地方创建dp二维数组一定是内层是列，外层是行的这种写法，如下：
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        if dp[0][0] == 0:
            return 0
        # 第一行
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
        print('dp:', dp)
        # 第一列
        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j-1][0]

        print('dp:', dp)

        for k in range(1, m):
            for l in range(1, n):
                if obstacleGrid[k][l] != 1:
                    dp[k][l] = dp[k-1][l] + dp[k][l-1]
        return dp[-1][-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    result = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(result)
