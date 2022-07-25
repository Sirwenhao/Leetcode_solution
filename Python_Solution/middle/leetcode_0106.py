"""
    1、从中序与后序遍历序列构造二叉树
"""
# 2022/7/25  author:WH
class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder: return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        separator_idx = inorder.index(root_val)

        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1:]

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder) - 1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root