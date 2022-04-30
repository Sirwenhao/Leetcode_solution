"""
    1、简单题，想法从中间分开往两边查找
"""

# 力扣加加
def isSymmetric(root):
    def dfs(root1, root2):
        if root1 == root2 == None: return True
        if not root1 and not root2: return False
        if root1.val != root2.val: return False
        return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
    if not root: return True
    return dfs(root.left, root.right)


# # 2022/4/3 复习

# def isSymmetric(root):
#     if not root:
#         return True
#     def dfs(left, right):
#         if not (left or right):
#             return True
#         if not (left and right):
#             return False
#         if left.val != right.val:
#             return False
#         return dfs(left.left, right.right) and dfs(left.right, right.left)

#     return dfs(root.left, root.right)
