'''
    考虑不使用for循环解决
'''

# # leetcode 提交超时
# def isPowerOfFour(n):
#     while n != 1:
#         n, i = divmod(n, 4)
#         if i != 0:
#             return False
#         else:
#             continue
#     return n==1


# leetcode加加
# 所有4的幂次方的二进制表示中，1都在奇数位，其他位置上都是0
# trick:如果一个数字n是2的幂次方则一定有二进制按位与满足：n&(n-1)=0
# 判断是不是只在奇数为上有1，可以将其二进制表示与对应的奇数为都是1，偶数位都是0的二进制数字相与
# 如此题中的：01010101010101010101010101010101 = 0x55555555

# def isPowerOfFour(n):
#     if n == 1:
#         return True
#     elif n < 4:
#         return False
#     else:
#         if not n & (n-1) == 0:
#             return False
#         else:
#             return n & 0x55555555 == n

# 解法3
def isPowerOfFour(num):
    binary_num = bin(num)[2:]
    print('binary_num:', binary_num)
    return binary_num.strip('0') == '1' and len(binary_num) % 2 == 1


n = 64
result = isPowerOfFour(n)
print(result)