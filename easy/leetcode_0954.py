'''
    1、最关键的问题是，所给数组并非按照给定的数字顺序执行，而是只要重组后有任何一组满足条件即可
'''

# # 解法一：自己写的有问题，逻辑应该正确
# def canRecordDoubled(arr):
#     if len(arr) == 0:
#         return False
    
#     dic = []
#     arr = list(arr).sort()
#     for j in arr:
#         if 2*j in arr:
#             dic.append(j)
#             dic.append(2*j)

#         else:
#             return False

#     for i in range(len(dic)/2):
#         if dic[2*i+1] == 2*dic[2*i]:
#             return True
#         else:
#             return False


# 解法二：leetcode高赞解答
# 使用了python内置的collections模块
# counter是一个容器对象，字典的子类，主要用于统计散列对象，示例见下：

import collections

# a = collections.Counter("hello world")
# print(a["l"]) # 3
# print(a)


def canRecordDoubled(arr):
    num_map = collections.Counter(arr)
    # print(num_map)
    for num in sorted(num_map, key=abs):
        # print('num:',num)
        # print('num_map[num]:', num_map[num])
        # print('num_map[2*num]:', num_map[2*num])
        if num_map[num] > num_map[2*num]:
            return False
        num_map[2*num] -= num_map[num]
        # print(num_map[2*num])
        # print(num_map[num])
    return True

arr = list([4,-2,2,-4])
# arr.sort()

result = canRecordDoubled(arr)
print(result)