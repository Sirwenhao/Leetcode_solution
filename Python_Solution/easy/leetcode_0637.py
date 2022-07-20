"""
    1、二叉树的层平均值
    2、层序遍历，并求出每一层的节点值的均值
"""
# 2022/7/20  author:WH
class Solution:
    def averageOfLevels(self, root):
        if not root: return []
        que = deque([root])
        ans = []
        while que:
            size = len(que)
            sum = 0
            for _ in range(size):
                cur = que.popleft()
                sum += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.eight)
            ans.append(sum / size)
        return ans