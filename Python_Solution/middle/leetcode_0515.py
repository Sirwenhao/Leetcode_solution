"""
    1、二叉树专题：在每个树行中找出最大值
    2、二叉树层序遍历的变形
"""
# 2022/7/20  author:WH
class Solution:
    def largestValues(self, root):
        if not root: return []
        ans = []
        que = deque([root])
        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(max(result))
        return ans