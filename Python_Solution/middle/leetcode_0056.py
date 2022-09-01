"""
    1、合并区间
"""
# 2022/8/2 author:WH
# class Solution:
#     def merge(self, intervals):
#         ans = []
#         if len(intervals) == 0:
#             return []
#         intervals.sort(key=lambda x:x[0])
#         start, end = intervals[0]
#         for i,j in intervals[1:]:
#             if end < i:
#                 ans.append([start, end])
#                 start, end = i, j
#             else:
#                 end = max(end, j)
#         ans.append([start, end])
#         return ans

# github合并区间问题模板
# def merge(intervals):
#     ans = []
#     intervals.sort()
#     start, end = intervals[0]
#     for i,j in intervals[1:]:
#         if end < i:
#             ans.append([start, end])
#             start, end = i, j
#         else:
#             end = max(end, j)
#     ans.append([start, end])
#     return ans

# 2022/9/1  author:WH
class Solution:
    def merge(self, intervals):
        # 先按照左边界排序
        intervals.sort(key=lambda x:x[0])
        ans = []
        # left和right记录区间的左右边界
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            # 当前区间与前一个区间无相交
            if intervals[i][0] > intervals[i-1][1]:
                ans.append([left, right])
                # 需要更新左右边界
                left, right = intervals[i][0], intervals[i][1]
            else:
                right = max(right, intervals[i][1])
        ans.append([left, right])
        return ans


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = Solution().merge(intervals)
    print(result)
