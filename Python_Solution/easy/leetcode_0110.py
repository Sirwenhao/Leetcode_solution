"""
    1、平衡二叉树
    2、高度平衡二叉树的定义：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1
    3、Python字典的.get()方法
"""
# 2022/7/23  author:代码随想录

class Solution:
    def isBalanced(self, root):
        if not root: return True
        height_map = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            else:
                real_node = stack.pop()
                left, right = height_map.get(real_node.left, 0), height_map(real_node.right, 0)
                if abs(left - right) > 1: return False
                height_map[real_node] = 1 + max(left, right)
        return True

# 2022/7/23  author:WH
class Solution:
    def isBalanced(self, root):
        if self.get_height(root) != -1: return True
        else: return False

    def get_height(self, root):
        if not root: return 0
        if (left_height == self.get_height(root.left)) == -1: return -1
        if (right_height == self.get_height(root.right)) == -1: return -1
        if abs(left_height - right_height) > 1: return -1
        else: return 1 + max(left_height, right_height)



# dict = {
#     "a": "1",
#     "b": "2",
#     "c": "4",
#     }

# print(dict.get('a'))
# print(dict.get('e', 10))
# print(dict)