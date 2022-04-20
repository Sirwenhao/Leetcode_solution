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
def maxAre(height):
    left = 0
    right = len(height)-1
    max_v = 0
    while left < right:
        max_v = max(max_v, min(height[right], height[left]) * (right-left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_v





height = [1,8,6,2,5,4,8,3,7]
result = maxAre(height)
print(result)
