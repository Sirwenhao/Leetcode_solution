# 24/3/16 author:WH
# 2的幂次方的判断，考虑到了除2取余的方法，但效率太低，思维难度太低
# 考虑到了2进制的方法，但没想到按位操作,X与X-1的按位与操作
# 纯数学的方法，取2为底数的对数，返回值必定为整数

# 按位与
# 偶数幂次方是不可能有负数的。。。。。。
import math

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1)) == 0
    
class Solution:
    def isPowerOfTwo(self, n):
        return n>0 and math.log2(n).is_integer()
    
    
if __name__ == "__main__":
    n = 4
    result = Solution().isPowerOfTwo(n)
    print(result)
        

