"""
    1、求0的数量
"""

def trailingZeros(n):
    count = 0
    for i in range(5, n+1, 5):
        while i%5==0:
            i //= 5  #用于控制质因子5出现重复的情况
            count+=1
    return count

result = trailingZeros(25)
print(result)