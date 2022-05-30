## Leetcode刷题总结——回溯

2022/5/7版本，后续再补....

### 1. 相关题目编号：

- 0017电话号码的字母组合：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
- 0039组合总和：https://leetcode-cn.com/problems/combination-sum/
- 0040组合总和II：https://leetcode-cn.com/problems/combination-sum-ii/
- 0046全排列I：https://leetcode-cn.com/problems/permutations/
- 0047全排列II：https://leetcode-cn.com/problems/permutations-ii/
- 0713乘积小于K的子数组：https://leetcode-cn.com/problems/subarray-product-less-than-k/

放弃篇~：

- 0037 解数独
- 0051 N皇后
- 0332 重新安排形成

### 2. 代码实现

##### 2.1. 0017

注意对比三种解法之间的区别，个人认为代码随想录的解法更加直观

```python
# 2022/5/7 9:43 author：WH
class Solution:
    def letterCombinations(self, digits):
        # 首先创建list存放数字对应的字母
        dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # 结果集
        ans = []
        # 当前组合，用于判断当前所选择的是否已经满足条件,这个地方要注意初始值给的是""
        current = ""

        # 定义回溯函数结构体,start_index表示当前状态的起始位置
        def backtracking(digits, start_index, current):
            # base condition
            if start_index == len(digits):
                ans.append(current[:])
                return

            # 单层递归逻辑
            # 此处for循环遍历的条件有一点点不一样，需注意下
            for character in dic[int(digits[start_index])-2]: # 一开始dic后面给了()导致报错
                if len(current) == len(digits):
                    ans.append(current)
                backtracking(digits, start_index+1, current+character)
        # 差点忽略了基本情况
        if len(digits) == 0:
            return []
        backtracking(digits, 0, current)
        return ans
    
# author: 代码随想录
class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.answer: str = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0)
        return self.answers
    
    def backtracking(self, digits: str, index: int) -> None:
        # 回溯函数没有返回值
        # Base Case
        if index == len(digits):    # 当遍历穷尽后的下一层时
            self.answers.append(self.answer)
            return 
        # 单层递归逻辑  
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter   # 处理
            self.backtracking(digits, index + 1)    # 递归至下一层
            self.answer = self.answer[:-1]  # 回溯
            
# 回溯简化版本
class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0, '')
        return self.answers
    
    def backtracking(self, digits: str, index: int, answer: str) -> None:
        # 回溯函数没有返回值
        # Base Case
        if index == len(digits):    # 当遍历穷尽后的下一层时
            self.answers.append(answer)
            return 
        # 单层递归逻辑  
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.backtracking(digits, index + 1, answer + letter)    # 递归至下一层 + 回溯
            
            
# author: 力扣加加
class Solution:
    def letterCombinations(self, digits):
        mapper = [" "," ","abc","def","ghi",
                "jkl","mno","pqrs","tuv","wxyz"]

        def backtrack(digits, start):
            if start >= len(digits):
                return ['']
            ans = []
            for i in range(start, len(digits)):
                for c in mapper[int(digits[i])]:
                    for p in backtrack(digits, i+1):
                        if start == 0:
                            if len(c + p) == len(digits):
                                ans.append(c+p)
                        else:
                            ans.append(c+p)
            return ans
        if not digits:
            return []
        return backtrack(digits, 0)


if __name__ == '__main__':
    digits = "234"
    result = Solution().letterCombinations(digits)
    print(result)
```

##### 2.2. 0039

