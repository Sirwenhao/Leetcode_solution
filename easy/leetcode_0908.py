"""
    1、相对来说比较清晰，但是要考虑到极端情况，即nums[max]-k和nums[min]+k的大小关系
"""
# # 解法一：自己写
# class Solution:
#     def smallestRangeI(self, nums, k):
#         # 分情况讨论,先取出nums中的最大最小值
#         max_v, min_v = max(nums), min(nums)
#         if max_v - min_v >= 2*k:
#             return max_v-k - (min_v+k)
#         else:
#             return 0

# 解法二：官解
class Solution:
    def smallestRangeI(self, nums, k):
        return max(0, (max(nums)-min(nums)-2*k))

if __name__ == '__main__':
    nums = [1, 3, 6]
    k = 2
    result = Solution().smallestRangeI(nums, k)
    print(result)
    # a = max(nums)
    # b = min(nums)
    # print(a, b)
