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

def removeDuplicates(nums):
    if nums:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1 
                nums[left] = nums[right]
        return left+1

    else:
        return 0
                   



list = [0,0,1,1,1,2,2,3,3,4]
# list = [1,1,2]
result = removeDuplicates(list)

print(result)
print(list)