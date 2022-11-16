# 2022/11/16 author:WH
# 相当于不使用内置的sorth函数对数组nums进行排序
# 要求是原地排序的所以必须在原数组上进行修改

# # 三种颜色需要两次遍历，每次排一种颜色
# # 使用双指针之快慢指针，时间复杂度O(n),空间复杂度O(1)
# class Solution:
#     def sortColor(self, nums):
#         n = len(nums)
#         # 使用ptr指定头部位置
#         slow = 0
#         for fast in range(n):
#             if nums[fast] == 0:
#                 nums[fast], nums[slow] = nums[slow], nums[fast]
#                 slow += 1
#         for fast in range(slow, n):
#             if nums[fast] == 1:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#                 slow += 1
#         return nums

# # 双指针遍历，同时操作两个字符
# class Solution:
#     def sortColor(self, nums):
#         n = len(nums)
#         slow = fast = 0
#         for i in range(n):
#             if nums[i] == 1:
#                 nums[i], nums[fast] = nums[fast], nums[i]
#                 fast += 1
#             elif nums[i] == 0:
#                 nums[i], nums[slow] = nums[slow], nums[i]
#                 if slow < fast:
#                     nums[i], nums[fast] = nums[fast], nums[i]
#                 slow += 1
#                 fast += 1
#         return nums

# 双指针,遍历0和2
class Solution:
    def sortColor(self, nums):
        n = len(nums)
        slow, fast = 0, n-1
        i = 0
        while i <= fast:
            while i <= fast and nums[i] == 2:
                nums[i], nums[fast] = nums[fast], nums[i]
                fast -= 1
            if nums[i] == 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
            i += 1
        return nums


if __name__ == "__main__":
    nums = [0,2,1,1,1,2,0,0]
    result = Solution().sortColor(nums)
    print(nums)