"""
    1、美丽值得计算是一部分
    2、遍历所有字符串是另一部分
    3、算法应该使用的是递归（判断失误）
    4、包含字符的字符串长度至少为3，当作剪枝条件
"""
# 2022/12/13 author:WH
from collections import Counter
class Solution:
    def beautySum(self, s):
        ans = 0
        n = len(s)
        for i in range(n):
            cnt = Counter()
            for j in range(i, n):
                cnt[s[j]] += 1
                ans += max(cnt.values()) - min(cnt.values())
        return ans

if __name__ == "__main__":
    s = "aabcb"
    result = Solution().beautySum(s)
    print(result)
