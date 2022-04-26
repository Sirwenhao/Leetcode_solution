"""
    1、不使用除法、乘法和mod运算符实现数字xiangchu
"""

# 力扣加加
class Solution:
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError
        if abs(divisor) == 1:
            result = dividend if 1 == divisor else -dividend
            return min(2**31-1, max(-2**31, result))

        # 确定结果的符号
        sign = ((dividend >= 0) == (divisor >= 0))
        result = 0
        # abs也可以卸载while条件中，不过可能会多计算几次
        _divisor = abs(divisor)
        _dividend = abs(dividend)

        while _divisor <= _dividend:
            r, _dividend = self._multi_divide(_divisor, _dividend)
            result += r

        result = result if sign else -result

        # 注意返回值不能超过32位有效符号位的表示范围
        return min(2**31-1, max(-2**31, result))

    def _multi_divide(self, divisor, dividend):
        """
        翻倍除法，如果可以被除，则下一步除数翻倍，直至除数大于被除数
        返回商加总的结果与被除数的剩余值；
        """
        result = 0
        times_count = 1
        while divisor <= dividend:
            dividend -= divisor
            result += times_count
            times_count += times_count
            divisor += divisor
        return result, dividend