"""
    1、合并区间
"""
# 2022/8/2 author:WH
class Solution:
    def merge(self, intervals):
        ans = []
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x:x[0])
        start, end = intervals[0]
        for i,j in intervals[1:]:
            if end < i:
                ans.append([start, end])
                start, end = i, j
            else:
                end = max(end, j)
        ans.append([start, end])
        return ans

# # github合并区间问题模板
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
#         ans.append([start, end])
#         return ans


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = Solution().merge(intervals)
    print(result)
