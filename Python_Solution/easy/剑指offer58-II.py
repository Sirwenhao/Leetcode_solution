"""
1、剑指offer58II左旋字符串
"""
# 2022/6/27  author:WH
# class Solution:
#     def reverseLeftWords(self, s, n):
#         step = n % len(s)
#         ans = s[step:] + s[:step]
#         print(s[step:])
#         print(s[:step])
#         return ans

# 2022/6/27  author:代码随想录
# class Solution:
#     def reverseLeftWords(self, s, n):
#         return s[n:] + s[:n]

# 2022/09/26  author:WH
# 这道题目真正考察的是对于剑指offer58的理解
# 三次反转：翻转前半部分、翻转后半部分、整体反转

class Solution:
    def reverseList(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return None

    def reverseLeftWords(self, s, n):
        s = list(s)
        l = len(s)-1
        self.reverseList(s, 0, n-1)
        self.reverseList(s, n, l)
        self.reverseList(s, 0, l)
        return ''.join(s)


if __name__ == "__main__":
    # s = "abcdefg"
    # n = 2
    s = "lrloseumgh"
    n = 6
    result = Solution().reverseLeftWords(s, n)
    print(result)