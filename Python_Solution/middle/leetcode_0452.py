"""
    1、用最少数量的箭引爆气球
    2、贪心加排序
    3、相似题型：757.设置交集大小至少为2
    4、同leetcode_0406中lambda用法
"""
# 2022/8/2  author:WH

class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[0])
        if len(points) == 0:
            return 0
        ans = 1
        for i in range(1, len(points)):
            # 两个气球只要不挨着就得多用一只箭，下面用的大于号
            if points[i][0] > points[i-1][1]:
                ans += 1
            else:
                # 更新重叠气球的最小右边界
                points[i][1] = min(points[i][1], points[i-1][1])
        return ans


if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    result = Solution().findMinArrowShots(points)
    print(result)