"""
    1、划分字母区间
    2、一个字母最多只能出现在一个划分好的区间中，不管次数有多少
    3、关键点在于找到之前遍历过的所有字母的最远边界，这个边界即为切割点
"""
# 2022/8/2  author:WH
# 错解
# class Solution:
#     def partitionLabels(self, s):
#         ans = []
#         # 双指针做法
#         start = end = 1
#         while end <= len(s):
#             for i in range(start):
#                 if not(s[i] in s[:end] and s[i] not in s[end:]):
#                     start += 1
#                     end = start
#                 else:
#                     ans.append(start+1)
#                     end = start
#         return ans

# 2022/8/2  author:代码随想录
# class Solution:
#     def partitionLabels(self, s):
#         hash = [0] * 26
#         # 这个hash列表中存储的是对应元素的最大索引，元素的位置对应字母顺序
#         for i in range(len(s)):
#             hash[ord(s[i]) - ord('a')] = i
#         print('hash:', hash)
#         ans = []
#         left = right = 0
#         for i in range(len(s)):
#             right = max(right, hash[ord(s[i]) - ord('a')])
#             # 如果最大出现位置和序号相同，说明此点为切割点
#             if i == right:
#                 ans.append(right - left + 1)
#                 left = right+1
#         return ans

# 2022/8/2  author:github
class Solution:
    def partitionLabels(self, s):
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c)-ord('a')] = i
        ans = []
        left = right = 0
        for i, c in enumerate(s):
            right = max(right, last[ord(c) - ord('a')])
            if i == right:
                ans.append(right - left + 1)
                left = right+1
        return ans


if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    result = Solution().partitionLabels(S)
    print(result)