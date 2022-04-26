'''
    1、颠倒二进制位，可不是首位相互交换的啊
    2、|在python中表示按位或, &表示按位与
'''

# # 力扣加加解法一
# def reverseBits(n):
#     result = 0
#     for i in range(32):
#         print('result << 1:', bin(result << 1)) # << 表示将result << 1左移一位
#         print('n & 1:', n & 1)  #先把0扩充成与n同样长度的二进制数，然后对应位按位与
#         result = (result << 1) | (n & 1) # |在python中表示按位或
#         n >>= 1
#     return result


# 力扣加加解法二
def reverseBits(n):
    ans = 0
    for i in range(31, -1, -1):
        ans |= ((n >> i) & 1) << (31 - i)

n = 0b00000010100101000001111010011100
result = reverseBits(n)
print(result)