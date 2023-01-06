# 2023/1/6  author:WH
# 枚举，时间复杂度:O(NlogN)，空间复杂度:O(1), 其中N=num
class Solution:
    def countEven(self, num):
        ans = 0
        for i in range(1, num+1):
            cur = 0
            while i != 0:
                cur += i % 10
                i //= 10
            ans += (cur % 2 == 0)
        return ans
    
if __name__ == "__main__":
    result = Solution().countEven(30)
    print(result)