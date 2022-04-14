"""
    1、多米诺骨牌，有想到先进行排序然后对比
"""

# def numEquivDominoPairs(dominos):
#     dominos = [sorted(lst) for lst in dominos]
#     cnt = 0
#     for l in dominos:
#         if dominos.count(l) > 1:
#             dominos.remove(l)
#             cnt += 1

#     return cnt

def numEquivDominoPairs(dominoes) -> int:
    n = len(dominoes)
    cnt = 0
    cntMapper = dict()

    for a, b in dominoes:
        k = str(a) + str(b) if a > b else str(b) + str(a)
        cntMapper[k] = cntMapper.get(k, 0) + 1
    for k in cntMapper:
        v = cntMapper[k]
        if v > 1:
            cnt += (v * (v - 1)) // 2
    return cnt

dominos = [[1,2],[2,1],[3,4],[1,2],[6,5]]
result = numEquivDominoPairs(dominos)
print(result)


# # dominos = sorted(dominos.item())
# # dominos = map(lambda lst:lst.sort(), dominos)
# # for lst in dominos:
# #     lst.sort()

# print(dominos)
# dominos = [sorted(lst) for lst in dominos]
# print(dominos)