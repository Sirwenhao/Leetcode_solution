# 2023/3/23  author:WH


# 时间复杂度:O(mn)，其中m为数组nums的长度，n为查询次数
# 定义等差子数列函数

# class Solution:
#     def checkArithmeticSubarrays(self, nums, l, r):
#         a = len(list(l))
#         print(a)
#         answer = [0] * a
#         for i in range(a):
#             if self.sameSub(nums, l[i], r[i]):
#                 answer[i] = True
#             else:
#                 answer[i] = False
#         return answer
         
        
#     def sameSub(self, nums, left, right):
#         numlist = sorted(nums[left:right+1])
#         b = len(numlist)
#         i = 0
#         while i < b-2:
#             if numlist[i+1]-numlist[i] != numlist[i+2]-numlist[i+1]:
#                 return False
#             i += 1
#         return True

# leetcode
# 设计函数检查是否为等差数列，步骤同上，但是判断等差的函数内核不同

class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def check(nums, l, r):
            n = r - l + 1
            s = set(nums[l:l+n])
            a1, an = min(nums[l:l+n]), max(nums[l:l+n])
            d, mod = divmod(an - a1, n-1)
            return mod == 0 and all((a1 + (i-1)*d) in s for i in range(1, n))
        return [check(nums, left, right) for left, right in zip(l, r)]

if __name__ == "__main__":
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]
    result = Solution().checkArithmeticSubarrays(nums, l, r)
    print(result)