'''
    1、置位位数表示二进制中的1的个数
    2、要求二进制中1的个数为质数，质数：在大于1的自然数中，除1和自身外不再有其他因数的自然数
'''

# 定义判断是否为质数的函数
def isPrimeNumber(n):
    while n <= 1:
        return False
    i = int(n ** 0.5)  # 注意这个地方判断质数时最大计算到其开根号的值
    for j in range(2, i+1):
        if n % j == 0:
            return False   
    return True


def countPrimeSetBits(left, right):
    c = 0
    for i in range(left, right+1):
        b = bin(i)[2:]  # 计算i的二进制,此处用[2:]把二进制数前面的ob去掉
        print("%d的二进制表示为:%s"%(i, b))
        num = b.count("1")
        print('1的数量为：%d'%num)
        if isPrimeNumber(num):
            c += 1
        
    return c

# # leetcode官解

# def isPrime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# def countPrimeSetBits(left, right):
#     return sum(isPrime(x.bit_count()) for x in range(left, right+1))

left = 10
right = 15

result = countPrimeSetBits(left, right)
print(result)
