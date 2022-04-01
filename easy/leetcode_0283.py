'''
    1、不能开辟新的存储空间
'''

# 解法一：有问题

# def moveZeros(nums):
#     for j in range(len(nums)):
#         i = 0
#         while i < len(nums)-1:
#             cnt = 0
#             if nums[i] == 0:
#                 cnt = nums[i+1]
#                 nums[i+1] = nums[i]
#                 nums[i] = cnt
#                 i+=1
#         j+=1
#     return nums

# 解法二：双指针
# 第一个指针把所有非0项前移，第二个指针把剩余所有位置全部置零

# def moveZeros(nums):
#     if not nums:
#         return False
    
#     j = 0
#     for i in range(len(nums)):
#         if nums[i]:
#             nums[j] = nums[i]
#             j+=1

#     for k in range(j, len(nums)):
#         nums[k] = 0

#     return nums


# 解法三
# 1、左指针指向已处理好的非零序列的尾部
# 2、右指针不断向右移动，遇到非零数就交换，同时左指针右移一位

def moveZeros(nums):
    left = right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums

nums = [0,1,0,3,12]
result = moveZeros(nums)
print(result)