# 2022/6/23  author:WH
# 考虑使用双指针
# class Solution:
#     def reverseString(self, s):
#         l, r = 0, len(s)-1
#         while l <= r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#         return s  # 这个地方可以不用返回s，因为本来就是直接在字符串s上进行操作的

# 2022/09/13  author:WH
class Solution:
    def reverseString(self, s):
        l, r = 0, len(s)-1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    result = Solution().reverseString(s)
    print(result)