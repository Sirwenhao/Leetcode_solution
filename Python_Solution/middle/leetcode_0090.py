"""
    1、给定一个可能包含重复元素的整数数组，返回其所有可能的子集
    2、子集问题2
"""
# 与子集问题1不同，此问题的原始整数数组是包含重复数字的
# 遇到重复元素需要考虑跳过
# 回溯不使用标记
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def subsetsWithDup(self, nums):
        nums.sort()
        self.ans.clear()
        self.current.clear()
        self.backtracking(nums, 0)
        return self.ans

    def backtracking(self, nums, start_index):
        self.ans.append(self.current[:])
        if start_index == len(nums):
            return
        
        # 定义单层循环
        for i in range(start_index, len(nums)):
            # 添加一个判断，如果nums[i]已经存在直接跳过
            # 这个地方对于重复元素的剪枝还是没有搞明白
            # 在leetcode_0040中有讲述过去重的情况，请返回参考
            # 这个地方的去重涉及到"树层去重"和"树枝去重"
            if nums[i] == nums[i-1] and i > start_index:
                continue
            self.current.append(nums[i])
            self.backtracking(nums, i+1)
            self.current.pop()
    

if __name__ == "__main__":
    nums = [1,2,2]
    result = Solution().subsetsWithDup(nums)
    print(result)
