"""
    1、回溯专题
    2、递增子序列
"""
# 这个解答方法是错误的，首先不能对原数组进行排序，其递增子序列是在原数组的基础上进行查找的
# # 递增子序列所有情况
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current =[]
    
#     def findSubsequences(self, nums):
#         nums.sort()
#         self.ans.clear()
#         self.current.clear()
#         # 递增子序列最少包含两个元素，把起始位置设置为1，便于添加元素
#         self.backtracking(nums, 0)
#         return self.ans

#     def backtracking(self, nums, start_index):
#         if len(self.current) >= 2:
#             self.ans.append(self.current[:])
#             return

#         for i in range(start_index, len(nums)):

#             self.current.append(nums[i])
#             self.backtracking(nums, i+1)
#             self.current.pop()
        
# # 代码随想录解法
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []

#     def findSubsequences(self, nums):
#         self.backtracking(nums, 0)
#         return self.ans

#     def backtracking(self, nums, start_index):
#         if len(self.current) >= 2:
#             self.ans.append(self.current[:])
            
#         if start_index == len(nums):
#             return

#         usedList = set()
#         for i in range(start_index, len(nums)):
#             if (self.current and nums[i] < self.current[-1]) or nums[i] in usedList:
#                 continue
#             usedList.add(nums[i])
#             self.current.append(nums[i])
#             self.backtracking(nums, i+1)
#             self.current.pop()

# 2022/05/29  author:WH
# 此版本的答案有重复解，会出现重复集合，需要去重
# 这个版本的解也有问题，力扣提交不能通过
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []

#     def findSubsequences(self, nums):
#         self.ans.clear()
#         self.current.clear()
#         self.backtracking(nums, 0)
#         return self.ans

#     def backtracking(self, nums, start_index):
#         if len(self.current) >= 2:
#             self.ans.append(self.current[:])
#         if start_index == len(nums):
#             return

#         for i in range(start_index, len(nums)):
#             # 去重，去掉重复使用的重复出现的元素
#             if i > start_index and nums[i] == nums[i-1]:
#                 continue
#             self.current.append(nums[i])
#             self.backtracking(nums, i+1)
#             self.current.pop()

class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def findSubsequences(self, nums):
        self.ans.clear()
        self.current.clear()
        self.backtracking(nums, 0)
        return self.ans
    
    def backtracking(self, nums, start_index):
        if len(self.current) >= 2:
            self.ans.append(self.current[:])

        if len(self.current) == len(nums):
            return
        
        usedList = set()
        for i in range(start_index, len(nums)):
            if (self.current and nums[i] < self.current[-1]) or nums[i] in usedList:
                continue
            usedList.add(nums[i])
            self.current.append(nums[i])
            self.backtracking(nums, i+1)
            self.current.pop()

if __name__ == "__main__":
    nums = [4,7,6,7]
    result = Solution().findSubsequences(nums)
    print(result)