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

# 2022/5/6 写回溯法尝试解决
class Solution:
    def letterCombinations(self, digits):
        # 先要创建一个待查的备用数据集合
        dic = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # 定义存放当前需要判断的参数的存储空间
        res = []
        # 定义回溯函数结构体
        def backtracking(digits, start_index, s): # 回溯的参数一开始也没有想明白，没有想到s
            if start_index == len(digits):
                res.append(s)
                return
            for character in dic[int(digits[start_index])-2]:  # 此处回溯的横向深度遍历对象一开始没有找对
                backtracking(digits, start_index+1, s+character) # 这个地方也没又想到s+character
        # base condition
        if len(digits) == 0:
            return []
        backtracking(digits, 0, "")
        return res



if __name__ == '__main__':
    digits = "234"
    result = Solution().letterCombinations(digits)
    print(result)