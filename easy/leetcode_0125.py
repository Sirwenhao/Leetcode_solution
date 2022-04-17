"""
    1、验证字符串是否为回文数
    2、考虑从两边向中间靠拢，头尾双指针写法
    3、python中的isalnum()函数用于检查字符串是否只由字母和数字组成，返回值是布尔类型
    4、.lower()方法为将字符串中所有的大写字符转换为对应的小写字符
"""
# # 力扣加加解法一：

# def isPalindrome(s):
#     left, right = 0, len(s)-1
#     while left < right:
#         if not s[left].isalnum():  # isalnum()是判断字符串是否仅由字母和数字组成的函数
#             left += 1
#             continue
#         if not s[right].isalnum():
#             right -= 1
#             continue
#         if s[left].lower() == s[right].lower():
#             left += 1
#             right -= 1
#         else:
#             break
#     return right <= left

# 力扣加加解法2

def isPalindrome(s):
    """
    使用语言特性进行求解
    """
    s = ''.join(i for i in s if i.isalnum()).lower()
    return s == s[::-1]

s = 'noon'
result = isPalindrome(s)
print(result)