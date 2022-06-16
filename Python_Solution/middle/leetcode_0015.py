"""
    1、给定一个列表，找出和为零的三个数，不能重复
    2、不能重复，首先想到的是数据结构中的集合.用循环可以但是循环嵌套时间复杂度过高
    3、竟然没提前想到先排序，晕~
    4、Python3使用map函数返回的是一个迭代器，使用方法为：map(function, iterable,...)
    5、根据函数function对指定序列元素做映射
"""
# 排序之后，使用指针的做法
# def threeSum(nums):
#     nums.sort()
#     ans = []
#     for i in range(len(nums)):
#         left = i+1
#         right = len(nums)-1
#         for j in range(left+1, right):
#             if nums[i]+nums[left]+nums[j] == 0:
#                 ans.append([nums[i], nums[left], nums[j]])
#     return ans


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
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums, res = sorted(nums), []
        for i in range(len(nums) - 2):
            cur, l, r = nums[i], i + 1, len(nums) - 1
            if res != [] and res[-1][0] == cur: continue

            while l < r:
                if cur + nums[l] + nums[r] == 0:
                    res.append([cur, nums[l], nums[r]])
                    while l < r - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                if cur + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(nums)
    print(result)