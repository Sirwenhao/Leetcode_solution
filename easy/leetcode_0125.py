"""
    1、验证字符串是否为回文数
    2、考虑从两边向中间靠拢，头尾双指针写法
"""

def isPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if not s[left].isalnum():  # isalnum()是判断字符串是否仅由字母和数字组成的函数
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            break
    return right <= left

s = 'noon'
result = isPalindrome(s)
print(result)