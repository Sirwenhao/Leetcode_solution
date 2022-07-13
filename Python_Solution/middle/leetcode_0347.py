"""
    1、出现频率最高的前k个元素
    2、Python字典的get()方法
    3、Python数据结构——堆(heapq)
"""
# 2022/7/13  author:WH
# 最好的做法肯定是用队列，把每次统计到的出现次数大的元素从尾部进入，把之前的从头部输出
# import queue
# class Solution:
#     def topKFrequent(self, nums, k):
#         ans = []
#         que = queue
#         max_V = 0
#         for i in range(len(nums)):
#             num = 0
#             num = nums.count(nums[i])
#             if num > max_V:
#                 max_V = num
#                 que.push(nums[i])
#         for j in range(k):
#             ans.append(que.pop())
#         return ans

# 2022/7/13  author:代码随想录
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        # 统计元素出现的频率
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        # 对频率排序，定义一个小顶堆，大小为k
        pri_que = []
        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            # 如果堆的大小大于了k，则队列弹出，保证堆的大小一直为k
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        # 找出前k个高频元素，小顶堆先弹出的是小元素，因此倒序输出到数组中
        result = [0] * k
        for i in range(k-1, -1, -1):
            # 此处的[1]即取出其第一维，即元素而不是其频次
            result[i] = heapq.heappop(pri_que)[1]
        return result


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    result = Solution().topKFrequent(nums, k)
    print(result)