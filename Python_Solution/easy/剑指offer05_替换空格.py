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
# class Solution:
#     def replaceSpace(self, s):
#         counter = s.count(' ')
#         res = list(s)
#         print(res)
#         # 每碰到一个空格就多拓展出两个新的空格用于存储
#         res.extend([' '] * counter * 2)
#         print(res)
#         # 原始字符串的末尾，拓展后字符串的末尾
#         left, right = len(s)-1, len(res)-1
#         while left >= 0:
#             if res[left] != ' ':
#                 res[right] = res[left]
#                 right -= 1
#             else:
#                 res[right - 2: right + 1] = '%20'
#                 right -= 3
#             left -= 1
#         return ''.join(res)

# 2022/7/2  author:WH
# 没有使用双指针的方法
# class Solution:
#     def replaceSpace(self, s):
#         return '%20'.join(s.split(' '))

# 使用双指针：左右指针
# class Solution:
#     def replaceSpace(self, s):
#         # 首先，每次遇到空格都需要把字符串s的长度+2
#         spaceNum = s.count(" ")
#         # 转换为字符串类型，str是不可变类型
#         ans = list(s + spaceNum * 2 * " ")        
#         # 利用双指针：左右指针
#         # left指向原字符串末端，right指向新字符串末端
#         left, right = len(s)-1, len(ans)-1
#         while left >= 0:
#             if ans[left] != " ":
#                 ans[right] = ans[left]
#                 right -= 1
#             else:
#                 ans[right-2:right+1] = "%20"
#                 right -= 3
#             left -= 1
#         return ''.join(ans)

# 2022/09/13  author:WH
# class Solution:
#     def replaceSpace(self, s):
#         return "%20".join(s.split(" "))

# 2022/09/13  author:WH
# 可以AC
# class Solution:
#     def replaceSpace(self, s):
#         # 第一步先给原字符串开辟空间
#         spaceNum = s.count(" ")
#         # print(spaceNum)
#         ans = list(s + spaceNum*2*" ")
#         # print(ans)
#         # 左指针指向的是未经拓展的s的最右侧
#         left =len(s)-1
#         # 右指针指向的是经过拓展的s的最右侧
#         right = len(ans)-1
#         while left >= 0:
#             if s[left] != ' ':
#                 ans[right] = s[left]
#                 right -= 1
#             else:
#                 ans[right-2:right+1] = "%20"
#                 right -= 3
#             left -= 1
#         return ''.join(ans)


# 2022/09/14  author:WH
# 非双指针做法
class Solution:
    def replaceSpace(self, s):
        for idx in range(len(s)):
            if s[idx] == ' ':
                s = s[:idx] + '%20' + s[idx+1:]
        return s


if __name__ == "__main__":
    s = "we are the world!"
    result = Solution().replaceSpace(s)
    print(result)