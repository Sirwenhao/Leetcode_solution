"""
    1、第一次做力扣中等难度题，当然是不会
    2、好的一点在于此题基本思路还算明白，但具体操作是不会写
"""


def platesBetweenCandles(s, queries):
    n = len(s)
    presum, sum = [0] * n, 0
    left, l = [0] * n, -1
    for i, ch in enumerate(s):
        if ch == '*':
            sum += 1
        else:
            l = i
        presum[i] = sum
        left[i] = l
    right, r = [0] * n, -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            r = i
        right[i] = r
    ans = [0] * len(queries)
    for i, (x, y) in enumerate(queries):
        x, y = right[x], left[y]
        if x >= 0 and y >= 0 and x < y:
            ans[i] = presum[y] - presum[x]
    return ans

s = "**|**|***|"
queries = [[2,5],[5,9]]

result = platesBetweenCandles(s, queries)
print(result)