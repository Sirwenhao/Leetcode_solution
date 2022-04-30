'''
    1、属于动态规划的分类。关键点：所偷金额最大，被偷的两家不是邻居
    2、第一个想到的是递归
    3、此题的关键问题在于找寻状态方程，这种情况最好找一下变量和不变量之间的关系
'''

def rob(nums):
    if not nums:
        return 0

    size = len(nums)
    if size == 1:
        return nums[0]

    dp = [0] * size
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, size):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[size-1] 
