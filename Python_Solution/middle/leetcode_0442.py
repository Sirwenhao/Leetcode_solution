"""
    1、此题难度就在于限定了时间复杂度和空间复杂度
    2、时间复杂度O(n)和常空间复杂度O(1)
"""

# 2022/5/8 author:WH
# 想法把出现次数多余一次的数字往左边放，最后返回这些数字对应在原数组中的切片
class Solution:
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums) if num - 1 != i]
    
if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    result = Solution().findDuplicates(nums)
    print(result)
