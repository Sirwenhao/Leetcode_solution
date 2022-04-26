"""
    1、字典序的概念
"""
# # 力扣加加解法
# def nextPermutation(nums):
#     down_index = None
#     for i in range(len(nums)-2, -1, -1):
#         if nums[i] < nums[i+1]:
#             down_index = i
#             break
#     if down_index is None:
#         nums.reverse()
#     else:
#         for i in range(len(nums)-1, i, -1):
#             if nums[down_index] < nums[i]:
#                 nums[down_index], nums[i] = nums[i], nums[down_index]
#                 break
#         i, j = down_index+1, len(nums)-1
#         while i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#             j -= 1

# 官解

def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = len(nums)-1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i+1, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1 

nums = [3,1,2,3]
nextPermutation(nums)
print(nums)