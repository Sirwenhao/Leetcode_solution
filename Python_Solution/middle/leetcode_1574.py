# 2023/3/25  author:WH

# 题意中有两点要求：第一点要求是连续子数组，第二点要求子数组必须是最短的
# 删除连续的子序列之后，需要满足剩下的子序列中，左边子序列的最大值小于等于右遍子序列的最小值，并且两个子序列都不存在递减情况

# class Solution:
#     def findLengthOfShortestSubarray(self, arr):
#         n = len(arr)
#         i, j = 0, n-1
#         while i < n-1 and arr[i] <= arr[i+1]:
#             i += 1
#         while j > 1 and arr[j] >= arr[j-1]:
#             j -= 1
#         if j <= i:
#             return 0
#         ans = min(n - i - 1, j)
#         r = j
#         for l in range(i+1):
#             while r < n and arr[r] < arr[l]:
#                 r += 1
#             ans = min(ans, r-l-1)
#         return ans

# 参考官解
class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        j = n-1
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        ans = j
        for i in range(n):
            while j < n and arr[i] > arr[j]:
                j += 1
            ans = min(ans, j-i-1)
            if i+1 < n and arr[i] <= arr[i+1]:
                break
        return ans

if __name__ == "__main__":
    arr = [1,2,3,10,4,2,3,5]
    result = Solution().findLengthOfShortestSubarray(arr)
    print(result)
