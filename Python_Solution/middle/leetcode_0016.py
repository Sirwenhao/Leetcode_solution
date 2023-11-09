# 23/11/09 author:WH

from cmath import inf

class Solution:
    def threeSumClosest(self, nums, target):
        ans = inf
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                new_value = nums[i] + nums[j] + nums[k]
                if new_value == target:
                    return new_value
                if abs(new_value - target) < abs(ans - target):
                    ans = new_value
                if new_value > target:
                    k -= 1
                else:
                    j += 1
        return ans
    
if __name__ == '__main__':
    # nums = [-1,2,1,-4]
    # target = 1
    nums = [4,0,5,-5,3,3,0,-4,-5]
    target = -2
    result = Solution().threeSumClosest(nums, target)
    print(result)