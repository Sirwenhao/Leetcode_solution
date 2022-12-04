# 2022/12/03  author:WH
# python内置的函数isdigit()判断是否为数字
class Solution:
    def secondHighest(self, s):
        numsList = []
        for c in s:
            if c.isdigit() and not c in numsList:   
                numsList.append(c)
        print(sorted(numsList))
        numsList.sort()
        if len(numsList) < 2:
            return -1
        return int(numsList[-2])

if __name__ == "__main__":
    # s = "dfa12321afd"
    s = "sjhtz8344"
    result = Solution().secondHighest(s)
    print(result)
