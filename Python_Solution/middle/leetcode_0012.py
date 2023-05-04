# 2023/5/4  author:WH

class Solution:
    def intToRoman(self, num):
        vs = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        cs = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        ans = []
        for c,v in zip(cs, vs):
            while num >= v:
                num -= v
                ans.append(c)
        return "".join(ans)
    
if __name__ == "__main__":
    num = 1998
    result = Solution().intToRoman(num)
    print(result)