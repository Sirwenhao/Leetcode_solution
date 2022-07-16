"""
    1、滑动窗口最大值
"""
# 2022/7/12  author:WH
# 此法可解但会超时
# class Solution:
#     def maxSlindingWindow(self, nums, k):
#         ans = []
#         left, right = 0, k
#         while right <= len(nums):
#             ans.append(max(nums[left:right]))
#             right += 1
#             left += 1
#         return ans

# 2022/7/12  author:代码随想录
# 定义单调队列(从大到小)
# class MyQueue:
#     def __init__(self):
#         # 用list实现单调队列
#         self.queue = []
#     # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出
#     # pop之前判断队列是否为空
#     def pop(self, value):
#         if self.queue and value == self.queue[0]:
#             # python列表使用pop操作时，只需要给pop指定需要操作的元素的索引
#             self.queue.pop(0)
#     # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出
#     # 直到push的数值小于等于队列入口元素的数值为止
#     
#     def push(self, value):
#         while self.queue and value > self.queue[-1]:
#             # list的默认pop操作为弹出最后一个元素
#             self.queue.pop()
#         self.queue.append(value)

#     # 查询当前队列里的最大值，直接返回队列前端
#     def front(self):
#         return self.queue[0]

# class Solution:
#     def maxSlindingWindow(self, nums, k):
#         que = MyQueue()
#         ans = []
#         for i in range(k):
#             # 先将前k个元素放进队列
#             que.push(nums[i])
#         # ans记录前k个元素的最大值
#         ans.append(que.front())
#         for i in range(k, len(nums)):
#             # 滑动窗口移除最前面的元素
#             que.pop(nums[i-k])
#             # 滑动窗口加入最后面的元素
#             que.push(nums[i])
#             # 记录对应的最大值
#             ans.append(que.front())
#         return ans

# 2022/7/16  
# author:https://github.com/doocs/leetcode/tree/main/solution/0200-0299/0239.Sliding%20Window%20Maximum
# 单调队列常见题型：找出滑动窗口中的最大值/最小值，其模板为：
# q = queue()
# for i in range(n):
#     # 判断队头是否划出滑动窗口
#     while q and check_out(q[0]):
#         q.popleft()
#     while q and check[q[-1]]:
#         q.pop()
#     q.append(i)


from collections import deque
class Solution:
    def maxSlindingWindow(self, nums, k):
        q = deque()
        ans = []
        for i, v in enumerate(nums):
            if q and i - k + 1 > q[0]:
                q.popleft()
            while q and nums[q[-1]] <= v:
                q.pop()
            # 双向队列q中存储的是索引
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans  


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = Solution().maxSlindingWindow(nums, k)
    print(result)