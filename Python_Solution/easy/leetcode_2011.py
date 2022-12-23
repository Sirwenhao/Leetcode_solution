# 2022/12/23  author:WH
# 时间复杂度:O(N)，空间复杂度:O(1)
# class Solution:
#     def finalValueAfterOperations(self, operations):
#         X = 0
#         for i in operations:
#             if i[:-1] == "--" or i[1:] == "--":
#                 X -= 1
#             elif i[:-1] == "++" or i[1:] == "++":
#                 X += 1
#         return X

# 2022/12/23  author:官解
# 跟第二次的想法不谋而合，只需要关注第二个元素即可
class Solution:
    def finalValueAfterOperations(self, operations):
        return sum(1 if op[1] == "+" else -1 for op in operations)

if __name__ == "__main__":
    operations = ["--X","X++","X++"]
    # operations = ["++X","++X","X++"]
    result = Solution().finalValueAfterOperations(operations)
    print(result)
