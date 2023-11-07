# 23/11/06 author:WH
# 最长公共前缀

# class Solution:
#     def longestCommonPrefix(self, strs):
#         def inUse(strs, j):
#             i = 0
#             while i < len(strs)-2 and j <= min(len(strs[i]), len(strs[i+1])):
#                 while strs[i][j] == strs[i+1][j]:
#                     i += 1
#                     continue
#                 else:
#                     return False
#             return True
#         l = 0
#         k = 0
#         if strs[0] == "":
#             return ""
#         while inUse(strs, k):
#             l += 1
#             k += 1
#         return strs[0][:l]

# 23/11/07 author:WH
# 一开始还是自己没有想的很清楚，不难但是关键点没有捋清楚
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) <= 1:
            return strs[0]
        flag = strs[0]
        i = 0
        minLength = len(flag)
        for k in range(1, len(strs)):
            minLength = min(minLength, len(strs[k]))
        while i < minLength:
            for j in strs[1:]:
                if j[i] == flag[i]:
                    continue
                else:
                    return flag[:i]
            i += 1
        return flag[:i]

        

    
if __name__ == "__main__":
    # strs = ["flower", "flow", "flight"]
    strs = ["ab", "a"] 
    # strs = ["dog","racecar","car"]
    result = Solution().longestCommonPrefix(strs)
    print(result)


            


            