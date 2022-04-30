'''
    1、关键点一：两个元素相等
    2、关键点二：两个元素所以之差的绝对值不大于给定值k
'''

# def containsNearbyDuplicate(nums, k):
#     for i in range(len(nums)-k+1):
#         for j in range(i+1, i+k+1):
#             if nums[i] == nums[j]:
#                 return True
#             else:
#                 continue
#     return False

# 解法二:力扣加加解法

def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, j in enumerate(nums):
        if j in dic and i - dic[j] <= k:
            return True
        dic[j] = i
    return False


# 2022/3/30 复习

# def containsNearbyDuplicate(nums, k):
#     dic = {}
#     for i,j in enumerate(nums):
#         if j in dic and dic[j] - i <= k:
#             return True
#         else:  # 此处出错
#             dic[j] = i
#     return False



nums = [1,2,3,1,2,3]
k = 2
result = containsNearbyDuplicate(nums, k)
print(result)