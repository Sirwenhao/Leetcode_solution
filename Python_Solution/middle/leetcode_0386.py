"""
    1、按字典序返回所有整数
    2、要求时间复杂度O(n)，空间复杂度:O(1)
    3、字典序：ASCII码对应的顺序，第一位相同则以第二位为标准排序，以此类推。
"""

# 力扣官解
def lexicalOrder(n):
    ans = [0]*n
    num = 1
    for i in range(n):
        ans[i] = num
        if num * 10 <= n:
            num *= 10
        else:
            while num % 10 == 9 or num + 1 > n: # 此步不理解
                num //= 10
            num += 1
    return ans
    
n = 13
result = lexicalOrder(n)
print(result)