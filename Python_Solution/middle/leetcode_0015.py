"""
    1、给定一个列表，找出和为零的三个数，不能重复
    2、不能重复，首先想到的是数据结构中的集合.用循环可以但是循环嵌套时间复杂度过高
    3、竟然没提前想到先排序，晕~
    4、Python3使用map函数返回的是一个迭代器，使用方法为：map(function, iterable,...)
    5、根据函数function对指定序列元素做映射
"""

# def threeSum(nums):
#     n = len(nums)
#     nums.sort()
#     ans = list()
#     # 枚举a
#     for first in range(n):
#         if first > 0 and nums[first] == nums[first-1]:
#             continue
#         # c对应的指针初始值指向数组的最右端
#         third = n-1
#         target = -nums[first]
#         # 枚举b
#         for second in range(first+1, n):
#             # 需要和上一次枚举的数不同
#             if second > first + 1 and nums[second] == nums[second - 1]:
#                 continue
#             # 需要保证b的指着在c的左侧
#             while second < third and nums[second] + nums[third] > target:
#                 third -= 1

#             # 如果指针重合，随着b后续的增加
#             # 就不会有满足a+b+c=0并且b<c的情况了，退出循环
#             if second == third:
#                 break
#             if nums[second] + nums[third] == target:
#                 ans.append([nums[first], nums[second], nums[third]])
#     return ans

# 2022/5/1 review
# 转换法：确定一个数字，再找另外两个即可
# class Solution:
#     def threeSum(self, nums):
#         # 遇到数组如果与索引顺序无关，可以考虑先进行排序
#         nums.sort()
#         #定义空哈希表，用于存储结果
#         dir = set()
#         # 转换问题
#         for j in range(len(nums)):
#             # 定义双指针
#             left, right = j+1, len(nums)-1
#             while left < right:
#                 if nums[left]+nums[right] == -nums[j]:
#                     dir.add((nums[j], nums[left], nums[right]))
#                 if nums[left]+nums[right] > -nums[j]:
#                     right -= 1 
#                 else:
#                     left += 1
#         return list(map(list, dir))  #直接使用map语法把集合元素转成列表

# class Solution:
#     def threeSum(self, nums):
#         n, res = len(nums), []
#         if n < 3:
#             return res
#         nums.sort()
#         for i in range(n-2):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             j, k = i+1, n-1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     res.append([nums[i], nums[j], nums[k]])
#                     j += 1
#                     k -= 1
#                     while j < n and nums[j] == nums[j-1]:
#                         j += 1
#                     while k > i and nums[k] == nums[k+1]:
#                         k -= 1
#                 elif nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 else:
#                     k -= 1
#         return res

# 2022/6/15  author:代码随想录
# class Solution:
#     def threeSum(self, nums):
#         ans = []
#         n = len(nums)
#         nums.sort()
#         for i in range(n):
#             left = i + 1
#             right = n - 1
#             if nums[i] > 0:
#                 break
#             if i >= 1 and nums[i] == nums[i - 1]:
#                 continue
#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]
#                 if total > 0:
#                     right -= 1
#                 elif total < 0:
#                     left += 1
#                 else:
#                     ans.append([nums[i], nums[left], nums[right]])
#                     while left != right and nums[left] == nums[left + 1]: left += 1
#                     while left != right and nums[right] == nums[right - 1]: right -= 1
#                     right -= 1
#         return ans

# 2022/6/16  author:代码随想录  双指针法
# class Solution:
#     def threeSum(self, nums):
#         if len(nums) < 3: return []
#         nums, res = sorted(nums), []
#         for i in range(len(nums) - 2):
#             cur, l, r = nums[i], i + 1, len(nums) - 1
#             if res != [] and res[-1][0] == cur: continue  # 去重

#             while l < r:
#                 if cur + nums[l] + nums[r] == 0:
#                     res.append([cur, nums[l], nums[r]])
#                     while l < r - 1 and nums[l] == nums[l + 1]:
#                         l += 1
#                     while r > l and nums[r] == nums[r - 1]:
#                         r -= 1
#                 if cur + nums[l] + nums[r] > 0:
#                     r -= 1
#                 else:
#                     l += 1
#         return res

# 2022/6/22  author:WH
# 双指针法，初步想法：左右指针相对比较好固定，但是中间指针需要单独的遍历
# 情况考虑不清楚

# class Solution:
#     def threeSum(self, nums):
#         # 漏掉了一种情况
#         if len(nums) < 3: return []
#         # 先排序
#         nums.sort()
#         ans = []
#         # 设置中间数
#         for i in range(1, len(nums) - 2):
#             # 定义左右指针
#             left, right = i+1, len(nums) - 1
#             if ans != [] and ans[-1][0] == nums[i]: continue   # 去重
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] == 0:
#                     ans.append([nums[i], nums[left], nums[right]])
#                     while left < right - 1 and nums[left] == nums[left+1]:
#                         left += 1
#                     while right > left and nums[right] == nums[right-1]:
#                         right -= 1
#                 if nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     left += 1
#         return ans

# 2022/7/3  author:WH
# 这个版本的解答有些问题，并不能完全返回全部解集
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         # 此处使用哈希表是为了去重
#         ans = set()
#         for i in range(len(nums)-2):
#             left, right = i+1, len(nums)-1
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] == 0:
#                     ans.add((nums[i], nums[left], nums[right]))  # 这一步是重点
#                 if nums[i] + nums[left] + nums[right] < 0:
#                     left += 1
#                 else:
#                     right -= 1
#         # map函数将哈希集合ans映射成为list
#         return list(map(list, ans))

# 2022/09/20  author:WH
# class Solution:
#     def threeSum(self, nums):
#         # 又一次忘掉排序
#         nums.sort()
#         ans = []
#         for i in range(len(nums)):
#             left, right = i+1, len(nums)-1
#             # 排序之后的nums前面一定有元素值为负数
#             if nums[i] > 0:
#                 break
#             if i >= 1 and nums[i] == nums[i-1]:
#                 continue
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] < 0:
#                     left += 1
#                 elif nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     ans.append([nums[i], nums[left], nums[right]])
#                     # 对left和right的去重逻辑
#                     while left != right and nums[left] == nums[left+1]: left += 1
#                     while left != right and nums[right] == nums[right-1]: right -= 1
#                     left += 1
#                     right -= 1
#         return ans


# # 2022/10/01  author:WH
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         ans = set()
#         for i in range(len(nums)):
#             left, right = i+1, len(nums)-1
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] == 0:
#                     ans.add((nums[i], nums[left], nums[right]))
#                 if nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     left += 1
#         return list(map(list, ans))

# # 2022/11/12 author:WH
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         ans = set()
#         for i in range(len(nums)-2):
#              left, right = i+1, len(nums)-1
#              while left < right:
#                 if nums[i] + nums[left] + nums[right] == 0:
#                     ans.add((nums[i], nums[left], nums[right]))
#                 if nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                      left += 1
#         return list(map(list, ans))

# 23/11/08 author:WH

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                flag = nums[i] + nums[j] + nums[k]
                if flag == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                if flag > 0:
                    k -= 1
                else:
                    j += 1
        return list(map(list, ans))

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0]
    result = Solution().threeSum(nums)
    print(result)