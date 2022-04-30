"""
    1、leetcode所对应的最大回文数乘积
    2、两个n位数的乘积最多是2n位
"""

# # 解法一：时间复杂度过高，时间复杂度O((10**n-10**(n-1))**2 + len(num))
# def largestPalindrome(n):
#     max_v = 0
#     # 判断一个数字是否是回文数
#     def isPalindrome(num):
#         num = str(num)
#         if num[::1] == num[::-1]:
#             return True
#         return False

#     num = 0
#     if n-1 >= 0 and n <= 8:
#         # while 10**(n-1) <= i < 10**n and 10**(n-1) <= j < 10**n:
#         for i in range(10**(n-1), 10**n):
#             for j in range(10**(n-1), 10**n):
#                 num = i*j
#                 result = isPalindrome(num)
#                 if result:
#                     max_v = max(max_v, num)

#         result = max_v % 1337
#     return result


# leetcode官解

def largestPalindrome(n):
    if n==1:
        return 9
    upper = 10**n-1
    for left in range(upper, upper // 10, -1): # 枚举回文数的左半部分
        p, x = left, left
        print(p)
        print(x)
        while x:
            p = p*10 + x%10 # 反转左半部分至其末尾，构造回文数p
            print(p)
            x//=10
        x = upper
        while x*x >= p:
            if p % x == 0:
                return p % 1337
            x -= 1

n = 2
result = largestPalindrome(n)
print(result)


# # 判断一个数字是否是回文数
# def Palindrome(num):
#     num = str(num)
#     if num[::1] == num[::-1]:
#         return True
#     return False

# num = 9008
# result = Palindrome(num)
# print(result)