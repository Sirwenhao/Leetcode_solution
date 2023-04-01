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
    
if __name__ == "__main__":
    # s = "LeetCode@LeetCode.com"
    s = '1(234)567-890'
    result = Solution().maskPII(s)
    print(result)