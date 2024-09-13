# 24/9/13  @author:WH

class Solution:
    def subarraySum(self, nums, k):
        ans = []
        slow, fast = 0, 1
        while fast <= len(nums):
            subarrsum = sum(nums[slow:fast])
            if subarrsum == k:
                ans.append(nums[slow:fast])
                slow += 1
                fast += 1
            elif subarrsum < k:
                fast += 1
            elif subarrsum > k:
                slow += 1
        return len(ans)
    
    
if __name__ == "__main__":
    # nums = [1,2,3]
    # nums = [1,1,1]
    nums = [-1, -1, 1]
    k = 0
    # k = 3
    result = Solution().subarraySum(nums, k)
    print(result)
                