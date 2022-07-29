"""
    1、贪心算法
    2、跳跃游戏
"""
# 2022/7/29  author:WH

class Solution:
    def canJump(self, nums):
        Coverage = 0
        if len(nums) == 1: return True
        i = 0
        while i <= Coverage:
            Coverage = max(i + nums[i], Coverage)
            if Coverage >= len(nums)-1: return True
            i += 1
        return False

if __name__ == "__main__":
    nums = [3, 2, 1, 0, 4]
    result = Solution().canJump(nums)
    print(result)