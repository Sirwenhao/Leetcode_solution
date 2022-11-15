# 2022/11/15  author:WH
# 初步想法：将其中的所有词存成字典，键是其本身，对应的值为alphabetical顺序
# 若对应的值相等，则属于同一异位序词汇，将其键值存入到同一个列表中，加入结果集


# class Solution:
#     def groupAnagrams(self, strs):
#         ans = []
#         temp = []
#         dic = {}
#         for val in strs:
#             dic[val] = sorted(val)
#         # print(dic)
#         def getKey(dict, value):
#             return [k for k,v in dict.items() if v==value]
        

# 2022/11/15 author:官解
# 学习到了Python中的collections.defaultdict()函数的具体用法，具体可以参考Joplin笔记
import collections
class Solution:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)
        # print('mp:', mp)
        for st in strs:
            # 对字符按字母序排序这点想到了，但是没想到用sorted()
            key = "".join(sorted(st))
            mp[key].append(st)
        # print('mp:', mp)
        return list(mp.values())



if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)