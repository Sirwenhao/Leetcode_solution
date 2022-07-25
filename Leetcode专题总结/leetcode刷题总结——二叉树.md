## Leetcode刷题总结——二叉树

- 二叉树相关基本知识点
- 二叉树相关leetcode练习题

### 二叉树相关基本知识点

- 节点拥有的子树的数量即为度，度为0的节点即为叶节点或终端节点
- 树的度即树内各节点的度的最大值

#### 二叉树的种类

- 满二叉树
- 完全二叉树
- 二叉搜索树
- 平衡二叉搜索树

满二叉树：即一棵树只有度为0和2的节点，且度为0的节点在同一层，则这棵树称为满二叉树。其深度为k，节点数为$2^k-1$

完全二叉树：（理解相对有难度）在完全二叉树中，除了最底层的节点可能没填满之外，其余每层节点数都达到了最大值，并且最下面一层的节点都集中在该层的最左边若干位置。假设最底层是第i层，则该层对应的节点数为：$1—2^{i-1}$

二叉搜索树（二叉排序树）：节点存储数值，是一种有序树。

- 如左子树不为空，则左子树上所有节点的值均小于它的根节点的值
- 如右子树不为空，则右子树上所有节点的值均大于它的根节点的值
- 它的左右子树分别为二叉搜索树

平衡二叉搜索树，又被称为AVL（Adelson-Velsky and Landis）树，有以下性质：

- 可以是一颗空树
- 非空时，左右两个子树的高度差的绝对值不超过1，并且左右两个子树是一颗平衡二叉树

#### 二叉树的存取方式

- 顺序存储（使用数组），内存中连续分布
- 链式存储（使用指针），通过指针串联，可以不在连续的存储空间上

#### 二叉树的遍历方式

- 深度优先遍历（DFS）：先往深处走，遇到叶子节点再往回退。前序、中序、后序是相对于中间节点的位置而言的
  - 前序遍历（中左右）（递归法，迭代法）
  - 中序遍历（左中右）（递归法，迭代法）
  - 后序遍历（左右中）（递归法，迭代法）
- 广度优先搜索（BFS）：一层一层遍历
  - 层序遍历（迭代法）

#### 二叉树节点的定义

C++版本

```c++
struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
```

Python版本

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### 二叉树相关leetcode习题

按照代码随想录分类

#### 1.二叉树的遍历方式

递归遍历相关：前序、中序、后序

首先写递归算法时，要明确递归结构写法的三要素：

- 确定递归函数的参数和返回值，要搞清楚哪些参数是递归函数要处理的，还要搞明白递归函数的返回值是什么
- 确定递归终止条件，每一次递归的结果使用递归栈结构保存的，终止条件不正确会导致递归栈溢出
- 确定单层递归逻辑，即确定调用自己的那一步的写法

二叉树的前后中序遍历，递归写法

```python
# 2022/7/18  author:WH
# 二叉树前序遍历(递归写法)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class Solution:
    def preorderTraversal(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            ans.append(root.value)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return ans
```

```python
# 2022/7/18  author:WH
# 二叉树中序遍历(递归写法)
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
            traversal(root.left)
            ans.append(root.value)
            traversal(root.right)
        traversal(root)
        return ans
```

```python
# 2022/7/18  author:WH
# 二叉树后续遍历(递归写法)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class Solution:
    def postorderTraversal(self, root):
        ans = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            ans.append(root.value)
        traversal(root)
        return ans
```

二叉树的前后中序遍历，非递归写法

```python
# 2022/7/18  author:WH
# 前序遍历(迭代法)
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop() # 中，先入栈，先出栈
            ans.append(node.value)
            if node.right:
                stack.append(node.right) # 右，先入栈，后出栈
            if node.left:
                stack.append(node.left) # 左，后入栈，先出栈
        return result
```

```python
# 2022/7/18  author:WH
# 中序遍历(迭代法)
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        ans = []
        stack = []
        cur = root
        while stack or root:
            if cur:
                stack.append(cur) # 左
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.value) # 中
                cur = cur.right # 右
        return ans
```

