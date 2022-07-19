"""
    1、二叉树的右视图
    2、二叉树层序遍历相关
"""
# 2022/7/19  author:WH
class Solution:
    def rightSideView(self, root):
        if not root: return []
        queue = deque([root])
        ans = []
        # 'from collections import deque' 导入
        # deque相比list的好处是，list的pop(0)是O(n)复杂度，deque的popleft()是O(1)复杂度
        while queue:
            node = queue[-1]
            ans.append(node.val)

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans