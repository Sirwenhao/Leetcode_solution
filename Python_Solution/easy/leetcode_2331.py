# 2023/2/6  author:WH
# 核心方法是递归

# leetcode官解
class Solution:
    def evaluateTree(self, root):
        # 如果当前节点为叶子节点，则返回其值。
        if root.left is None:
            return root.val == 1 # 也可以使用return bool(root.val)可以将0和1两种取值情况都包含
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)

# 解法二：github
class Soluton:
    def evaluateTree(self, root):
        if root.left is None:
            return bool(root.val)
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        return l or r if root.val == 2 else l and r
