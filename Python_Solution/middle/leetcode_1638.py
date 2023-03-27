# 2023/3/27  author:WH
# 需要有一个判断是否是为子串的函数，给定两个字符串a和A，要能判断出a是否为A的子串


# github解法
# 解法一：枚举，枚举s和t中不同的字符的位置，向左右两侧拓展，直到遇到不同的字符为止。
# 如此，即可得到以该位置为中心的满足条件的子串对数目
class Solution:
    def countSubstrings(self, s, t):
        ans = 0
        m, n = len(s), len(t)
        for i,a in enumerate(s):
            for j,b in enumerate(t):
                if a != b:
                    l = r = 0
                    while i > l and j > l and s[i-l-1] == t[j-l-1]:
                        l += 1
                    while i+r+1 < m and j+r+1 < n and s[i+r+1] == t[j+r+1]:
                        r += 1
                    ans += (l+1) * (r+1)
        return ans

    # def isSubstrings(self, str1, str2):
    #     for i in str2:
    #         if i == str1[0] and str1 == str2[i:i+len(str1)]:
    #             return True
    #         else:
    #             continue
    #     return False

if __name__ == "__main__":
    s = "abe"
    t = "bbc"
    result = Solution().countSubstrings(s, t)
    print(result)