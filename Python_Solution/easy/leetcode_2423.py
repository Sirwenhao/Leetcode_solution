# 2023/4/29  author:WH
from collections import Counter
class Solution:
    def equalFrequency(self, word):
        cnt = Counter(word)
        for c in cnt.keys():
            cnt[c] -= 1
            if len(set(v for v in cnt.values() if v)) == 1:
                return True
            cnt[c] += 1
        return False
    
if __name__ == "__main__":
    word = "abcc"
    result = Solution().equalFrequency(word)
    print(result)