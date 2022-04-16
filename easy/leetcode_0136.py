"""
    1、只出现一次的数字
    2、list删除元素的三种操作：remove是删除首个符合条件（根据元素值）的元素，pop删除元素（根据索引值），del根据索引值删除元素
"""

# # 解法一
# def singleNumber(nums):
#     # 先排序
#     nums.sort()
#     i = goal = 0
#     while i < len(nums):
#         key = nums[i]
#         nums.remove(key)
#         if key not in nums:
#             goal = key
#         i+=1
#     return goal

# 解法二:力扣加加
# 原则：任何数和0异或是自身，任何数与自身异或是0

def singleNumber(nums):
    single_number = 0
    for num in nums:
        single_number ^= num
    return single_number


# # 解法三：力扣官解

# from functools import reduce
# def singleNumber(nums):
#     return reduce(lambda x, y: x^y, nums)


nums = [4,1,2,1,2]
# nums.pop(2)
# nums.remove(nums[0])
# print(nums)
result = singleNumber(nums)
print(result)