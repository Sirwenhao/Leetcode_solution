"""
    1、二叉树的前序遍历
    2、主要问题在于递归函数的写法
    3、前序遍历的顺序中左右
"""
# 2022/7/18  author:WH
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        result = []
        def traversal(root):
            if root == None:
                return
            result.append(root.val) # 中
            traversal.append(root.left) # 左
            traversal.append(root.right) # 右
        traversal(root)
        return result
