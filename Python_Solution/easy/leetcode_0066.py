"""
    1、加1操作，但是有可能有进位的情况需要注意下
    2、力扣加加的解法对每一位的考虑出自两个点：加1之后当前位的值为多少和加1之后对应的进位值为多少
"""

# 力扣加加
def plusOne(digits):
    carry = 1 # 设置为1，用于检测每一位上的数字是否为9
    for i in range(len(digits)-1, -1, -1):
        print(i)
        digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10 # (carry + digits[i]) // 10的值只能为1或0
        print(digits)
    return [carry] + digits if carry else digits # 如需进位，此处carry为1，定为真


digits = [9,9,9,7,9]
result = plusOne(digits)
print(result)