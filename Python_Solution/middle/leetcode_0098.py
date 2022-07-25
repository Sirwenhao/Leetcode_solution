"""
    1、验证二叉搜索树
    2、二叉搜索树的定义：左子树节点的值均小于当前节点，柚子树结点的值均大于当前节点，左右子树自身也都是二叉搜索树
"""
# 2022/7/25  author:WH
# 考察二叉树的中序遍历，额外增加了一个对节点值进行判断的条件而已
# 二叉树中序遍历，迭代写法
class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur:
                stack.append(cur) # 左
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val <= pre.val: return False
                pre = cur
                cur = cur.right # 右
        return True

        
# 二叉树中序遍历，递归写法
class Solution:
    def isValidBST(self, root):
        def dfs(root):
            if not root: return True
            if not dfs(root.left): return False
            if prev >= root.val: return False
            prev = root.val
            if not dfs(root.right): return False
            return True

        prev = float('-inf')
        return dfs(root)
