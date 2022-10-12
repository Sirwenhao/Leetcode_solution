# 二叉树的遍历
# 前、中、后续三种遍历顺序；递归和迭代两种递归写法

# 二叉树遍历的递归写法

# 递归——前序

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def preorderTraverse(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            ans.append(root.value)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return ans

# 递归——中序
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def inorderTraversal(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            ans.append(root.left)
            traversal(root.value)
            traversal(root.right)
        traversal(root)
        return ans

# 递归——后序
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            ans.append(root.left)
            traversal(root.right)
            traversal(root.value)
        traversal(root)
        return ans
        

# 迭代——前序
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


# 迭代——中序
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
