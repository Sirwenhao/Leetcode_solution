"""
    1、解法一：时间复杂度O(m*n*k), 空间复杂度O(n*m)
"""
# 解法一
def shiftGrid(grid, k):
    m = len(grid)
    n = len(grid[0])
    for _ in range(k):
        new_grid = [[0]*m for _ in range(n)]  # 之前报错是把这一步写在了while循环外面
        for i in range(m):
            for j in range(n-1):
                new_grid[i][j+1] = grid[i][j]

        for i in range(m-1):
            new_grid[i+1][0] = grid[i][n-1]
            
        new_grid[0][0] = grid[m-1][n-1]
        grid = new_grid # 这一步也忘记更新了，第二次移动是在前一次移动结果的基础上进行的
    return grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
result = shiftGrid(grid, k)
print(result)

# n = len(grid)
# m = len(grid[0])
# print('n:',n)
# print('m:',m)