```python
# 2022/7/18  author:WH
# 后序遍历(迭代法)
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop() # 中先入栈，先出栈
            ans.append(node.val)
            if node.left:
                stack.append(node.left) # 左先入栈，后出栈
            if node.right:
                stack.append(node.right) # 右后入栈，先出栈
        return ans[::-1]
```

二叉树的层序遍历

所谓层序遍历一个二叉树，即从左到右一层一层的去遍历。需要借助一个辅助数据结构队列来实现，队列先进先出，符合一层一层遍历的逻辑，这种层序遍历实质上就是图论中的广度优先遍历。

```python
# 2022/7/19  author:WH
# 二叉树层序遍历的递归解法
class Solution:
    def levelOrder(self, root):
        res = []
        def helper(root, depth):
            if not root: return []
        	if len(res) == depth: res.append([])
            res[depth].append(root.val)
            if root.left: helper(root.left, depth + 1)
            if root.right: helper(root.right, depth + 1)
        helper(root, 0)
        return res
```

```python
# 2022/7/19  author:WH
# 二叉树层序遍历的迭代解法
class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(result)
        return ans
```

与二叉树的层序遍历相关的leetcode习题

- 0107二叉树的层次遍历II
- 0199二叉树的右视图
- 0637二叉树的层平均值
- 0429N叉树的层序遍历
- 0515在每个树行中寻找最大值
- 0116填充每个结点的下一个右侧节点指针
- 0117填充每个结点的下一个右侧节点指针II
- 0104二叉树的最大深度
- 0111二叉树的最小深度

```python
# 0107二叉树的层次遍历II
# 2022/7/18  author:WH
class Solution:
    def levelOrderBottom(self, root):
        ans = []
        def helper(root, depth):
            if not root: return
        	if len(ans) == depth: ans.append([])
            ans[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)
        helper(root, 0)
       	return ans[::-1]
```

```python
# 0199二叉树的右视图
# 2022/7/20  author:WH
class Solution:
    def rightSideView(self, root):
        ans = []
        que = deque([root])
        if not root: return []
    	while que:
            cur = que[-1]
            ans.append(cur.val)
            for _ in range(len(que)):
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return ans 
```

```python
# 0637二叉树的树层平均值
# 2022/7/20  author:WH
class Solution:
    def averageOfLevels(self, root):
        if not root: return []
    	ans = []
        que = deque([root])
        while que:
            size = len(que)
            total = 0
            for _ in range(size):
                cur = que.popleft()
            	total += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(total / size)
        return ans         
```

```python
# 0429N叉树的层序遍历
# 2022/7/20  author:WH
class Solution:
    def levelOrder(self, root):
        if not root: return []
    	que = deque([root])
        ans = []
        while que:
            result = []
            for _ in range(len(que)):
            	cur = que.popleft()
            	result.append(cur.val)
                if cur.children:
                    que.extend(cur.children)
            ans.append(result)
        return ans
```

```python
# 0515在每个树行中寻找最大值
# 2022/7/20  author:WH
class Solution:
    def largestValues(self, root):
        if not root: return []
        ans = []
        que = deque([root])
        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(max(result))
        return ans
```

```python
# 0116填充每个结点的下一个右侧节点指针
# 2022/7/20  后期补充~
```

```python
# 0117填充每个结点的下一个右侧节点指针II
# 2022/7/20  后期补充~
```

```python
# 0104二叉树的最大深度
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 2022/7/20  author:WH
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        ans = []
        que = [root]
        while que:
            result = 0
            for _ in range(len(que)):
                # 这个地方必须是pop(0)出最左侧元素
                cur = que.pop(0)
                result.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            ans.append(result)
        return len(ans)
```

