"""
    1、给定一个列表，找出和为零的三个数，不能重复
    2、不能重复，首先想到的是数据结构中的集合.用循环可以但是循环嵌套时间复杂度过高
    3、竟然没提前想到先排序，晕~
"""
# 排序之后，使用指针的做法
# def threeSum(nums):
#     nums.sort()
#     ans = []
#     for i in range(len(nums)):
#         left = i+1
#         right = len(nums)-1
#         for j in range(left+1, right):
#             if nums[i]+nums[left]+nums[j] == 0:
#                 ans.append([nums[i], nums[left], nums[j]])
#     return ans


def threeSum(nums):
    n = len(nums)
    nums.sort()
    ans = list()
    # 枚举a
    for first in range(n):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        # c对应的指针初始值指向数组的最右端
        third = n-1
        target = -nums[first]
        # 枚举b
        for second in range(first+1, n):
            # 需要和上一次枚举的数不同
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            # 需要保证b的指着在c的左侧
            while second < third and nums[second] + nums[third] > target:
                third -= 1

            # 如果指针重合，随着b后续的增加
            # 就不会有满足a+b+c=0并且b<c的情况了，退出循环
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])
    return ans

nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)