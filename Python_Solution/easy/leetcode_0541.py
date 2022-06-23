"""
    1、0541反转字符串II
"""
# 2022/6/23  author:WH  参考代码随想录
class Solution:
    def reverseStr(self, s, k):
        if len(s) < k: return s[::-1]
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p:p2][::-1] + s[p2:] # 关键步骤
            p += 2*k
        return s
if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    result = Solution().reverseStr(s, k)
    print(result)