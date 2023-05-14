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

from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        cnt = Counter(barcodes)
        barcodes.sort(key=lambda x: (-cnt[x], x)) # 按照次数从大到小排序，如果次数一样就按照元素排序
        n = len(barcodes)
        ans = [0] * len(barcodes)
        ans[::2] = barcodes[:(n+1) // 2]
        ans[1::2] = barcodes[(n+1) // 2:]
        return ans
        
    
if __name__ == "__main__":
    barcodes = [1,1,1,2,2,2]
    result = Solution().rearrangeBarcodes(barcodes)
    print(result)
            