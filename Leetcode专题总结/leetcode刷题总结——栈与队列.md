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
        self.que.append(x)
       
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
        if len(s) == 0:
            return False
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if i != dict[stack.pop()]:
                    return Fasle
                else:
                    continue
        return len(stack) == 0
    
if __name__ == "__main__":
    s = "({[]})"
    result = Solution().isValid(s)
    print(result)
```

#### 2.4 逆波兰表达式求值

逆波兰表达式是一种后缀表达式，及后缀表达式转中缀表达式计算求值。应该是使用栈把数字先压栈，遇到运算符时把栈顶两个元素出栈进行计算，然后再把计算结果压栈。

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
            while q and nums[q[-q]] <= v:
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

