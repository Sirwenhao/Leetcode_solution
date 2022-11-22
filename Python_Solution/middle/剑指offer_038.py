# 2022/11/19 author:WH
# moorethreads二面笔试题
# 剑指offer38字符串全排列

# leetcode评论区答案
# class Solution:
#     def permutation(self, s):
#         def backtrack(s, ans, temp, index, end):
#             if index==end:
#                 ans.append(temp)
#             else:
#                 for i in range(end):
#                     if visit[i] or (i>0 and not visit[i-1] and s[i]==s[i-1]):
#                         continue
#                     visit[i]=True
#                     temp += s[i]
#                     backtrack(s,ans,temp,index+1,end)
#                     temp = temp[:-1]
#                     visit[i]=False

#         global visit
#         n = len(s)
#         ans = []
#         temp = ""
#         visit = [False for _ in range(n)]
#         s=list(s)
#         s.sort()
#         backtrack(s,ans,temp,0,n)
#         return ans

# # 2022/11/19 author:newcoder
# # 相对理解较容易
# class Solution:
#     def permutation(self, s):
#         n = len(s)
#         if n <= 1:
#             return [s]
#         ans = []
#         for i in range(n):
#             s1 = s[i]
#             for s2 in self.permutation(s[:i]+s[i+1:]):
#                 new_str = s1+s2
#                 if new_str not in ans:
#                     ans.append(new_str)
#         ans.sort()
#         return ans

# 2022/11/19 author:WH
# 参考代码随想录的全排列写法
# 错解
# class Solution:
#     def permutation(self, s):
#         # 结果集
#         res = []
#         def backtracking(s, preStr, index):
#             if index == len(s):
#                 res.append(preStr)
#             else:
#                 for i in s:
#                     # 拷贝一份新的调用，否则无法正常循环
#                     pre = preStr[:]
#                     pre += i
#                     left_s = s[:]
#                     backtracking(left_s, pre, index+1)
#         backtracking(s, '', 0)
#         return list(set(res))

# # 2022/11/19 回溯
# class Solution:
#     def permutation(self, s):
#         def backtracking(s, index, end):
#             if index == end-1:
#                 res.append(''.join(s))
#                 return
#             dic = set()
#             for i in range(index, end):
#                 if s[i] in dic:continue
#                 dic.add(s[i])
#                 s[i], s[index] = s[index], s[i]
#                 backtracking(s, index+1, end)
#                 s[i], s[index] = s[index], s[i]

#         res = []
#         s = list(s)
#         backtracking(s, 0, len(s))
#         return res

# # 2022/11/20  author:WH
# # 没有办法解决重复字符问题，如aab
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = ''

#     def permutation(self, s):
#         self.ans.clear()
#         self.backtracking(s, 0)
#         return self.ans
        
#     def backtracking(self, s, start_index):
#         if len(self.current) == len(s):
#             self.ans.append(self.current[:])
#             return
#         for i in range(len(s)):
#             # 剪枝条件，如果当前字符已经在current中了，就跳过当前的这个找下一个
#             if s[i] in self.current:
#                 continue
#             self.current += s[i]
#             self.backtracking(s, start_index+1)
#             self.current = self.current[:-1]

# 2022/11/22 author:WH
# 上述方法在去重的逻辑部分还不够完善，并不能解决一个字符只用一次的限定问题
# 想法：开辟一组与字符串等长的标志位，默认全为False，如果用到就置为True
class Solution:
    def __init__(self):
        self.ans = []
        self.current = ''

    def permutation(self, s):
        flag = [False for _ in range(len(s))]
        self.ans.clear()
        self.backtracking(s, 0, flag)
        return self.ans

    def backtracking(self, s, start_index, flag):
        if len(self.current) == len(s):
            self.ans.append(self.current)
            return
        for i in range(len(s)):
            if flag[i]:
                continue
            flag[i] = True
            self.current += s[i]
            self.backtracking(s, start_index+1, flag)
            flag[i] = False
            self.current = self.current[:-1]


if __name__ == "__main__":
    s = "ABC"
    result = Solution().permutation(s)
    print(result)
    