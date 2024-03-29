"""
1、每个位上数字的平方值和如果最终能归为1，则就是快乐数
2、属于哈希表专题
"""
# 2022/6/13   author:WH
# 第一想法：递归,自己写的，但是有点问题，没能通过
# 如何使用哈希表，把一个数字n变成每一位上数字的集合
# 此方法没有考虑到特殊情况：快乐数可能存在循环，从而导致计算中进入死循环，递归爆炸
# 第二种情况是虽然没有死循环，但值不断增大，最后接近无穷大
# class Solution:
#     def isHappy(self, n):
#         s = str(n)
#         global total
#         total = 0
#         for i in range(len(s)):
#             total += int(s[i]) ** 2
#         if total == 1:
#             return True
#         total = self.isHappy(total)
#         return total == 1


# 代码随想录
# class Solution:
#     def isHappy(self, n):
#         def calculate_happy(num):
#             sum = 0
#             # 从个位数开始依次取数字平方和
#             while num:
#                 sum += (num % 10) ** 2
#                 num = num // 10
#             return sum
#         # 记录中间结果
#         record = set()
#         while True:
#             n = calculate_happy(n)
#             if n == 1:
#                 return True
#             #  如果中间结果重复出现，说明出现了死循环，该数不是快乐数
#             if n in record:
#                 return False
#             else:
#                 record.add(n)

# 2022/6/19  author:WH
# class Solution:
#     def calculate(self, num):
#         sum = 0
#         while num:
#             i = num % 10
#             sum += i**2
#             num = num // 10
#         return sum
#     def isHappy(self, n):
#         record = set()   # 用于记录已经出现过的情况，防止再次出现，陷入死循环
#         while True:
#             n = self.calculate(n)
#             if n == 1:
#                 return True
#             if n in record:
#                 return False
#             else:
#                 record.add(n)

# 2022/10/01  author:WH
# 关键点在使用set进行去重，因为又可能出现的数字通过下属运算后进入死循环
class Solution:
    def isHappy(self, n):
        def get_next(n):
            ans = 0
            while n > 0:
                n, digit = divmod(n, 10)
                ans += digit ** 2
            return ans
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_next(n)
        return n==1


if __name__ == "__main__":
    n = 19
    result = Solution().isHappy(n)
    print(result)

