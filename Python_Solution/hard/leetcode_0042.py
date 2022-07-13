"""
    1、接雨水
"""
# 2022/7/13  author:WH
# 参考代码随想录，但是时间会超时
class Solution:
    def trap(self, height):
        sum = 0
        for i in range(len(height)):
            if i == 0 or i == len(height)-1: continue
            left = height[i]
            right = height[i]
            for j in range(i+1, len(height)):
                if height[j] > right: right = height[j]
            for k in range(i-1, -1, -1):
                if height[k] > left: left = height[k]
            h = min(left, right) - height[i]
            if h > 0: sum += h
        return sum
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = Solution().trap(height)
    print(result)
        
