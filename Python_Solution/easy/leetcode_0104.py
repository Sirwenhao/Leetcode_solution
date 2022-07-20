"""
    1、二叉树的最大深度
"""
# class Solution:
#     def maxDepth(self, root):
#         if not root: return 0
#         q, depth = [root, None], 1
#         while q:
#             node = q.pop(0)
#             if node:
#                 if node.left: q.append(node.left)
#                 if node.right: q.append(node.right)
#             elif q:
#                 q.append(None)
#                 depth += 1
#             return depth

# 2022/7/20  author:WH
class Solution:
    def maxDepth(self, root):
        ans = 0
        if not root: return 0
        que = root
        while que.left or que.right:
            ans += 1
        return ans+1
