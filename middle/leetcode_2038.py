"""
    1、贪心算法，力扣官方题解
"""

def winnerOfGame(colors):
    freq = [0, 0]
    cur, cnt = 'C', 0
    for c in colors:
        if c != cur:
            cur = c
            cnt = 1
        else:
            cnt += 1
            if cnt >= 3:
                freq[ord(cur) - ord('A')] += 1 # ord用于返回字符对应的ASCII码
    return freq[0] > freq[1]

colors = 'ABBBBBBAAA'
result = winnerOfGame(colors)
print(result)