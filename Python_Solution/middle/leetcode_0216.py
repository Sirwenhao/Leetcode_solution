"""
    1、回溯专题，组合总和III
    2、数字范围1~9，总和为n,数字个数为k
"""

# 2022/5/22  author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def combinationSum3(self, k, n):
        self.ans.clear()
        self.current.clear()
        self.backtracking(k, n, 1)
        return self.ans

    def backtracking(self, k, n, start_index):
        if len(self.current) == k and sum(self.current) == n:
            self.ans.append(self.current[:])
            return
        
        for i in range(start_index, 10):
            # 剪枝
            if sum(self.current) > n:
                return

            self.current.append(i)
            self.backtracking(k, n, i+1) # 树枝元素不能重复使用
            self.current.pop()

if __name__ == "__main__":
    k = 3
    n = 9
    result = Solution().combinationSum3(k, n)
    print(result)

