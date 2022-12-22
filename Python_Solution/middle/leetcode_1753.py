# # 2022/12/21  author:WH
# # 配对的原则是每次配对都取最大的两个元素进行配对
# # a+b < c时，a和b全部都参与配对
# # a+b > c时，a,b中分别有一部分与c配对，c配完之后，a，b中剩余部分继续配对直至其中一个为0
# class Solution:
#     def maximumScore(self, a, b, c):
#         v = [a, b, c]
#         v.sort()
#         if v[0] + v[1] < v[2]:
#             return v[0] + v[1]
#         return (sum(v) // 2)

# # 2022/12/22  author:leetcode官解
# class Solution:
#     def maximumScore(self, a, b, c):
#         s = a + b + c
#         max_val = max(a, b, c)
#         return s - max_val if s < max_val*2 else s//2

# 2022/12/22  author:github
# 贪心+模拟：每次贪心的从最大的两堆石头中取石子，直至至少有两堆石子堆变为空
# 时间复杂度：O(n)，n为石子总数
# class Solution:
#     def maximumScore(self, a, b, c):
#         s = sorted([a, b, c])
#         ans = 0
#         while s[1]:
#             ans += 1
#             s[1] -= 1
#             s[2] -= 1
#             s.sort()
#         return ans

if __name__ == "__main__":
    a = 2
    b = 4
    c = 6
    result = Solution().maximumScore(a, b, c)
    print(result)