"""
    1、补打卡
    2、所谓旋转操作是指只能将左侧的字符传到右侧，将最左侧的字符传到左右侧视为一次循环
    3、解法一自己写的空间换时间，时间复杂度O(N),空间复杂度:O(N)

"""

# # 解法一

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    else:
        for i in range(len(s)):
            # print(s[1:len(s)])
            s = s[1:len(s)] + s[0]
            # print(s)
            if s == goal:
                return True
            else:
                continue
        return i+1 < len(s)


s = "abcde"
# goal = "cdeab"
goal = "abced"

result = rotateString(s, goal)
print(result)