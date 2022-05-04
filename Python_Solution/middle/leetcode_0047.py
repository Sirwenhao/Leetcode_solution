"""
    1、回溯专题
"""

class Solution:
    def permuteUnique(self, nums):
        # 结果不能重复则考虑使用集合来存放
        ans = {}
        def dfs():
