# 2023/1/23 author:WH
class Solution:
    def calculateTax(self, brackets, income):
        ans = 0
        if income <= brackets[0][0]:
            return float(income * brackets[0][1])
        i = 1
        while i < len(brackets) and income > brackets[i][0]:
            ans += float((brackets[i][0] - brackets[i-1][0])*brackets[i][1])
            i += 1
        return ans

if __name__ == "__main__":
    brackets = [[3,50],[7,10],[12,25]]
    income = 10
    result = Solution().calculateTax(brackets, income)
    print(result)