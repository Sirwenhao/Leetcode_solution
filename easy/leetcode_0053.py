"""
    1、最大子序列和，核心滑动窗口
    2、判断关键窗长和序列数据之和
"""
# 前缀和+暴力解

# import sys
# def maxSubArray(nums) -> int:
#     n = len(nums)
#     maxSum = -sys.maxsize
#     sum = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i, n):
#             sum += nums[j]
#             maxSum = max(maxSum, sum)
#     return maxSum


# class Solution:
# def maxSubArray(nums):
#     maxSum = nums[0]
#     minSum = sum = 0
#     for i in range(len(nums)):
#         sum += nums[i]
#         maxSum = max(maxSum, sum - minSum)
#         minSum = min(sum, minSum)
#     return maxSum

# 2022/3/26  复习
# 分治法

# import sys
# class Solution:
#     def maxSubArray(self, nums):
#         return self.helper(nums, 0, len(nums) - 1)
#     def helper(self, nums, l, r):
#         if l > r:
#             return -sys.maxsize
#         mid = (l + r) // 2
#         left = self.helper(nums, l, mid - 1)
#         right = self.helper(nums, mid + 1, r)
#         left_suffix_max_sum = right_prefix_max_sum = 0
#         sum = 0
#         for i in reversed(range(l, mid)):
#             sum += nums[i]
#             left_suffix_max_sum = max(left_suffix_max_sum, sum)
#         sum = 0
#         for i in range(mid + 1, r + 1):
#             sum += nums[i]
#             right_prefix_max_sum = max(right_prefix_max_sum, sum)
#         cross_max_sum =left_suffix_max_sum + right_prefix_max_sum + nums[mid]
#         return max(cross_max_sum, left, right)

# 2022/4/3 复习
# 解法二：前缀和加暴力解，时间复杂度为O(n^2)，空间复杂度为O(N)

# import sys
# def maxSubArray(nums):
#     n = len(nums)
#     maxSum = -sys.maxsize
#     sum = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i, n):
#             sum += nums[j]
#             maxSum = max(maxSum, sum)

#     return maxSum

# # 2022/3/26 复习 
# '''
#     1、完全没有思路，
# '''

# import sys
# class Solution:
#     def maxSubArray(self, nums):
#         return self.helper(nums, 0, len(nums) - 1)
#     def helper(self, nums, l, r):
#         if l > r:
#             return -sys.maxsize
#         mid = (l + r) // 2
#         left = self.helper(nums, l , mid - 1)
#         right = self.helper(nums, mid + 1, r)
#         left_suffix_max_sum = right_prefix_max_sum = 0
#         sum = 0
#         for i in reserved(range(l, mid)):
#             sum += nums[i]
#             left_suffix_max_sum = max(left_suffix_max_sum, sum)
#         sum = 0
#         for i in range(mid+1, r+1):
#             sum += nums[i]
#             right_prefix_max_sum = max(right_prefix_max_sum, sum)
#         cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
#         return max(cross_max_sum, left, right)


# 优化前缀和

def maxSubArray(nums):
    n = len(nums)
    maxSum = nums[0]
    minSum = sum = 0
    for i in range(n):
        sum += nums[i]
        maxSum = max(maxSum, sum - minSum) #sum-minSum 
        minSum = min(minSum, sum)



nums = [-2,1,-3,4,-1,2,1,-5,4]

result = maxSubArray(nums)
print(result)