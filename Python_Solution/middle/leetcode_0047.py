"""
    1、回溯专题
"""
# # 代码随想录
# class Solution:
#     def permuteUnique(self, nums):
#         if len(nums) == 0:
#             return []
#         res = []
#         # 定义标志变量用于判断是否进行剪枝
#         used = [0] * len(nums)
#         def backtracking(nums, used, path):
#             # 结果不能重复则考虑使用集合来存放
#             # 终止条件
#             if len(path) == len(nums):
#                 res.append(path.copy())
#                 return 
#             for i in range(len(nums)):
#                 if not used[i]:
#                     if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
#                         continue
#                     used[i] = 1
#                     path.append(nums[i])
#                     backtracking(nums, used, path)
#                     path.pop() # 回溯
#                     used[i] = 0

#         backtracking(sorted(nums), used, [])
#         return res

# # 力扣加加
# class Solution:
#     def permuteUnique(self, nums):
#         # 排序方便去重
#         nums.sort()
#         res = []
#         def backtracking(nums, pre_list):
#             if len(nums) <= 0:
#                 res.append(pre_list)
#             else:
#                 for i in range(len(nums)):
#                     if i > 0 and nums[i] == nums[i-1]:
#                         continue
#                     p_list = pre_list.copy()
#                     p_list.append(nums[i])
#                     left_nums = nums.copy()
#                     left_nums.pop(i)
#                     backtracking(left_nums, p_list)
#         backtracking(nums, [])
#         return res

# # 力扣高赞
# class Solution:
#     def permuteUnique(self, nums):
#         nums.sort()
#         self.res = []
#         # check作为校验位，相应位置元素为0则表示被使用过
#         check = [0 for i in range(len(nums))]
#         self.backtracking(nums, [], check)
#         return self.res

#     def backtracking(self, nums, current, check):
#         if len(current) == len(nums):
#             self.res.append(current)
#             return
#         for i in range(len(nums)):
#             if check[i] == 1:
#                 continue
#             if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
#                 continue
#             check[i] = 1
#             self.backtracking(nums, current+[nums[i]], check)
#             check[i] = 0

# 

if __name__ == '__main__':
    nums = [1,1,2]
    result = Solution().permuteUnique(nums)
    print(result)