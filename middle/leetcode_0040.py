"""
    1、回溯法典型
    2、数字不重复
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        与39题的区别是不能重用元素，而元素可能有重复
        不能重用好解决，回溯的index往下一个就行；
        元素可能有重复，就让结果的去重蛮烦一些
        """
        size = len(candidates)
        if size == 0:
            return []

        # 先排序
        candidates.sort()
        path = []
        res = []
        self._find_path(candidates, path, res, target, 0, size)
        return res

    def _find_path(self, candidates, path, res, target, begin, size):
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                if left_num < 0:
                    break
                # 如果存在重复的元素，前一个元素已经遍历的后一个元素与之后元素组合的所有可能
                if i > begin and candidates[i]  == candidates[i-1]:
                    continue
                path.append(candidates[i])
                # 开始的index往后移一格
                self._find_path(candidates, path, res, left_num, i+1, size)
                path.pop()