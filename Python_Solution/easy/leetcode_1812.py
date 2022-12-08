# 2022/12/08 author:WH
# 不用构造棋盘，根据索引值即可判断，两个维度索引值如果和为奇数则为白，反之为黑
# 纯数学方法
class Solution:
    def squareIsWhite(self, coordinates):
        if (ord(coordinates[0]) - ord('a') + int(coordinates[1])) % 2 != 0:
            return False
        else:
            return True

# print(ord('b')-ord('a'))

if __name__ == "__main__":
    coordinates = "a1"
    result = Solution().squareIsWhite(coordinates)
    print(result)