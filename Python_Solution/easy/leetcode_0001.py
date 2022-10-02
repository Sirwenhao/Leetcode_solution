"""Two Sum"""

"""
    1、Solution One
    2、暴力破解，时间：O(N^2),空间：O(1) 
"""
# class Solution:
#     def twoSum(self, nums, target):
#         l = len(nums)
#         for i in range(l):
#             for j in range(l+1, l): #注意起点l+1
#                 if nums[i] + nums[j] == target:
#                     return [i, j ]
#         return []


"""
    1、Solution Two
    2、hash map
"""

# class Solution:
#     def twoSum(self, nums, target):
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#         return []

# 2022/6/13  author:WH
# 但是此种方法只能返回一组解，有效解可能不止一组
# class Solution:
#     def twoSum(self, nums, target):
#         dic = dict()
#         result = []
#         for i, j in enumerate(nums):
#             dic[j] = i
#         for k in dic:
#             if target - k in dic and target - k > k:
#                 result.append([dic[k], dic[target - k]])
#             else:
#                 continue
#         return result

# 代码随想录解法,同样无法找出所有符合条件的解
# class Solution:
#     def twoSum(self, nums, target):
#         dic = dict()
#         for idx, val in enumerate(nums):
#             if target - val not in dic:
#                 dic[val] = idx
#             else:
#                 return [dic[target - val], idx]

# 2022/10/01  author:WH
class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for idx, val in enumerate(nums):
            if target - val not in dic:
                dic[val] = idx
            else:
                return [idx, dic[target-val]]


if __name__ == "__main__":
    nums = [1,3,5,6,7,9]
    target = 10
    result = Solution().twoSum(nums, target)
    print(result)