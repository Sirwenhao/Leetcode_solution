"""
    1、无重叠区间
    2、原则：需要移除的区间总数尽量小
"""
# 2022/8/2  author:WH
# 有问题
# class Solution:
#     def eraseOverlapIntervals(self, intervals):
#         intervals.sort(key=lambda x:(x[0], x[1]))
#         ans = 0
#         for i in range(1, len(intervals)-1):
#             if intervals[i-1][1] > intervals[i][0] and intervals[i][1] > intervals[i+1][0]:
#                 intervals = intervals[:i] + intervals[i+1:]
#                 ans += 1
#             elif intervals[i-1][1] > intervals[i][0] and intervals[i][i] <= intervals[i+1][0]:
#                 intervals = intervals[i:]
#             else:
#                 continue
#         return ans

# 2022/8/2  author:代码随想录
# 逆向思维：需要统计的是需要移除的区间个数，那么可以反过来考虑总数-不需要移除的
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        ans = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                end = intervals[i][1]
                ans += 1
        return len(intervals)-ans

if __name__ == "__main__":
    # intervals = [[1,2],[2,3],[3,4],[1,3]]
    intervals = [[1,2],[1,2],[1,2]]
    result = Solution().eraseOverlapIntervals(intervals)
    print(result)