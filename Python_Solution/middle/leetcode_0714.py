"""
    1、买卖股票的最佳时机含手续费
"""
# 2022/8/3  author:WH
# class Solution:
#     def maxProfit(self, prices, fee):
#         ans = 0
#         minPrice = prices[0]
#         for i in range(1, len(prices)):
#             if prices[i] < minPrice:
#                 minPrice = prices[i]
#             if prices[i] >= minPrice and prices[i] <= minPrice+fee:
#                 continue
#             if prices[i] > minPrice+fee:
#                 ans += prices[i] - minPrice - fee
#                 minPrice = prices[i] - fee
#         return ans

# 2022/8/3  author:github高赞
# 和心思想：动态规划解法
# 动态规划法。
# 设 f1 表示当天持有股票的最大利润，f2 表示当天没持有股票的最大利润。
# 初始第 1 天结束时，f1 = -prices[0]，f2 = 0。
# 从第 2 天开始，当天结束时：
# 若持有，则可能是前一天持有，今天继续持有；也可能前一天没持有，今天买入，f1 = max(f1, f2 - price)。
# 若没持有，则可能是前一天持有，今天卖出；也可能是前一天没没有，今天继续没持有，f2 = max(f2, f1 + price - fee)。
# 最后返回 f2 即可。

# class Solution:
#     def maxProfit(self, prices, fee):
#         f1, f2 = -prices[0], 0
#         for price in prices[1:]:
#             f1 = max(f1, f2-price)
#             f2 = max(f2, f1+price-fee)
#         return f2

# 2022/9/2  author:WH
class Solution:
    def maxProfits(self, prices, fee):
        ans = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            # 情况二：相当于买入
            if prices[i] < minPrice:
                minPrice = prices[i]
            # 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
            if prices[i] >= minPrice and prices[i] <= minPrice + fee:
                continue
            # 情况一：可以售卖
            if prices[i] > minPrice + fee:
                # 累加每天的收益
                ans += prices[i] - minPrice - fee
                # 更新最小值（如果还在收获利润的去建立，表示并不是真正的卖出。
                # 而计算利润每次都要减掉手续费，所以要minPrice = prices[i] - fee
                # 这样在明天收获利润的时候，才不会多减一次手续费）
                minPrice = prices[i] - fee
        return ans


if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2
    result = Solution().maxProfits(prices, fee)
    print(result)