```python
# 2022/5/7 author:WH 回溯加剪枝
# 关键问题一：元素可以被无限制重复选取，只要满足条件即可
# 关键问题二：一定要注意排序的使用
class Solution:
    def combinationsSum(self, candidates, target):
        # 结果集
        ans = []
        # 当前解集
        current = []
        # 先排序
        candidates.sort()

        # 定义回溯函数结构体
        def backtracking(candidates, target, start_index, current):
            if sum(current) == target:
                # 此处符合条件的当前解集以前拷贝的方式加入到结果集
                ans.append(current[:])
                return

            # 定义剪枝模块
            if sum(current) > target:
                return

            # 定义单层循环逻辑
            for i in range(start_index, len(candidates)):
                current.append(candidates[i])
                # 用i来控制每次取元素的起始位置，关键点此处不用i+1表示可以重复读取当前的数
                backtracking(candidates, target, i, current)
                current.pop() # 回溯

        backtracking(candidates, target, 0, current)
        return ans

# 代码随想录
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        因为本题没有组合数量限制，所以只要元素总和大于target就算结束
        '''
        self.path.clear()
        self.paths.clear()

        # 为了剪枝需要提前进行排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:]) # 因为是shallow copy，所以不能直接传入self.path
            return
        # 单层递归逻辑 
        # 如果本层 sum + condidates[i] > target，就提前结束遍历，剪枝
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target: 
                return 
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)  # 因为无限制重复选取，所以不是i-1
            sum_ -= candidates[i]   # 回溯
            self.path.pop()        # 回溯
    
    

if __name__ == '__main__':
    candidates = [2,7,6,3,5,1]
    target = 9

    result = Solution().combinationsSum(candidates, target)
    print(result)
```

##### 2.3.0040

```python
# 2022/5/7 0:12 Author:WH 回溯
class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        current = []
        # 排序这个关键步骤不能少
        candidates.sort()

        # 定义回溯部分主体
        def backtracking(candidates, target, start_index, current):
            # base condition
            if sum(current) == target:
                ans.append(current[:])  # 此处用浅拷贝
                return # 这个return语句被我遗忘了

            for i in range(start_index, len(candidates)):  # 此处的start_index是防止重复取元素
                # 剪枝操作
                if sum(current) > target:
                    return
                # 剪枝操作：跳过同一树层使用过的元素
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                current.append(candidates[i])
                backtracking(candidates, target, i+1, current)
                current.pop()

        backtracking(candidates, target, 0, current)
        return ans

# 力扣加加
class Solution:
    def combinationSum2(self, candidates, target):
        """
        与39题的区别是不能重用元素，而元素可能有重复
        不能重用好解决，回溯的index往下一个就行；
        元素可能有重复，就让结果的去重麻烦一些
        """
        size = len(candidates)
        if size == 0:
            return []

        # 先排序
        candidates.sort()
        path = []
        res = []
        self._find_path(candidates, path, res, target, 0, size)
        return res

    def _find_path(self, candidates, path, res, target, begin, size):
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                if left_num < 0:
                    break
                # 如果存在重复的元素，前一个元素已经遍历的后一个元素与之后元素组合的所有可能
                if i > begin and candidates[i]  == candidates[i-1]:
                    continue
                path.append(candidates[i])
                # 开始的index往后移一格
                self._find_path(candidates, path, res, left_num, i+1, size)
                path.pop()

                
                
if __name__ == '__main__':
    candidates = [5,2,2,1,2]
    target = 5
    result = Solution().combinationSum2(candidates, target)
    print(result)
```

### 3.  相关学习资料

- 代码随想录：https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E9%A2%98%E7%9B%AE%E5%88%86%E7%B1%BB%E5%A4%A7%E7%BA%B2%E5%A6%82%E4%B8%8B
- 力扣加加：https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/thinkings/backtrack

### 4. 回溯专题总结

2022/5/21~2022/5/22更新，以《代码随想录》分类为参考

#### 4.1. 组合问题

- 0017 电话号码的字母组合
- 0039 组合总和
- 0040 组合总和II
- 0077 组合
- 0216 组合总和III

4.1.1 组合问题中的关键点：如何保证取过的元素不被重复选取?（使用参数start_index）

使用参数start_index记录<font color=red>下一层递归搜索的起始位置</font>，每次从集合[1,2,3,...,n]中选取元素，可选择的范围逐渐收缩，而这种收缩就是由start_index决定的。内层循环中的嵌套回溯中的参数start_index可以决定当前元素是否能够重复选取（取i或i+1）。

难点：树层去重和树枝去重的实现

具体实例：

0077 组合

```python
# 2022/5/21 author:WH
class Solution:
	def __init__(self):
        self.ans = []
        self.current = []
    def combine(self, n, k):
        self.ans.clear()
        self.current.clear()
        self.backtracking(n, k, 1)
        return self.ans
    def backtracking():
        if len(self.current) == k:
            self.ans.append(self.current[:])
            return
        for i in range(start_index, n+1):
            self.current.append(i)
            self.backtracking(n, k, i+1)  # 关键点：i+1
            self.current.pop()
            
# 上述解法的剪枝版本
# 剪枝优化的版本
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def combine(self, n, k):
        self.ans.clear()
        self.current.clear()
        self.backtracking(n, k, 1)
        return self.ans

    def backtracking(self, n, k, start_index):
        if len(self.current) == k:
            self.ans.append(self.current[:])
            return

        for i in range(start_index, n-(k-len(self.current))+2):
            self.current.append(i)
            self.backtracking(n, k, i+1)
            self.current.pop()
```

0017 电话号码的字母组合

```python
# 2022/5/22 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = ''
        self.dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits):
        self.ans.clear()
        self.backtracking(digits, 0)
        return self.ans
    def letterCombinations(self, digits, index):
        if index == len(digits):
            self.ans.append(self.current[:])
            return
        for i in self.dic[int(digits[index])-2]:
            if len(self.current) > len(digits):
                return
            self.current += i
            self.backtracking(digits, index+1)
            self.current = self.current[:-1]
```

0039 组合总和

```python
# 2022/5/21 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []
    def combinationsSum(self, candidates, target):
        candidates.sort()
        self.ans.clear()
        self.current.clear()
        self.backtracking(candidates, target, 0) 
        return self.ans
    def backtracking(self, candidates, target, start_index):
        if sum(self.current) == target:
            self.ans.append(self.current[:])
            return
        for i in range(start_index, len(candidates)):
            # 剪枝
            if sum(self.current) > target:
            	return
            self.current.append(candidates[i])
            self.backtracking(candidates, target, i) // 关键点:不用i+1了，表示可以重复读取当前的数
            self.current.pop() # 回溯
```

0040 组合总和II

```python
# 2022/5/21 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.ans.clear()
        self.current.clear()
        self.backtracking(candidates, target, 0)
        return self.ans

    def backtracking(self, candidates, target, start_index):
        if sum(self.current) == target:
            self.ans.append(self.current[:])
            return
        for i in range(start_index, len(candidates)):
            # 剪枝
            if sum(self.current) > target:
                return
            # 去重，这个地方的i>start_index没有想明白
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
            self.current.append(candidates[i])
            self.backtracking(candidates, target, i+1)
            self.current.pop()
```

0216 组合总和III

```python
# 2022/5/22  author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def combinationSum3(self, k, n):
        self.ans.clear()
        self.current.clear()
        self.backtracking(k, n, 1)
        return self.ans
    def backtracking(k, n, start_index):
        if len(self.current) == k and sum(self.current) == n:
            self.ans.append(self.current[:])
            return
        for i in range(start_index, 10):
            if sum(self.current) > n:
               return
        	self.current.append(i)
            self.backtracking(k, n, i+1)
            self.current.pop()
```

2022/5/25~2022/5/26更新，author: WH

#### 4.2 分割/切割问题

- 0093 复原IP地址
- 0131 分割回文串

4.2.1 切割问题中的关键点：起始点start_index和每次遍历的变量i共同决定了每次所截取到的字符串字串，s[strat_index:i+1]这个才是每次所截取到的字串，需要做的操作就是判断这个字串是否合法。

