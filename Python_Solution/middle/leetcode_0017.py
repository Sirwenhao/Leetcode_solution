"""
    1、仅包含数字2-9的字符串，返回去对应的字母组合
    2、类似于电话的实体按键，2->(a,b,c)，3->(d,e,f),...,9->(w,x,y,z)
"""


# 力扣加加解法：回溯法
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
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return list()
        dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",}

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in dic[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()
        
        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

# 2022/5/2 review
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


if __name__ == '__main__':
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)