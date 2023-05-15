# 2023/5/14  author:WH

# class Solution:
#     def rearrangeBarcodes(self, barcodes):
#         n = len(barcodes)
#         ans = [0] * n
#         ans[0] = barcodes[0]
#         for i in range(1, n):
#             if barcodes[i] != ans[-1]:
#                 ans.append(barcodes[i])
#         return ans

# from collections import Counter
# class Solution:
#     def rearrangeBarcodes(self, barcodes):
#         cnt = Counter(barcodes)
#         barcodes.sort(key=lambda x: (-cnt[x], x)) # 按照次数从大到小排序，如果次数一样就按照元素排序
#         n = len(barcodes)
#         ans = [0] * len(barcodes)
#         ans[::2] = barcodes[:(n+1) // 2]
#         ans[1::2] = barcodes[(n+1) // 2:]
#         return ans

# 利用堆
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes):
        count = {}
        for barcode in barcodes:
            count[barcode] = count.get(barcode, 0) + 1
        # 构建最大堆, 将出现次数和条形码对插入堆中
        max_heap = []
        for barcode, freq in count.items():
            heapq.heappush(max_heap, (-freq, barcode))
        n = len(barcodes)
        ans = [0] * n
        index = 0

        # 填充奇数索引位置
        while max_heap:
            freq, barcode = heapq.heappop(max_heap)
            for _ in range(-freq):
                ans[index] = barcode
                index += 2
                if index >= n:
                    index = 1
        return ans
    
if __name__ == "__main__":
    barcodes = [1,1,1,2,2,2]
    result = Solution().rearrangeBarcodes(barcodes)
    print(result)