"""
    1、不使用除法、乘法和mod运算符实现数字相除
"""

# # 力扣加加
# class Solution:
#     def divide(self, dividend, divisor):
#         if divisor == 0:
#             raise ZeroDivisionError
#         if abs(divisor) == 1:
#             result = dividend if 1 == divisor else -dividend
#             return min(2**31-1, max(-2**31, result))

#         # 确定结果的符号
#         sign = ((dividend >= 0) == (divisor >= 0))
#         result = 0
#         # abs也可以卸载while条件中，不过可能会多计算几次
#         _divisor = abs(divisor)
#         _dividend = abs(dividend)

#         while _divisor <= _dividend:
#             r, _dividend = self._multi_divide(_divisor, _dividend)
#             result += r

#         result = result if sign else -result

#         # 注意返回值不能超过32位有效符号位的表示范围
#         return min(2**31-1, max(-2**31, result))

#     def _multi_divide(self, divisor, dividend):
#         """
#         翻倍除法，如果可以被除，则下一步除数翻倍，直至除数大于被除数
#         返回商加总的结果与被除数的剩余值；
#         """
#         result = 0
#         times_count = 1
#         while divisor <= dividend:
#             dividend -= divisor
#             result += times_count
#             times_count += times_count
#             divisor += divisor
#         return result, dividend


# 官解：二分查找
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 一般情况，使用类二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev
        
        candidates = [divisor]
        # 注意溢出
        while candidates[-1] >= dividend - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])
        
        ans = 0
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] >= dividend:
                ans += (1 << i)
                dividend -= candidates[i]

        return -ans if rev else ans


if __name__ == '__main__':
    dividend = 7
    divisor = -3
    result = Solution().divide(dividend, divisor)
    print(result)