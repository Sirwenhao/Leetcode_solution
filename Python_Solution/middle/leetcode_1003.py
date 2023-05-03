# 2023/5/3  author:WH
# # 可以通过但是时间复杂度和空间复杂度都比较高
# class Solution:
#     def isValid(self, s):
#         if len(s) % 3 != 0:
#             return False
#         i = 0
#         while i <= len(s):
#             if s[i:i+3] == "abc":
#                 s = s[:i] + s[i+3:]
#                 i = 0
#             else:
#                 i += 1
#         return len(s) == 0
    
class Solution:
    def isValid(self, s):
        if len(s) % 3:
            return False
        t = []
        for c in s:
            t.append(c)
            if ''.join(t[-3:]) == 'abc':
                t[-3:] = []
        return not t
    
class Solution:
    def isValid(self, s):
        while True:
            s_ = s.replace("abc", "")
            if s_ == "": return True
            elif s_ == s != "": return False
            s = s_
    
if __name__ == "__main__":
    s = "aabcbc"
    result = Solution().isValid(s)
    print(result)