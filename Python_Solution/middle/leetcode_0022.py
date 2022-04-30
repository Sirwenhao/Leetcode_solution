"""
    1、用于生成所有有效的括号
"""
# 力扣加加
def generateParenthesis(n):
    res = []
    def dfs(l, r, s):
        if l > n or r > n: return
        if (l == r == n): res.append(s)
        if l < r: return
        # 加一个左括号
        dfs(l+1, r, s + '(')
        # 加一个右括号
        dfs(l, r + 1, s+')')
    dfs(0, 0, '')
    return res

# # 爱学习的饲养员,leetcode运行示例竟然超时不能提交
# def generateParenthesis(n):
#     result = []
#     backtracking(n, result, 0, 0, "")
#     return result

# def backtracking(n, result, left, right, s):
#     if right > left:
#         return
#     if(left == n and right == n):
#         result.append(s)
#         return
#     if left < n:
#         backtracking(n, result, left+1, right, s+"(")
#     if right < left:
#         backtracking(n, result, left, right+1, s+")")


n = 2
result = generateParenthesis(n)
print(result)