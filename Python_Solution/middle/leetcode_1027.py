# 2023/4/23  author:WH

class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        f = [[1] * 1001 for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for k in range(i):
                j = nums[i] - nums[k] + 500
                f[i][j] = max(f[i][j], f[k][j]+1)
                ans = max(ans, f[i][j])
        return ans
    
if __name__ == "__main__":
    nums = [9,4,7,2,10]
    result = Solution().longestArithSeqLength(nums)
    print(result)