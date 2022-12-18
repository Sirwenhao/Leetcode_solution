# author:WH 2022/12/17
# 贪心+双指针
# class Solution:
#     def canChoose(self, groups, nums):
#         n = 0
#         for g in groups:
#             while n + len(g) <= len(nums):
#                 if nums[n:n+len(g)] == g:
#                     n += len(g)
#                     break # 跳出while循环，选择groups中下一个选项
#                 n += 1
#             else:
#                 return False
#         return True

# 贪心枚举：枚举nums中每一位nums[j]做为起点时是否与当前的groups[i]相匹配
# 如果匹配则groups要跳到下一个元素，即i后移一位，同时指针j向后移动groups[i].length位
# 如果不满足匹配，则将j后移一位
# class Solution:
#     def canChoose(self, groups, nums):
#         n, m = len(groups), len(nums)
#         i = j = 0
#         while i < n and j < m:
#             g = groups[i]
#             if g == nums[j:j+len(g)]:
#                 j += len(g)
#                 i += 1
#             else:
#                 j += 1
#         return i == n

# 2022/12/18 review
class Solution:
    def canChoose(self, groups, nums):
        m, n = len(groups), len(nums)
        i = j = 0
        while i < m and j < n:
            g = groups[i]
            if g == nums[j:j+len(g)]:
                j += len(g)
                i += 1
            else:
                j += 1
        return i == m


if __name__ == "__main__":
    groups = [[1,-1,-1],[3,-2,0]]
    nums = [1,-1,0,1,-1,-1,3,-2,0]
    result = Solution().canChoose(groups, nums)
    print(result)