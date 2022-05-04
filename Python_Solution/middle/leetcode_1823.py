"""
    1、约瑟夫环问题：n个人围成一个圈，每次数k个数字，被数到的人出局，求圈中所剩下的最后一个人的标号。
"""

# 想法：每次循环之后的位置应该是当前位置i加上移动步数j：i+j，然后对环的大小l求余：(i+j)%l
# 有问题，未解决
# class Solution:
#     def findTheWinner(self, n, k):
#         # 创建参与游戏的人员列表
#         lst = [i+1 for i in range(n)]
#         # 初始位置为第一位参与者，并且计数也把这位参与者算入
#         # 循环结束条件应该是lst长度为1,即剩下最后一个游戏玩家
#         start = 1
#         next = (start+k)%5
#         while len(lst) != 1:
#             # 当前位置（移动之后的）
#             current = lst.index((current+k-1) % n)
#             # lst.remove(current)
#             flag -= 1
#             current = lst.index((current+1) % n)
#         return current+1

# from collections import deque
# class Solution:
#     def findTheWinner(self, n, k):
#         q = deque(range(1, n+1))
#         while len(q) > 1:
#             for _ in range(k-1):
#                 # print('q.popleft():', q.popleft())
#                 q.append(q.popleft()) # 使用队列可以完成这种循环式的列表
#             q.popleft()
#         return q[0]

# 递归，此递归式的含义是返回其最终对应的游戏获胜者
# class Solution:
#     def findTheWinner(self, n, k):
#         return 1 if n==1 else (k + self.findTheWinner(n-1, k)-1) % n + 1

class Solution:
    def findTheWinner(self, n, k):
        if n == 1:
            return 1
        ans = (k + self.findTheWinner(n - 1, k)) % n
        return n if ans == 0 else ans
            
# # 迭代法
# class Solution:
#     def findTheWinner(self, n, k):
#         winner = 1
#         for i in range(2, n+1):
#             winner = (k + winner - 1) % i + 1
#         return winner

if __name__ == '__main__':
    n, k = 5, 2
    result = Solution().findTheWinner(n, k)
    print(result)





# 测试代码
# lst = [i for i in range(5)]
# print(lst)