具体实例：

0093 复原IP地址

```python
# 2022/5/25 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        
    def restoreIPAddress(self, s):
        self.ans.clear()
        self.backtracking(self, s, 0, 0)
        return self.ans
    def backtracking(self, s, start_index, dotNum):
        if dotNum == 3:
            if self.isValid(s, start_index, len(s)-1):
                self.ans.append(s[:])
            return False
        for i in range(start_index, len(s)):
            if self.isValid(s, start_index, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, dotNum+1)
                s = s[:i+1] + s[i+2:] # 回溯
            else:
                break
                
         def isValid(self, s, start, end):
            if start > end:
                return Fasle
            if s[start] == 0 and start != end:
                return False
            if not 0 <= int(s[satrt:end+1]) <= 255:
                return False
if __name__ == "__main__":
    s = "25525511135"
    result = Solution().restoreIPAddress(s)
    print(result)
```

0131 分割回文串

```python
# 2022/5/25 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []
        
    def partition(self, s):
        self.ans.clear()
        self.current.clear()
        self.backtracking(s, 0)
        return self.ans
    
    def backtracking(self, s, start_index):
        if start_index >= len(s):
            self.ans.append(self.current[:])
            return self.ans
        for i in range(start_index, len(s)):
            # 判断是否满足回文
            if s[start_index:i+1][::1] == s[start_index:i+1][::-1]:
                self.current.append(s[start_index:i+1])
                self.backtracking(s, i+1)
                self.current.pop()
            else:
                continue
                
if __name__ == "__main__":
    s = "aab"
    result = Solution().partition(s)
    print(result)           
```

#### 4.3 子集问题

- 0078 子集
- 0090 子集II

4.3.1 子集问题中的关键点：集合是无序的，元素顺序并不影响最终结果，因此取过的元素不会再重取，需要使用start_index。

具体实例：

0078 子集

```python
#2022/5/25 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []
        
    def subsets(self, nums):
        self.ans.clear()
        self.current.clear()
        self.backtracking(nums, 0)
        return self.ans
    
    def backtracking(self, nums, start_index):
        self.ans.append(self.current[:])
        if start_index == len(nums):
            return
        for i in range(start_index, len(nums)):
            self.current.append(nums[i])
            self.backtracking(nums, i+1)
            self.current.pop()
if __name__ == "__name__":
    nums = [1,2,3]
    result = Solution().subsets(nums)
    p        
```

0090 子集II

```python
#2022/5/26 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []
        
    def subsetsWithDup(self, nums, start_index):
        self.ans.clear()
        self.current.clear()
        self.backtracking(nums, 0)
        return self.ans
    def backtracking(self, nums, start_index):
        self.current(nums[i])
        if start_index == len(nums):
            return
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i]==nums[i-1]:
                continue
            else:
                self.current.append(nums[i])
                self.backtracking(start_index, i+1) # 树枝不能重复选取
                self.current.pop()
                
if __name__ == "__main__":
    nums = [1,2,2]
    result = Solution().subsetsWithDup(nums)
    print(result)
```

0491 递增子序列

```python
# 2022/05/29  author:Wh
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def findSubsequences(self, nums):
        self.ans.clear()
        self.current.clear()
        self.backtracking(nums, 0)
        return self.ans
    
    def backtracking(self, nums, start_index):
        if len(self.current) >= 2:
            self.ans.append(self.current[:])

        if len(self.current) == len(nums):
            return
        
        usedList = set()
        for i in range(start_index, len(nums)):
            if (self.current and nums[i] < self.current[-1]) or nums[i] in usedList:
                continue
            usedList.add(nums[i])
            self.current.append(nums[i])
            self.backtracking(nums, i+1)
            self.current.pop() 
```

#### 4.4 排列问题

- 0046 全排列
- 0047 全排列II

```python
# 2022/5/30  author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []
```
