# 2023/1/5  author:WH
# leetcode官解
# class Solution:
#     def maxValue(self, n, index, maxSum):
#         left, right = 1, maxSum
#         while left < right:
#             mid = (left + right + 1) // 2
#             if self.valid(mid, n, index, maxSum):
#                 left = mid
#             else:
#                 right = mid - 1
#         return left

#     def valid(self, mid, n, index, maxSum):
#         left = index
#         right = n - index - 1
#         return mid + self.cal(mid, left) + self.cal(mid, right) <= maxSum

#     def cal(self, big, length):
#         if length + 1 < big:
#             small = big - length
#             return ((big - 1 +small) * length) // 2
#         else:
#             ones = length - (big-1)
#             return (big - 1 + 1) * (big - 1) // 2 + ones

# github
class Solution:
    def maxValue(self, n, index, msxSum):
        def sum(x, cnt):
            return (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x + 1)*x // 2 + cnt - x
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

if __name__ == "__main":
    n = 4
    index = 2
    maxSum = 6
    result = Solution().maxValue(n, index, maxSum)
    print(result)