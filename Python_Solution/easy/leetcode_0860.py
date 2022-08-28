"""
    1、柠檬水找零
    2、遇到10和20的同时还要处理5和10
    3、贪心关键点在于遇到20美元，先用10美元解决
"""
# 2022/8/1  author:WH
# class Solution:
#     def lemonadeChange(self, bills):
#         five = ten = twenty = 0
#         for i in bills:
#             if i == 5:
#                 five += 1
#             elif i == 10:
#                 if five <= 0: return False
#                 ten += 1
#                 five -= 1
#             else:
#                 if five > 0 and ten > 0:
#                     five -= 1
#                     ten -= 1
#                     twenty += 1
#                 elif five >= 3:
#                     five -= 3
#                     twenty += 1
#                 else:
#                     return False
#         return True

# 2022/8/28  author:WH
# 关键点在于遇到面值为20的优先考虑使用面值10解决，如果不行，则使用两个5
class Solution:
    def lemonadeChange(self, bills):
        five = ten = twenty = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five < 1:
                    return False
                ten += 1
                five -= 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True

if __name__ == "__main__":
    bills = [5,5,5,10,20]
    result = Solution().lemonadeChange(bills)
    print(result)