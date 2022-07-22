"""
    1、合并二叉树
"""
# 2022/7/22  author:WH
class Solution:
    def mergeTrees(self, root1, root2):
        return self.addTrees(root1, root2)

    def addTrees(self, tree1, tree2):
        if not tree1: return tree2
        if not tree2: return tree1
        que1 = deque([tree1])
        que2 = deque([tree2])
        while que1 or que2:
            node1 = que1.popleft()
            node2 = que2.popleft()
            if node1.left and node2.left:
                que1.append(node1.left)
                que2.append(node2.left)
            if node1.right and node2.right:
                que1.append(node1.right)
                que2.append(node2.right)
            node1.val += node2.val
            # 这一步是没有想到的，如果tree1为空则需要tree2补充
            if not node1.left and node2.left: node1.left = node2.left
            if not node1.right and node2.right: node1.right = node2.right
        return tree1


# 代码随想录解法
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1: 
            return root2
        if not root2: 
            return root1

        queue = deque()
        queue.append(root1)
        queue.append(root2)

        while queue: 
            node1 = queue.popleft()
            node2 = queue.popleft()
            # 更新queue
            # 只有两个节点都有左节点时, 再往queue里面放.
            if node1.left and node2.left: 
                queue.append(node1.left)
                queue.append(node2.left)
            # 只有两个节点都有右节点时, 再往queue里面放.
            if node1.right and node2.right: 
                queue.append(node1.right)
                queue.append(node2.right)

            # 更新当前节点. 同时改变当前节点的左右孩子. 
            node1.val += node2.val
            if not node1.left and node2.left: 
                node1.left = node2.left
            if not node1.right and node2.right: 
                node1.right = node2.right

        return root1