"""
    1、二叉树的最大深度
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q, depth = [root, None], 1
        while q:
            node = q.pop(0)
            if node:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            elif q:
                q.append(None)
                depth += 1
            return depth

