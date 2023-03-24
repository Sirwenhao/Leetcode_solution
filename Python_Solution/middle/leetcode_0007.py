# 2023/3/24  author:WH
# 考察数字位与符号位的操作
# class Solution:
#     def reverse(self, x):
#         if 0 < int(str(x)[:1]) < 9:
#             return int(str(x)[::-1])
#         else:
#             return -int(str(x)[1::-1])

# x为一个数字，取出其中的每一位数就相当于是除10取余，反转输出体现了栈的思想
# 超时，但是测试可以通过
# class Solution:
#     def reverse(self, x):
#         ans = 0
#         flag = x//abs(x)
#         x = abs(x)
#         while x != 0:
#             tmp = x%10
#             x //= 10
#             # 第一步在此处对ans的计算没想到以下公式
#             ans = ans*10 + tmp
#         return 0 if ans < -(2**31) or ans > 2**31-1 else flag*ans

class Solution:
    def reverse(self, x):
        y = int(str(abs(x))[::-1])
        res = -y if x < 0 else y
        return 0 if res < -(2**31) or res > 2**31-1 else res

if __name__ == "__main__":
    x = -123
    # x = 123
    result = Solution().reverse(x)
    print(result)