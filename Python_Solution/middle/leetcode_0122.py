"""
    1、买股票的最佳时机拓展版本，可以多次买卖
    2、关键条件是多次买卖不能同步进行
    3、与leetcode121和leetcode309为同一类型的题目
"""


# 此算法应该有问题，奇怪的是竟然通过了leetcode的提交
# class Solution:
#     def maxProfits(self, prices):
#         res = 0
#         for i in range(len(prices)-1):
#             if prices[i+1] > prices[i]:
#                 res += prices[i+1]-prices[i]
#         return res

# 2022/7/30  author:代码随想录
# 贪心算法，关键点在于正利润
class Solution:
    def maxProfits(self, prices):
        res = 0
        for i in range(len(prices)-1):
            res += max(prices[i+1] - prices[i], 0)
        return res

# prices = [7,1,5,3,6,4,10,8,9,1,9]
prices = [1,3,6,7,10]
result = Solution().maxProfits(prices)
print(result)