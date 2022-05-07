### Leetcode刷题总结——回溯

2022/5/7版本，后续再补...

#### 1. 相关题目编号：

- 0017电话号码的字母组合：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
- 0039组合总和：https://leetcode-cn.com/problems/combination-sum/
- 0040组合总和II：https://leetcode-cn.com/problems/combination-sum-ii/
- 0046全排列I：https://leetcode-cn.com/problems/permutations/
- 0047全排列II：https://leetcode-cn.com/problems/permutations-ii/
- 0713乘积小于K的子数组：https://leetcode-cn.com/problems/subarray-product-less-than-k/

#### 2. 代码实现

##### 2.1. 0017.注意对比三种解法之间的区别，个人认为代码随想录的解法更加直观

```python
# 2022/5/7 9:43 author：WH
class Solution:
    def letterCombinations(self, digits):
        # 首先创建list存放数字对应的字母
        dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # 结果集
        ans = []
        # 当前组合，用于判断当前所选择的是否已经满足条件,这个地方也要注意初始值给的是""
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

2.2. 0039.

#### 3.  相关学习资料

- 代码随想录：https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E9%A2%98%E7%9B%AE%E5%88%86%E7%B1%BB%E5%A4%A7%E7%BA%B2%E5%A6%82%E4%B8%8B
- 力扣加加：https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/thinkings/backtrack

