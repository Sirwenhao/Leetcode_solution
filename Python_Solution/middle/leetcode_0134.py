"""
    1、加油站
"""
# 2022/8/1  author:代码随想录
# class Solution:
#     def canCompleteCircuit(self, gas, cost):
#         curSum = 0
#         minSum = float('inf')
#         for i in range(len(gas)):
#             curSum += gas[i] - cost[i]
#             minSum = min(minSum, curSum)

#         if curSum < 0:
#             return False
#         if minSum >= 0:
#             return 0

#         for i in range(len(gas)-1, 0, -1):
#             minSum += gas[i] - cost[i]
#             if minSum >= 0:
#                 return i
#         return -1

# 2022/8/1  author:代码随想录贪心二
class Solution:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i+1
        if totalSum < 0:
            return -1
        return start


if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = Solution().canCompleteCircuit(gas, cost)
    print(result)