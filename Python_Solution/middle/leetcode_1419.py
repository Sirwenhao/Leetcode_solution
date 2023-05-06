# 2023/5/6  author:WH
# # 判断是否为有效字符串，还需要考虑字符串中字符的原始顺序
# from collections import Counter
# class Solution:
#     def minNumberOfFrogs(self, croakOfFrogs):
#         temp = Counter(croakOfFrogs)
#         if not temp["c"] == temp["r"] == temp["o"] == temp["a"] == temp["k"]:
#             return -1
#         else:
#             ans = 0
#             n = len(croakOfFrogs)
#             i = 0
#             while i < n:
#                 if croakOfFrogs[i:i+5] == "croak":
#                     i += 5
#                     ans = 1
#                     # continue
#                 else:
#                     ans += 1
#                     i += 5
#         return ans

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):
        if len(croakOfFrogs) % 5 != 0:
            return -1
        idx = {c: i for i, c in enumerate('croak')}
        cnt = [0] * 5
        ans = x = 0
        for i in map(idx.get, croakOfFrogs):
            print(i)
            cnt[i] += 1
            if i == 0:
                x += 1
                ans = max(ans, x)
            else:
                if cnt[i - 1] == 0:
                    return -1
                cnt[i - 1] -= 1
                if i == 4:
                    x -= 1
        return -1 if x else ans


if __name__ == "__main__":
    # croakOfFrogs = "croakcroak"
    croakOfFrogs = "crcoakroak"
    result = Solution().minNumberOfFrogs(croakOfFrogs)
    print(result)



