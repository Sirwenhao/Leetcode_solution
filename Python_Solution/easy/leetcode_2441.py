# 2023/5/13  author:WH
class Solution:
    def findMaxK(self, nums):
        nums.sort()
        ans = -1
        n = len(nums)
        while n > 0:
            if ((-1)*nums[n-1]) in nums:
                ans = nums[n-1]
                break
            n -= 1
        return ans
    
if __name__ == "__main__":
    nums = [-1, 2, -3, 3]
    result = Solution().findMaxK(nums)
    print(result)