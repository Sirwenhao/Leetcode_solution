"""
    1、简单题，想法从中间分开往两边查找
    2、关键点在于搞清楚内部逻辑
"""

# # 力扣加加
# def isSymmetric(root):
#     def dfs(root1, root2):
#         if root1 == root2 == None: return True
#         if not root1 and not root2: return False
#         if root1.val != root2.val: return False
#         return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
#     if not root: return True
#     return dfs(root.left, root.right)


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

# 2022/7/21  author:WH
class Solution:
    def isSymmetric(self, root):
        if not root: return False
        que = deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            leftNode = que.popleft()
            rightNode = que.popright()
            if not leftNode and not rightNode: continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val: return False
            que.append(leftNode.left)
            que.append(rightNode.right)
            que.append(leftNode.right)
            que.append(rightNode.left)
        return True

# 2022/7/21  author:WH
# 逻辑性强，步骤清晰
class Solution:
    def isSymmetric(self, root):
        if not root: return False
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        elif left.val != right.val: return False

        # 递归调用自己的那一步，上述的操作是为了确保调用之前左右节点都不为空，数值相同
        outside = self.compare(left.left, right.right) # 判断外侧节点
        inside = self.compare(left.right, right.left) # 判断内侧节点
        isSmae = outside and inside
        return isSmae