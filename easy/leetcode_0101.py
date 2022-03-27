"""
    1、简单题，想法从中间分开往两边查找
"""


def isSymmetric(root):
    l = len(root)
    middle_point = int(l // 2) + 1
    for i, j in zip(range(0, middle_point), range(l - 1, middle_point, -1)):
        if root[i] == root[j]:
            return True
        else:
            continue

    return

root = [1,2,3,2,2]

result = isSymmetric(root)
print(result)