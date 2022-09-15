"""
    题目描述：
    现在有一个只包含小写字母的字符串，两个人轮流操作，每次操作可以选择两个相邻的相同字符
    并将其一起消除，游戏将一直进行到其中一个人无法操作，首先无法操作的人将会输掉这场游戏
    请问先手的人能否赢下游戏？

    样例输入：
    3
    abcdcba
    aab
    baab
"""

class Solution:
    def eraseNeighbor(self, s):
        # print(s[0])
        s1 = list(i for i in s[::-1])
        # print(s1)
        cnt = 0
        for ch in s[1:]:
            if ch == s1.pop():
                cnt += 1
            else:
                continue
        if cnt % 2 != 0:
            print('Yes')
        else:
            print('No')

if __name__ == "__main__":
    # s = 'abcdcba'
    s = 'aab'
    # s = 'baab'
    result = Solution().eraseNeighbor(s)
    print(result)