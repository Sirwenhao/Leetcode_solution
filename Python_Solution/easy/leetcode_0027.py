"""
    1、0027移除元素
    2、类别：数组
    3、双指针专题中的快慢指针
"""

# 2022/6/1  author:WH
# class Solution:
#     def removeElement(self, nums, val):
#         if len(nums) == 0:
#             return False
#         slow = fast = 0
#         while fast < len(nums):
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
#         return slow

# 2022/7/2  author:WH
# 双指针：快慢指针
# 版本1：存在的问题是使用for循环改变不了数组中出现连续val值的情况
class Solution:
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(0, len(nums)-1):
            if nums[fast] == val:
                slow = fast
                nums[fast], nums[fast+1] = nums[fast+1], nums[fast]
        return slow

# 版本2
# 主要是利用nums[fast] != val进行判断
# class Solution:
#     def removeElement(self, nums, val):
#         slow, fast = 0, 0
#         while fast < len(nums):
#             if nums[fast] != val:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 slow += 1
#             fast += 1
#         return slow

# 2022/09/11  
# 没写出来。。。。。。
# class Solution:
#     def removeElement(self, nums, val):
#         slow = fast = 0
#         for fast in range(len(nums)):
#             if nums[fast] != val:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 slow += 1
#             # fast += 1
#         return slow

# # author:WH
# class Solution:
#     def removeElement(self, nums, val):
#         slow = fast = 0
#         while fast < len(nums):
#             # 一步一步把每一个不等于val的值送到前面去
#             if nums[fast] != val:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 slow += 1
#             fast += 1
#         return slow


# # 23/11/28 author:WH
class Solution:
    def removeElement(self, nums, val):
        slow = fast = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            else:
                continue
        return fast


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = Solution().removeElement(nums, val)
    print(result)