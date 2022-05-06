"""
    1、子集问题，从一个大的集合中找到满足条件的子集合的数目
"""
# 自己写，尝试使用回溯法解决
# 可以解决，但提交到leetcode时显示超过了最大递归深度，报错
# class Solution:
#     def __init__(self):
#         self.ans = []  # 定义一个空的列表作为结果集
#         self.path = []  # 定义一个当前列表

#     def numSubarrayProductLessThanK(self, nums, k):
#         self.ans.clear()
#         self.path.clear()
#         # 先排序方便剪枝
#         nums.sort()
#         self.backtracking(nums, k, 0)

#         # 去除嵌套列表中的重复部分
#         res = []
#         for val in self.ans:
#             if val not in res:
#                 res.append(val)
#         return res

#     # 定义回溯法函数结构体
#     def backtracking(self, nums, k, start_index):
#         # base case
#         if start_index == len(nums):
#             self.ans += self.path[:]
#             return

#         # 单层递归逻辑
#         for i in range(start_index, len(nums)):
#             # 判断当前的量是否满足条件
#             current = nums[start_index:i+1]
#             num = 1
#             for j in range(len(current)):
#                 num *= current[j]
#             if num < k:
#                 self.path.append(current)
#                 self.backtracking(nums, k, i+1)
#                 self.path.pop()
#             else:
#                 continue

# 自己写的双层循环遍历，但是结果集有重复解，待优化
# class Solution:
#     def numSubarrayProductLessThanK(self, nums, k):
#         # 基础判断
#         if k == 0:
#             return 0

#         # 先排序方便处理
#         nums.sort()
#         ans = [] # 作为结果集，存放结果
#         current = [] # 存放当前情况数据以便判断

#         def isOk(lst):
#             num = 1
#             for i in lst:
#                 num *= i
#             return num
            
#         for start_index in range(len(nums)): # 外层循环遍历寻找符合条件的起始位置
#             current.clear()
#             current.append(nums[start_index])
#             if isOk(current) < k:
#                 ans.append(current[:])
#             else:
#                 current.pop()
#             for current_index in range(start_index+1, len(nums)): # 内层循环对剩余列表元素进行判断
#                 if nums[current_index] * isOk(current) < k:
#                     current.append(nums[current_index])
#                     ans.append(current[:])
#         return ans
                    

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0:
            return 0
        ans, s, j = 0, 1, 0
        for i, v in enumerate(nums):
            s *= v
            while s >= k and j <= i:
                s //= nums[i]
                j += 1
            ans += i-j+1
        return ans
                

if __name__ == '__main__':
    nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3] # 像这种含有重复元素的会出现重复计数的情况
    k = 19
    result = Solution().numSubarrayProductLessThanK(nums, k)
    print(result)
    # print(len(result))

   

# # test 一行代码解决求一个列表中所有元素的乘积
# lst = [1,2,3,4,5]
# num = 1
# for i in range(len(lst)):
#     num *= lst[i]
# print(num)
# res = [[2], [5], [6], [10], [2], [5], [6, 10], [2], [5, 6], [10], [2, 5], [6], [10], [2, 5], [6, 10], [2, 5, 6], [10]]
# # res1 = res.remove[i if res.count(i) > 1]
# for i in res:
#     if res.count(i) > 1:
#         res.remove(i) 
# print(res)