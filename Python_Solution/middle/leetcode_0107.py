"""
    1、二叉树的层序遍历
    2、递归解法和迭代解法
    3、所谓层序遍历就是每一层从左到右依次遍历
"""
# 2022/7/19  author:WH
# 递归解法

# leetcode二叉树在编译器的本地调试
# 定义二叉树的节点

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# 定义列表转换为树的模块
def List2Tree(l):
    q = []
    if not l:
        return
    root = TreeNode(val=l.pop(0))
    q.append(root)
    while q:
        t = q.pop(0)
        if l:
            if l[0] != 'null':
                t.left = TreeNode(val=l.pop(0))
                q.append(t.left)
            else:
                l.pop(0)
        if l:
            if l[0] == 'null':
                t.right = TreeNode(val=l.pop(0))
                q.append(t.right)
            else:
                l.pop(0)
    return root

class Solution:
    def levelOrder(self, root):
        ans = []
        def helper(root, depth):
            if not root: return []
            if len(ans) == depth: ans.append([])
            print(ans)
            ans[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)
        helper(root, 0)
        return ans

# class Solution:
#     def levelOrder(self, root):
#         ans = []
#         if not root:
#             return []
#         from collections import deque
#         que = deque([root])
#         while que:
#             size = len(que)
#             result = []
#             for _ in range(size):
#                 cur = que.popleft()
#                 result.append(cur.val)
#                 if cur.left:
#                    que.append(cur.left)
#                 if cur.right:
#                     que.append(cur.right)
#             ans.append(result)
#         return ans


if __name__ == "__main__":
    root = List2Tree([3, 9, 20, 'null', 'null', 15, 7])
    result = Solution().levelOrder(root)
    print(result)