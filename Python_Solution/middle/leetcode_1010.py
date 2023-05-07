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
#                     ans += 1
#         return ans

# # github答案
from collections import Counter
# class Solution:
#     def numPairsDivisibleBy60(self, time):
#         cnt = Counter(t % 60 for t in time)
#         ans = sum(cnt[x] * cnt[60 - x] for x in range(1, 30))
#         ans += cnt[0] * (cnt[0] - 1) // 2
#         ans += cnt[30] * (cnt[30] - 1) // 2
#         return ans

class Solution:
    def numPairsDivisibleBy60(self, time):
        cnt = Counter()
        ans = 0
        for x in time:
            x %= 60
            y = (60 - x) % 60
            ans += cnt[y]
            cnt[x] += 1
        return ans

    
if __name__ == "__main__":
    time = [30, 20, 150, 100, 40]
    result = Solution().numPairsDivisibleBy60(time)
    print(result)