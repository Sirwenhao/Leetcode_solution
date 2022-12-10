"""
    2022/12/10 author:WH
"""

class Solution:
    def countBits(self, n):
        i = 0
        ans = []
        while i < n+1:
            ans.append(self.CountNum(i))
            i += 1
        return ans


    def CountNum(self, num):
        res = 0
        while num:
            num &= (num-1)
            res += 1
        return res

if __name__ == "__main__":
    n = 5
    result = Solution().countBits(n)
    print(result)