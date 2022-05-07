"""
    1、回溯法典型
    2、数字不重复
"""
# # 力扣加加
# class Solution:
#     def combinationSum2(self, candidates, target):
#         """
#         与39题的区别是不能重用元素，而元素可能有重复
#         不能重用好解决，回溯的index往下一个就行；
#         元素可能有重复，就让结果的去重麻烦一些
#         """
#         size = len(candidates)
#         if size == 0:
#             return []

#         # 先排序
#         candidates.sort()
#         path = []
#         res = []
#         self._find_path(candidates, path, res, target, 0, size)
#         return res

#     def _find_path(self, candidates, path, res, target, begin, size):
#         if target == 0:
#             res.append(path.copy())
#         else:
#             for i in range(begin, size):
#                 left_num = target - candidates[i]
#                 if left_num < 0:
#                     break
#                 # 如果存在重复的元素，前一个元素已经遍历的后一个元素与之后元素组合的所有可能
#                 if i > begin and candidates[i]  == candidates[i-1]:
#                     continue
#                 path.append(candidates[i])
#                 # 开始的index往后移一格
#                 self._find_path(candidates, path, res, left_num, i+1, size)
#                 path.pop()


# 2022/5/7 0:12 Author:WH 回溯
class Solution:
    def __init__(self):
        self.ans = []  # 用于存放结果集
        self.current = []  # 用于考虑当前情况

    def combinationSum2(self, candidates, target):
        self.ans.clear()
        self.current.clear()
        # 排序这个关键步骤不能少
        candidates.sort()
        self.backtracking(candidates, target, 1)
        return self.ans

    # 定义回溯部分主体
    def backtracking(self, candidates, target, start_index):
        # base condition
        if start_index == len(candidates):
            self.ans.append(self.current[:])  # 此处用浅拷贝
            return # 这个return语句被我遗忘了

        for i in range(len(candidates)):
            self.current.append(candidates[i])
            if sum(self.current) == target:
                self.ans += self.current
            self.backtracking(candidates, target, start_index+1)
            self.current.pop()
            


if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    result = Solution().combinationSum2(candidates, target)
    print(result)
