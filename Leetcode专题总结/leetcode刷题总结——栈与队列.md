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

Python中的queue和simpleQueue没有类似于peek的功能，也无法用索引访问

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

