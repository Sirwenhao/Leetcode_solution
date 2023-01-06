# 2023/1/6  author:WH
# 枚举，时间复杂度:O(NlogN)，空间复杂度:O(1), 其中N=num
# class Solution:
#     def countEven(self, num):
#         ans = 0
#         for i in range(1, num+1):
#             cur = 0
#             while i != 0:
#                 cur += i % 10
#                 i //= 10
#             ans += (cur % 2 == 0)
#         return ans

# 时间复杂度 O(logn)，空间复杂度 O(1)。其中 n 为 num 的值。
class Solution:
    def countEven(self, num):
        ans = num // 10 * 5 - 1 # 每一个a~a+10的分数段中包含多少个偶数
        x, s = num // 10, 0
        while x:
            s += x % 10
            x //= 10
        ans += (num % 10 + 2 - (s & 1)) >> 1
        return ans

    
if __name__ == "__main__":
    result = Solution().countEven(30)
    print(result)