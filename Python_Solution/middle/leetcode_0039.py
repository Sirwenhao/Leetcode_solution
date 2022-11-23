"""
    1、目标数据给定，组合数据个数不确定
    2、回溯法模板：
    res = []
    def backtrack(路径， 选择列表):
        if 满足结束条件:
            res.append(路径)
            return
        
    for 选择 in 选择列表:
        做选择  
        backtrack(路径，选择列表)
        撤销选择
"""
# 回溯法专题习题一
# class Solution:
#     def combinationsSum(self, candidates, target):
#         """
#         回溯法，层层递减，得到符合条件的路径就加入到结果中，超出则剪枝
#         主要是要注意一些细节，避免重复等
#         """
#         size = len(candidates)
#         if size <= 0:
#             return []
#         # 先排序，便于后面剪枝
#         candidates.sort()
#         path = []
#         res = []
#         self._find_path(target, path, res, candidates, 0, size)
#         return res

#     def _find_path(self, target, path, res, candidates, begin, size):
#         """沿着路径往下走"""
#         if target == 0:
#             res.append(path.copy())  # .copy()的使用方法涉及到深浅拷贝
#         else:
#             for i in range(begin, size):
#                 left_num = target - candidates[i]
#                 # 如果剩余值为负数，说明超过了，剪枝
#                 if left_num < 0:
#                     break
#                 # 否则把当前值加入路径
#                 path.append(candidates[i])
#                 # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除
#                 # 因为根据他们得到的解一定在之前就找到过了
#                 self._find_path(left_num, path, res, candidates, i, size)
#                 # 记得把当前值移出路径才能进入下一个值的路径
#                 path.pop()


# # 代码随想录
# class Solution:
#     # 定义两个全局变量用于存放结果集和符合条件的结果
#     def __init__(self):
#         self.path = []
#         self.paths = []

#     def combinationsSum(self, candidates, target):
#         self.path.clear()
#         self.paths.clear()
#         self.backtracking(candidates, target, 0, 0)
#         return self.paths

#     def backtracking(self, candidates, target, sum, start_index):
#         # 基础情况
#         if sum == target:
#             self.paths.append(self.path[:]) # 因为是浅拷贝，所以不能直接传入self.path
#             return
#         if sum > target:
#             return

#         # 单层递归逻辑
#         for i in range(start_index, len(candidates)):
#             sum += candidates[i]
#             self.path.append(candidates[i])
#             self.backtracking(candidates, target, sum, i)
#             sum -= candidates[i] # 回溯
#             self.path.pop() # 回溯

# 回溯加剪枝
# class Solution:
#     def __init__(self):
#         self.path = []
#         self.paths = []

#     def combinationsSum(self, candidates, target):
#         self.path.clear()
#         self.paths.clear()

#         # 为了剪枝需要提前进行排序
#         candidates.sort()
#         self.backtracking(candidates, target, 0, 0)
#         return self.paths

#     def backtracking(self, candidates, target, sum, start_index):
#         # 基本情况
#         if sum == target:
#             self.paths.append(self.path[:])
#             return
#         # 此处与非剪枝版本有区别
#         # 如果本层sum + candidates[i] > target,就提前结束遍历，剪枝
#         for i in range(start_index, len(candidates)):
#             if sum + candidates[i] > target:
#                 return
#             sum += candidates[i]
#             self.path.append(candidates[i])
#             self.backtracking(candidates, target, sum, i)
#             sum -= candidates[i]
#             self.path.pop()
        
# 2022/5/7 author:WH 回溯加剪枝
# 关键问题一：元素可以被无限制重复选取，只要满足条件即可
# 关键问题二：一定要注意排序的使用
# class Solution:
#     def combinationsSum(self, candidates, target):
#         # 结果集
#         ans = []
#         # 当前解集
#         current = []
#         # 先排序
#         candidates.sort()

#         # 定义回溯函数结构体
#         def backtracking(candidates, target, start_index, current):
#             if sum(current) == target:
#                 # 此处符合条件的当前解集以浅拷贝的方式加入到结果集
#                 ans.append(current[:])
#                 return

#             # 定义剪枝模块
#             if sum(current) > target:
#                 return

#             # 定义单层循环逻辑
#             for i in range(start_index, len(candidates)):
#                 current.append(candidates[i])
#                 # 用i来控制每次取元素的起始位置，关键点此处不用i+1表示可以重复读取当前的数
#                 backtracking(candidates, target, i, current)
#                 current.pop() # 回溯

#         backtracking(candidates, target, 0, current)
#         return ans

# # 2022/5/21 author:WH
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []

#     def combinationsSum(self, candidates, target):
#         candidates.sort()
#         self.ans.clear()    
#         self.current.clear()
#         self.backtracking(candidates, target, 0)
#         return self.ans

#     def backtracking(self, candidates, target, start_index):
#         if sum(self.current) == target:
#             self.ans.append(self.current[:])
#             return
#         for i in range(start_index, len(candidates)):
#             # 如果不加上这个if语句，递归栈会炸
#             if sum(self.current) > target:
#                 return
#             self.current.append(candidates[i])
#             self.backtracking(candidates, target, i) # 关键点:不用i+1了，表示可以重复读取当前的数
#             self.current.pop()

# # 2022/11/14 author:WH
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []

#     def combinationsSum(self, candidates, target):
#         candidates.sort()
#         self.ans.clear()
#         self.current.clear()
#         self.backtracking(candidates, target, 0)
#         return self.ans

#     def backtracking(self, candidates, target, start_index):
#         if sum(self.current) == target:
#             self.ans.append(self.current[:]) # 以浅拷贝的方式加入结果集
#             return
#         for i in range(start_index, len(candidates)):
#             if sum(self.current) > target:
#                 return
#             self.current.append(candidates[i])
#             self.backtracking(candidates, target, i)
#             self.current.pop()
    
# 2022/11/20 author:WH
class Solution:
    def __init__(self):
        self.ans = []
        self.current = []

    def combinationsSum(self, candidates, target):
        # 先排序(没想到)
        candidates.sort()
        self.ans.clear()
        self.current.clear()
        self.backtracking(candidates, target, 0)
        return self.ans

    def backtracking(self, candidates, target, start_index):
        if sum(self.current) == target:
            self.ans.append(self.current[:])
            return
        for i in range(start_index, len(candidates)):
            if sum(self.current) > target:
                return
            self.current.append(candidates[i])
            self.backtracking(candidates, target, i)
            self.current.pop()
    
# # 2022/11/23 author:WH
# # 与上述解答案不一致，此处去重的逻辑不太一样，体会一下
# class Solution:
#     def __init__(self):
#         self.ans = []
#         self.current = []
    
#     def combinationsSum(self, candidates, target):
#         candidates.sort()
#         self.ans.clear()
#         self.current.clear()
#         self.backtracking(candidates, target, 0)
#         return self.ans

#     def backtracking(self, candidates, target, start_index):
#         if sum(self.current) == target:
#             # 此处加入结果集是要使用浅拷贝的形式
#             self.ans.append(self.current[:])
#             return
#         for i in range(start_index, len(candidates)):
#             if sum(self.current) > target:
#                 continue
#             self.current.append(candidates[i])
#             self.backtracking(candidates, target, start_index+1)
#             self.current.pop()



if __name__ == '__main__':
    candidates = [2,7,6,3,1,5]
    target = 9
    result = Solution().combinationsSum(candidates, target)
    print(result)