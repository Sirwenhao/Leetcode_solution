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
- 确定递归终止条件，每一次递归的结果使用递归栈结构保存的，终止条件不正确会导致递归站溢出
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

#### 二叉树的属性

#### 二叉树的修改与改造

#### 求二叉树的属性

#### 二叉树公共祖先问题

#### 二叉搜索树的修改与改造