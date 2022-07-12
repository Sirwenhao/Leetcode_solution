"""
    1、滑动窗口最大值
"""
# 2022/7/12  author:WH
# 此法可解但会超时
class Solution:
    def maxSlindingWindow(self, nums, k):
        ans = []
        left, right = 0, k
        while right <= len(nums):
            ans.append(max(nums[left:right]))
            right += 1
            left += 1
        return ans

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = Solution().maxSlindingWindow(nums, k)
    print(result)