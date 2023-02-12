# 2023/2/12  author:WH
# # 本来是计划先写出board所有字符的位置排列，然后按图索骥
# # 这是第一种做法由图查字符
# class Solution:
#     def alphabetBoardPath(self, target):
#         k = 0
#         board = [[0]*5] * 6
#         print(board)
#         while k < 26:
#             for i in range(6):
#                 for j in range(5):
#                     board[i][j] = chr(97+k)
#             k += 1
#         print(board)

class Solution:
    def alphabetBoardPath(self, target):
        currentX, currentY = 0, 0
        ans = []
        for i in target:
            newX = int(ord(i)-ord('a')) // 5 # 表示行数
            newY = int(ord(i)-ord('a')) % 5 # 表示列数
            if newX < currentX:
                ans.append('U'*(currentX-newX))
            if newX > currentX:
                ans.append('D'*(newX-currentX))
            if newY < currentY:
                ans.append('L'*(currentY-newY))
            if newY > currentY:
                ans.append('R'*(newY-currentY))
            ans.append('i')
            currentX, currentY = newX, newY
        return "".join(ans)



if __name__ == "__main__":
    target = "leet"
    result = Solution().alphabetBoardPath(target)
    print(result)