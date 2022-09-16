"""
    翻转单词顺序
    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
    为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student.",
    则输出"student. a am I".
"""
# 2022/09/16  author:WH
class Solution:
    def allReverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    def wordReverse(self, nums):
        slow = fast = 0
        ans = []
        while slow < len(nums):
            while fast < len(nums) and nums[fast] != ' ':
                ans.append(nums[slow])
            self.allReverse(ans, slow, fast+1)
            slow = fast + 1
            fast += 1
        return None

    def sentenceReverse(self, s):
        sList = [i for i in s]
        l = self.allReverse(sList, 0, len(sList)-1)
        self.wordReverse(l)
        return ''.join(l)