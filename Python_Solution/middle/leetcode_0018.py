"""
1、哈希表专题
2、四数之和
3、难点在于去重的逻辑，我自己总是忘记。另外虽然使用哈希表可以实现去重，但是也要明白列表的去重方法。
"""
# 2022/6/16  author:代码随想录  双指针法
# class Solution:
#     def fourSum(self, nums, target):
#         nums.sort()
#         n = len(nums)
#         res = []
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]: continue
#             for j in range(i+1, n):
#                 if j > i + 1 and nums[j] == nums[j-1]: continue
#                 l = j + 1
#                 r = n - 1

#                 while l < r:
#                     if nums[i] + nums[j] + nums[l] + nums[r] > target: r -= 1
#                     elif nums[i] + nums[j] + nums[l] + nums[r] < target: l += 1
#                     else:
#                         res.append([nums[i], nums[j], nums[l], nums[r]])
#                         while l < r and nums[l] == nums[l + 1]: p += 1
#                         while l < r and nums[r] == nums[r - 1]: r -= 1
#                         l += 1
#                         r -= 1
#         return res

# 2022/6/22  author:WH
# class Solution:
#     def fourSum(self, nums, target):
#         if len(nums) < 4: return []
#         nums.sort()
#         ans = set()
#         for i in range(len(nums) - 3):
#             for j in range(i+1, len(nums) - 2):
#                 left, right = j+1, len(nums) - 1
#                 while left < right:
#                     if nums[i] + nums[j] + nums[left] + nums[right] == target:
#                         ans.add((nums[i], nums[j], nums[left], nums[right]))
#                     if nums[i] + nums[j] + nums[left] + nums[right] < target:
#                         left += 1
#                     else:
#                         right -= 1
#         return list(map(list, ans))

# 2022/7/4  author:WH
# 这个版本还是在去重上差点意思
# class Solution:
#     def fourSum(self, nums, target):
#         if len(nums) < 4: return []
#         nums.sort()
#         ans = []
#         for i in range(len(nums)-3):
#             for j in range(i+1, len(nums)-2):
#                 left, right = j+1, len(nums)-1
#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right] 
#                     if total == target:
#                         ans.append([nums[i], nums[j], nums[left], nums[right]])
#                     if total < target:
#                         left += 1
#                     else:
#                         right -= 1
#         return ans

# # 2022/7/6 0:28  author:WH
# # 关键逻辑在于去重，使用哈希集合去重
# class Solution:
#     def fourSum(self, nums, target):
#         if len(nums) < 4: return []
#         nums.sort()
#         ans = set()
#         for i in range(len(nums)-3):
#             for j in range(i+1, len(nums)-2):
#                 left, right = j+1, len(nums)-1
#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right] 
#                     if total == target:
#                         ans.add((nums[i], nums[j], nums[left], nums[right]))
#                     if total < target:
#                         left += 1
#                     else:
#                         right -= 1
#         return list(map(list, ans))

# 2022/09/21 author:WH
# 感觉代码没有问题，但没能AC
# class Solution:
#     def fourSum(self, nums, target):
#         if len(nums) < 4:
#             return []
#         # 先对nums排序
#         nums.sort()
#         ans = []
#         # 相比三数之和多一层遍历
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)):
#                 # 如果出现了nums[j]==nums[i]的情况，要跳过
#                 if j > i and nums[j] == nums[j-1]:
#                     continue
#                 left = j+1
#                 right = len(nums)-1
#                 while left < right:
#                     total = nums[i] + nums[j] + nums[left] + nums[right]
#                     if total > target:
#                         right -= 1
#                     elif total < target:
#                         left += 1
#                     else:
#                         ans.append([nums[i], nums[j], nums[left], nums[right]])
#                         while left < right and nums[left] == nums[left+1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right-1]:
#                             right -= 1
#                         left += 1
#                         right -= 1
#         return ans

# class Solution:
#     def fourSum(self, nums, target):
#         nums.sort()
#         n = len(nums)
#         res = []
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for k in range(i+1, n):
#                 if k > i + 1 and nums[k] == nums[k-1]:
#                     continue
#                 p = k + 1
#                 q = n - 1
#                 while p < q:
#                     if nums[i] + nums[k] + nums[p] + nums[q] > target: q -= 1
#                     elif nums[i] + nums[k] + nums[p] + nums[q] < target: p += 1
#                     else:
#                         res.append([nums[i], nums[k], nums[p], nums[q]])
#                         while p < q and nums[p] == nums[p + 1]: p += 1
#                         while p < q and nums[q] == nums[q - 1]: q -= 1
#                         p += 1
#                         q -= 1
#         return res

# # 2022/11/12 author:WH
# class Solution:
#     def fourSum(self, nums, target):
#         nums.sort()
#         ans = set()
#         for i in range(len(nums)-3):
#             for j in range(len(nums)-2):
#                 left, right = j+1, len(nums)-1
#                 while left < right:
#                     if nums[i] + nums[j] + nums[left] + nums[right] == target:
#                         ans.add((nums[i], nums[j], nums[left], nums[right]))
#                     if nums[i] + nums[j] + nums[left] + nums[right] < target:
#                         left += 1
#                     else:
#                         right -= 1
#         return list(map(list, ans))


# 23/11/13 author:WH

class Solution:
    def fourSum(self, nums, target):
        ans = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                m, n = j + 1, len(nums)-1
                while m < n:
                    v = nums[i] + nums[j] + nums[m] + nums[n]
                    if v == target:
                        ans.add((nums[i], nums[j], nums[m], nums[n]))
                    if v > target:
                        n -= 1
                    else:
                        m += 1
        return list(map(list, ans))

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    # nums = [2, 2, 2, 2, 2]
    # target = 8
    result = Solution().fourSum(nums, target)
    print(result)