'''
    1、求另外一个满足条件的数组
    2、条件1：新数组数字个数为n
    3、条件2：新数组中每一位数字的范围为：[1, 6]
    4、条件3：新数组的均值为：总数组均值-现有数组均值
    5、条件4：满足m+n长度的数组中数字之和可以整除m+n
'''
# import random
# def missingRolls(rolls, mean, n):
#     mean_n = float(mean) - float(sum(rolls))/len(rolls)
#     list1 = []
#     while len(list1) < n:
#         list1.append(random.randint(1, 6))
        
#     if mean_n == float(sum(list1))/n:
#         return list1
#     else:
#         continule


rolls = [3, 2, 4, 3]
mean = 4
n = 2

result = missingRolls(rolls, mean, n)
print(result)