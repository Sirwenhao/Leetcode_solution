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

二叉搜索树：节点存储数值，是一种有序树。

- 如左子树不为空，则左子树上所有节点的值均小于它的根节点的值
- 如右子树不为空，则右子树上所有节点的值均大于它的根节点的值
- 它的左右子树分别为二叉排序树

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

#### 二叉树的遍历方式

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



#### 二叉树的属性

#### 二叉树的修改与改造

#### 求二叉树的属性

#### 二叉树公共祖先问题

#### 二叉搜索树的修改与改造