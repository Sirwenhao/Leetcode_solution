"""
    1、接雨水
"""
# 2022/7/13  author:WH
# 参考代码随想录，但是时间会超时
# class Solution:
#     def trap(self, height):
#         sum = 0
#         for i in range(len(height)):
#             if i == 0 or i == len(height)-1: continue
#             left = height[i]
#             right = height[i]
#             for j in range(i+1, len(height)):
#                 if height[j] > right: right = height[j]
#             for k in range(i-1, -1, -1):
#                 if height[k] > left: left = height[k]
#             h = min(left, right) - height[i]
#             if h > 0: sum += h
#         return sum

# 2022/7/13  author:WH
# 参考leetcode官解双指针版本
# class Solution:
#     def trap(self, height):
#         ans = 0
#         left, right = 0, len(height) - 1
#         leftMax = rightMax = 0
#         while left < right:
#             leftMax = max(leftMax, height[left])
#             rightMax = max(rightMax, height[right])
#             if height[left] < height[right]:
#                 ans += leftMax - height[left]
#                 left += 1
#             else:
#                 ans += rightMax - height[right]
#                 right -= 1
#         return ans

# 2022/7/16  author:WH
# 当前位置的蓄水量，取决于左右两边蓄水量的最小值与当前位置高度之间的差值
# class Solution:
#     def trap(self, height):
#         ans = 0
#         left, right = 0, len(height)-1
#         leftMax = rightMax = 0
#         while left < right:
#             leftMax = max(leftMax, height[left])
#             rightMax = max(rightMax, height[right])
#             if height[left] < height[right]:
#                 ans += leftMax - height[left]
#                 left += 1
#             else:
#                 ans += rightMax - height[right]
#                 right -= 1
#         return ans

class Solution:
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0
        left_max = [height[0]] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        right_max = [height[n - 1]] * n
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = Solution().trap(height)
    print(result)
        
