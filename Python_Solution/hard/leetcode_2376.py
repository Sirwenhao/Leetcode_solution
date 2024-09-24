# 24/9/20 @author:WH

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        def isUnique(num):
            n = len(str(num))
            s = set(str(num))
            if n == len(s):
                return 1
            else:
                return 0
        ans = 0
        for i in range(1, n+1):
            ans += isUnique(i)
        return ans
    
    
# 24/9/24 @author:WH
# 数位DP

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # @cache
        def dfs(i, mask, lead, limit):
            if i >= len(s):
                return int(lead ^ 1)
            up = int(s[i]) if limit else 9
            ans = 0
            for j in range(up + 1):
                if mask >> j & 1:
                    continue
                if lead and j == 0:
                    ans += dfs(i + 1, mask, True, limit and j == up)
                else:
                    ans += dfs(i+1, mask | 1 << j, False, limit and j == up)
            return ans

        s = str(n)
        return dfs(0, 0, True, True)
        
    
    
if __name__ == "__main__":
    n = 135
    result = Solution().countSpecialNumbers(n)
    print(result)
