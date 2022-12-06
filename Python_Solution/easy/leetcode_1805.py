# 2022/12/06 author:WH
# 字符串的replace方法之后返回的是一个全新的字符串，但是原字符串不会改变
# class Solution:
#     def numDifferentIntegers(self, word):
#         # for i in range(len(word)):
#         #     # print(word[i])
#         #     if 'a' <= word[i] <= 'z':
#         #         word = word.replace(word[i], ' ')
#         # 双指针：快慢指针
#         ans = []
#         slow = fast = 0
#         while slow < len(word):
#             # slow是第一个非空格位
#             while slow < len(word) and not word[slow].isdigit():
#                 slow += 1
#             fast = slow
#             while fast < len(word) and word[fast].isdigit():
#                 fast += 1
#             if fast-slow>1 and word[slow] == '0':
#                 slow += 1
#             if word[slow:fast] not in ans:
#                 ans.append(word[slow:fast])
#             slow = fast
#         return ans
        
# leetcode提交版本
class Solution:
    def numDifferentIntegers(self, word):
        slow = fast = 0
        n = len(word)
        ans = []
        while True:
            while slow < n and not word[slow].isdigit():
                slow += 1
            if slow == n:
                break
            fast = slow
            while fast < n and word[fast].isdigit():
                fast += 1
            while fast-slow>1 and word[slow] == 0:
                slow += 1
            if not word[slow:fast] in ans:
                ans.append(word[slow:fast])
            slow = fast
        return len(ans)



if __name__ == "__main__":
    word = "a123bc34d8ef34"
    result = Solution().numDifferentIntegers(word)
    print(result)

