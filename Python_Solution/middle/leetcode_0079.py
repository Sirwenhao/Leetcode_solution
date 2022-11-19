# 2022/11/17 author:WH
# 回溯(深度优先搜索)

# class Solution:
#     def exist(self, board, word):
#         def dfs(i, j, cur):
#             if cur == len(word):
#                 return True
#             if i<0 or i>=m or j<0 or j>=n or board[i][j]=='0' or word[cur]!=board[i][j]:
#                 return False
#             t = board[i][j]
#             board[i][j] = '0'
#             for a,b in ([0,1],[0,-1],[1,0],[-1,0]):
#                 x, y = a+i, b+j
#                 if dfs(x,y,cur+1):
#                     return True
#             board[i][j] = t
#             return False
#         m,n = len(board), len(board[0])
#         return any(dfs(i,j,0) for i in range(m) for j in range(n))

# # 2022/11/18 author:WH
# # 默写:核心算法是回溯加剪枝条件
# class Solution:
#     def exist(self, board, word):
#         ans = [0]*len(word)
#         m, n = len(board), len(board[0])
#         def dfs(l, r, board):
#             for k in range(len(word)):
#                 for i,j in ([0, 1], [1, 0], [-1, 0], [0, -1]):
#                     if board[l][r] == word[k]:
#                         k += 1
#                         return True
#                     l += i
#                     r += j
#                     dfs(l, r, board)

# 2022/11/18 author:WH
# 上面没写出来，参考解答，关键步骤注释
class Solution:
    def exist(self, board, word):
        def dfs(i, j, cur):
            if cur == len(word):
                return True
            if i<0 or j<0 or i>=m or j>=n or board[i][j]=='0' or word[cur]!=board[i][j]:
                return False
            t = board[i][j]
            board[i][j] = '0'
            for a,b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x, y = i+a, j+b
                if dfs(x, y, cur+1):
                    return True
            board[i][j] = t
            return False
        m, n = len(board), len(board[0])
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))

# # leetcode官解
# class Solution:
#     def exist(self, board, word):
#         directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
#         def check(i, j, k):
#             if board[i][j] != word[k]:
#                 return False
#             if k == len(word)-1:
#                 return True
#             visited.add((i, j))
#             result = False
#             for di, dj in directions:
#                 newi, newj = i+di, j+dj
#                 if 0<= newi < len(board) and 0<=newj < len(board[0]):
#                     if (newi, newj) not in visited:
#                         if check(newi, newj, k+1):
#                             result = True
#                             break
#             visited.remove((i, j))
#             return result
#         h, w = len(board), len(board[0])
#         visited = set()
#         for i in range(h):
#             for j in range(w):
#                 if check(i, j, 0):
#                     return True
#         return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = Solution().exist(board, word)
    print(result)
