"""
    1、0027移除元素
    2、类别：数组
    3、双指针专题中的快慢指针
"""

# 2022/6/1  author:WH
class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return False
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = Solution().removeElement(nums, val)
    print(result)