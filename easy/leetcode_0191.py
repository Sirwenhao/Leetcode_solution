'''
    1、给一个无符号二进制数，返回其中1的个数
    2、吹爆n&(n-1)这个操作，这个操作可以把n对应二进制中的最后一个1变为0
    3、因此不断循环，直至n二进制全为0即可，统计下循环的次数即为1的个数
    4、值得注意的是：二进制中1的个数被称为这一串二进制数的汉明重量
'''
# # 力扣加加
# def hammingWeight(n):
#     res = 0
#     while n:
#         res += 1
#         n &= (n-1) #这一步牛逼
#     return res

# 官解：解法一循环检查二进制位

def hammingWeight(n):
    ans = sum(1 for i in range(32) if n&(1<<i))  # 1<<i表示1左移i位，相当于1乘以2的i次方
    return ans

n = 0b00000000000000000000000000001011

result = hammingWeight(n)
print(result)