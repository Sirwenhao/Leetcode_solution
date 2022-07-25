"""
    1、从前序与中序遍历构造二叉树
"""
# 2022/7/25  author:WH
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder: return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        separator_idx = inorder.index(root.val)

        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1:]

        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_right):]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
    