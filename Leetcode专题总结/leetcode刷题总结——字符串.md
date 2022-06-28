## Leetcode刷题总结——字符串

2022/6/28版本

#### 1、相关题目编号

- 0344反转字符串
- 0541反转字符串II
- 剑指offer05替换空格
- 0151反转字符串里的单词
- 剑指offer58II左旋字符串
- KMP算法理论基础
  - 0028实现strStr
  - 0459重复的字符字串

#### 2、代码实现

##### 2.1 0344

```python
# 2022/6/28  author:WH
# 双指针法（左右指针）
class Solution:
    def reverseString(self, s):
        l, r = 0, len(s)-1
        while l <= r:
        	s[l], s[r] = s[r], s[l]
        	l += 1
        	r -= 1
        return s
    
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    result = SOlution().reverseString(s)
    print(result)
```

##### 2.2 0541

反转字符串，注意核心操作步骤的写法

```python
# 2022/6/28  author:WH
class Solution:
    def reverseStr(self, s, k):
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p:p2][::-1] + s[p2:]  # 关键操作步骤，python反转字符串的快捷方法[::-1]
            p += 2*k
        return s
    
if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    result = Solution().reverseStr(s, k)
    print(result)
```

##### 2.3 剑指offer 05

替换空格

```python
# 2022/6/28  author:WH
# method1
class Solution:
    def replaceSpace(self, s):
        return "%20".join(s.split(" "))
    
# method2
class Solution:
    def replaceSpace(self, s):
        n = len(s)
        for idx, val in enumerate(s[::-1]):
            print(idx, val)
            if val == " ":
                s = s[:n-(idx+1)] + "%20" + s[n-idx:]
            print(s)
        return s

if __name__ == "__main__":
    s = "we are the world!"
    result = Solution().replaceSpace(s)
    print(result)
```

