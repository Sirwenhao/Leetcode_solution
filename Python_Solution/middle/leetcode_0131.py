"""
    1、给定一个字符串，对其进行分割且分割之后的字符串均为回文串
    2、有一个关键点：子串必须是连续的
"""
# 回溯法 author:WH
class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.current = []
    def partition(self, s):
        self.ans.clear()
        self.current.clear()
        # 定义回溯函数结构
        def backtracking(s, start_index):
            if start_index >= len(s):
                self.ans.append(self.current[:])
                return
            for i in range(start_index, len(s)):
                if s[start_index:i+1][::1] == s[start_index:i+1][::-1]:
                    self.current.append(s[start_index:i+1])
                    backtracking(s, i+1)
                    self.current.pop()
                else:
                    continue
        backtracking(s, 0)
        return self.ans
        

if __name__ == "__main__":
    s = "aab"
    result = Solution().partition(s)
    print(result)

# str = "abba"
# def isPalindrome(str):
#     return str[::1] == str[::-1]
# print(isPalindrome(str))