```python
# 0111二叉树的最小深度
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量
# 2022/7/20  author:WH
class Solution:
    def minDepth(self, root):
        if not root: return 0
    	que = [(root, 1)]
        while que:
            cur, depth = que.pop(0)
            # 一个节点的左右子节点都不存在，即为叶子节点
            if cur.left == None and cur.right == None: return depth
            if cur.left:
                que.append((cur.left, depth+1))
            if cur.right:
                que.append((cur.right, depth+1))
       return 0
```



翻转二叉树，看似简单，但是要清晰理解其内部的逻辑。反转的原则：交换每一个树节点的左右孩子。其遍历方式可能涉及到前中后序和层序，但中序遍历是不行的。中序遍历的顺序为左中右，在执行中序之前已经进行过左子节点的交换操作了，中序遍历会导致子节点被反转两次。

```python
# 0226翻转二叉树
# 2022/7/21  author:WH
# 前序遍历，递归版本
class Solution:
    def invertTree(self, root):
        if not root: return None
    	root.left, root.right = root.right, root.left
        self.invertTree(root.left) # 左节点
        self.invertTree(root.right) # 右节点
        return root
# 前序遍历，迭代版本
# 深度优先DFS（前序遍历）
class Solution:
    def invertTree(self, root):
        if not root: return None
    	ans = [root]
        while ans:
            node = ans.pop()
            node.left, node.right = node.right, node.left # 中
            if node.left: ans.append(node.left)  # 左
            if node.right: ans.append(node.right) # 右
        return root
    
# 层序遍历，迭代版本
# 广度优先BFS（层序遍历）
from collections import deque
class Solution:
    def invertTree(self, root):
        if not root: return None
    	que = deaue([root])
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                node.left, node.right = node.right, node.left
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
         return root
```

```python
# 下述版本，可以判断每一层中的节点是否满足数值层面的对称，但是无法判断位置是否对称
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def symmetric(candidate_list):
#             left, right = 0, len(candidate_list)-1
#             while left <= right:
#                 if candidate_list[left] != candidate_list[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True

#         if not root: return False
#         que = deque([root])
#         while que:
#             result = []
#             for _ in range(len(que)):
#                 node = que.popleft()
#                 result.append(node.val)
#                 if node.left: que.append(node.left)
#                 if node.right: que.append(node.right)
#             # print(result)
#             ans = symmetric(result)
#             # print(ans)
#         return ans

# 0101对称二叉树
# 2022/7/21  author:WH
# 迭代法，使用队列
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
        	que.append(leftNode.left) # 左节点的左子树
            que.append(rightNode.right) # 右节点的右子树
            que.append(leftNode.right) # 左节点的右子树
            que.append(rightNode.right) # 右节点的左子树
        return True
    
class Solution:
    def isSymmetric(self, root):
        if not root: return False
    	return self.compare(root.left, root.right)
    def compare(self, left, right):
        if left == None and right != None: return False
    	elif left != None and right == None: return False
    	elif  left == None and right == None: return True
    	elif left.val != right.val: return False
   		# 单层递归逻辑
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        ans = outside and inside
        return ans
```

```python
# 0222统计完全二叉树的节点个数
# 2022/7/22 author:WH
# 迭代法
class Solution:
    def countNode(self, root):
        if not root: return 0
    	ans = 0
        que = deque([root])
        while que:
            result = 0
            for _ in range(len(que)):
                node = que.popleft()
                result += 1
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            ans += result
        return ans
    
# 递归法
class Solution:
    def countNod(self, root):
        return self.getNodeNum(root)
    def getNodeNum(self, root):
        if not root: return 0
    	leftNum = self.getNodeNum(root.left) # 左
        rightNum = self.getNodeNum(root.right) # 右
        totalNum = leftNum + rightNum + 1 # 中
        return totalNum
```

```python
# 0617合并二叉树
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
            node1.val += node2.val
            if node1.left and node2.left:
                que1.append(node1.left)
                que2.append(node2.left)
            if node1.right and node2.right:
                que1.append(node1.right)
                que2.append(node2.right)
            # 接下来这一步没有考虑到，即tree1为空时，需用tree2来替换并返回
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
```

