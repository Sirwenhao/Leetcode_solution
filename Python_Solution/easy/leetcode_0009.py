# 2023/4/20  author:WH

# 判断回文数
class Solution:
    def isPalindrome(self, x):
        flag = len(str(x))//2
        i = 0
        while i < flag:
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                return False
            i += 1
        return True

if __name__ == "__main__":
    x = 121
    result = Solution().isPalindrome(x)
    print(result)