"""
    1、回溯法典型
    2、一开始考虑使用循环，但时间复杂度过高，实现困难
"""

# # 力扣加加解法一，使用内置库函数
# class Solution:
#     def permute(self, nums):
#         # 先排序
#         # nums.sort()
#         # res = []
#         import itertools
#         return itertools.permutations(nums)

# 力扣加加解法二：回溯法
class Solution:
    def permute(self, nums):
        """自己写回溯法"""
        res = []
        def backtrack(nums, pre_list):
            if len(nums) <= 0:
                res.append(pre_list)
            else:
                for i in nums:
                    # 注意copy一份新的调用，否则无法正常循环
                    p_list = pre_list.copy()
                    p_list.append(i)
                    left_nums = nums.copy()
                    left_nums.remove(i)
                    backtrack(left_nums, p_list)
        backtrack(nums, [])
        return res


# # 力扣加加解法三：回溯
# class Solution:
#     def permute(self, nums):
#         res = []
#         length = len(nums)
#         def backtrack(start=0):
#             if start == length:
#                 # nums[:]返回nuns的一个副本，指向新的引用，
#                 res.append(nums[:])
#             for i in range(start, length):
#                 nums[start], nums[i] = nums[i], nums[start]
#                 backtrack(start+1)
#                 nums[start], nums[i] = nums[i], nums[start]
#         backtrack()
#         return res


if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().permute(nums)
    print(list(result))

# nums = [1,2,3]
# num = nums[:]
# print(num)