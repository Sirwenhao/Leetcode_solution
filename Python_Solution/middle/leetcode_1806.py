# 2023/1/10  author:WH

class Solution:
    def reinitializePermutation(self, n):
        perm = [i for i in range(n)]
        target = perm
        ans = 0
        while True:
            perm = [perm[i//2] if i%2 == 0 else perm[n//2 + (i-1)//2] for i in range(n)]
            print(perm)
            ans += 1
            if perm == target:
                return ans

if __name__ == "__main__":
    n = 4
    result = Solution().reinitializePermutation(n)
    print(result)
