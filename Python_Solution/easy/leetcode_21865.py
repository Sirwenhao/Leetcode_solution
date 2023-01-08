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
# 一次遍历, 时间复杂度O(n x m),空间复杂度O(1), 其中 n 和 m 分别是字符串数组 words 和字符串 pref 的长度。
# class Solution:
#     def prefixCount(self, words, pref):
#         return sum(w.startswith(pref) for w in words)

# 2023/1/8  author:github
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0

    def insert(self, w):
        node = self
        for c in w:
            i = ord(c) - ord('a')
            if node.children[i] is None:
                node.children[i] = Trie()
            node = node.children[i]
            node.cnt += 1

    def search(self, pref):
        node = self
        for c in pref:
            i = ord(c) - ord('a')
            if node.children[i] is None:
                return 0
            node = node.children[i]
        return node.cnt


class Solution:
    def prefixCount(self, words, pref):
        tree = Trie()
        for w in words:
            tree.insert(w)
        return tree.search(pref)


if __name__ == "__main__":
    words = ["pay","attention","practice","attend"]
    pref = "at"
    result = Solution().prefixCount(words, pref)
    print(result)
