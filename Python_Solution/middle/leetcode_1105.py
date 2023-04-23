# 2023/4/23  author:WH

from math import inf
class Solution:
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        dp = [inf] * (n+1)
        dp[0] = 0
        for i,b in enumerate(books):
            curWidth = 0
            maxHeight = 0
            j = i
            while j >= 0:
                curWidth += books[j][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                dp[i + 1] = min(dp[i+1], dp[j]+maxHeight)
                j -= 1
        return dp[n]
    
if __name__ == "__main__":
    books = [[1,1], [2,3], [2,3], [1,1], [1,1], [1,1],[1,2]]
    shelfWidth = 4
    result = Solution().minHeightShelves(books, shelfWidth)
    print(result)