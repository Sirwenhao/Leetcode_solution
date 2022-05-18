"""
    1、回溯法典型问题：组合问题
    2、k代表数字长度，n代表数字范围上限
"""   

class Solution:
    def combine(self, n, k):
        nums = [i+1 for i in range(n)]
        ans = []
        current = []
        start_index = 0
        def backtracking(nums, start_index):
            if len(current) == k:
                ans.append(current[:])
            for i in range(start_index, len(nums)):
                current.append(nums[i])
                start_index += 1
                backtracking(nums, start_index)
                current.pop()
        backtracking(nums, start_index)
        return ans


if __name__ == "__main__":
    n = 4
    k = 2
    result = Solution().combine(n, k)
    print(result)