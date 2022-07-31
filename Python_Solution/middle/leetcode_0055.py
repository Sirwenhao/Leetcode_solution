"""
    1、贪心算法
    2、跳跃游戏
"""
# 2022/7/29  author:WH

# class Solution:
#     def canJump(self, nums):
#         Coverage = 0
#         if len(nums) == 1: return True
#         i = 0
#         while i <= Coverage:
#             Coverage = max(i + nums[i], Coverage)
#             if Coverage >= len(nums)-1: return True
#             i += 1
#         return False

# 2022/7/31  author:github

class Solution:
    def canJump(self, nums):
        Coverage = 0
        for i,num in enumerate(nums):
            print('i:', i)
            print('Coverage:', Coverage)
            if i > Coverage:
                return False
            Coverage = max(Coverage, i + num)
        return True

if __name__ == "__main__":
    # nums = [3, 2, 1, 0, 4]
    nums = [2,3,1,1,4]
    result = Solution().canJump(nums)
    print(result)