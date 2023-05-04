# 2023/5/4  author:WH

# class Solution:
#     def intToRoman(self, num):
#         vs = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
#         cs = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
#         ans = []
#         for c,v in zip(cs, vs):
#             while num >= v:
#                 num -= v
#                 ans.append(c)
#         return "".join(ans)
    
class Solution:
    def intToRoman(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
    
if __name__ == "__main__":
    num = 1998
    result = Solution().intToRoman(num)
    print(result)