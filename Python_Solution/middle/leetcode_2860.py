# 24/9/4 author:@WH
# 核心点：总要选出一定数量的学生,假设这个数量为k，则必有
# - 被选中的nums[i] < k
# - 未被选中的nums[i] > k
# - nums[i] == k 不被允许 

class Solution:
    @staticmethod
    def countWays(nums):
        nums.sort()
        n = len(nums)
        ans = nums[0] > 0 # 表示一个学生都不选
        for k in range(1, n):
            if nums[k-1] < k < nums[k]:
                ans += 1
        return ans + 1    
    
if __name__ == "__main__":
    # nums = [6,0,3,3,6,7,2,7]
    nums = [1, 1]
    result = Solution.countWays(nums)
    print(result)
        
