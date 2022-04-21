"""
    1、山羊拉丁文
    2、核心点：分两种情况判断首字符，末尾都要添加索引长度的字母‘a’
    3、如何获取以空格为间隔的字符
"""

VOWEL_SET = set('aeiouAEIOU')
# 评论区高赞
# def toGoatLatin(sentence):
#     return ' '.join((word if word[0] in VOWEL_SET else word[1:] + word[0]) + 'ma' + (idx+1)*'a'
#                         for idx, word in enumerate(sentence.split()))

def toGoatLatin(sentence):
    str2 = ''
    for idx, word in enumerate(sentence.split()):
        if word[0] in VOWEL_SET:
            str1 = ''.join(word + 'ma' + (idx+1)*'a')
        else:
            str1 = ''.join(word[1:] + word[0] + 'ma' + (idx+1)*'a')
        str2 = str2 + ' ' + str1
    return str2

sentence = "I speak Goat Latin"
result = toGoatLatin(sentence)
print(result)