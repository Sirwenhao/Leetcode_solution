"""
    1、二叉树中序遍历
    2、中序遍历顺序：左中右
"""
# 2022/7/18  author:WH
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# class Solution:
#     def inorderTraversal(self, root):
#         ans = []
#         def traversal(root):
#             if root == None:
#                 return
#             traversal(root.left)
#             ans.append(root.val)
#             traversal(root.right)
#         traversal(root)
#         return ans

# 2022/7/18  author:WH
# 迭代法
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        ans = []
        stack = []
        cur = root
        while cur or stack:
            # 访问左子树的最底层节点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 处理完最左子树之后，处理栈顶节点
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans