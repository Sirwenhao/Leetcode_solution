# 2023/2/4  author:WH
# 先对coins进行排序，起始元素是从0开始的

# class Solution:
#     def getMaximumConsecutive(self, coins):
#         coins.sort()
#         ans = 1
#         for i in coins:
#             if i > ans:
#                 return ans
#             else:
#                 ans += i
#         return ans

class Solution:
    def getMaximumConsecutive(self, coins):
        coins.sort()
        ans = 0
        for v in coins:
            if v > ans+1:
                break
            ans += v
        return ans+1

if __name__ == "__main__":
    coins = [1,1,1,4]
    result = Solution().getMaximumConsecutive(coins)
    print(result)
