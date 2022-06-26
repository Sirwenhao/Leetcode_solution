"""
    1、字符串专题
"""
# 2022/6/26  author:WH
# 想法：把字符串整体反转，然后删除开头和结尾的空格
# 中间部分就按照空格分隔开，分割之后进行翻转
class Solution: 
    # 删除多余空格，双指针
    def deleteSpace(self, s):
        l, r = 0, len(s) - 1
        while l <= r and s[l] == " ":
            l += 1
        while l <= r and s[r] == " ":
            r -= 1
        tmp = []
        while l <= r:
            if s[l] != " ":
                tmp.append(s[l])
            elif tmp[-1] != " ":
                tmp.append(s[l])
            l += 1
        return tmp
    # 翻转字符串
    def reverseString(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return None

    # 反转每个单词
    def wordsReverse(self, s):
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != " ":
                end += 1
            self.reverseString(s, start, end-1)
            start = end+1
            end += 1
        return None

    def reverseWords(self, s):
        s = self.deleteSpace(s)
        self.reverseString(s, 0, len(s)-1)
        self.wordsReverse(s)
        return ''.join(s)

if __name__ == "__main__":
    s = " the sky is  blue "
    result = Solution().reverseWords(s)
    print(result)

