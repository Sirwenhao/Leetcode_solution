"""
    1、不含重复元素的数组nums，返回其所有可能的子集
    2、子集问题1
"""

# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []

#     def subsets(self, nums):
#         # 首先先排序
#         nums.sort()
#         self.ans.clear()
#         self.current.clear()
#         self.backtracking(nums, 0)
#         return self.ans

#     # 定义回溯函数结构体
#     # 子集问题不需要剪枝
#     def backtracking(self, nums, start_index):
#         self.ans.append(self.current[:])
#         # 此处递归的终止条件没有想到
#         if start_index == len(nums):
#             return
        
#         for i in range(start_index, len(nums)):
#             self.current.append(nums[i])
#             self.backtracking(nums, i+1)
#             self.current.pop()

# 2022/11/30  author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def subsets(self, nums):
        self.ans.clear()
        self.current.clear()
        nums.sort()
        self.backtracking(nums, 0)
        return self.ans

    def backtracking(self, nums, start_index):
        # 此处没有考虑清楚终止条件
        # if len(self.current) <= len(nums):
        #     self.ans.append(self.current[:])
        #     return
        # # 去重
        # if self.current in self.ans:
        #     continue
        # 想到了终止条件是剩余子集为空，但没想到start_index > len(nums)
        # 其实不用加终止条件也可以，因为默认的终止条件就是start_index > len(nums)结束
        self.ans.append(self.current[:])

        for i in range(start_index, len(nums)):
            self.current.append(nums[i])
            self.backtracking(nums, i+1)
            self.current.pop()



if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().subsets(nums)
    print(result)