## Leetcode刷题总结——栈与队列

2022/7/15  author:WH

### 1.相关题目编号

- 0232用栈实现队列
- 0225用队列实现栈
- 0020有效的括号
- 0150逆波兰表达式求值
- 0239滑动窗口求最大值
- 0347前k个高频元素
- 0042接雨水

### 2.代码实现

#### 2.1 0232用栈实现队列

栈是先进后出的数据类型，队列是先进先出的数据类型。用栈实现队列，需要两个基本栈，一个专门用于输入一个专门用于输出。

```python
# 2022/7/15  author:WH
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x):
        self.stack_in.append(x)
        
    def pop(self):
        if self.empty():
            return None
       	if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self):
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
    
    def empty(self):
        return not (self.stack_in or self.stack_out)
```

#### 2.2 0225用队列实现栈

以对列实现栈有两种方式：单队列和双队列。

Python中的queue和SimpleQueue没有类似于peek的功能，也无法用索引访问

单队列版本

```python
# 2022/7/15  author:WH
from collections import deque
class MyStack:
    def __init__(self):
        self.que = deque()
        
    def push(self, x):
        n = len(self.que)
        self.que.append(x)
        for _ in range(n):
            self.que.append(self.que.popleft())
       
    def pop(self):
        if self.empty():
            return None
        for i in range(len(self.que)):
            self.que.append(self.que.popleft())
        return self.que.popleft()
    
    def top(self):
        if self.empty():
            return None
        else:
            return self.que[-1]
        
    def empty(self):
        return len(self.que) == 0
    
# 这个版本竟然也能AC
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.queue.pop()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue
```

双队列版本

```python
# 2022/7/16  author:WH
from collections import deque
class MyStack:
    def __init__(self):
        self.que_in = deque()
        self.que_out = deque()
        
    def push(self, x):
        self.que_in.append(x)
    
    def pop(self):
        if self.empty():
            return None
        for i in range(len(self.que_in)-1):
            self.que_out.append(self.que_in.popleft())
        self.que_in, self.que_out = self.que_out, self.que_in
        return self.que_out.popleft()
    
    def top(self):
        if self.empty():
            return None
        return self.que_in[-1]
    
    def empty(self):
        return len(self.que_in) == 0
```

#### 2.3 0020有效的括号

```python
# 2022/7/16  author:WH
class Solution:
    def isValid(self, s):
        dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                # 先确保stack不为空才可以pop
                if len(stack) != 0:
                	if i != dict[stack.pop()]:
                    	return Fasle
                	else:
                    	continue
                else:
                    return False             
        return len(stack) == 0
    
class Solution:
    def isValid(self, s):
        l = []
        dic = {'()', '{}', '[]'}
        for i in s:
            if i in '({[':
                l.append(i)
            elif not l or l.pop()+i not in dic:
                return False
        return not l
    
if __name__ == "__main__":
    s = "({[]})"
    result = Solution().isValid(s)
    print(result)
```

#### 2.4 0150逆波兰表达式求值

逆波兰表达式是一种后缀表达式，及后缀表达式转中缀表达式计算求值。应该是使用栈把数字先压栈，遇到运算符时把栈顶两个元素出栈进行计算，然后再把计算结果压栈。两个考点：eval()函数和f"{}"表达式用法

```python
# 2022/7/16  author:WH
class Solution:
    def evalRPN(self, tokens):
        # 创建栈，用于将非运算符元素压栈
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                f_ele, s_ele = stack.pop(), stack.pop()
                stack.append(int(eval(f"{s_ele} {item} {f_ele}")))
        return int(stack.pop())

# 2022/10/05 author:github
import operator
class Solution:
    def evalRPN(self, tokens):
        opt = {
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.truediv}
    s = []
    for i in tokens:
        if i in opt:
            s.append(int(opt[i](s.pop(-2), s.pop(-1))))
        else:
            s.append(int(i))
    return s[0]
    
# 2022/10/05  author:github
class Solution:
    def evalRPN(self, tokens):
        nums = []
        for i in tokens:
            if len(i) > 1 or i.isdigit():
                nums.append(int(i))
            else:
                if i == "+":
                    nums[-2] += nums[-1]
                elif i == "-":
                    nums[-2] -= nums[-1]
                elif i == "*":
                    nums[-2] *= nums[-1]
                else:
                    nums[-2] = int(nums[-2] / nums[-1])
                nums.pop()
        return nums[0]

if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    result = Solution().evalRPN(tokens)
    print(result) 
```

#### 2.5 0239滑动窗口求最大值

```python
# 2022/7/16  author:https://github.com/doocs/leetcode/tree/main/solution/0200-0299/0239.Sliding%20Window%20Maximum
# 单调队列常见模型：找出滑动窗口中的最大值/最小值，模板
q = deque()
for i in range(n):
    # 判断队头是否滑出窗口
    while q and check_out(q[0]):
        q.popleft()
    while q and check(q[-1]):
        q.pop()
    q.append(i)
        
class Solution:
    def maxSlindingWindow(self, nums):
        for i, v in enumerate(nums):
            if q and i-k+1 > q[0]:
                q.popleft()
            while q and nums[q[-1]] <= v:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
    
    
# 2022/7/16  author:代码随想录
# 定义单调队列（从大到小）
class MyQueue:
    def __init__(self):
        # 用list实现单调队列
        self.queue = []
    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出
    # pop之前判断队列是否为空
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出
    # 直到push的数值小于等于队列入口元素的数值为止
    # 这样就保持了队列里的元素是单调从大到小的
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        
    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlindingWindow(self, nums, k):
        que = MyQueue()
        ans = []
        for i in range(k):
            que.push(nums[i])
        ans.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            ans.append(que.front())
        return ans
    
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = Solution().maxSlindingWindow(nums, k)
    print(result)
```

#### 2.6 0347前k个高频元素

top K问题可以用堆解决

```python
# 2022/7/16  author:https://github.com/doocs/leetcode/tree/main/solution/0300-0399/0347.Top%20K%20Frequent%20Elements
class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        hp = []
        for num, freq in counter.items():
            if len(hp) == k:
                heappush(hp, (freq, num))
                heappop(hp)
            else:
                heappush(hp, (freq, num))
        return [t[1] for t in hp]
    
# 2022/7/16  author:代码随想录
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        pri_que = []
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
       result = [0] * k
       for i in range(k-1, -1, -1):
            result[i] heapq.heappop(pri_que)[1]
       return result           
    
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    result = Solution().topKFrequent(nums, k)
    print(result)
```

#### 2.7 0042接雨水

同面试题17.21 直方图的水量。核心：双指针，两种计算方法：单独一列的计算和单独一行的计算。

![image-20221008100800231](https://gitee.com/sirwenhao/typora-illustration/raw/master/image-20221008100800231.png)

动态规划思想：对于位置i，此处最大水量取决于<font color=yellow>下标i左右两侧最大高度的最小值，再减去`height[i]`即为当前位置所对应的水量</font>

```python
# 2022/7/16  author:WH
# 双指针：左右指针
class Solution:
    def trap(self, height):
        ans = []
        leftMax = rightMax = 0
        left, right = 0, len(height)-1
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
    
# 2022/7/16  author:同上链接
class Solution:
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0
        left_max = [height[0]] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        right_max = [height[n - 1]] * n
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
  
if __name__ == "__name__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = Solution().trap(height)
    print(result)
```

