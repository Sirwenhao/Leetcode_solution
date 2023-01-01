# 2023/1/1  author:WH
# class Solution:
#     def repeatedCharacter(self, s):
#         for i in range(1, len(s)):
#             if s[i] not in s[:i]:
#                 continue
#             else:
#                 return s[i]

# 2023/1/1  author:github
# from collections import Counter
# class Solution:
#     def repeatedCharacter(self, s):
#         cnt = Counter()
#         for c in s:
#             cnt[c] += 1
#             if cnt[c] == 2:
#                 return c

# 2023/1/1  author:WH
# mask中的第i位用于记录第i个字母是否出现过
class Solution:
    def repeatedCharacter(self, s):
        mask = 0
        for c in s:
            i = ord(c) - ord('a')
            if mask >> i & 1: # >>左移
                return c
            mask |= 1 << i # |表示或 <<右移


if __name__ == "__main__":
    s = "abccbaacz"
    result = Solution().repeatedCharacter(s)
    print(result)