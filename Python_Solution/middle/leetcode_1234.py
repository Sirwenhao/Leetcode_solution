# 2023/2/13 author:WH
# # 没有理解好题意，要求的是替换子串，子串
# from collections import defaultdict
# class Solution:
#     def balancedString(self, s):
#         count_dict = defaultdict(int)
#         for c in s:
#             count_dict[c] += 1
#         l = len(s)//4
#         print(l)
#         # print(count_dict['Q'])
#         return (max(0, count_dict['Q']-l) + max(0, count_dict['W']-l) + max(0, count_dict['E']-l) + max(0, count_dict['R']-l))

# 要找到需要改变的是那些字符，需要改变的有多少个以及子串位置
# 使用Counter计数+双指针

from collections import Counter
class Solution:
    def balancedString(self, s):
        cnt = Counter(s)
        n = len(s)
        if all(v <= n//4 for v in cnt.values()):
            return 0
        ans, j = n, 0
        for i, c in enumerate(s):
            cnt[c] -= 1
            while j <= i and all(v <= n//4 for v in cnt.values()):
                ans = min(ans, i-j+1)
                cnt[s[j]] += 1
                j += 1
        return ans




if __name__ == "__main__":
    # s = "QWER"
    # s = "QQQR"
    s = "WWEQERQWQWWRWWERQWEQ"
    result = Solution().balancedString(s)
    print(result)

