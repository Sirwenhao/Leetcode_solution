
"""
    1、二叉树问题，头疼
"""

# # leetcode官解，对树这种数据结构还是不熟悉

# from collections import deque

# def levelOrder(root):
#     if not root:
#         return []
#     ans = list()
#     q = deque([root])
    
#     while q:
#         cnt = len(q)
#         level = list()
#         for _ in range(cnt):
#             cur = q.popleft()
#             level.append(cur.val)
#             for child in cur.children:
#                 q.append(level)
#         ans.append(level)
#     return ans

# 2022/7/20  author:WH
# N叉树的层序遍历
class Solution:
    def leverOrder(self, root):
        if not root: return []
        ans = []
        # 把根节点添加进入到deque中，根节点的

        que = deque([root])
        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                if cur.children:
                    que.extend(cur.children)
            ans.append(result)
        return ans