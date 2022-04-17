"""
    1、统计最常见的单词，不能在banned内，标点符号不算
    2、python如何以标点或者空格区分字符串
"""

# def mostCommonWord(paragraph, banned):
#     for i in paragraph:
#         if not i.isalpha() and i != " ":
#             paragraph = paragraph.replace(i, '')
#     lst = list(paragraph.lower().split(" "))
#     # print(lst)
#     k = 0
#     # lst1 = []
#     for i in range(len(lst)):
#         if lst[i] in banned:
#             # print(lst[i])
#             lst.remove(lst[i])
#             k += 1
#     print(lst)
#     max_v = 0
#     for j in lst:
#         print(j)
#         num = lst.count(j)
#         print(num)
#         max_v = max(max_v, num)
#     return max_v

# 解法二：官解

from collections import Counter

def mostCommonWord(paragraph, banned):
    ban = set(banned)
    freq = Counter()
    word, n = "", len(paragraph)
    for i in range(n+1):
        if i < n and paragraph[i].isalpha():
            word += paragraph[i].lower()
        elif word:
            if word not in ban:
                freq[word] += 1
            word = ""
    maxFreq = max(freq.values())
    return next(word for word, f in freq.items() if f == maxFreq)




paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# print('hit' in banned)


result = mostCommonWord(paragraph, banned)
print(result)
# paragraph = paragraph.translate(str.maketrans(",", string.punctuation))
# for i in paragraph:
    # print(i)
    # if not i.isalpha() and i != " ":
        # print(i)
        # paragraph = paragraph.replace(i, '')
        # print(paragraph)
# paragraph = paragraph.replace(",", "")
# paragraph = paragraph.replace(".", "")
# lst = list(paragraph.lower().split(" "))
# num = lst.count('hit')
# print(lst)
# print(num)