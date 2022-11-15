# 2022/11/14 author:WH
# 摩尔线程一面算法题
# 矩阵中的元素matrix[row][col]经过90度旋转之后变换到位置matrix[col][n-row-1]

# # 当时写的这个解，写错了
# class Solution:
#     def rotateImage(self, matrix):
#         n = len(matrix) #行
#         m = len(matrix[0]) #列
#         print(m)
#         matrix_new = [[0] * m for _ in range(n)]
#         print(matrix_new)
#         for i in range(m):
#             for j in range(n):
#                 matrix_new[n-i-1][j] = matrix[j][i]
#         matrix[:] =matrix_new
#         return matrix

# leetcode原题时行列数相等，但此题更一般的情况应该是行列不同

# 借鉴别人的算法，先对矩阵转置，再对矩阵水平翻转
# class Solution:
#     def rotateImage(self, matrix):
#         row = len(matrix) #行
#         col = len(matrix[0]) #列
#         for i in range(row):
#             for j in range(i, col-1): # 下限设置为i防止重复遍历，只遍历上三角矩阵
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         print(matrix) # 输出还是原来的维度
#         matrix_new = []
#         for i in range(col):
#             matrix_new.append([a[i] for a in matrix])
#         print(matrix_new)

#         for i in range(row):
#             matrix_new[i] = matrix_new[i][::-1]
#         print(matrix_new)


# 此方法可解，但并非In-place办法
class Solution:
    def rotateImage(self, matrix):
        row, col = len(matrix), len(matrix[0])
        matrix_new = [[matrix[i][j] for i in range(row)] for j in range(col)]
        print(matrix_new)
        for i in range(len(matrix_new)):
            matrix_new[i] = matrix_new[i][::-1]
        return matrix_new

# # 水平翻转+主对角线翻转
# class Solution:
#     def rotateImage(self, matrix):
#         n = len(matrix)
#         for i in range(n // 2):
#             for j in range(n):
#                 matrix[i][j], matrix[n-i-1][j] = matrix[n-1-i][j], matrix[i][j]
#         for i in range(n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         return matrix


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    result = Solution().rotateImage(matrix)
    print(result)