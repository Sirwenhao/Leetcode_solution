"""
    1、翻转二叉树
"""
# 0226翻转二叉树
# 2022/7/21  author:WH
# 前序遍历，递归版本
class Solution:
    def invertTree(self, root):
        if not root: return None
    	root.left, root.right = root.right, root.left
        self.invertTree(root.left) # 左节点
        self.invertTree(root.right) # 右节点
        return root
# 前序遍历，迭代版本
# 深度优先DFS（前序遍历）
class Solution:
    def invertTree(self, root):
        if not root: return None
    	ans = [root]
        while ans:
            node = ans.pop()
            node.left, node.right = node.right, node.left # 中
            if node.left: ans.append(node.left)  # 左
            if node.right: ans.append(node.right) # 右
        return root
    
# 层序遍历，迭代版本
# 广度优先BFS（层序遍历）
from collections import deque
class Solution:
    def invertTree(self, root):
        if not root: return None
    	que = deaue([root])
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                node.left, node.right = node.right, node.left
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
         return root