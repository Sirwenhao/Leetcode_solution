"""
    1、图片平滑器
    2、核心点：中心值与其周围8个值之和求平均
"""

# # 力扣加加解法
# def imageSmoother(matrix):
#     m,n = len(matrix), len(matrix[0])
#     # 建立
#     pre = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
#     for i in range(1, m+1):
#         for j in range(1, n +1):
#             pre[i][j] = pre[i-1][j]+ pre[i][j-1] - pre[i-1][j-1] + matrix[i-1][j-1]
#     ans = [[0 for _ in range(n)] for _ in range(m)]
#     # 使用，等价于以(x1,y1)为矩阵左上角以(x2,y2)为矩阵右下角的所有格子的和
#     for i in range(m):
#         for j in range(n):
#             x1,y1,x2,y2 = max(0, i-1),max(0, j-1),min(m-1, i+1),min(n-1, j+1)
#             cnt = (y2 - y1 + 1) * (x2 - x1 + 1)
#             ans[i][j] = (pre[x2+1][y2+1] + pre[x1][y1] - pre[x1][y2+1] - pre[x2+1][y1])//cnt
#     return ans

# 官解

def imageSmoother(img):
    m, n = len(img), len(img[0])
    ans = [[0] * n for _ in range(m)]
    print('ans:',ans)
    for i in range(m):
        for j in range(n):
            total, num = 0, 0
            for x in range(max(i-1, 0), min(i+2, m)):
                for y in range(max(j-1, 0), min(j+2, n)):
                    total += img[x][y]
                    print('total:', total)
                    num += 1
                ans[i][j] = total // num
    return ans

img = [[1,1,1],[1,0,1],[1,1,1,]]
result = imageSmoother(img)
print(result)