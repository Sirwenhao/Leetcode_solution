# 2022/12/28  author:WH
# 双指针：两端逼近
# 只要两端存在相同元素就要往中间内缩
class Solution:
    def minimumLength(self, s):
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            while left+1 < right and s[left] == s[left+1]:
                left += 1
            while left < right-1 and s[right-1] == s[right]:
                right -= 1
            left, right = left+1, right-1
        return max(0, right-left+1)

# 2022/12/28  author:官解
class Solution:
    def minimumLength(self, s):
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and s[left] == c:
                left += 1
            while right >= left and s[right] == c:
                right -= 1
        return right - left + 1


if __name__ == "__main__":
    # s = "cabaabac"
    s = "aabccabba"
    result = Solution().minimumLength(s)
    print(result)
