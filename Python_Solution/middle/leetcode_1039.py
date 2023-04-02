# 2023/4/2  author:WH
# 动态规划

# github解法
from functools import cache
class Solution:
    def minScoreTriangulation(self, values):
        @cache
        def dfs(i, j):
            if i+1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + values[i]*values[k]*values[j] for k in range(i+1, j))
        return dfs(0, len(values)-1)
    
if __name__ == "__main__":
    values = [3,7,4,5]
    result = Solution().minScoreTriangulation(values)
    print(result)