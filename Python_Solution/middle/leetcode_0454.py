"""
1、四数相加
2、哈希表专题
"""
# 2022/6/14  author:代码随想录
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count
if __name__ == "__main__":
    nums1 = [3,1,4]
    nums2 = [-2,4,3]
    nums3 = [-1,3,2]
    nums4 = [3,-2,0]
    result = Solution().fourSumCount(nums1, nums2, nums3, nums4)
    print(result)