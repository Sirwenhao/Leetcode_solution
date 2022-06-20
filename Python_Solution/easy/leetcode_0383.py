"""
1、383赎金信
2、哈希表专题
"""
# 2022/6/20  author:WH
# class Solution:
#     def canConstruct(self, ransomNote, magazine):
#         dic1 = {}
#         dic2 = {}
#         for i in ransomNote:
#             if i in dic1:
#                 dic1[i] += 1
#             else:
#                 dic1[i] = 1
#         print('dic1:', dic1)
#         for j in magazine:
#             if j in dic2:
#                 dic2[j] += 1
#             else:
#                 dic2[j] = 1
#         print('dic2:', dic2)
        
#         for k in dic1:
#             if k in dic2 and dic2[k] >= dic1[k]:
#                 continue
#             else:
#                 return False
#         return True

# 2022/6/20  author:代码随想录
class Solution:
    def canConstruct(self, ransomNote, magazine):
        arr = [0] * 26
        for x in magazine:
            arr[ord(x) - ord('a')] += 1
        for x in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1
        return True


if __name__ == "__main__":
    ransomNote = "fihjjjjei"
    magazine = "hjibagacbhadfaefdjaeaebgi"
    result = Solution().canConstruct(ransomNote, magazine)
    print(result)


