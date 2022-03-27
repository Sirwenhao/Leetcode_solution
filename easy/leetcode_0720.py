"""
    1、leetcode720求列表中长度最长的单词
    2、下列揭发可以通过测试实例，但是上传报错
    3、如果列表中有同样长度的单词，无法区分
"""

# def longestWord(word):
#     dic = {}
#     for j in word:
#         l = len(list(j))
#         dic1 = {l: j}
#         dic.update(dic1)
#     m = max(dic.keys())
#     return dic[m]
#
# words = ["a","banana","app","appl","ap","apply","apple","bnanan"]
#
# result = longestWord(words)
# print(result)


def longestWord(words):
    words.sort(key=lambda x: (-len(x), x), reverse=True)
    longest = ""
    candidates = {""}
    for word in words:
        if word[:-1] in candidates:
            b = word[:-1]
            longest = word
            candidates.add(word)
    return longest

# def longestWord(words):
#     words.sort()
#     res = set([''])
#     longestWord = ''
#     for word in words:
#         # print('word[:-1]:', word[:-1])
#         if word[:-1] in res:
#             res.add(word)
#             if len(word) > len(longestWord):
#                 longestWord = word
#     return longestWord


words = ["a","banana","app","appl","ap","apply","apple","bnanannnn"]
# words.sort()
# words.sort(key=lambda x:(-len(x), x), reverse=True)
# print(words)

result = longestWord(words)
print(result)