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

# # 2022/11/15 author:github
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):


if __name__ == "__main__":
    nums1 = [1,3,5]
    nums2 = [2, 4]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)