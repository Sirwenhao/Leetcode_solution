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

