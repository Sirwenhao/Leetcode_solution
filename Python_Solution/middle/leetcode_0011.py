"""
    1、盛水最多的容器
"""

# 解法一：核心含义是从一个数组中找到两个元素a和b，这两个元素满足:
# min(a, b)*(index(b) - index(1))为最大
# 时间复杂度O(N^2)
# def maxAre(height):
#     max_v = 0
#     for i in range(len(height)):
#         for j in range(i+1, len(height)):
#             max_v = max(min(height[i], height[j]) * (j-i), max_v)
#     return max_v

# 解法二：官解提示和力扣加加都提示了双指针，自己写
# 时间复杂度：O(N)
# class Solution:
# def maxAre(self, height):
#     left = 0
#     right = len(height)-1
#     max_v = 0
#     while left < right:
#         max_v = max(max_v, min(height[right], height[left]) * (right-left))
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_v

# # 2022/5/1 review
# # 双指针
# class Solution:
#     def maxArea(self, heights):
#         left, right = 0, len(heights)-1
#         max_v = 0
#         while left < right:
#             max_v = max(max_v, (right-left) * min(heights[right], heights[left]))
#             if heights[left] > heights[right]: # 实际参与计算的高度是由最低的高度所主导的
#                 left += 1
#             if heights[left] <= heights[right]:
#                 right -= 1
#         return max_v

# 双指针
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        res = 0
        while i < j:
            t = (j-i)*min(height[i], height[j])
            res = max(res, t)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

if __name__ == "__main__":
    # heights = [1,8,6,2,5,4,8,3,7]
    heights = [1,2,1]
    result = Solution().maxArea(heights)
    print(result)
