"""
    1、字符串专题
"""
# 2022/6/26  author:WH
# 想法：把字符串整体反转，然后删除开头和结尾的空格
# 中间部分就按照空格分隔开，分割之后进行翻转
# class Solution: 
#     # 删除多余空格，双指针
#     def deleteSpace(self, s):
#         l, r = 0, len(s) - 1
#         while l <= r and s[l] == " ":
#             l += 1
#         while l <= r and s[r] == " ":
#             r -= 1
#         tmp = []
#         while l <= r:
#             if s[l] != " ":
#                 tmp.append(s[l])
#             elif tmp[-1] != " ":
#                 tmp.append(s[l])
#             l += 1
#         return tmp
#     # 翻转字符串
#     def reverseString(self, s, l, r):
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#         return None

#     # 反转每个单词
#     def wordsReverse(self, s):
#         start, end = 0, 0
#         while start < len(s):
#             while end < len(s) and s[end] != " ":
#                 end += 1
#             self.reverseString(s, start, end-1)
#             start = end+1
#             end += 1
#         return None

#     def reverseWords(self, s):
#         s = self.deleteSpace(s)
#         self.reverseString(s, 0, len(s)-1)
#         self.wordsReverse(s)
#         return ''.join(s)

# 2022/6/29  author:WH
# class Solution:
#     def deleteExtraSpace(self, s):
#         # 左右指针实现两端多余空格的删除
#         l, r = 0, len(s)-1
#         while l <= r and s[l] == " ":
#             l += 1
#         while l <= r and s[r] == " ":
#             r -= 1
#         ans = [] # 用于存放删除字符串内部多余空格之后的结果
#         # 参考代码随想录
#         while l <= r:
#             if s[l] != " ":
#                 ans.append(s[l])
#             elif ans[-1] != " ": # 对应情况为当前字符为" "，但原字符串末尾非空格，可以append
#                 ans.append(s[l])
#             l += 1
#         return ans

#     def reverseString(self, s, left, right):
#         while left <= right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#         return None

#     def reverseEachWords(self, s):
#         start, end = 0, 0
#         while start < len(s):
#             while end < len(s) and s[end] != " ":  # 这个位置更改and前后两部分顺序会报错
#                 # print('end:', end)
#                 end += 1
#             self.reverseString(s, start, end-1)
#             start = end+1
#             end += 1
#         return None

#     def reverseWords(self, s):
#         s = self.deleteExtraSpace(s)
#         self.reverseString(s, 0, len(s)-1)
#         self.reverseEachWords(s)
#         return ''.join(s)

# 2022/6/29  author:代码随想录
class Solution:
    def reverseWords(self, s):
        s_list = [i for i in s.split(" ") if len(i) > 0]
        return " ".join(s_list[::-1])

if __name__ == "__main__":
    s = " the sky is  blue "
    result = Solution().reverseWords(s)
    print(result)

