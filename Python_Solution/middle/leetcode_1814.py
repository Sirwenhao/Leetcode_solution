# 2023/1/17  author:WH
# 时间复杂度过高，O(n*(n-1)), 空间复杂度O(1)

class Solution:
    def countNicePairs(self, nums):
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + int(str(nums[j])[::-1]) == nums[j] + int(str(nums[i])[::-1]):
                    ans += 1
                else:
                    continue
        return ans


if __name__ ==  "__main__":
    nums = [42, 11, 1, 97]
    result = Solution().countNicePairs(nums)
    print(result)