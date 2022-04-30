'''
    1、leetcode加加
'''

def isUgly(n):
    if n <= 0:
        return False
    for i in (2, 3, 5):
        while n % i == 0:
            n /= i
    return n == 1

# n = 6
# result = isUgly(n)
# print(result)
