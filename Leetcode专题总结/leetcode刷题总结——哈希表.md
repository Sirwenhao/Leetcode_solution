## Leetcode刷题总结——哈希表

2022/6/17      author:WH

### 1.相关题目编号：

- 0242有效的字母异位词
- 0349两个数组的交集
- 0202 快乐数
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

2.2 0349

```python
# 2022/6/19  author:WH
class Solution:
    def intersection(self, nums1, nums2):
        res = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
        return res
    
# 2022/6/19  author:代码随想录
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
    
    
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = Solution().intersection(nums1, nums2)
    print(result)
```

2.3 0202

```python
# 2022/6/19  author:WH
class Solution:
    def calculate(self, num):
        sum = 0
        while num:
            i = num % 10
            sum += i**2
            num = num // 10
        return sum
    def isHappy(self, n):
        record = set()   # 用于记录已经出现过的情况，防止再次出现，陷入死循环
        while True:
            n = self.calculate(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)
if __name__ == "__main__":
    n = 19
    result = Solution().isHappy(n)
    print(result)
```

2.4 0001

```python
# 2022/6/19  author:WH  存在问题，有些案例不能通过，出现索引值相同的情况
class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, j in enumerate(nums):
            dic[j] = i
        if target-k in dic:
            return [dic[i], dic[target-k]]
        return 0
    
# 2022/6/19  author:代码随想录
class Solution:
    def twoSum(self, nums, target):
        record = {}
        for idx, val in enumerate(nums):
            if target - val not in record:
                record[val] = idx
            else:
                return [record[target - val], idx]
            
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)
```

