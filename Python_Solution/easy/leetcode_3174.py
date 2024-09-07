# 24/9/5  @author:WH

# 解法1: 正则查找+递归
import re
class Solution:
    def clearDigits(self, s):
        match = re.search(r'[a-z][0-9]', s)
        if match:
            num_index = match.start()
            s = s[:num_index] + s[num_index+2:]
            return self.clearDigits(s)
        return s
        
# 解法2: 栈
class Solution:
    def clearDigits(self, s):
        ans = []
        for i in s:
            if i.isalpha():
                ans.append(i)
            elif i.isdigit():
                ans.pop()
        return "".join(ans)
                
            
            
if __name__ == "__main__":
    s = 'avvvbcd345'
    result = Solution().clearDigits(s)
    print(result)