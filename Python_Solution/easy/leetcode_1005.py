"""
    1、1005K次取反后求数组和最大值
    2、关键点每次都要改变数组中最小值的符号
"""
# 2022/7/31  author:WH
# 可以考虑递归的写法
class Solution:
    def largestSumAfterKNegations(self, nums, k):
        # 先排序，便于处理最小值
        nums.sort()
        # 定义标志变量
        flag = 0
        if flag < k:
            nums[0] = -nums[0]
            flag += 1
            self.largestSumAfterKNegations(nums, k-1)
        return sum(nums)

if __name__ == "__main__":
    # nums = [2, -3, -1, 5, -4]
    nums =  [4,2,3]
    k = 1
    result = Solution().largestSumAfterKNegations(nums, k)
    print(result)
