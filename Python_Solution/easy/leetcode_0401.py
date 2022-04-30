'''
    1、二进制手表，很有意思的问题
    2、顶部的四个数字只能代表0-11范围内的数字
    3、底部六位数字只能代表32，16，8，4，2，1这五个数字
    4、笛卡尔积问题，查一下笛卡尔积再复习巩固一下
'''
# 力扣加加

# from itertools import combinations

# def readBinaryWatch(turnedOn):
#     def possible_number(count, minute=False):
#         if count == 0: return [0]
#         if minute:
#             return filter(lambda a:a < 60, map(sum, combinations([1,2,4,8,16,32], count)))
#         return filter(lambda a: a < 12, map(sum, combinations([1,2,4,8], count)))

#     ans = set()
#     for i in range(min(4, turnedOn + 1)):
#         for a in possible_number(i):
#             for b in possible_number(turnedOn - i, True):
#                 ans.add(str(a) + ":" + str(b).rjust(2, '0'))
#     return list(ans)   

# leetcode官解
# 知识点：python中f表达式的用法：f"{表达式}",如此式中的f"{h}:{m:02d}",其中02d表示输出是多少位，整数格式

# def readBinaryWatch(turnedOn):
#     ans = list()
#     for h in range(12):
#         for m in range(60):
#             if bin(h).count("1") + bin(m).count("1") == turnedOn:
#                 # print(f"{h}:{m:02d}")
#                 ans.append(f"{h}:{m:02d}")
#     return ans

def readBinaryWatch(turnedOn):
    return [str(a) + ":" + str(b).rjust(2, '0') for a in range(12) for b in range(60) if (bin(a) + bin(b)).count('1')==turnedOn]

turnedOn = 1
result = readBinaryWatch(turnedOn)
print(result) 

