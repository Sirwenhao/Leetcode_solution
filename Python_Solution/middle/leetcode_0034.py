"""
1、数组升序排列找出起始位置和终止位置并返回
"""
# 2022/5/9 authoe:WH 解法一：二分加递归
# 要分清楚情况：
# 第一target不在nums内部，直接返回[-1,-1]
# 第二target在nums所属的范围内部，但是nums中没有这个值
class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        # 定义二分搜索
        def binarySearch(nums, target:int):
            left, right = 0, len(nums)-1
            while left <= right:   # 这个位置的等于号是要取到的，要不会报错
                middle = (left + right) // 2
                if nums[middle] > target:
                    right = middle-1
                elif nums[middle] < target:
                    left = middle+1
                else:
                    return middle
            return -1
        index = binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        left, right = index, index
        # 二分查找的位置是从中间开始的，防止漏掉左侧解
        while left-1>0 and nums[left-1] == target:
            left -= 1
        # 防止漏掉右侧解
        while right+1>0 and nums[right+1] == target:
            right += 1
        return [left, right]    


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    result = Solution().searchRange(nums, target)
    print(result)