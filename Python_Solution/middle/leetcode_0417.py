"""
    1、太平洋大西洋流水问题，首先看懂题目很关键，非常关键
    2、需要注意边界的处理
"""

# 力扣官解

# # 深度优先搜索DFS
# class Solution:
#     def pacificAtlantic(self, heights):
#         m, n = len(heights), len(heights[0])

#         def search(starts):
#             visited = set()
#             def dfs(x, y):
#                 if (x, y) in visited:
#                     return
#                 visited.add((x, y))
#                 for nx, ny in ((x, y+1), (x, y-1), (x-1, y), (x+1, y)):
#                     if 0<= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
#                         dfs(nx, ny)
#             for x,y in starts:
#                 dfs(x, y)
#             return visited

#         pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
#         atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]
#         return list(map(list, search(pacific) & search(atlantic)))


# 广度优先搜素
class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            q = deque(starts)
            visited = set(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x, y+1), (x, y-1),(x-1, y), (x+1, y)):
                    if 0<=nx<m and 0<=ny<n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            return visited
    
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))