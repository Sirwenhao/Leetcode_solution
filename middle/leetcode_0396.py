"""
    1、旋转函数
"""
# # 自己写的解法，感觉应该没问题，但是还是有示例没有通过
# def maxRotateFunction(nums):
#     n = len(nums)
#     max_v = 0
#     for i in range(len(nums)):
#         nums1 = nums[n-i:n] + nums[0:n-i]
#         # print(nums1)
#         f = 0
#         for j in range(len(nums1)):
#             f += j * nums1[j]
#         max_v = max(max_v, f)
#     print(max_v)
#     return max_v

# 力扣官解

def maxRotateFunction(nums):
    f, n, numSum = 0, len(nums), sum(nums)
    for i, num in enumerate(nums):
        f += i * num
    res = f
    for i in range(n-1,0,-1):
        f = f + numSum- n*nums[i]
        res = max(res, f)
    return res


nums = [4,3,2,6]
result = maxRotateFunction(nums)
print(result)


# 定义旋转列表
# nums = [4,3,2,6]
