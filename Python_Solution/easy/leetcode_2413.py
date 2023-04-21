# 2023/4/21  author:WH

class Solution:
    def smallestEvenMultiple(self, n):
        return n if n % 2 == 0 else 2*n
    

if __name__ == "__main__":
    n = 5
    result = Solution().smallestEvenMultiple(n)
    print(result)