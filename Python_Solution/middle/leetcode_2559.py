# 2023/6/2  author:WH

# 超时，通过率92/93
# class Solution:
#     def vowelStrings(self, words, queires):
#         flag = ['a', 'e', 'i','o', 'u']
#         ans = []
#         for q in queires:
#             num = 0
#             # print(words[q[0]:q[1]+1])
#             for s in (words[q[0]:q[1]+1]):
#                 if s[0] in flag and s[-1] in flag:
#                     num += 1
#             ans.append(num)
#             num = 0
#         return ans

# github
from bisect import bisect_right, bisect_left
class Solution:
    def vowelStrings(self, words, quires):
        vowels = set("aeiou")
        nums = [i for i, w in enumerate(words) if w[0] in vowels and w[-1] in vowels]
        return [bisect_right(nums, r) - bisect_left(nums, l) for l, r in quires]


if __name__ == "__main__":
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0,2], [1,4],[1,1]]
    result = Solution().vowelStrings(words, queries)
    print(result)
