# 2022/12/15 author:WH
# 第一步将字符串全部转换为对应的数值，第二递归计算字符串和，递归次数为k
# class Solution:
#     def getLucky(self, s, k):
#         n = len(s)
#         ans = ""
#         for i in range(n):
#             ans += str(ord(s[i]) - ord('a') + 1)
#         j = 0
#         while j < k:
#             num = 0
#             for i in range(len(ans)):
#                 num += int(ans[i])
#             ans = str(num)
#             j += 1
#         return num

# leetcode官解
class Solution:
    def getLucky(self, s, k):
        digits = "".join(str(ord(ch)-ord('a')+1) for ch in s)
        for i in range(k):
            if len(digits) == 1:
                break
            total = sum(int(ch) for ch in digits)
            digits = str(total)
        return int(digits)

if __name__ == "__main__":
    s = "zbax"
    k = 2
    result = Solution().getLucky(s, k)
    print(result)