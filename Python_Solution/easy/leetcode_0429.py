
"""
    1、二叉树问题，头疼
"""

# leetcode官解，对树这种数据结构还是不熟悉

from collections import deque

def levelOrder(root):
    if not root:
        return []
    ans = list()
    q = deque([root])
    
    while q:
        cnt = len(q)
        level = list()
        for _ in range(cnt):
            cur = q.popleft()
            level.append(cur.val)
            for child in cur.children:
                q.append(level)
        ans.append(level)
    return ans
>>>>>>> 01c7d28b36c2a0d6850f76944563b6ce436cd214
