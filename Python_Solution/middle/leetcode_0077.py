"""
    1、回溯法典型问题：组合问题
    2、k代表数字长度，n代表数字范围上限
"""   

# class Solution:
#     def combine(self, n, k):
#         nums = [i+1 for i in range(n)]
#         ans = []
#         current = []
#         start_index = 0
#         def backtracking(nums, start_index):
#             if len(current) == k:
#                 ans.append(current[:])
#             for i in range(start_index, len(nums)):
#                 current.append(nums[i])
#                 start_index += 1
#                 backtracking(nums, start_index)
#                 current.pop()
#         backtracking(nums, start_index)
#         return ans

# # 2022/5/21 author:WH
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []

#     def combine(self, n, k):
#         self.ans.clear()
#         self.current.clear()
#         self.backtracking(n, k, 1)
#         return self.ans

#     def backtracking(self, n, k, start_index):
#         if len(self.current) == k:
#             self.ans.append(self.current[:])
#             return

#         for i in range(start_index, n+1):
#             self.current.append(i)
#             self.backtracking(n, k, i+1)
#             self.current.pop()

# 剪枝优化的版本
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def combine(self, n, k):
        self.ans.clear()
        self.current.clear()
        self.backtracking(n, k, 1)
        return self.ans

    def backtracking(self, n, k, start_index):
        if len(self.current) == k:
            self.ans.append(self.current[:])
            return

        for i in range(start_index, n-(k-len(self.current))+2):
            self.current.append(i)
            self.backtracking(n, k, i+1)
            self.current.pop()     

if __name__ == "__main__":
    n = 4
    k = 2
    result = Solution().combine(n, k)
    print(result)