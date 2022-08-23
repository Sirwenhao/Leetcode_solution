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
# class Solution:
#     def canCompleteCircuit(self, gas, cost):
#         start = 0
#         curSum = 0
#         totalSum = 0
#         for i in range(len(gas)):
#             curSum += gas[i] - cost[i]
#             totalSum += gas[i] - cost[i]
#             if curSum < 0:
#                 curSum = 0
#                 start = i+1
#         if totalSum < 0:
#             return -1
#         return start

# 2022/8/23  author:WH
# 如果要能到达终点，关键点肯定是能一直往前走，也就是说当前状态之前的油量大于等于接下来的路程量
class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        i = j = n-1
        cnt = rest = 0
        while cnt < n:
            rest += gas[j] - cost[j]
            cnt += 1
            j = (j+1) % n
            while rest < 0 and cnt < n:
                i -= 1
                rest += gas[i] - cost[i]
                cnt += 1
        return -1 if rest < 0 else i


if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = Solution().canCompleteCircuit(gas, cost)
    print(result)