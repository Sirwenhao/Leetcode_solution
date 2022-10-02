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
    
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        r = [0] * 26
        for i in range(len(s)):
            r[ord(s[i]) - ord('a')] += 1
            r [ord(t[i]) - ord('a')] -= 1
        return all(c==0 for c in r)
    
if __name__ == "__main__":
    s = 'recordsdss'
    t = 'recordsdss'
    result = Solution().isAnagram(s, t)
    print(result)
```

#### 2.2 0349

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

#### 2.3 0202

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
                
class Solution:
    def isHappy(self, n):
        def get_next(n):
            ans = 0
            while n > 0:
                n, digit = divmod(n, 10)
                ans += digit ** 2
            return ans
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_next(n)
        return n==1
                
if __name__ == "__main__":
    n = 19
    result = Solution().isHappy(n)
    print(result)
```

#### 2.4 0001

```python
# 2022/6/19  author:代码随想录
class Solution:
    def twoSum(self, nums, target):
        record = {}
        for idx, val in enumerate(nums):
            if target - val not in record:
                record[val] = idx
            else:
                return [record[target - val], idx]
            
# 2022/10/01
class Solution:
    def twoSum(self, nums, target):	
        dic = {}
        for idx, val in enumerate(nums):
            m = target - val
            if m in dic:
                return [dic[m], idx]
            dic[val] = idx
            
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9	
    result = Solution().twoSum(nums, target)
    print(result)
```

#### 2.5 0454

```python
# 2022/6/19   author:WH
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        dic1 = {}
        for i in nums1:
            for j in nums2:
                if i + j in dic1:
                    dic1[i + j] += 1
                else:
                    dic1[i + j] = 1
        print('dic1:', dic1)
        cnt = 0
        for m in nums3:
            for n in nums4:
                key = - m - n
                if key in dic1:
                    cnt += dic1[key]
        return cnt
    
# 2022/10/01  author:WH
# 漏解，但具体原因不清楚
# 感觉应该是有些索引顺序不同的重复解没有计入
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                k = 0
                while k < len(nums3):
                    if 0-(nums1[i]+nums2[j]+nums3[k]) in nums4:
                        l = nums4.index(0-(nums1[i]+nums2[j]+nums3[k]))
                        ans.append([i,j,k,l])
                    k += 1
        return len(ans)
    
if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    result = Solution().forSumCount(nums1, nums2, nums3, nums4)  
```

#### 2.5 0015

```python
# 2022/6/22  author:WH
class Solution:
    def threeSum(self, nums):
        nums.sort()
        # 使用哈希表实现去重
        ans = set()
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.add([nums[i], nums[left], nums[right]]) #此条语句如果按照此写法会报错:"unhashable type list"
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return list(map(list, ans))

# 2022/6/22  author:WH
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            if ans != [] and ans[-1][0] == nums[i]: continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right - 1 and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans 
    
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    result = Solution().threeSum(nums)
    print(result)
```

#### 2.6 0018

```python
# 2022/6/22  author:WH  使用哈希表去重
class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                left, right = j+1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return list(map(list, ans))
        
 class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                l = j + 1
                r = n - 1

                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] > target: r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target: l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: p += 1
                        while l < r and nums[r] == nums[r - 1]: r -= 1
                        l += 1
                        r -= 1
        return res
       
 if __name__ == "__main__":
    nums = [2,2,2,2,2]
    target = 8
    result = Solution().fourSum(nums, target)
    print(result)
```

