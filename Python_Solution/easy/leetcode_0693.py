'''
    1、考点：十进制转二进制数
'''

# 解法一：可以解答但超时，时间复杂度为：N
# def hasAlternatingBits(n):
#     list1 = []
#     while n:
#         y = n % 2
#         n = n // 2
#         list1.append(y)
        

#     # list1.reverse()
#     for i in range(len(list1)-1):
#         if list1[i] != list1[i+1]:
#             return True

# 解法二：力扣官方解法，时间复杂度为O(logN),空间复杂度O(1)

# def hasAlternatingBits(n):
#     prev = 0
#     while n:
#         cur = n % 2
#         if cur == prev:
#             return False
#         prev = cur
#         n //= 2
#     return True

# 解法三：采用位运算
# 第一步：将n与n >> 1按位异或得结果a
# 第二步：将异或之后的结果a与a-1按位与
# 原理：当且仅当n为交替位二进制数时，按照此方法所得的a的二进制所有位上均为1
# 时间复杂度为：O(1)仅用了常熟时间解决

def hasAlternatingBits(n):
    a = n ^ (n-1)
    return a & (a+1) == 0

n = 5
result = hasAlternatingBits(n)
print(result)