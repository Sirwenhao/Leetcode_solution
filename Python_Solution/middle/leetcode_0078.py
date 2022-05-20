"""
    1、不含重复元素的数组nums，返回其所有可能的子集
    2、子集问题1
"""

class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def subsets(self, nums):
        # 首先先排序
        nums.sort()
        self.ans.clear()
        self.current.clear()
        self.backtracking(nums, 0)
        return self.ans

    # 定义回溯函数结构体
    # 子集问题不需要剪枝
    def backtracking(self, nums, start_index):
        self.ans.append(self.current[:])
        # 此处递归的终止条件没有想到
        if start_index == len(nums):
            return
        
        for i in range(start_index, len(nums)):
            self.current.append(nums[i])
            self.backtracking(nums, i+1)
            self.current.pop()

if __name__ == "__main__":
    nums = [1,2,3]
    result = Solution().subsets(nums)
    print(result)