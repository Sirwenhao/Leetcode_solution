"""
    1、简单题，想法从中间分开往两边查找
"""

# def isSymmetric(root):
#     l = len(root)
#     middle_point = int(l // 2) + 1
#     for i, j in zip(range(0, middle_point), range(l - 1, middle_point, -1)):
#         if root[i] == root[j]:
#             return True
#         else:
#             continue

#     return


# 2022/4/3 复习

def isSymmetric(root):
    if not root:
        return True
    def dfs(left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)

root = [1,2,3,2,2]

result = isSymmetric(root)
print(result)