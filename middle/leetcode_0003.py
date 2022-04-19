"""
    1、无重复字符的子串的最大长度
"""

# # 最初的想法是，遍历每个元素如果和前面所有的元素不同则将其拼接到前面，如果相同那就更新左边界
# def lengthOfLongestSubstrng(s):
#     max_l = 0
#     i = 1
#     s = ''
#     while i < len(s):
#         assert 
#         if s[i-1] == s[i]:
#             i += 1
#         else:
#             s += s[i-1] + s[i]

        
# 力扣加加
# 思路：哈希表+滑动窗口。哈希表建立字符和出现位置之间的映射，滑动窗口存储所有的非重复元素，找最大的窗口
# counter.get(word, 0)返回字典counter中元素word对应的值，默认为0

from collections import defaultdict


def lengthOfLongestSubstring(s):
    l = 0
    ans = 0
    counter = defaultdict(lambda: 0)  # 默认字典中的键对应的元素值为0

    for r in range(len(s)):
        print(counter.get(s[r], 0)) # python中的get()函数
        while counter.get(s[r], 0) != 0:
            counter[s[l]] = counter.get(s[l], 0) - 1
            l += 1
        counter[s[r]] += 1
        ans  = max(ans, r - l + 1)
    return ans


s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(result)


# 字符串拼接测试
# a = 's'
# b = 'a'
# print(a+b)