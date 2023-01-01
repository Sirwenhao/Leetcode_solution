# 2023/1/1  author:WH
class Solution:
    def repeatedCharacter(self, s):
        for i in range(1, len(s)):
            if s[i] not in s[:i]:
                continue
            else:
                return s[i]

if __name__ == "__main__":
    s = "abccbaacz"
    result = Solution().repeatedCharacter(s)
    print(result)