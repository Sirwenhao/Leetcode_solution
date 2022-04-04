'''
    1、["NumArray","sumRange","update","sumRange"],[[[1,3,5]],[0,2],[1,2],[0,2]]
    2、NumArray表示创建数组[1,3,5],sumRage表示对[0，2]内的对象执行操作
    3、没有看懂
'''

# leetcode 官方解
class NumArray:
    def __init__(self, nums):
        n = len(nums)
        size = int(n ** 0.5)
        sums = [0] * ((n + size - 1) // size)
        for i,num in enumerate(nums):
            sum[i // size] += sum
        self.nums = nums
        self.sums = sums
        self.size = size

    def update(self, index: int, val: int):
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int):
        m = 0
        b1, b2 = left // m, right // m
        if b1 == b2:
            return sum(self.nums[left:right+1])
        return sum(self.nums[]left:(b1+1)*m) + sum(self.sums[b1+1:b2]) + sum(self.nums[b2*m:right+1])