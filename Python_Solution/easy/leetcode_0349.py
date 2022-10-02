'''
    1、一开始理解的有点小问题，与顺序无关，就是单纯数学意义上的交集
'''

# 2022/6/12  author:WH
# class Solution:
#     def intersection(self, nums1, nums2):
#         # 使用set哈希集合
#         nums1 = set(nums1)
#         nums2 = set(nums2)
#         return list(nums1 & nums2)

# 2022/6/19  author:WH
# class Solution:
#     def intersection(self, nums1, nums2):
#         res = []
#         nums1 = list(set(nums1))
#         nums2 = list(set(nums2))
#         for i in range(len(nums1)):
#             if nums1[i] in nums2:
#                 res.append([nums1[i]])
#         return res

# 2022/10/01  author:WH
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,2,1]
    nums2 = [1,2,3,5]
    result = Solution().intersection(nums1, nums2)
    print(result)