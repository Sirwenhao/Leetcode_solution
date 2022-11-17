"""
    1、用于生成所有有效的括号
"""
# # 力扣加加
# class Solution:
#     def generateParenthesis(self, n):
#         res = []
#         def dfs(l, r, s):
#             if l > n or r > n: return
#             if (l == r == n): res.append(s)
#             if l < r: return
#             # 加一个左括号
#             dfs(l+1, r, s + '(')
#             # 加一个右括号
#             dfs(l, r + 1, s+')')
#         dfs(0, 0, '')
#         return res

# # 爱学习的饲养员,leetcode运行示例竟然超时不能提交
# class Solution:
#     def generateParenthesis(self, n):
#         result = []
#         self.backtracking(n, result, 0, 0, "")
#         return result

#     def backtracking(self, n, result, left, right, s):
#         if right > left:
#             return
#         if(left == n and right == n):
#             result.append(s)
#             return
#         if left < n:
#             self.backtracking(n, result, left+1, right, s+"(")
#         if right < left:
#             self.backtracking(n, result, left, right+1, s+")")

# # 2022/11/13 author:github
# # DFS+剪枝
# # l代表左括号的数目，r代表右括号的数目，t表示当前形成的括号序列
# class Solution:
#     def generateParenthesis(self, n):
#         def dfs(l, r, t):
#             if l > n or r > n or l < r:
#                 return
#             if l == n and r == n:
#                 ans.append(t)
#                 return
#             dfs(l+1, r, t+'(')
#             dfs(l, r+1, t+')')
#         ans = []
#         dfs(0, 0, '')
#         return ans

# 2022/11/17 author:WH
# 错解，忘记了
# class Solution:
#     def generateParenthesis(self, n):
#         def dfs(l, r, t):
#             if l<0 or r<0 or l<r:
#                 return
#             if l==n and r==n:
#                 ans.append(t)
#             dfs(l+1, r, t+'(')
#             dfs(l, r+1, t+')')
#         ans = []
#         dfs(0,0,'')
#         return ans

class Solution:
    def generateParenthesis(self, n):
        def dfs(l, r, t):
            if l>n or r>n or l<r:
                return
            if l==n and r==n:
                ans.append(t)
            dfs(l+1, r, t+'(')
            dfs(l, r+1, t+')')
        ans = []
        dfs(0, 0, '')
        return ans


if __name__ == "__main__":
    n = 2
    result = Solution().generateParenthesis(n)
    print(result)