```python
# 0543二叉树的直径
# 2022/7/22  author:力扣官解
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
        	l_depth = depth(node.left)
            r_depth = depth(node.right)
            self.ans = max(self.ans, l_depth + r_depth + 1)
            return max(l_depth, r_depth) + 1
        depth(root)
        return self.ans - 1
```

```python
# 0110平衡二叉树
# 2022/7/23  author:代码随想录
# 迭代解法
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
    
# 递归解法
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
```

```python
# 0257二叉树的所有路径
# 2022/7/24  author:WH
# 迭代法
class Solution:
    def binaryTreePaths(self, root):
        stack, path_st, result = deque([root]),  deque(), []
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
```

```python
# 0257二叉树的所有路径
# 2022/7/24  author:WH
# 递归法
class Soution:
    def binaryTreePaths(self, root):
        path = ''
        result = []
        if not root: return result
    	self.traversal(root, path, result)
        return result
    
    def traversal(self, cur, path, result):
        path += str(cur.val)
        if not cur.left and not cur.right:
            result.append(path)
        if cur.left:
            self.traversal(cur.left, path + '->', result)
        if cur.right:
            self.traversal(cur.right, path + '->', result)
```

```python
# 不同的二叉搜索树
# 2022/7/24  author:WH
# 二叉搜索树的概念：若左子树不为空，左子树所有结点的值小于根节点。若右子树不为空，右子树所有结点的值大于根节点。七左右子树也为二叉搜索树

class Solution:
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]
```

```python
# 验证二叉搜索树
# 2022/7/25  author:WH
# 迭代 中序遍历
class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val <= pre.val: return False
            	pre = cur
                cur = cur.right
        return True
    
# 递归，中序遍历
class Solution:
    def isValidBST(self, root):
        def dfs(root):
            if not root: return True
        	if not dfs(root.left): return False # 左
        	if prev >= root.val: return False  # 中
        	prev = root.val
            if not dfs(root.right): return False # 右
        	return True
        prev = float('-inf')
        return dfs(root)
```

```python
# 105从前序与中序遍历构造二叉树
# 2022/7/25  author:WH
# 递归
class Solution:
    def buildTree(self, preorder, inorder):
        # 第一步：空树以及递归终止的条件
        if not preorder: return None
    	# 第二步：前序遍历的第一个元素，就是中间节点
    	root_val = preorder[0]
        root = TreeNode(root_val)
        # 第三步：根据中间节点，找分割点
        seperator_idx = inorder.index(root_val)
        
        # 第四步：切割inorder数组，并计算左、右部分
        inorder_left = inorder[:seperator_idx]
        inorder_right = inorder[seperator_idx + 1]
        
        # 第五步：切割preorder数组，得到preorder的左右部分
        # 这一步借助了无论是中序还是前序，数组大小相等的概念，直接利用中序找到的左右部分长度对前序进行分割
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]
        
        # 第六步：递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
```

```python
# 106从中序遍历与后序遍历构造二叉树
# 2022/7/25  author:WH
# 递归
class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder: return None
    	root_val = postorder[-1]
        root = TreeNode(root_val)
        
        separator_idx = inorder.index(root_val)
        
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]
        
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left) + 1:len(postorder) - 1]
        
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        return root
```

```python
# 0114二叉树展开成链表
# 2022/7/25  author:github
class Solution:
    def flatten(self, root):
        while root:
            if root.left:
                pre = root.left
                # 如果right不为空就一直遍历到最后
                while pre.right:
                    pre = pre.right
                # right遍历到最后之后，把原来root的right的部分接到最后面
                pre.right = root.right
                # 再把原来root的左侧部分接到其右侧
                root.right = root.left
                root.left = None
            root = root.right
```









#### 二叉树的属性

#### 二叉树的修改与改造

#### 求二叉树的属性

#### 二叉树公共祖先问题

#### 二叉搜索树的修改与改造