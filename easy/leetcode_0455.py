<<<<<<< HEAD
"""
    1、分饼干，首先第一步排序，这个没有考虑到其实，这个要重点记一下
"""

# 解法一，有参考力扣加加
def findContentChildren(g: list, s: list):
    g.sort()
    s.sort()
    cnt = 0
    student = biscuits = 0
    while student < len(g) and biscuits < len(s):
        if s[biscuits] >= g[student]:
            student+=1
            cnt += 1
        biscuits += 1

    return cnt



g = [1,4,3,5,3]
s = [1,2,2]
result = findContentChildren(g, s)
print(result)
        
=======
"""
    1、分饼干，首先第一步排序，这个没有考虑到其实，这个要重点记一下
"""

# 解法一，有参考力扣加加
def findContentChildren(g: list, s: list):
    g.sort()
    s.sort()
    cnt = 0
    student = biscuits = 0
    while student < len(g) and biscuits < len(s):
        if s[biscuits] >= g[student]:
            student+=1
            cnt += 1
        biscuits += 1

    return cnt



g = [1,4,3,5,3]
s = [1,2,2]
result = findContentChildren(g, s)
print(result)
        
>>>>>>> 01c7d28b36c2a0d6850f76944563b6ce436cd214
