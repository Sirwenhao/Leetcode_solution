"""
    1、二分查找
    2、更新的的是左右边界，中心middle值是左右两个边界的均值
"""

# 2022/5/9 author:WH
class Solution:
    def search(self, nums, target):
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            middle = (left+right) // 2
            if nums[middle] < target:
                left = middle+1
            elif nums[middle] > target:
                right = middle
            else:
                return middle
        return -1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    target = 3
    result = Solution().search(nums, target)
    print(result)