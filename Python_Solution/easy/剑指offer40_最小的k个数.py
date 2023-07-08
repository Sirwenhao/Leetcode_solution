# 2023.07.08
# 剑指offer第40题，荣耀笔试题

# 解法一：使用内置sort()函数排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        return sorted(tinput)[:k]

# 解法二：对比排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        l = len(tinput)
        if l < k or k == 0:
            return []
        ans = []
        while k > 0:
            min_num = min(tinput)
            min_index = tinput.index(min_num)
            ans.append(tinput.pop(min_index))
            k -= 1
        return ans
    
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            key = arr[0]
            left = quickSort([i for i in arr[1:] if i < key])
            right = quickSort([j for j in arr[1:] if j >= key])
            return left + [key] + right
        n = len(tinput)
        if k > n or k == 0:
            return []
        arr = quickSort(tinput)
        return arr[:k] 
        

if __name__ == "__main__":
    # arr = [0,1,2,1]
    # k = 1
    arr = [3,2,1]
    k = 2
    result = Solution().GetLeastNumbers_Solution(arr, k)
    print(result)