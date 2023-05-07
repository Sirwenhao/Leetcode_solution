# 2023/5/7  author:WH
# # 超时
# class Solution:
#     def numPairsDivisibleBy60(self, time):
#         ans = 0
#         n = len(time)
#         time.sort()
#         # print(time)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if (time[i] + time[j]) % 60 != 0:
#                     continue
#                 else:
#                     ans += 1
#         return ans

# 
    
if __name__ == "__main__":
    time = [30, 20, 150, 100, 40]
    result = Solution().numPairsDivisibleBy60(time)
    print(result)