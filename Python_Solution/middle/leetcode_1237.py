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
    
