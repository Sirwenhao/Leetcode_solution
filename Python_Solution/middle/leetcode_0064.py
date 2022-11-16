# 2022/11/16  author:WH
# 所有路径上数字之和最小的那条
# 我自己的解法，仅仅根据下一步的值的大小是无法确定所有路径遍历完之后的情况的
# class Solution:
#     def minPathSum(self, grid):
#         row, col = len(grid), len(grid[0])
#         ans = grid[0][0]
#         i = j = 0
#         while i < row-1 or j < col-1:
#             if grid[i+1][j] < grid[i][j+1]:
#                 i += 1
#                 ans += grid[i][j]
#             else:
#                 j += 1
#                 ans += grid[i][j]
#         return ans

# 2022/11/16  author:官解
# 动态规划
class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]  
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[rows-1][cols-1]



if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    result = Solution().minPathSum(grid)
    print(result)