# 2023/2/18  author:WH

class Solution:
    def findSolution(self, customfunction, z):
        ans = []
        y = 1000
        for x in range(1, 1001):
            while y and customfunction.f(x, y) < z:
                y -= 1
            if y == 0:
                break
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans
    
# github解法
from bisect import bisect_left
class Solution:
    def findSolution(self, customfunction, z):
        ans = []
        for x in range(1, z+1):
            y = 1 + bisect_left(range(1, z+1), z, key=lambda y:customfunction.f(x, y))
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans
