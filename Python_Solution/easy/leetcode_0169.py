"""
    1、出现次数大于n//2(向下取整)的元素
"""
# # 自己写的解法：可以运行但是超时
# def majorityElement(nums):
#     for i in range(len(nums)):
#         if nums.count(nums[i]) > len(nums)//2:
#             return nums[i]
#     return None

# # 官解
# import collections

# def majorityElement(nums):
#     counts = collections.Counter(nums)
#     return max(counts.keys(), key=counts.get)


# 力扣加加
# 投票算法：原理是通过消除不同元素直至没有不同元素，剩下的就是满足条件的元素，关键在于消除不同元素。
# 投票算法的最坏情况，是每一个非众数元素都与众数元素进行消除

def majorityElement(nums):
    count, majority = 1, nums[0]
    for num in nums[1:]:
        if count == 0:
            majority = num
        if num == majority:
            count += 1
        else:
            count -= 1
    return majority

nums = [3,2,3]
result = majorityElement(nums)
print(result)
