"""
    1、一个长度为n的数组nums，把里面的数字全部变为一样的需要的最小步数
    2、并且这个一样的数字还只能是nums已存在的数字
"""

# 想法：循环列表把所有的元素都变成当前的元素，统计最小步骤的情况，需要双循环
# class Solution:
#     def minMoves2(self, nums):
#         # 先排序
#         nums.sort()
#         ans = []
#         for i in nums:
#             value = 0
#             for j in nums:
#                 value += abs(j-i)
#             ans.append(value)
#         print(ans)
#         min_v = min(ans)
#         return min_v

# 一开始的想法，隐约感觉肯定是找最中间的元素对应的情况移动步数最少，但实际证明还是不太懂
# 当所有的元素都变为nums[n//2]时，所需要的移动步数最少
class Solution:
    def minMoves2(self, nums):
        nums.sort()
        total = 0
        for i in nums:
            total += abs(i - nums[len(nums)//2])
            print(total)
        return total
    
if __name__ == "__main__":
    nums = [1,10,2,9]
    result = Solution().minMoves2(nums)
    print(result)