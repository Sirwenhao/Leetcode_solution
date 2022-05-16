"""
    1、回溯法典型
    2、一开始考虑使用循环，但时间复杂度过高，实现困难
    3、不含重复数字的数组，返回其所有子集
"""

# # 力扣加加解法一，使用内置库函数
# class Solution:
#     def permute(self, nums):
#         # 先排序
#         # nums.sort()
#         # res = []
#         import itertools
#         return itertools.permutations(nums)

# # 力扣加加解法二：回溯法
# class Solution:
#     def permute(self, nums):
#         """自己写回溯法"""
#         res = []
#         def backtrack(nums, pre_list):
#             if len(nums) <= 0:
#                 res.append(pre_list)
#             else:
#                 for i in nums:
#                     # 注意copy一份新的调用，否则无法正常循环
#                     p_list = pre_list.copy()
#                     p_list.append(i)
#                     left_nums = nums.copy()
#                     left_nums.remove(i)
#                     backtrack(left_nums, p_list)
#         backtrack(nums, [])
#         return res


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

# 2022/5/11 author:WH
# 有一个值得考虑的问题是结集中元素排列顺序是否需要考虑
# 另外一点，此题要求的是全排列，因此所有子集均为全元素的排列
# class Solution:
#     def permute(self, nums):
#         # 创建结果集
#         res = []
#         start_index = 0
#         current = []
#         def backtracking(nums, start_index):
#             if len(current) == len(nums):
#                     res.append(current[:])
#                     return
#             for i in range(start_index, len(nums)):
#                 current.append(nums[i])
#                 backtracking(nums, start_index+1)
#                 start_index -= 1
#                 current.pop()
#             return res
#         backtracking(nums, start_index)
# 上部分代码逻辑没有问题，但是无法控制字符重复出现的情况
# 代码随想录中介绍的解决方法是使用一个数组对已经选择过的数字进行标记
# 此题一共有两个版本：版本一是使用used_list对使用过的元素进行标记，版本二不使用used_list而直接判断，用过则continue

# # 版本一
# class Solution:
#     def permute(self, nums):
#         """
#         同一树层上的数字可以重复选取，同一树枝上的数字不可以
#         """
#         # 结果集
#         ans = []
#         # 定义当前结果集
#         current = []
#         # 定义数组用于标记已经使用过的数字
#         used = [False] * len(nums)  
#         # 定义回溯函数结构体
#         def backtracking(nums, used):
#             if len(current) == len(nums):
#                 ans.append(current[:])
#                 return 
#             # 定义单层递归逻辑
#             for i in range(0, len(nums)):
#                 # 遇到已经使用过的元素直接跳过
#                 if used[i] == True:
#                     continue
#                 used[i] = True
#                 current.append(nums[i])
#                 backtracking(nums, used)
#                 current.pop()
#                 used[i] = False
#             return ans
#         return backtracking(nums, used)
        
# 版本二：不适用used做标记，遇见重复直接跳过
class Solution:
    def permute(self, nums):
        """定义结果集"""
        ans = []
        """定义满足条件的当前结果"""
        current = []
        """定义回溯函数主体"""
        def backtracking(nums):
            if len(current) == len(nums):
                ans.append(current[:])
                return
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtracking(nums)
                current.pop()
        backtracking(nums)
        return ans

if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().permute(nums)
    print(result)