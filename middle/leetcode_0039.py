"""
    1、目标数据给定，组合数据个数不确定
    2、回溯法（还没有搞清楚这个方法的核心思想）
"""

class Solution:
    def combinationsSum(self, candidates, target):
        """
        回溯法，层层递减，得到符合条件的路径就加入到结果中，超出则剪枝
        主要是要注意一些细节，避免重复等
        """
        size = len(candidates)
        if size <= 0:
            return []

        # 先排序，便于后面剪枝
        candidates.sort()

        path = []
        res = []
        self._find_path(self, target, path, res, candidates, 0, size)
        return res

    def _find_path(self, target, path, res, candidates, begin, size):
        """沿着路径往下走"""
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates
                # 如果剩余值为负数，说明超过了，剪枝
                if left_num < 0:
                    break
                # 否则把当前值加入路径
                path.append(candidates[i])
                # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除
                # 因为根据他们得到的解一定在之前就找到过了
                self._find_path(left_num, path, res, candidates, i, size)
                # 记得把当前值移出路径才能进入下一个值的路径
                path.pop()


