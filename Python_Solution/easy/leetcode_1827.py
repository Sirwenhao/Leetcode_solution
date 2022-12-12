# 2022/12/11 author:WH
# 使用最少的次数使数组递增

# 超时,if语句没有优化好，continue的时候对应的i也需要随着改变
class Solution:
    def minOperations(self, nums):
        i = 1
        ans = 0
        while i < len(nums):
            if nums[i] > nums[i-1]:
                i += 1
                continue
            ans += nums[i-1]+1 - nums[i]
            nums[i] = nums[i-1]+1
            i += 1
        return ans

if __name__ == "__main__":
    # nums = [1, 1, 1]
    nums = [1,5,2,4,1]
    result = Solution().minOperations(nums)
    print(result)
