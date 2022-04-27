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