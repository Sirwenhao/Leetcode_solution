"""
    1、二叉树的所有路径
"""
# 2022/7/24  author:WH
class Solution:
    def binaryTreePaths(self, root):
        stack, path_st, result = deque([root]), deque(), []
        path_st.append(str(root.val))

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            if not (cur.left or cur.right): result.append(path)
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
        return result