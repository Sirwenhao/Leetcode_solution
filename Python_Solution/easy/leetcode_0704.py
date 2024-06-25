"""
    1、二分查找
    2、更新的的是左右边界，中心middle值是左右两个边界的均值
    3、属于leetcode专题中的数组类
"""

# 2022/5/9 author:WH
# class Solution:
#     def search(self, nums, target):
#         nums.sort()
#         left, right = 0, len(nums)-1
#         while left < right:
#             middle = (left+right) // 2
#             if nums[middle] < target:
#                 left = middle+1
#             elif nums[middle] > target:
#                 right = middle
#             else:
#                 return middle
#         return -1

# 2022/5/31 author:WH
# 此版本存在问题，当判断左右边界与middle对应值大小之后，新的边界复制并非是此版本的情况
# 这一块有两种写法:分别对应于左闭右闭的写法和左闭右开的写法

# # 版本一：左闭右闭[left, right]
# class Solution:
#     def search(self, nums, target):
#         left, right = 0, len(nums)-1
#         # 千万不要忘记先进行排序
#         nums.sort()
#         while left <= right:
#             middle = (left + right) // 2
#             if nums[middle] > target:
#                 right = middle-1
#             elif nums[middle] < target:
#                 left = middle+1
#             else:
#                 return middle
#         return -1
        
# 版本二：左闭右开[left,right)
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle+1
            else:
                return middle
        return -1
    
    
# 24/6/25 @author:WH

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
        return -1


if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    target = 7
    result = Solution().search(nums, target)
    print(result)