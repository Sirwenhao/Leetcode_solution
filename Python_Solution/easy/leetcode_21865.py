# 2023/1/8  author:WH
# 自己写的解法: 时间复杂度O(N),空间复杂度:O(1)
# class Solution:
#     def prefixCount(self, words, pref):
#         ans = 0
#         i = 0
#         n = len(pref)
#         while i < len(words):
#             if len(words[i]) >= n and words[i][:n] == pref:
#                 ans += 1
#                 i += 1
#             else:
#                 i += 1
#                 continue
#         return ans

# 2023/1/8 author:github
# 一次遍历
class Solution:
    def prefixCount(self, words, pref):
        return sum(w.startswith(pref) for w in words)


if __name__ == "__main__":
    words = ["pay","attention","practice","attend"]
    pref = "at"
    result = Solution().prefixCount(words, pref)
    print(result)
