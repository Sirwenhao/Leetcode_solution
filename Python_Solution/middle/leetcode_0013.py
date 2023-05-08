# 2023/5/8  author:WH
# Python 3.10及以上版本才有pairwise工具

from itertools import pairwise
class Solution:
    def romanToInt(self, s):
        ans = 0
        r = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        for a, b in pairwise(s):
            if r[a] < r[b]:
                ans -= r[a]
            else:
                ans += r[a]
        return ans + r[s[-1]]
    
if __name__ == "__main__":
    s = "MCMXCIV"
    result = Solution().romanToInt(s)
    print(result)
