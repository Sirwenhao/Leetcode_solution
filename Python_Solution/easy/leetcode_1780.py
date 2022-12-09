# 2022/12/09 author:WH
# 判断一个数字能否有3的幂次组成
# 判断与整数幂次相关的问题一般尽量往进制上面思考

class Solution:
    def checkPowersOfThree(self, n):
        while n:
            if n % 3 >= 2:
                return False
            n //= 3
        return True

if __name__ == "__main__":
    n = 12
    result = Solution().checkPowersOfThree(n)
    print(result)