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
# class Solution:
#     def reverseWords(self, s):
#         s_list = [i for i in s.split(" ") if len(i) > 0]
#         return " ".join(s_list[::-1])

# 2022/7/2  author:WH
# 不使用双指针
# class Solution:
#     def reverseWords(self, s):
#         return ' '.join([i for i in s.split(' ') if len(i) > 0][::-1])

# 使用双指针：左右指针
# class Solution:
#     # 删除多余空格, 使用左右指针
#     def removeExtraspace(self, s):
#         left, right = 0, len(s)-1
#         while left <= right and s[left] == " ":
#             left += 1
#         while left <= right and s[right] == " ":
#             right -= 1
#         temp = []
#         while left <= right:
#             if s[left] != " ":
#                 temp.append(s[left])
#             elif temp[-1] != " ":
#                 temp.append(s[left])
#             left += 1
#         return temp

    # 双指针：左右指针反转字符串
    # def reverseString(self, s, l, r):
    #     while l < r:
    #         s[l], s[r] = s[r], s[l]
    #         l += 1
    #         r -= 1
    #     return None

#     # 双指针：快慢指针反转字符串
#     def reverseEachWord(self, s):
#         slow = fast = 0
#         while slow <= len(s)-1:
#             while fast < len(s) and s[fast] != " ":
#                 fast += 1
#             self.reverseString(s, slow, fast-1)
#             slow = fast+1
#             fast += 1
#         return None

#     def reverseWords(self, s):
#         l = self.removeExtraspace(s)
#         self.reverseString(l, 0, len(l)-1)
#         self.reverseEachWord(l)
#         return ''.join(l)

# 2022/09/16  author:WH
# class Solution:
#     def reverseWords(self, s):
#         sList = list(i for i in s.split(" ") if len(i) >= 1)
#         print(sList)
#         return ' '.join(sList[::-1])

# 2022/09/16  author:WH
class Solution:
    def removeExtraspace(self, s):
        left, right = 0, len(s)-1
        while s[left] == ' ' and left <= right:
            left += 1
        while s[right] == ' ' and left <= right:
            right -= 1
        tmp = []
        # 删除内部多余空格
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':
                tmp.append(s[left])
            left += 1
        return tmp
    # 翻转整个字符串
    def reverseString(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None
    # 翻转每个单词
    def reverseEachWords(self, nums):
        slow = fast = 0
        n = len(nums)
        while slow < n:
            while fast != ' ' and fast < n:
                fast += 1
            self.reverseString(s, slow, fast-1)
            slow = fast+1
            fast += 1
        return None

    def reverseWords(self, s):
        # 删除左右两侧多余的空格和内部多余空格
        l = self.removeExtraspace(s)
        self.reverseString(l, 0, len(l)-1)
        self.reverseEachWords(l)
        return ''.join(l)


if __name__ == "__main__":
    s = " the sky is  blue "
    result = Solution().reverseWords(s)
    print(result)

