"""
    1、子数组为连续数组
"""

# 2022/6/2  author:WH
# 暴力解法：双循环遍历
# 报错：超时
# class Solution:
#     def minSubArrayLen(self, target, nums):
#         if target > sum(nums):
#             return 0
#         minLength = len(nums)+1
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if sum(nums[i:j+1]) >= target:
#                     print(nums[i:j+1])
#                     minLength = min(minLength, j-i+1)
#         return minLength

# 力扣官解
# class Solution:
#     def minSubArrayLen(self, target, nums):
#         if sum(nums) < target:
#             return 0

#         minLength = len(nums)+1
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 total += nums[i]
#                 if total >= target:
#                     minLength = min(minLength, j-i+1)
#                     break
#         return 0 if minLength == len(nums)+1 else minLength


# 双指针：快慢指针
class Solution:
    def minSubArrayLen(self, target, nums):
        res = float("inf")
        Sum = 0
        slow = 0
        for fast in range(len(nums)):
            Sum += nums[fast]
            while Sum >= target:
                res = min(res, fast-slow+1)
                Sum -= nums[slow]
                slow += 1
        return 0 if res == float("inf") else res

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    result = Solution().minSubArrayLen(target, nums)
    print(result)
