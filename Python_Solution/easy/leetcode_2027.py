# 2022/12/28  author:WH
# 贪心：遍历字符串查找"X"遇到，将指针往后移动三位，当前三位不管如何变化都算作一次操作。如非"X"则指针后移一位
class Solution:
    def minimumMoves(self, s):
        ans = i = 0
        while i < len(s):
            if s[i] == "X":
                i += 3
                ans += 1
            else:
                i += 1
        return ans

if __name__ == "__main__":
    s = "XXOX"
    result = Solution().minimumMoves(s)
    print(result)
