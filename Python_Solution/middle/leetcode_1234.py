# 2023/2/13 author:WH
# 没有理解好题意，要求的是替换子串，子串
from collections import defaultdict
class Solution:
    def balancedString(self, s):
        count_dict = defaultdict(int)
        for c in s:
            count_dict[c] += 1
        l = len(s)//4
        print(l)
        # print(count_dict['Q'])
        return (max(0, count_dict['Q']-l) + max(0, count_dict['W']-l) + max(0, count_dict['E']-l) + max(0, count_dict['R']-l))


if __name__ == "__main__":
    # s = "QWER"
    # s = "QQQR"
    s = "WWEQERQWQWWRWWERQWEQ"
    result = Solution().balancedString(s)
    print(result)

