# 2023/1/10  author:WH
# class Solution:
#     def reinitializePermutation(self, n):
#         perm = [i for i in range(n)]
#         target = perm
#         ans = 0
#         while True:
#             perm = [perm[i//2] if i%2 == 0 else perm[n//2 + (i-1)//2] for i in range(n)]
#             print(perm)
#             ans += 1
#             if perm == target:
#                 return ans

# 2023/1/10  author:WH
# 找规律+模拟
"""
    观察数字的变化规律可以发现：
    1、新数组的偶数位数字依次是原数组的前半段数字
    2、新数组的奇数位数字依次是原数组的后半段数字
    即，如果原数组的某个数字下标 i 在 [0, n >> 1) 范围内，那么这个数字的新下标就是 i << 1；否则，新下标就是 (i - (n >> 1)) << 1 | 1。
    另外，每一轮操作，数字移动的路径都是一样的，只要有一个数字（数字 0 和 n−1 除外）回到了它原来的位置，那么整个序列就和之前的一致了。
    因此，我们选择数字 1，初始时下标也是 1，每次将数字 1 移动到新的位置，直到数字 1 回到原来的位置，就可以得到最小的操作次数。
    时间复杂度 O(n)，空间复杂度 O(1)。
"""
class Solution:
    def reinitializePermutation(self, n):
        ans, i = 0, 1
        while 1:
            ans += 1
            if i < n >> 1:
                i <<= 1
            else:
                i = (i - (n >> 1)) << 1 | 1
            if i == 1:
                return ans



if __name__ == "__main__":
    n = 4
    result = Solution().reinitializePermutation(n)
    print(result)
