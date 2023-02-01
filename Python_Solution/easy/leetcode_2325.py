# 2023/2/1  author:WH
# 先从密钥中解出每个字符对应于字母表中的位置，再根据位置解密message
# class Solution:
#     def decodeMessage(self, key, message):
#         key = set(key)
#         # 出错在使用集合去重后原始字符顺序被改变了
#         key.remove(' ')
#         print(key)
#         dic = {}
#         for idx, val in enumerate(key):
#             dic[val] = chr(97+idx)
#         print(dic)
#         ans = "".join(dic.get(c, " ") for c in message) # 此处的.get()方法避免不存在的key引起key error
#         return ans

class Solution:
    def decodeMessage(self, key, message):
        cur = 'a'
        dic = {}
        for c in key:
            if c != " " and c not in dic:
                dic[c] = cur
                cur = chr(ord(cur) + 1)
        print(dic)
        ans = "".join(dic.get(c, " ") for c in message)
        return ans

# author:github
# from string import ascii_lowercase
# class Solution:
#     def decodeMessage(self, key, message):
#         dic = {}
#         i = 0
#         for c in key:
#             if c not in dic:
#                 dic[c] = ascii_lowercase[i]
#                 i += 1
#         return "".join(dic[c] for c in message)


if __name__ == "__main__":
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    result = Solution().decodeMessage(key, message)
    print(result)
