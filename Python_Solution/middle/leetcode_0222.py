"""
    1、统计完全二叉树的节点个数
    2、完全二叉树是指除了最后一层每一层的节点个数都满，最后一层节点个数在1到2^k-1(k为对应二叉树的层数)个之间
"""
# 2022/7/22  author:WH
# 迭代版本，直接AC
class Solution:
    def countNode(self, root):
        if not root: return 0
        ans = 0
        que = deque([root])
        while que:
            # 用于记录每一层的节点总数
            result = 0
            for _ in range(len(que)):
                node = que.popleft()
                result += 1
                if node.left: que.append(node.left)
                if node.right: que.append(node.left)
            print(result)
            ans += result
        return ans

# 2022/7/22  author:代码随想录
# 递归解法
class Solution:
    def countNode(self, root):
        return self.getNodeNum(root)
    
    def getNodeNum(self, cur):
        if not cur: return 0
        leftNum = self.getNodeNum(cur.left)  # 左
        rightNum = self.getNodeNum(cur.right) # 右
        totalNum = leftNum + rightNum + 1 # 中
        return totalNum