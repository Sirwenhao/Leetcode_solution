# 2022/12/29 author:WH
# 考虑交集
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        # ans = (set(nums1)&set(nums2)) | (set(nums1)&set(nums3)) | (set(nums2)&set(nums3))
        return list((set(nums1)&set(nums2)) | (set(nums1)&set(nums3)) | (set(nums2)&set(nums3)))
    
if __name__ == "__main__":
    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]
    result = Solution().twoOutOfThree(nums1, nums2, nums3)
    print(result)