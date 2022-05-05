"""
    1、子集问题，从一个大的集合中找到满足条件的子集合的数目
"""
# 自己写，尝试使用回溯法解决
class Solution:
    def __init__(self):
        self.ans = []  # 定义一个空的列表作为结果集
        self.path = []  # 定义一个当前列表

    def numSubarrayProductLessThanK(self, nums, k):
        self.ans.clear()
        self.path.clear()
        # 先排序方便剪枝
        nums.sort()
        self.backtracking(nums, k, 0)
        for k in self.ans:
            if self.ans.count(k) > 1:
                self.ans.remove(k)
        return self.ans

    # 定义回溯法函数结构体
    def backtracking(self, nums, k, start_index):
        # base case
        if start_index == len(nums):
            self.ans += self.path[:]
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            # 判断当前的量是否满足条件
            current = nums[start_index:i+1]
            num = 1
            for j in range(len(current)):
                num *= current[j]
            if num < k:
                self.path.append(current)
                self.backtracking(nums, k, i+1)
                self.path.pop()
            else:
                continue
if __name__ == '__main__':
    nums = [10, 2, 5, 6]
    k = 100
    result = Solution().numSubarrayProductLessThanK(nums, k)
    print(result)
    print(len(result))

   

# # test 一行代码解决求一个列表中所有元素的乘积
# lst = [1,2,3,4,5]
# num = 1
# for i in range(len(lst)):
#     num *= lst[i]
# print(num)
# res = [[2], [5], [6], [10], [2], [5], [6, 10], [2], [5, 6], [10], [2, 5], [6], [10], [2, 5], [6, 10], [2, 5, 6], [10]]
# # res1 = res.remove[i if res.count(i) > 1]
# for i in res:
#     if res.count(i) > 1:
#         res.remove(i) 
# print(res)