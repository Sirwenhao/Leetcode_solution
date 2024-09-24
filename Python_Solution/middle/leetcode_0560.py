# 24/9/13  @author:WH

# 两层for循环
class Solution:
    def subarraySum(self, nums, k):
        ans = []
        n = len(nums)
        for slow in range(n):
            subarrsum = 0
            for fast in range(slow, n):
                subarrsum += nums[fast]
                if subarrsum == k:
                    ans.append(nums[slow:fast+1])
        return len(ans)
    
    
# 前缀和

class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        prefix_sum = 0
        sum_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            if (prefix_sum-k) in sum_count:
                ans += sum_count[prefix_sum-k]
            sum_count[prefix_sum] += sum_count.get(prefix_sum, 0) + 1
        return ans
            
                
            
    
    
if __name__ == "__main__":
    # nums = [1,2,3]
    # nums = [1,1,1]
    nums = [-1, -1, 1]
    k = 0
    # k = 3
    result = Solution().subarraySum(nums, k)
    print(result)
                