# 2022/12/06 author:WH
# 字符串的replace方法之后返回的是一个全新的字符串，但是原字符串不会改变
class Solution:
    def numDifferentIntegers(self, word):
        # for i in range(len(word)):
        #     # print(word[i])
        #     if 'a' <= word[i] <= 'z':
        #         word = word.replace(word[i], ' ')
        # 双指针：快慢指针
        ans = []
        slow = fast = 0
        while slow < len(word):
            # slow是第一个非空格位
            while slow < len(word) and not word[slow].isdigit():
                slow += 1
            fast = slow
            while fast < len(word) and word[fast].isdigit():
                fast += 1
            if fast-slow>1 and word[slow] == '0':
                slow += 1
            if word[slow:fast] not in ans:
                ans.append(word[slow:fast])
            slow = fast
        return ans
        

if __name__ == "__main__":
    word = "a123bc34d8ef34"
    result = Solution().numDifferentIntegers(word)
    print(result)

