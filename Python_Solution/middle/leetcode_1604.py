# 2023/2/7  author:WH
# # 下述解法缺乏最关键的步骤：先对KeyName和KeyTime的排序操作
# class Solution:
#     def alertNames(self, KeyName, KeyTime):
#         if len(KeyName) < 3:
#             return []
#         res = []
#         flag = 1
#         i = 1
#         while i < len(KeyName):
#             if KeyName[i] == KeyName[i-1] and abs(int(KeyTime[i][:2])-int(KeyTime[i-1][:2]))<=1:
#                 flag += 1
#                 if flag >= 3 and KeyName[i] not in res:
#                     res.append(KeyName[i])
#             i += 1
#         return res

# # 官解
# from collections import defaultdict
# class Solution:
#     def alertNames(self, KeyName, KeyTime):
#         timeMap = defaultdict(list)
#         for name, time in zip(KeyName, keyTime):
#             hour, minute = int(time[:2]), int(time[3:])
#             timeMap[name].append(hour * 60 + minute)

#         ans = []
#         for name, times in timeMap.items():
#             times.sort()
#             if any(t2-t1 <= 60 for t1, t2 in zip(times, times[2:])):
#                 ans.append(name)
#         ans.sort()
#         return ans

# github
from collections import defaultdict
class Solution:
    def alertNames(self, keyName, keyTime):
        d = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            t = int(t[:2]) * 60 + int(t[3:])
            d[name].append(t)
        ans = []
        for name, ts in d.items():
            if (n := len(ts)) > 2:
                ts.sort()
                for i in range(n - 2):
                    if ts[i + 2] - ts[i] <= 60:
                        ans.append(name)
                        break
        ans.sort()
        return ans


if __name__ == "_-main__":
    keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
    keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
    result = Solution().alertNames(keyName, keyTime)
    print(result)
