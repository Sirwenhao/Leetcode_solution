"""
    1、打家劫舍III
    2、python中的缓存释放@cache
    3、上述命令的google解释：What is @cache in Python?
    Caching is one approach that, when used correctly, 
    makes things much faster while decreasing the load on computing resources. 
    Python's functools module comes with the @lru_cache decorator, 
    which gives you the ability to cache the result of your functions using the Least Recently Used (LRU) strategy.
    """

# 2022/7/26  author:github
# 递归
from functools import cache


class Solution:
    def rob(self, root):
        @cache
        def dfs(root):
            if not root: return 0
            if root.left is None and root.right is None: return root.val
            a = dfs(root.left) + dfs(root.right)
            b = root.val
            if root.left:
                # 不能是相邻的两个节点
                b += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                b += dfs(root.right.left) + dfs(root.right.right)
            return max(a, b)
        return dfs(root)
