"""
    1、删除回文字符串
    2、也是看leetcode加加的解释，才明白消除的最大次数也就是两次
    3、时间复杂度：O(N),空间复杂度：O(1)
"""
# def removePalindromeSub(s):
#     if s == '':
#         return 0
#     return 1 if s == s[::-1] else 2

def removePalindromeSub(s):
    if s == '':
        return 0

    def isPalindrome(s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    return 1 if isPalindrome(s) else 1


s = "ababaababa"
result = removePalindromeSub(s)
print(result)
