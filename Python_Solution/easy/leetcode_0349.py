'''
    1、一开始理解的有点小问题，与顺序无关，就是单纯数学意义上的交集
'''

# def intersection(nums1, nums2):
#     a = len(nums1)
#     b = len(nums2)
#     list = []
#     if a > b:
#         for i in range(b):
#             if nums2[i] in nums1 and nums2[i] not in list:
#                 list.append(nums2[i])
#             else:
#                 continue
#     else:
#         for i in range(a):
#             if nums1[i] in nums2 and nums1[i] not in list:
#                 list.append(nums1[i])
#             else:
#                 continue

#     return list

# nums1 = [1,2,2,1]
# nums2 = [2,2]

# result = intersection(nums1, nums2)
# print(result)

# 2022/6/12  author:WH
class Solution:
    def intersection(self, nums1, nums2):
        # 使用set哈希集合
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,2,1]
    nums2 = [1,2,3,5]
    result = Solution().intersection(nums1, nums2)
    print(result)