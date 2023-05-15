# 2023/5/15  author:WH

# 没有看出来此题的本质是找等价行，所谓等价行指相同的或者互补的行
from collections import Counter
class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())
    
if __name__ == "__main__":
    matrix = [[0,0,0],[0,0,1],[1,1,0]]
    result = Solution().maxEqualRowsAfterFlips(matrix)
    print(result)