# 2023/5/18  author:WH

class Solution:
    def addNegabinary(self, arr1, arr2):
        ans = []
        l1 = len(arr1)
        l2 = len(arr2)
        x1 = x2 = 0
        while l1 > 0:
            x1 += arr1[l1-1] * (-2) ** (l1-1)
            l1 -= 1
        while l2 > 0:
            x2 += arr2[l2-1] * (-2) ** (l2-1)
            l2 -= 1
        res = x1 + x2
        print(res)
        s = str(bin(res))[2:] # ord()是ASCII码
        for i in s:
            ans.append(int(i))
        return ans
    
if __name__ == "__main__":
    arr1 = [1,1,1,1,1]
    arr2 = [1,0,1]
    result = Solution().addNegabinary(arr1, arr2)
    print(result)