"""Two Sum"""

"""
    1、Solution One
    2、暴力破解，时间：O(N^2),空间：O(1) 
"""
class Solution:
    def twoSum(self, nums, target):
        l = len(nums)
        for i in range(l):
            for j in range(l+1, l): #注意起点l+1
                if nums[i] + nums[j] == target:
                    return [i, j ]
        return []


"""
    1、Solution Two
    2、hash map
"""

class Solution:
    def twoSum(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []