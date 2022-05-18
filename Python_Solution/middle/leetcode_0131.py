"""
    1、给定一个字符串，对其进行分割且分割之后的字符串均为回文串
    2、有一个关键点：子串必须是连续的
"""
# 回溯法 author:WH
class Solution:
    def partition(self, s):
        ans = []
        current = []
        start_index = 0
        # 定义一个判断是否满足回文的函数
        def isPalindrome(str):
            left, right = 0, len(str)-1
            while left < right:
                if str[left] != str[right]:
                    return False
                left += 1
                right -= 1
            return True
        # 定义回溯函数主体
        def backtracking(s, start_index):
            if start_index >= len(s):
                ans.append(current[:])
                return
            # 定义单层循环
            for i in range(start_index, len(s)):
                if isPalindrome(s):
                    current += s[start_index:i+1]
                    start_index += 1
                    backtracking(s, start_index)
                    current.pop()
                else:
                    continue
        backtracking(s, start_index)
        return ans

if __name__ == "__main__":
    s = "aab"
    result = Solution().partition(s)
    print(result)

# str = "abba"
# def isPalindrome(str):
#     return str[::1] == str[::-1]
# print(isPalindrome(str))