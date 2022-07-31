"""
    1、跳跃游戏II
    2、关键点在于最小步数
"""
# 2022/7/31  author:WH
class Solution:
    def jump(self, nums):
        res = 0
        curC = 0
        nextC = 0
        for i in range(len(nums)):
            nextC = max(nextC, i+nums[i])
            if i == curC:
                if curC != len(nums)-1:
                    res += 1
                    curC = nextC
                    if curC > len(nums)-1:
                        break
                else:
                    break
        return res

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    result = Solution().jump(nums)
    print(result)