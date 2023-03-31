# 2023/3/31  author:WH
# 没有看懂题意，但是这个题真的不难。。。

# class Solution:
#     def maxWithOfVerticalArea(self, points):
#         points.sort()
#         ans = 0
#         for i in range(len(points)-1):
#             ans = max(ans, points[i+1][0]-points[i][0])
#         return ans
# github解法
from itertools import pairwise
class Solution:
    def maxWithOfVerticalArea(self, points):
        points.sort()
        return max(b[0] - a[0] for a,b in pairwise(points))
    
if __name__ == "__main__":
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    result = Solution().maxWithOfVerticalArea(points)
    print(result)