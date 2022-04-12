"""
    1、返回各位都不同的数字
    2、参考了leetcode的解法，其实是很简单的题目，一开始没有想到通过不同数位排列组合去考虑
"""

def countNumberWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10    
    cnt, l =10, 9
    for i in range(n-1):
        l *= (9 - i)
        cnt += l
    return cnt

n = 3
result = countNumberWithUniqueDigits(n)
print(result)