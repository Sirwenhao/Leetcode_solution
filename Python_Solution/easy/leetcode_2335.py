# 2023/2/11 author:WH

class Solution:
    def fillCups(self, amount):
        ans = 0
        while sum(amount):
            amount.sort()
            amount[-1] -= 1
            amount[-2] = max(0, amount[-2]-1)
            ans += 1
        return ans

if __name__ == "__main__":
    amount = [1,4,2]
    # amount = [5,4,4]
    result = Solution().fillCups(amount)
    print(result)