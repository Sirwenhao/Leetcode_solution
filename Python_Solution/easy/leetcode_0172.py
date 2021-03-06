"""
    1、求0的数量
"""
# # 力扣加加解法
# def trailingZeros(n):
#     count = 0
#     for i in range(5, n+1, 5):
#         while i%5==0:
#             i //= 5  #用于控制质因子5出现重复的情况
#             count+=1
#     return count

# 解法二：观察阶乘所有数字的规律可以得知，0的出现是因为含质因数2和5数字的出现所造成的
# 而在所有的阶乘数字中，含质因数2的数字在含质因数5的数字之前均会出现，核心原因是质因数5的出现

# def trailingZeros(n):
#     cnt = 0
#     for i in range(5, n+1, 5): #第一次写没想出来这个循环的写法
#         while i%5 == 0:
#             i //= 5
#             cnt += 1
#     return cnt

# 解法二：递归解法
# 一个整数n含有的质因数5数量可以表示为：n//5,但还需要考虑n//5之后的数是不是5

# def trailingZeros(n):
#     if n == 0:
#         return 0
#     return n//5 + trailingZeros(n//5)


# 2022/4/24 review
# 核心点在于质因数5的数量。i,j = divmod(a,b)返回两个值,i = a//b; j = a%b
# 下述解法在n=625时，不满足情况
# def trailingZeros(n):
#     i = n//5
#     j = i//5
#     five_num = i + j
#     if j >= 5:
#         j = j//5
#         five_num += j
#     return five_num

# 最好的方法——递归
def trailingZeros(n):
    if n==0: return 0
    return n//5 + trailingZeros(n//5)

result = trailingZeros(625)
print(result)