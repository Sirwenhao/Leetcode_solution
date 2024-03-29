# 2023/4/4  author:WH

# class Solution:
#     def myAtoi(self, s):
#         sNew = ""
#         for i in s:
#             if i == " ":
#                 continue
#             elif i == "+" or i == "-" or i.isdigit():
#                 sNew += "".join(i)
#         return int(sNew)

# # github解答
# class Solution:
#     def myAtoi(self, s):
#         if not s:
#             return 0
#         n = len(s)
#         if n == 0:
#             return 0
#         i = 0
#         while s[i] == ' ':
#             i += 1
#             if i == n:
#                 return 0
#         sign = -1 if s[i] == '-' else 1
#         if s[i] in ['-', '+']:
#             i += 1
#         res, flag = 0, (2**31-1)//10
#         while i < n:
#             if not s[i].isdigit():
#                 break
#             c = int(s[i])
#             if res > flag or (res == flag and c > 7):
#                 return 2**31-1 if sign > 0 else -(2**31)
#             res = res * 10 + c
#             i += 1
#         return sign * res

# 23/10/30 author:WH
# 这个版本本地可以，提交会出错 
class Solution:
    def myAtoi(self, s):
        for c in s:
            if c.isdigit() or c == '-':
                continue
            else:
                s = s.replace(c, '') # replace方法不改变原字符串
        if s[0] == '-':
            flag = -1
            s = s[1:]
        else:
            flag = 1
        if -2**23 <= flag*int(s) <= 2**23-1:
            return flag*int(s)
        return None

    

if __name__ == "__main__":
    s = "words and  -987"
    result = Solution().myAtoi(s)
    print(result)