'''
    1、知识点一：函数a，b = divmod(c, d)返回值为元组，a = c // d; b = c % d;
    2、知识点二：如何实施更新并获取一个不确定长度的整数的每一位上的数字
'''

def selfDividingNumbers(left, right):
    def isSelfDividing(num):
        x = num
        while x:
            x, d = divmod(x, 10)
            if d == 0 or num % d:
                return False
        return True
    return [i for i in range(left, right+1) if isSelfDividing(i)]



right = 22
left = 1

result = selfDividingNumbers(left, right)
print(result)