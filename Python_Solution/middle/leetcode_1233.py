# 2023/2/8  author:WH

# # author:WH 核心想法是排序之后进行元素对比
# class Solution:
#     def removeSubfolders(self, folder):
#         folder.sort()
#         # print(folder)
#         ans = folder[:1]
#         for i in folder[1:]:
#             # print(ans[-1][:2])
#             print(i[:len(ans[-1])])
#             # 起初漏掉了此处if语句中的and部分
#             if i[:len(ans[-1])] == ans[-1] and i[len(ans[-1]):len(ans[-1])+1] == '/':
#                 continue
#             else:
#                 # print(i)
#                 ans.append(i)
#         return ans

# # leetcode官解
# class Solution:
#     def removeSubfolders(self, folder):
#         folder.sort()
#         ans = [folder[0]]
#         for i in range(1, len(folder)):
#             if not ((pre := len(ans[-1])) < len(folder[i]) and ans[-1] == folder[i][:pre] and folder[i][pre] == "/"):
#                 ans.append(folder[i])
#         return ans

# # github 时间复杂度 O(n×logn×m)，空间复杂度 O(m)。其中 n 和 m 分别为数组 folder 的长度和数组 folder 中字符串的最大长度。
# class Solution:
#     def removeSubfolders(self, folder):
#         folder.sort()
#         ans = [folder[0]]
#         for f in folder[1:]:
#             m, n = len(ans[-1]), len(f)
#             if m >= n or not (ans[:-1] == f[:m] and f[m] == '/'):
#                 ans.append(f)
#         return ans

# 字典树
class Solution:
    def removeSubfolders(self, folder):


if __name__ == "__main__":
    # folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    result = Solution().removeSubfolders(folder)
    print(result)


