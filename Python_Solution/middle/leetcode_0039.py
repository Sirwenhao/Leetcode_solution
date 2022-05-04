"""
    1、目标数据给定，组合数据个数不确定
    2、回溯法（还没有搞清楚这个方法的核心思想）
    3、回溯法模板：

    res = []
    def backtrack(路径， 选择列表):
        if 满足结束条件:
            res.append(路径)
            return
        
    for 选择 in 选择列表:
        做选择
        backtrack(路径，选择列表)
        撤销选择
"""
# 回溯法专题习题一
# class Solution:
#     def combinationsSum(self, candidates, target):
#         """
#         回溯法，层层递减，得到符合条件的路径就加入到结果中，超出则剪枝
#         主要是要注意一些细节，避免重复等
#         """
#         size = len(candidates)
#         if size <= 0:
#             return []
#         # 先排序，便于后面剪枝
#         candidates.sort()
#         path = []
#         res = []
#         self._find_path(target, path, res, candidates, 0, size)
#         return res

#     def _find_path(self, target, path, res, candidates, begin, size):
#         """沿着路径往下走"""
#         if target == 0:
#             res.append(path.copy())  # .copy()的使用方法涉及到深浅拷贝
#         else:
#             for i in range(begin, size):
#                 left_num = target - candidates[i]
#                 # 如果剩余值为负数，说明超过了，剪枝
#                 if left_num < 0:
#                     break
#                 # 否则把当前值加入路径
#                 path.append(candidates[i])
#                 # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除
#                 # 因为根据他们得到的解一定在之前就找到过了
#                 self._find_path(left_num, path, res, candidates, i, size)
#                 # 记得把当前值移出路径才能进入下一个值的路径
#                 path.pop()


# # 代码随想录教程
# class Solution:
#     # 定义两个全局变量用于存放结果集和符合条件的结果
#     def __init__(self):
#         self.path = []
#         self.paths = []

#     def combinationsSum(self, candidates, target):
#         self.path.clear()
#         self.paths.clear()
#         self.backtracking(candidates, target, 0, 0)
#         return self.paths

#     def backtracking(self, candidates, target, sum, start_index):
#         # 基础情况
#         if sum == target:
#             self.paths.append(self.path[:]) # 因为是浅拷贝，所以不能直接传入self.path
#             return
#         if sum > target:
#             return

#         # 单层递归逻辑
#         for i in range(start_index, len(candidates)):
#             sum += candidates[i]
#             self.path.append(candidates[i])
#             self.backtracking(candidates, target, sum, i)
#             sum -= candidates[i] # 回溯
#             self.path.pop() # 回溯

# 回溯加剪枝


class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationsSum(self, candidates, target):
        self.path.clear()
        self.paths.clear()

        # 为了剪枝需要提前进行排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target, sum, start_index):
        # 基本情况
        if sum == target:
            self.paths.append(self.path[:])
            return
        # 此处与非剪枝版本有区别
        # 如果本层sum + candidates[i] > target,就提前结束遍历，剪枝
        for i in range(start_index, len(candidates)):
            if sum + candidates[i] > target:
                return
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum, i)
            sum -= candidates[i]
            self.path.pop()
        


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    result = Solution().combinationsSum(candidates, target)
    print(result)