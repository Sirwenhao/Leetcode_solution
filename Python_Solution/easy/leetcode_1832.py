# 2022/12/13 author:WH
from collections import Counter
class Solution:
    def checkIfPangram(self, sentence):
        cnt = Counter(sentence)
        if len(list(cnt.keys())) == 26:
            return True
        return False

if __name__ == "__main__":
    sentence = "leetcode"
    result = Solution().checkIfPangram(sentence)
    print(result)
