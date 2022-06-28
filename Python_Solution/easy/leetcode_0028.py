"""
    1、KMP算法
    2、字符串专题
"""
# 2022/6/28  author:WH
# 不使用KMP的解法
class Solution:
    def strStr(self, haystack, needle):
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                while haystack[i:i+len(needle)] == needle:
                    return i
        return -1

if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    result = Solution().strStr(haystack, needle)
    print(result)
