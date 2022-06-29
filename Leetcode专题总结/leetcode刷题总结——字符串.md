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
    
# method3
class Solution:
    def replaceSpace(self, s):
        counter = s.count(' ')
        res = list(s)
        res.extend([' ']*counter*2)
        left, right = len(s)-1, len(res)-1
        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right-2:right+1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)

if __name__ == "__main__":
    s = "we are the world!"
    result = Solution().replaceSpace(s)
    print(result)
```

##### 2.4 0151

反转字符串中的单词：单词用空格间隔隔开，但空格间隔有可能不仅仅只有一个空格，另外字符串左右两端有可能存在空格，需要去除掉

```python
# 2022/6/29  author:WH
class Solution:
    # 考虑使用双指针（左右指针）去除两端多余空格
    def removeExtraSpace(self, s):
        l, r = 0, len(s)-1
        while l <= r and s[l] == " ":
            l += 1
        while l <= r and s[r] == " ":
            r -= 1
        ans = []
        while l <= r:
            if s[l] != " ":
                ans.append(s[l])
            elif ans[-1] != " ":
                ans.append(s[l])
            l += 1
        return ans
    
    def reverseString(self, s, l, r):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return None
    
    def reverseEachWords(self, s):
        start, end = 0, 0
        while start < len(s):
            while end < n and s[end] != " ":
                end += 1
            self.reverseString(s, start, end-1)
            start = end+1
            end += 1
        return None
    
    def reverseWords(self, s):
        s = self.removeExtraSpace(s)
        self.reverseString(s, 0, len(s)-1)
        self.reverseEachWords(s)
        return ''.join(s)
        
        
# 2022/6/29  method2:代码随想录
class Solution:
    def reverseWords(self, s):
        s_list = [i for i in s.split(" ") if len(i) > 0]
        return " ".join(s_list[::-1])
        
if __name__ == "__main__":
    s = " the  sky  is    blue"
    result = Solution().reverseWords(s)
    pritn(result)
```

##### 2.5 剑指offer58-II 左旋字符串

```python
# 2022/6/29  author:WH
class Solution:
    def reverseLeftWords(self, s, n):
        return s[n:] + s[:n]
    
# 不允许使用切片以及反转
class Solution:
    def reverseLeftWords(self, s):
        def reverse_Sub(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        ans = list(s)
        end = len(ans)-1
        reverse_Sub(ans, 0, n-1)
        reverse_sub(ans, n, end)
        reserse_Sub(ans, 0, end)
        return ''.join(ans)

if __name__ == "__main__":
    s = "abcdefg"
    n = 2
    result = Solution().reverseLeftWords(s, n)
    print(result)
```

关于字符串、数组等反转操作，优先考虑使用双指针（左右指针）

KMP算法专题：

- 0028实现strStr
- 0459重复的子字符串

##### 2.6 0028

```python
# 2022/6/29  author:WH
# 不使用KMP算法
class Solution:
    def strStr(self, haystack, needle):
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                while haystack[i:i+l] == needle:
                    return i
        return -1
    
# 2022/6/29  author:代码随想录
# 使用KMP算法
class Solution:
    def strStr(self, haystack, needle):
        a = len(haystack)
        b = len(needle)
        if a == 0:
            return 0
        next = self.getNext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:
                p = next[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a-1:
                return j-a+1
            return -1
    def getNext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while (k>-1 and needle[k+1]!=needle[i]):
                k = next[k]
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k
        return next
if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    result = Solution().strStr(haystack, needle)
    print(needle)
```

