"""
    1、有序数组的平方
"""
# 2022/6/5  author:WH
class Solution:
    def sortedSquares(self, nums):
        left, right, k = 0, len(nums)-1, len(nums)-1
        new_Nums = [0]*len(nums)
        while left <= right:
            a = nums[left] ** 2
            b = nums[right] ** 2
            if a <= b:
                new_Nums[k] = b
                right -= 1
            else:
                new_Nums[k] = a
                left += 1
            k -= 1
        return new_Nums
    
# 24/9/8   author:@WH
class Solution:
    def sortedSquares(self, nums):
        return sorted([i**2 for i in nums])   


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    result = Solution().sortedSquares(nums)
    print(result)
