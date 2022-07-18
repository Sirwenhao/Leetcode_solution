"""
    1、二叉树的后序遍历
    2、后序遍历顺序：左右中
"""
# 2022/7/18  author:WH
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def postorderTraversal(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left) # 左
            traversal(root.right) # 右
            ans.append(root.val) # 中
        traversal(root)
        return ans