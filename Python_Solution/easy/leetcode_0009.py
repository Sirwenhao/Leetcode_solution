# 2023/4/20  author:WH

# # 判断回文数
# class Solution:
#     def isPalindrome(self, x):
#         flag = len(str(x))//2
#         i = 0
#         while i < flag:
#             if str(x)[i] != str(x)[len(str(x))-i-1]:
#                 return False
#             i += 1
#         return True

# # 反转字符串方法
# class Solution:
#     def isPalindrome(self, x):
#         if x < 0:
#             return False
#         y = int(str(x)[::-1])
#         return x == y

# # 左右移运算符的使用
# class Solution:
#     def isPalindrome(self, x):
#         s = str(x)
#         return s[:len(s) >> 1] == s[:-(len(s) >> 1)-1: -1]

# 数学方法
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x and x % 10 == 0):
            return False
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x //= 10
        return x in (y, y//10)

if __name__ == "__main__":
    x = 121
    result = Solution().isPalindrome(x)
    print(result)