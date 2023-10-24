# 2022/11/15 author:WH
# 找出两个正序数组的中位数，限制算法的时间为O(lon(m+n))
# 一般看到时间复杂度的限制，不难想到是二分法
# 中位数的是指一串数字中位于中间位置的数字。若字符串长度为奇数，则直接取中间；若为偶数，则取中间两个值的均值

# # 2022/11/15 author:WH
# # 简单粗暴的解法；直接合并两个字符串，然后查找中位数
# # 时间复杂度O(m+n),空间复杂度O(m+n)
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums = nums1 + nums2
#         nums.sort()
#         if len(nums)%2 == 0:
#             # 记住此处保存多位小数的方法
#             middle_num = '%.5f' %((nums[len(nums)//2] + nums[len(nums)//2-1])/2)
#         else:
#             middle_num = '%.5f' %(nums[len(nums)//2])
#         return middle_num

# # 2022/12/18 author:WH
# 要求时间复杂度为O(log(m+n))，此种计算复杂度一般考虑二分法
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums = nums1 + nums2
#         index = len(nums) // 2

#     def middleNum(self, array):
#         if len(array) == 1:
#             return '%.5f' %array[0]
#         if len(array) == 2:
#             return   '%.5f'%(array[0]+array[1])

# from cmath import inf
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         def findkth(i, j, k):
#             if i >= m:
#                 return nums2[j+k-1]
#             if j >= n:
#                 return nums1[i+k-1]
#             if k == 1:
#                 return min(nums1[i], nums2[j])
#             midVal1 = nums1[i+k//2-1] if i+k//2-1 < m else inf
#             midVal2 = nums2[j+k//2-1] if j+k//2-1 < n else inf
#             if midVal1 < midVal2:
#                 return findkth(i+k//2, j, k-k//2)
#             return findkth(i, j+k//2, k-k//2)
#         m, n = len(nums1), len(nums2)
#         left, right = (m+n+1) // 2, (m+n+2) // 2
#         return (findkth(0, 0, left) + findkth(0, 0, right)) / 2


# 23/10/24 author：WH
# 有点惊讶，这也能过。。。

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)
        if length % 2 == 0:
            return (nums3[length//2] + nums3[length//2+1])/2
        else:
            return nums3[length//2]

if __name__ == "__main__":
    nums1 = [1,3,5]
    nums2 = [2, 4]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)