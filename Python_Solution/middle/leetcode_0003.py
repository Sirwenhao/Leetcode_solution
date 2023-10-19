"""
    1、无重复字符的子串的最大长度
"""
     
# 力扣加加
# 思路：哈希表+滑动窗口。哈希表建立字符和出现位置之间的映射，滑动窗口存储所有的非重复元素，找最大的窗口
# counter.get(word, 0)返回字典counter中元素word对应的值，默认为0

# # 力扣加加
# from collections import defaultdict
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         l = 0
#         ans = 0
#         counter = defaultdict(lambda: 0)  # 默认字典中的键对应的元素值为0
#         # print('counter:', counter)

#         for r in range(len(s)):
#             print(counter.get(s[r], 0)) # python中的get()函数
#             while counter.get(s[r], 0) != 0:
#                 counter[s[l]] = counter.get(s[l], 0) - 1
#                 l += 1
#             counter[s[r]] += 1
#             ans  = max(ans, r - l + 1)
#         return ans

# # 官解
# # 滑动窗口，通过遍历每一个元素来判断窗口的大小
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         # 哈希集合，记录每个字符是否出现过
#         occ = set()
#         n = len(s)
#         # 右指针，初始值为-1，相当于在字符串左侧的左边，还没开始移动
#         rk, ans = -1, 0
#         for i in range(n):
#             if i != 0:
#                 # 左指针向右移动一格，移除一个字符
#                 occ.remove(s[i-1])
#             while rk+1 < n and s[rk+1] not in occ:
#                 # 不断移动右指针
#                 occ.add(s[rk+1])
#                 rk += 1
#             # 第i到第rk个字符是一个极长的无重复字符
#             ans = max(ans, rk-1-i)
#         return ans

# s = "abcabcbb"
# result = lengthOfLongestSubstring(s)
# print(result)

# # 2022/4/30 review
# 此版本中出现错误的原因通过debug可以看出，具体来说就是：
# 当遇到的第一个重复字符不在已知最长字符串的首位时，要从dir中删除从最左侧至重复字符位的所有元素
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         # 创建集合存放元素，防止出现重复
#         dir = set()
#         # 创建左指针，分别指向最左侧满足条件的位置，找到最右侧满足条件的位置，则位置之差即为所求
#         ans = left = 0
#         for right, value in enumerate(s):
#             if value not in dir:  # 用if循环会出现答案错误
#                 dir.add(value)
#             else:
#                 dir.remove(s[left])
#                 left += 1
#             ans = max(ans, right-left+1)
#         return ans

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         dir = set()
#         left = ans = 0
#         for right, value in enumerate(s):
#             while value in dir:
#                 dir.remove(s[left])
#                 left += 1
#             dir.add(value)
#             ans = max(ans, right-left+1)
#         return ans


# 23/10/19 author:WH
# 思路：双指针快慢指针  终止条件：快指针指向字符串的最后位置
# 不能解决所有字符都相同的情况
class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        slow, fast = 0, 1
        if len(s) <= 1:
            return 1
        while fast < len(s):
            if s[fast] not in s[slow:fast]:
                maxLength = max(maxLength, fast-slow+1)
                fast += 1
            else:
                index = s[slow:fast].find(s[fast])
                slow = index + 1
                fast += 1
        return maxLength



if __name__ == "__main__":
    s = "abcbacbb"
    # s = "aab"
    # s = "bbbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)

# 字符串拼接测试
# a = 's'
# b = 'a'
# print(a+b)