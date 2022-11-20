"""
    1、仅包含数字2-9的字符串，返回去对应的字母组合
    2、类似于电话的实体按键，2->(a,b,c)，3->(d,e,f),...,9->(w,x,y,z)
"""

# # 力扣加加解法：回溯法
# class Solution:
#     def letterCombinations(self, digits):
#         mapper = [" "," ","abc","def","ghi",
#                 "jkl","mno","pqrs","tuv","wxyz"]

#         def backtrack(digits, start):
#             if start >= len(digits):
#                 return ['']
#             ans = []
#             for i in range(start, len(digits)):
#                 for c in mapper[int(digits[i])]:
#                     for p in backtrack(digits, i+1):
#                         if start == 0:
#                             if len(c + p) == len(digits):
#                                 ans.append(c+p)
#                         else:
#                             ans.append(c+p)
#             return ans
#         if not digits:
#             return []
#         return backtrack(digits, 0)

# 官解:回溯加递归
# class Solution:
#     def letterCombinations(self, digits):
#         if not digits:
#             return list()
#         dic = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz",}

#         def backtrack(index):
#             if index == len(digits):
#                 combinations.append("".join(combination))
#             else:
#                 digit = digits[index]
#                 for letter in dic[digit]:
#                     combination.append(letter)
#                     backtrack(index + 1)
#                     combination.pop()
        
#         combination = list()
#         combinations = list()
#         backtrack(0)
#         return combinations

# # 2022/5/2 review
# class Solution:
#     def letterCombinations(self, digits):
#         dic = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']   
#         if len(digits) == 0:
#             return []
#         strs = [dic[int(d) - 2] for d in digits]
#         res = []
#         for s in strs:
#             if not res:
#                 res = list(s)
#             else:
#                 cache = []
#                 for item in res:
#                     for letter in s:
#                         cache.append(item+letter)
#                 res = cache
#         return res

# 代码随想录解法
# class Solution:
#     def __init__(self):
#         self.answers: List[str] = []
#         self.answer: str = ''
#         self.letter_map = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }

#     def letterCombinations(self, digits: str) -> List[str]:
#         self.answers.clear()
#         if not digits: return []
#         self.backtracking(digits, 0)
#         return self.answers
    
#     def backtracking(self, digits: str, index: int) -> None:
#         # 回溯函数没有返回值
#         # Base Case
#         if index == len(digits):    # 当遍历穷尽后的下一层时
#             self.answers.append(self.answer)
#             return 
#         # 单层递归逻辑  
#         letters: str = self.letter_map[digits[index]]
#         for letter in letters:
#             self.answer += letter   # 处理
#             self.backtracking(digits, index + 1)    # 递归至下一层
#             self.answer = self.answer[:-1]  # 回溯

# 2022/5/6 写回溯法尝试解决
# class Solution:
#     def letterCombinations(self, digits):
#         # 先要创建一个待查的备用数据集合
#         dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#         # 定义存放当前需要判断的参数的存储空间
#         res = []
#         # 定义回溯函数结构体
#         def backtracking(digits, start_index, s): # 回溯的参数一开始也没有想明白，没有想到s
#             if start_index == len(digits):
#                 res.append(s)
#                 return
#             for character in dic[int(digits[start_index])-2]:  # 此处回溯的横向深度遍历对象一开始没有找对
#                 backtracking(digits, start_index+1, s+character) # 这个地方也没又想到s+character
#         # base condition
#         if len(digits) == 0:
#             return []
#         backtracking(digits, 0, "")
#         return res

# # 2022/5/7 9:43 author：WH
# class Solution:
#     def letterCombinations(self, digits):
#         # 首先创建list存放数字对应的字母
#         dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#         # 结果集
#         ans = []
#         # 当前组合，用于判断当前所选择的是否已经满足条件,这个地方也要注意初始值给的是""
#         current = ""

#         # 定义回溯函数结构体,start_index表示当前状态的起始位置
#         def backtracking(digits, start_index, current):
#             # base condition
#             if start_index == len(digits):
#                 ans.append(current[:])
#                 return

#             # 单层递归逻辑
#             # 此处for循环遍历的条件有一点点不一样，需注意下
#             for character in dic[int(digits[start_index])-2]: # 一开始dic后面给了()导致报错
#                 if len(current) == len(digits):
#                     ans.append(current)
#                 backtracking(digits, start_index+1, current+character)
#                 # current -= character  # 回溯
#         # 忽略了基本情况
#         if len(digits) == 0:
#             return []
#         backtracking(digits, 0, current)
#         return ans

# # 2022/5/21 review author:WH
# # 还是忘记了，关键点还是没有特别清晰。。。。。。
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []
#         self.dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

#     def letterCombinations(self, digits):
        
#         self.ans.clear()
#         self.current.clear()
#         self.backtracking(digits, 0)
#         return self.ans

#     def backtracking(self, digits, start_index):
#         if len(self.current) == len(digits):
#             self.ans.append(self.current[:])
#             return

#         for i in range(start_index, len(digits)):
#             character = self.dic[int(digits[i])]

# # 对比上述错解，重写（参考了正解） 2022/5/21 author:WH
# class Solution: 
#     def __init__(self):
#         self.ans = []
#         self.current = ''
#         self.dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

#     def letterCombinations(self, digits):
#         self.ans.clear()
#         self.backtracking(digits, 0)
#         return self.ans

#     def backtracking(self, digits, index):
#         # 此处有使用到start_index，则递归终止的条件
#         if index == len(digits):
#             self.ans.append(self.current[:])
#             return
#         for i in self.dic[int(digits[index])-2]:
#             if len(self.current) > len(digits):
#                 return
#             self.current += i
#             self.backtracking(digits, index+1)
#             self.current = self.current[:-1] # 字符串的回溯

# # 2022/11/12 author:WH
# class Solution:
#     def __init__(self):
#         self.res = []
#         self.letter_map = {
#             '2':'abc',
#             '3':'def',
#             '4':'ghi',
#             '5':'jkl',
#             '6':'mno',
#             '7':'pqrs',
#             '8':'tuv',
#             '9':'wxyz'
#             }

#     def letterCombinations(self, digits):
#         self.res.clear()
#         if not digits: return []
#         self.backtracking(digits, 0, '')
#         return self.res

#     def backtracking(self, digits, index, ans):
#         if index == len(digits):
#             self.res.append(ans)
#             return
#         letters = self.letter_map[digits[index]]
#         for letter in letters:
#             self.backtracking(digits, index+1, ans+letter)

# # 2022/11/13 author:WH
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.letter_map = {
#             '2':'abc',
#             '3':'def',
#             '4':'ghi',
#             '5':'jkl',
#             '6':'mno',
#             '7':'pqrs',
#             '8':'tuv',
#             '9':'wxyz'
#             }

#     def letterCombinations(self, digits):
#         self.ans.clear()
#         if not digits: return []
#         self.backtracking(digits, 0, '')
#         return self.ans
#     def backtracking(self, digits, index, res):
#         if index == len(digits):
#             self.ans.append(res)
#             return
#         letters = self.letter_map[digits[index]]
#         for letter in letters:
#             self.backtracking(digits, index+1, res+letter)

# 2022/11/20 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.letter_dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

    def letterCombinations(self, digits):
        self.ans.clear()
        if not digits:
            return []
        self.backtracking(digits, 0, '')
        return self.ans

    def backtracking(self, digits, index, cur):
        if index == len(digits):
            self.ans.append(cur)
            return self.ans
        for letter in self.letter_dic[digits[index]]:
            self.backtracking(digits, index+1, cur+letter)


if __name__ == '__main__':
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)