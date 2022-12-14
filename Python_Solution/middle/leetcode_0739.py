# 2022/12/14  author:WH
# 每日温度
# # 有点问题
# class Solution:
#     def dailyTemperatures(self, temperatures):
#         slow = 0
#         fast = slow+1
#         ans = [0] * len(temperatures)
#         while fast < len(tempertures):
#             if tempertures[fast] <= tempertures[slow]:
#                 fast += 1
#             else:
#                 ans[slow] = fast-slow
#                 slow += 1
#                 fast = slow+1
#             # if fast == len(temperatures):
#             #     fast = slow+1
#         return ans

# 2022/12/14 author:github
class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0]*len(temperatures)
        stk = []
        for i,v in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < v:
                j = stk.pop()
                ans[j] = i-j
            stk.append(i)
        return ans


if __name__ == "__main__":
    tempertures = [55,38,53,81,61,93,97,32,43,78]
    result = Solution().dailyTemperatures(tempertures)
    print(result)

