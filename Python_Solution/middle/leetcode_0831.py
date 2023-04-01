# 2023/4/1  author:WH

class Solution:
    def maskPII(self, s):
        if s[0].isalpha():
            s = s.lower()
            return s[0] + '*****' + s[s.find('@')-1:]
        s = ''.join(c for c in s if c.isdigit())
        cnt = len(s)-10
        surf = '***-***-' + s[-4:]
        return surf if cnt == 0 else f'+{"*" * cnt}-{surf}'
    
# # leetcode官解
# class Solution:
#     def maskPII(self, s):
#         at = s.find('@')
#         if at >= 0:
#             return (s[0] + '*'*5 + s[at-1:]).lower()
#         s = "".join(i for i in s if i.isdigit())
#         return ["", "+*-", "+**-", "+***-"][len(s) - 10] + "***-***-" + s[-4:]

    
if __name__ == "__main__":
    # s = "LeetCode@LeetCode.com"
    s = '1(234)567-890'
    result = Solution().maskPII(s)
    print(result)