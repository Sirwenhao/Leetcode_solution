# 2023/4/26  author:WH

from itertools import accumulate
class Solution:
    def maxSumTwoOverleap(self, nums, firstLen, secondLen):
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = t = 0
        i = firstLen
        while i + secondLen -1 < n:
            t = max(t, s[i] - s[i - firstLen])
            ans = max(ans, t + s[i + secondLen] - s[i])
            i += 1
        t = 0
        i = secondLen
        while i + firstLen - 1 < n:
            t = max(t, s[i] - s[i - secondLen])
            ans = max(ans, t + s[i + firstLen] - s[i])
            i += 1
        return ans
    
if __name__ == "__main__":
    nums = [0,6,5,2,2,5,1,9,4]
    firstLen = 1
    secondeLen = 2
    result = Solution().maxSumTwoOverleap(nums, firstLen, secondeLen)
    print(result)