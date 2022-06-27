"""
1、剑指offer58II左旋字符串
"""
# 2022/6/27  author:WH
class Solution:
    def reverseLeftWords(self, s, n):
        step = n % len(s)
        ans = s[step:] + s[:step]
        print(s[step:])
        print(s[:step])
        return ans

if __name__ == "__main__":
    # s = "abcdefg"
    # n = 2
    s = "lrloseumgh"
    n = 6
    result = Solution().reverseLeftWords(s, n)
    print(result)