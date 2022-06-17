## Leetcode刷题总结——哈希表

2022/6/17      author:WH

### 1.相关题目编号：

- 0242有效的字母异位词
- 0349两个数组的交集
- 0001两数之和
- 0454四数相加
- 0015三数之和
- 0018四数之和

### 2.代码实现

#### 2.1. 0242

```python
# 2022/6/17  author:WH
# 统计两个字符串中所有字母的
class Solution:
    def isAnagram(self, s, t):
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1
        for j in range(len(t)):
            record[ord(s[j]) - ord("a")] -= 1
        for k in range(26):
            if record[k] != 0:
                return False
            	break
        return True
```

