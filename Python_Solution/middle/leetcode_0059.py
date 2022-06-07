"""
    1、螺旋矩阵II
    2、数组专题
"""
# 2022/6/6 author:WH
# 应该包含四层循环，用于模拟矩阵四条边的循环过程
class Solution:
    def generateMatrix(self, n):
        # 每一条边在循环时，都应该坚持左闭右开或者左开右闭的原则
        count = 1
        # 定义起始位置坐标
        start_x, start_y = 0, 0
        mid, loop = n // 2, n // 2
        # 生成空矩阵用于后续存放数据
        nums = [[0] * n for _ in range(n)]
        # 每次填充数字都是先从外部进行，然后循环到内层
        # 因此内层循环的上限使用n-offset，通过offset来控制递减
        for offset in range(1, loop+1):
            # 从左到右
            for i in range(start_x, n - offset):
                nums[start_x][i] = count
                count += 1
            # 从上到下
            for i in range(start_y, n - offset):
                nums[i][n - offset] = count
                count += 1
            # 从右到左
            for i in range(n - offset, start_y, -1):
                nums[n - offset][i] = count 
                count += 1
            # 从下到上
            for i in range(n - offset, start_x, -1):
                nums[i][start_y] = count
                count += 1
            start_x += 1
            start_y += 1

        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

# # leetcode官解 
# class Solution:
#     def generateMatrix(self, n):
#         matrix = [[0] * n for _ in range(n)]
#         count = 1
#         left, right, top, bottom = 0, n-1, 0, n-1
#         while left <= right and top <= bottom:
#             # 上方从左到右
#             for col in range(left, right + 1):
#                 matrix[top][col] = count
#                 count += 1
#             # 右侧从上到下
#             for row in range(top+1, bottom+1):
#                 matrix[row][right] = count
#                 count += 1
#             if left < right and top < bottom:
#                 # 下侧从右到左
#                 for col in range(right-1, left, -1):
#                     matrix[bottom][col] = count
#                     count += 1
#                 for row in range(bottom, top, -1):
#                     matrix[row][left] = count
#                     count += 1

#             left += 1
#             right -= 1
#             top += 1
#             bottom -= 1

#         return matrix

if __name__ == "__main__":
    n = 4
    result = Solution().generateMatrix(n)
    print(result)
