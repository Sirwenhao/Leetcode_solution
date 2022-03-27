"""
    1、leetcode0121计算最大利润
    2、其实就是计算列表中两个不同数字最大差，但是要求后一个值大于前一个值
"""

# # 解法无误，但会超时
# def maxProfit(prices):
#     m = 0
#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             m = max(m, prices[j] - prices[i])
#     print(m)
#     if m <= 0:
#         return 0
#     else:
#         return m






nums = [7,6,8,3,2]
result = maxProfit(nums)
print(result)