# 24/8/29 @author:WH

# 青蛙跳台阶问题
# 解法一：动态规划
# 核心点：站在当前位置审视，是如何来的（跳一步上来或者跳两步上来）
class Solution:
    def trainWays(self, num):
        if num == 0:
            return 1
        elif num <= 2:
            return num
        
        dp = [0] * (num+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, num+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[num]
   
   
# 递归

class Solution:
    def trainWays(self, num):
        if num <= 2:
            return num
        else:
            return self.trainWays(num-1) + self.trainWays(num-2) 
    
if __name__ == "__main__":
    num = 5
    result = Solution().trainWays(num)
    print(f'{result}')
        

