# 2023/1/1  author:WH
# class Solution:
#     def repeatedCharacter(self, s):
#         for i in range(1, len(s)):
#             if s[i] not in s[:i]:
#                 continue
#             else:
#                 return s[i]

# 2023/1/1  author:github
from collections import Counter
class Solution:
    def repeatedCharacter(self, s):
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            if cnt[c] == 2:
                return c

if __name__ == "__main__":
    s = "abccbaacz"
    result = Solution().repeatedCharacter(s)
    print(result)