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


# 24/7/16 author:WH
# 24/7/22 author:WH
# 这个问题的本质是矩阵的螺旋遍历

# 矩阵的螺旋遍历

# def spiralOrder(matrix):
#     if not matrix:
#         return []
#     result = []
#     top, bottom = 0, len(matrix) - 1
#     left, right = 0, len(matrix[0]) - 1
    
#     while top <= bottom and left <= right:
#         # 上方从左到右遍历
#         for i in range(left, right+1):
#             result.append(matrix[top][i])
#         top += 1
#         # 右侧从上到下遍历
#         for i in range(top, bottom+1):
#             result.append(matrix[i][right])
#         right -= 1
        
#         # 右侧从右到左遍历
#         if bottom >= top:
#             for i in range(right, left-1, -1):
#                 result.append(matrix[bottom][i])
#         bottom -= 1
        
#         # 左侧从下到上遍历
#         if left <= right:
#             for i in range(bottom, top-1, -1):
#                 result.append(matrix[i][left])
#         left += 1
#     return matrix
                
                
        
        
            
    


class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        count = 1
        # print(matrix)
        top, bottom = 0, n-1
        left, right = 0, n-1
        while top <= bottom and left <= right:
            # 遍历上方从左到右
            for i in range(left, right+1):
                matrix[top][i] = count
                count += 1
            top += 1
            
            # 遍历右侧从上到下
            for i in range(top, bottom+1):
                matrix[i][right] = count
                count += 1
            right -= 1
            
            # 遍历底部从右到左 
            if top <= bottom:    
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = count
                    count += 1
                bottom -= 1
            
            # 遍历左侧从下往上
            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1
                
        return matrix
            
        


if __name__ == "__main__":
    n = 4
    result = Solution().generateMatrix(n)
    print(result)
