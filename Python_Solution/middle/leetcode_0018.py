"""
1、哈希表专题
2、四数之和
"""
# 2022/6/16  author:代码随想录  双指针法
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                l = j + 1
                r = n - 1

                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] > target: r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target: l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: p += 1
                        while l < r and nums[r] == nums[r - 1]: r -= 1
                        l += 1
                        r -= 1
        return res

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


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = Solution().fourSum(nums, target)
    print(result)