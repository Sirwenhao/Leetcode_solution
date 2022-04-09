"""
    1、加1操作，但是有可能有进位的情况需要注意下
"""
# 想法：将数组中的数字组成对应的完整数，然后取二进制加法，然后将结果还原回列表
# 2022/4/9 遗漏

# def plusOne(digits):
#     carry = 1 # 表示进位数
#     if digits[-1] < 9:
#         digits[-1] = digits[-1] + 1
#         return digits
#     elif (digits[i] == 9 for i in range(len(digits))):
#         digits = [1].append(digits[i] == 0 for i in range(len(digits)))
#         return digits
#     else: (个位数上为9，首位不为9，其他位随意)


# 力扣加加
def plusOne(digits):
    carry = 1 # 设置为1，用于检测每一位上的数字是否为9
    for i in range(len(digits)-1, -1, -1):
        digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10 # (carry + digits[i]) // 10的值只能为1或0
    return [carry] + digits if carry else digits


digits = [9,9,9,7,9]
result = plusOne(digits)
print(result)