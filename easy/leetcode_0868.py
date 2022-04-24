"""
    1、两个1位置距离中的最大值
    2、python中的ord()用于获取字符的ASCII码
    3、python中的进制表示：bin(Num)为二进制、oct(Num)为八进制、hex(Num)为十六进制
    4、python
"""
# 自己写的解法：涉及到双指针（快慢指针）
# 时间复杂度O(N),空间复杂度O(1).N为转换后的二进制字符串长
# def binaryGap(n):
#     b_num = bin(n)[2:]
#     # print(b_num.count('1'))
#     if (b_num.count('1')) <= 1:
#         return 0
#     else:
#         k = 0
#         max_v = 0
#         for i,j in enumerate(b_num):
#             if j=='1':
#                 max_v = max(max_v, i-k)
#                 k = i
#         return max_v

# 力扣官解
# 遍历寻找1，用last记录上一个1的位置，i为当前1的位置，做差
# 技巧：位运算，n&1获取n的最低位，然后每次都将n>>1右移一位。任何数与1相与&，最后一位一定是这个数的原来的最后一位决定的

def binaryGap(n):
    last, ans, i = -1, 0, 0
    while n:
        if n & 1:
            if last != 1:
                ans = max(ans, i-last)
            last = i
        n>>=1
        i+=1
    return ans


n = 5
result = binaryGap(n)
print(result)


# b_num = bin(n)
# print(b_num[2:])
# One_num = b_num.count('1')
# print(One_num)