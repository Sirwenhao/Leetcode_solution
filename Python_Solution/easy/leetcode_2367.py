# 2023/3/31  author:WH
# 自己的写法

class Solution:
    def arithmeticTriplets(self, nums, diff):
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] + diff in nums:
                if nums[i] + 2*diff in nums:
                    ans += 1
                else:
                    continue
            else:
                continue
        return ans
    
# github解法一
from itertools import combinations

class Solution:
    def arithmeticTriplets(self, nums, diff):
        return sum(b-a == diff and c-b == diff for a,b,c in combinations(nums, 3))

# github解法二
class Solution:
    def arithmeticTriplets(self, nums, diff):
        vis = set(nums)
        return sum(x+diff in vis and x+diff*2 in vis for x in nums)

    
if __name__ == "__main__":
    nums = [0,1,4,6,7,10]
    diff = 3
    result = Solution().arithmeticTriplets(nums, diff)
    print(result)