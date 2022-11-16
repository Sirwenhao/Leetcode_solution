# 2022/11/17 author:官解
# 时间复杂度O(n),空间复杂度O(n)

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        nums_set = set(nums)
        # print(nums_set)
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_streak = 1
                while current_num+1 in nums_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    result = Solution().longestConsecutive(nums)
    print(result)