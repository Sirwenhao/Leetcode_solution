"""
1、哈希表专题
2、字母异位序：两个字符串其中所包含的字符出现次数相同
"""
# 初步想法：遍历字符串s，把s中的字符作为键，其出现次数作为值，存成字典
class Solution:
    def isAnagram(self, s, t):
        record = [0] * 26
        # 这个操作可以统计所有字符出现的频次
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1
        print(record)
        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1

        for i in range(26):
            if record[i] != 0:
                return False
                break      
        return True

if __name__ == "__main__":
    s = 'recordsdss'
    t = 'recordsdss'
    result = Solution().isAnagram(s, t)
    print(result)