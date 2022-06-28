"""
    1、KMP算法
    2、字符串专题
"""
# 2022/6/28  author:WH
# 不使用KMP的解法
# class Solution:
#     def strStr(self, haystack, needle):
#         l = len(needle)
#         for i in range(len(haystack)):
#             if haystack[i] == needle[0]:
#                 while haystack[i:i+len(needle)] == needle:
#                     return i
#         return -1

# 使用KMP算法
class Solution:
    def strStr(self, haystack, needle):
        a = len(haystack)
        b = len(needle)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:
                p = next[p]
            if needle[p+1] == haystack[j]:
                p+=1
            if p==a-1:
                return j-a+1
        return -1

    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        k=-1
        next[0] = k
        for i in range(1, len(needle)):
            while (k>-1 and needle[k+1]!=needle[i]):
                k = next[k]
            if needle[k+1]==needle[i]:
                k+=1
            next[i] = k
        return next
if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    result = Solution().strStr(haystack, needle)
    print(result)
