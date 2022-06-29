"""
    1、剑指0ffer05-替换空格
"""
# 2022/6/23  author:WH
# class Solution:
#     def replaceSpace(self, s):
#         for i in range(len(s)):
#             if s[i] == " ":
#                 s = s[:i] + "%20" + s[i+1:]
#         return s

# 2022/6/23  author:代码随想录
# class Solution:
#     def replaceSpace(self, s):
#         return "%20".join(s.split(" "))

#         n = len(s)
#         for e, i in enumerate(s[::-1]):
#             print(i, e)
#             if i == " ":
#                 s = s[:n - (e+1)] + "%20" + s[n-2:]
#             print("")
#         return s

# if __name__ == "__main__":
#     # s = "We are happy."
#     s = "     "
#     result = Solution().replaceSpace(s)
#     print(result)


# class Solution:
#     def replaceSpace(self, s):
#         return "%20".join(s.split(" "))

# 2022/6/29  author:代码随想录
class Solution:
    def replaceSpace(self, s):
        counter = s.count(' ')
        res = list(s)
        print(res)
        # 每碰到一个空格就多拓展出两个新的空格用于存储
        res.extend([' '] * counter * 2)
        print(res)
        # 原始字符串的末尾，拓展后字符串的末尾
        left, right = len(s)-1, len(res)-1
        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)

    
if __name__ == "__main__":
    s = "we are the world!"
    result = Solution().replaceSpace(s)
    print(result)