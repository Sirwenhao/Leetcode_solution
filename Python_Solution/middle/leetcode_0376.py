"""
    1、动态规划专题：摆动序列
"""
# 2022/7/30  author:WH
class Solution:
    def wiggleMaxLength(self, nums):
        # preC是第二位和第一位元素的差值，curC是第三位和第二位的元素的差值
        # 可通过判断两个差值是否异号来判断，序列是否起伏，而判断异号最容易的措施就是乘积小于0
        preC, curC, res = 0, 0, 1
        for i in range(len(nums) - 1):
            curC = nums[i+1] - nums[i]
            if curC * preC <= 0 and curC != 0:
                preC = curC
                res += 1
        return res

if __name__ == "__main__":
    nums = [1,7,4,9,2,5]
    result = Solution().wiggleMaxLength(nums)
    print(result)
