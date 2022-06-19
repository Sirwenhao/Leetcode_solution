"""
1、四数相加
2、哈希表专题
"""
# 2022/6/14  author:代码随想录
# class Solution:
#     def fourSumCount(self, nums1, nums2, nums3, nums4):
#         hashmap = dict()
#         for n1 in nums1:
#             for n2 in nums2:
#                 if n1 + n2 in hashmap:
#                     hashmap[n1+n2] += 1
#                 else:
#                     hashmap[n1+n2] = 1
#         # print(hashmap)
#         count = 0
#         for n3 in nums3:
#             for n4 in nums4:
#                 key = - n3 - n4
#                 print(hashmap)
#                 # print(key)
#                 if key in hashmap:
#                     count += hashmap[key]
#         return count

# 2022/6/19 author:WH  有问题，测试案例还是存在不通过的情况
# class Solution:
#     def fourSumCount(self, nums1, nums2, nums3, nums4):
#         dic1 = {}
#         dic2 = {}
#         for i in nums1:
#             for j in nums2:
#                 if i + j in dic1:
#                     dic1[i + j] += 1
#                 else:
#                     dic1[i + j] = 1
#         print('dic1:', dic1)

#         for m in nums3:
#             for n in nums4:
#                 if m + n in dic2:
#                     dic2[m + n] += 1
#                 else:
#                     dic2[m + n] = 1
#         print('dic2:', dic2)
#         cnt = 0
#         for m in dic1:
#             for n in dic2:
#                 if m - n == 0:
#                     cnt += dic1[m] * dic2[n]
#         return cnt

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        dic1 = {}
        for i in nums1:
            for j in nums2:
                if i + j in dic1:
                    dic1[i + j] += 1
                else:
                    dic1[i + j] = 1
        print('dic1:', dic1)
        count = 0
        for m in nums3:
            for n in nums4:
                key = - m - n
                print('key:', key)
                if key in dic1:
                    count += dic1[key]
        return count

if __name__ == "__main__":
    nums1 = [-1, -1]
    nums2 = [-1, 1]
    nums3 = [-1, 1]
    nums4 = [1, -1]
    result = Solution().fourSumCount(nums1, nums2, nums3, nums4)
    print(result)