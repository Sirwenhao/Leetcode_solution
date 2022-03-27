"""
    1、力扣加加解法
"""

# import sys
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         maxSum = -sys.maxsize
#         sum = 0
#         for i in range(n):
#             sum = 0
#             for j in range(i, n):
#                 sum += nums[j]
#                 maxSum = max(maxSum, sum)
#         return maxSum


# 2022/3/26 复习 
'''
    1、完全没有思路，
'''

import sys
class Solution:
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)
    def helper(self, nums, l, r):
        if l > r:
            return -sys.maxsize
        mid = (l + r) // 2
        left = self.helper(nums, l , mid - 1)
        right = self.helper(nums, mid + 1, r)
        left_suffix_max_sum = right_prefix_max_sum = 0
        sum = 0
        for i in reserved(range(l, mid)):
            sum += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum, sum)
        sum = 0
        for i in range(mid+1, r+1):
            sum += nums[i]
            right_prefix_max_sum = max(right_prefix_max_sum, sum)
        cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        return max(cross_max_sum, left, right)


nums = [-1, -2, -3, 1,2,3,4,56,6,-8,-100]

