"""
    1、map函数：map会根据给定的函数对指定序列做映射
    2、具体语法为：map(function, iterable,...),function运算规则函数，iterable为给定序列
    3、实例：map(lambda x: x**2,[1,2,3,4,5,6])
"""

# def maximumWealth(accounts):
#     sum = max_v = 0
#     for lst in accounts:
#         for i in range(len(lst)):
#             sum += lst[i]
#         max_v = max(max_v, sum)
#         sum = 0
#     return max_v

# def maximumWealth(accounts):
#     return max(map(sum, accounts))



accounts = [[1,2,3],[4,5,6]]
result = map(sum, accounts)
# result = maximumWealth(accounts)
print(result)

# sum = max_v = 0
# for lst in accounts:
#     for i in range(len(lst)):
#         sum += lst[i]
#         max_v = max(max_v, sum)
#         # print(max_v)
    
