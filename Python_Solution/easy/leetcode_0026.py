# 2022/3/6

"""
    1、0026删除数组中的重复项
    2、双指针遍历
"""

# def removeDuplicates(nums):
#     a = {}
#     m = 0
#     for i in nums:
#         if nums.count(i) > 1:
#             a[i] = nums.count(i)
#     for j in a:
#         m += a[j]
#     # print(m)
#     # print('\n')
#     for i in nums:
#         if nums.count(i) > 1:
#             nums.remove(i)
#         else:
#             continue
#     return m, nums


# def removeDuplicates(nums):
#     if not nums:
#         return 0
#     n = len(nums)
#     fast = slow = 1
#     while fast < n:
#         if nums[fast] != nums[fast - 1]:
#             nums[slow] = nums[fast]
#             slow += 1
#         fast += 1
#     return slow


# 2022/3/26复习

'''
    1、快慢双指针，快指针用于遍历所有元素
    2、首先判断nums是否为空
    3、不为空则fast指针直接从1开始，起点和slow就不一样
    4、判断slow和fast指针所指向的对象的值是否相等，若相等先让slow加一，再把fast所指给slow所指
    5、slow+1才是最终要返回的长度，可与debug看下，slow始终比最终长度少1
'''

# def removeDuplicates(nums):
#     if nums:
#         slow = 0
#         for fast in range(1, len(nums)):
#             if nums[slow] != nums[fast]:
#                 slow += 1
#                 nums[slow] = nums[fast]
#         return slow + 1
#     else:
#         return 0


# 2022/4/2 复习

# def removeDuplicates(nums):
#     if nums is None:
#         return False

#     left = right = 0
#     while right < len(nums)-1:
#         if nums[right] != nums[right+1]:
#             nums[left] = nums[right]
#             left += 1
#         right += 1

# def removeDuplicates(nums):
#     if nums:
#         left = 0
#         for right in range(1, len(nums)):
#             if nums[left] != nums[right]:
#                 left += 1 
#                 nums[left] = nums[right]
#         return left+1

#     else:
#         return 0
                   
# 2022/4/9 review
# 不允许开辟新的空间，也就是说只能在原始的空间上去执行操作的
# 关键在于慢指针（左指针）的使用，判断nums[left] == nums[right]是否为真、
# 若为真，left不变；若不为真，left+1滑到新位置，然后再把nums[right]给nums[left]

# def removeDuplicates(nums):
#     if nums is None:
#         return False
#     else:
#         cnt = left = 0
#         for right in range(1, len(nums)):
#             if nums[right] != nums[left]:
#                 cnt += 1
#                 left += 1
#                 nums[left] = nums[right]
#         return cnt+1

# list = [0,0,1,1,1,2,2,3,3,4]
# # list = [1,1,2]
# result = removeDuplicates(list)
# print(result)
# print(list)

# # 2022/6/1 author:WH  双指针解法
# class Solution:
#     def removeDuplicates(self, nums):
#         if len(nums) == 0:
#             return False
#         slow = fast = 0
#         for fast in range(1, len(nums)):
#             if nums[slow] != nums[fast]:
#                 slow += 1
#                 nums[slow] = nums[fast]
#         return nums

# 2022/11/24  author:WH
class Solution:
    def removeDuplicates(self, nums):
        slow = 0 
        for fast in range(slow, len(nums)):
            if nums[fast] > nums[slow]:
                nums[fast], nums[slow+1] = nums[slow+1], nums[fast]
                slow += 1
            else:
                continue
        return slow+1

# # 2022/11/14  author:WH
# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return False
#         slow = fast = 0
#         for fast in range(1, len(nums)):
#             if nums[slow] != nums[fast]:
#                 slow += 1
#                 nums[slow] = nums[fast]
#         return slow+1
 
# 23/11/27 author:WH
class Solution:
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            else:
                continue
        return slow+1




if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = Solution().removeDuplicates(nums)
    print(result)
    