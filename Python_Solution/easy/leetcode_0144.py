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

# class Solution:
#     def preorderTraversal(self, root):
#         result = []
#         def traversal(root):
#             if root == None:
#                 return
#             result.append(root.val) # 中
#             traversal.append(root.left) # 左
#             traversal.append(root.right) # 右
#         traversal(root)
#         return result


# 2022/7/18  author:WH
# 迭代法  前序：中左右
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            # 中
            ans.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入站
            if node.left:
                stack.append(node.left)
        return ans