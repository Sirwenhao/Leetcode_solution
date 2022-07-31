"""
    1、1005K次取反后求数组和最大值
    2、关键点每次都要改变数组中最小值的符号
    3、解题步骤可以分为四步：首先将数组按大小排序；从前向后遍历，改变符号同时更新数组，将k用完并求和
"""
# 2022/7/31  author:WH
# 可以考虑递归的写法
# class Solution:
#     def largestSumAfterKNegations(self, nums, k):
#         # 先排序，便于处理最小值
#         nums.sort()
#         # 定义标志变量
#         flag = 0
#         if flag < k:
#             nums[0] = -nums[0]
#             flag += 1
#             self.largestSumAfterKNegations(nums, k-1)
#         return sum(nums)

# 2022/7/31  author:代码随想录
# 核心思想是一样的
# class Solution:
#     def largestSumAfterKNegations(self, nums, k):
#         nums = sorted(nums, key=abs, reverse=True)
#         print('nums:', nums)
#         for i in range(len(nums)):
#             if k > 0 and nums[i] < 0:
#                 nums[i] *= -1
#                 k -= 1
#         if k > 0:
#             nums[-1] *= (-1)**k
#         return sum(nums)

# 2022/7/31  author:github
from collections import Counter
class Solution:
    def largestSumAfterKNegations(self, nums, k):
        counter = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if counter[i]:
                ops = min(counter[i], k)
                ans -= (i * ops * 2)
                counter[i] -= ops
                counter[i] += ops
                k -= ops
                if k == 0:
                    break
        if k > 0 and k % 2 == 1 and not counter[0]:
            for i in range(1, 101):
                if counter[i]:
                    ans -= 2 * i
                    break
        return ans


if __name__ == "__main__":
    # nums = [2, -3, -1, 5, -4]
    nums =  [4,2,3]
    k = 1
    result = Solution().largestSumAfterKNegations(nums, k)
    print(result)
