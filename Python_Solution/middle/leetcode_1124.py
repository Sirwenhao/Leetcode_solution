# 2023/2/15  author:WH
# 核心是找出一个子序列段，在此子序列内部，大于8的天数严格大于不大于8的天数
# 双指针，字符串子片段内部大于8的字符数超过字符段长度一般即可满足
# 满足条件的长度可能有多组，但要取其中长度最长的那一个
# 核心意思是找到满足子序列中包含超过半数子序列长度数量大于8值的最长子序列

# # 卡在了如何更新左右指针上
# class Solution:
#     def overNum(self, ans, num):
#         flag = 0
#         for i in ans:
#             if i > num:
#                 flag += 1
#         return flag > len(ans)//2
    
#     def longestWPI(self, hours):
#         i = 0
#         result = []
#         while i < len(hours):
#             left = i
#             res = []
#             for right in range(left+1, len(hour)):
#                 ans = hours[left:right+1]
#                 if self.overNum(ans, 8) and len(ans) > len(res):
#                     res = ans
#             i += 1
#             result.append(res)
        
#         return 

class Solution:
    def longestWPI(self, hours):
        ans = s = 0
        pos = {}
        for i,x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                ans = i + 1
            elif s - 1 in pos:
                ans = max(ans, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        print(pos)
        return ans



if __name__ == "__main__":
    hours = [9,9,6,0,6,6,9]
    result = Solution().longestWPI(hours)
    print(result)

    

