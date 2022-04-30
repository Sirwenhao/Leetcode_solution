'''
    1、最开始的想法不允许使用+-，那就是用二进制的运算解决
    2、没有进位的简单加法，直接按位异或即可得到最终值，但有进位的加法比较难以解决
    3、有进位的加法需要单独考虑进位的情况
    4、将此问题（a+b）拆分为:(a和b无进位的结果和a和b进位的结果两方面考虑)
    5、无进位加法使用异或运算实现，进位结果使用与运算和移位运算计算得出，循环此过程直至进位为0
'''

# def getSum(a, b):
#     num1 = a ^ b
#     num2 = (a&b) << 1
#     while num2 != 0:
#         temp = num1 ^ num2
#         num2 = (num1 & num2) << 1
#         num1 = temp
#     return num1

# 力扣加加解法
'''
    1、关键点1：位运算
    2、异或是一种无进位的加减法
    3、求与之后左移一位可以表示进位
'''

# python整数类型为unifying Long Intrgers, 即无限长整数类型
# 模拟32bit有符号整型加法

def getSum(a, b):
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF

    while b:
        carry = a & b
        a ^= b
        b = ((carry) << 1) & 0xFFFFFFFF
    return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

a = 19
b = 13
result = getSum(a, b)
print(result)

