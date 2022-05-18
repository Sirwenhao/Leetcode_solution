"""
    1、leetcode对应等级为难题
    2、给定三个数m,n,k；找出乘法表m*n中的第k个大小的数字
"""
# 我的想法先找出乘法表m*n中所有可能的结果，从小到大排序，找第k个结果
# 算法可解，但是两层循环导致超时
# # 关键问题就在于如何减小计算乘法表结果的复杂度，两个循环复杂度过高
# class Solution:
#     def findKthNumber(self, m, n, k):
#         result = []
#         for i in range(m):
#             for j in range(n):
#                 result.append((i+1)*(j+1))
#         result.sort()
#         return result[k-1]

# 补充知识点：python中整数左移与右移的区别：
# 左移操作a<<b表示a=a*(2^b)
# 右移操作a>>b表示a=a//(2^b)
# 上述解法的优化：
class Solution:
    def findKthNumber(self, m, n, k):
        left, right = 1, m*n
        while left < right:
            mid = (left+right) >> 1  # 此处整数右移一位表示//2^1
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid//i, n)
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        return left

        
if __name__ == "__main__":
    m = 2
    n = 3
    k = 6
    result = Solution().findKthNumber(m, n, k)
    print(result)




# result = map(lambda i, j: i*j, range(3), range(4))
# print(list(result))
# result = []
# for i in range(3):
#     for j in range(4):
#         result.append((i+1)*(j+1))

# result.sort()
# print(result)