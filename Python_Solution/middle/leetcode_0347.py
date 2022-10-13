"""
    1、出现频率最高的前k个元素
    2、Python字典的get()方法
    3、Python数据结构——堆(heapq)
"""

# 2022/7/13  author:代码随想录
# import heapq
# class Solution:
#     def topKFrequent(self, nums, k):
#         # 统计元素出现的频率
#         map_ = {}
#         for i in range(len(nums)):
#             map_[nums[i]] = map_.get(nums[i], 0) + 1
#         # 对频率排序，定义一个小顶堆，大小为k
#         pri_que = []
#         # 用固定大小为k的小顶堆，扫描所有频率的数值
#         for key, freq in map_.items():
#             heapq.heappush(pri_que, (freq, key))
#             # 如果堆的大小大于了k，则队列弹出，保证堆的大小一直为k
#             if len(pri_que) > k:
#                 heapq.heappop(pri_que)

#         # 找出前k个高频元素，小顶堆先弹出的是小元素，因此倒序输出到数组中
#         result = [0] * k
#         for i in range(k-1, -1, -1):
#             # 此处的[1]即取出其第一维，即元素而不是其频次
#             result[i] = heapq.heappop(pri_que)[1]
#         return result

# import heapq
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums, k):
#         counter = Counter(nums)
#         hp = []
#         for num, freq in counter.items():
#             if len(hp) == k:
#                 heapq.heappush(hp, (freq, num))
#                 heapq.heappop(hp)
#             else:
#                 heapq.heappush(hp, (freq, num))
#         return [t[1] for t in hp]

# 2022/10/07  author:WH
# 总结一下Python中的堆这种数据结构的用法
# 总结Python字典中的get()的用法
# import heapq
# class Solution:
#     def topKFrequent(self, nums, k):
#         dic = {}
#         for i in range(len(nums)):
#             dic[nums[i]] = dic.get(nums[i], 0) + 1
#         pri_que = []
#         for key, freq in dic.items():
#             # 核心思想是利用python中的小顶堆的性质，大值才能进入堆内，对内即包含k个排好序的值
#             heapq.heappush(pri_que, (freq, key))
#             if len(pri_que) > k:
#                 heapq.heappop(pri_que)
#         ans = [0] * k
#         for i in range(k-1, -1, -1):
#             ans[i] = heapq.heappop(pri_que)[1]
#         return ans

# 2022/10/13  author:github
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        hp = []
        for num, freq in counter.items():
            if len(hp) == k:
                heapq.heappush(hp, (freq, num))
                heapq.heappop(hp)
            else:
                heapq.heappush(hp, (freq, num))
        return [t[1] for t in hp]



if __name__ == "__main__":  
    nums = [1,1,1,2,2,3]
    k = 2
    result = Solution().topKFrequent(nums, k)
    print(result)