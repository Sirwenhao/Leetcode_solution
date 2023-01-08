# 2023/1/7  author:WH

# 解法有问题
# class Solution:
#     def minOperations(self, nums, x):
#         ans = 0
#         while x > 0:
#             left, right = 0, len(nums)-1
#             if x < nums[left] and x < nums[right]:
#                 return -1
#             elif nums[left] > x and nums[right] <= x:
#                 left += 1
#             elif nums[left] <= x and nums[right] > x:
#                 right -= 1
#             else:
#                 if nums[right] > nums[left]:
#                     x -= nums[right]
#                     right -= 1
#                     ans += 1
#                 else:
#                     x -= nums[left]
#                     left -= 1
#                     ans += 1
#         return ans

# 双指针：计算两端的部分元素和及元素和之和与x对比决定指针运动方向
class Solution:
    def minOperations(self, nums, x):
        ans = 0
        n = len(nums)
        left, right = -1, n
        lsum = rsum = 0
        


if __name__ == "__main__":
    nums = [1, 1, 4, 2, 3]
    x = 5
    result = Solution().minOperations(nums, x)
    print(result)
            

