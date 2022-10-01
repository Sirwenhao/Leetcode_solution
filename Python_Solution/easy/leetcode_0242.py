"""
1、哈希表专题
2、字母异位序：两个字符串其中所包含的字符出现次数相同
"""
# 初步想法：遍历字符串s，把s中的字符作为键，其出现次数作为值，存成字典
# class Solution:
#     def isAnagram(self, s, t):
#         record = [0] * 26
#         # 这个操作可以统计所有字符出现的频次
#         for i in range(len(s)):
#             record[ord(s[i]) - ord("a")] += 1
#         print(record)
#         for i in range(len(t)):
#             record[ord(t[i]) - ord("a")] -= 1

#         for i in range(26):
#             if record[i] != 0:
#                 return False
#                 break      
#         return True

# 2022/10/01  author:WH
# 只要满足所包含的字母相同、字母对应的数量相同即为异序词
# class Solution:
#     def isAnagram(self, s, t):
#         r = [0] * 26
#         for i in s:
#             r[ord(i) - ord('a')] += 1
#         print('r1:', r)
#         for j in t:
#             r[ord(j) - ord('a')] -= 1
#         print('r2:', r)
#         for k in range(26):
#             if r[k] != 0:
#                 return False
#         return True

# 2022/10/01  author:github高赞
# python中all函数：
# all() 函数用于判断给定的可迭代参数 
# iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        r = [0] * 26
        for i in range(len(s)):
            r[ord(s[i]) - ord('a')] += 1
            r[ord(t[i]) - ord('a')] -= 1
        return all(c==0 for c in r)

if __name__ == "__main__":
    s = 'recordsdss'
    t = 'recordsdss'
    result = Solution().isAnagram(s, t)
    print(result)