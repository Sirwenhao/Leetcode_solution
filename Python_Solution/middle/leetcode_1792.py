# 2023/2/21  author:WH
# 参考github解法
from heapq import heapify, heappop, heappush

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        h = [(a/b - (a+1)/(b+1), a, b) for a,b in classes]
        heapify(h)
        for _ in range(extraStudents):
            _, a, b = heappop(h)
            a, b = a+1, b+1
            heappush(h, (a/b - (a+1)/(b+1), a, b))
        return sum(v[1] / v[2] for v in h) / len(classes)
    
if __name__ == "__main__":
    classes = [[1,2],[3,5],[2,2]]
    extraStudents = 2
    result = Solution().maxAverageRatio(classes, extraStudents)
    print(result)
