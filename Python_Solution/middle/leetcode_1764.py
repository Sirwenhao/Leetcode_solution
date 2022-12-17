# author:WH 2022/12/17
# 贪心+双指针
class Solution:
    def canChoose(self, groups, nums):
        n = 0
        for g in groups:
            while n + len(g) <= len(nums):
                if nums[n:n+len(g)] == g:
                    n += len(g)
                    break # 跳出while循环，选择groups中下一个选项
                n += 1
            else:
                return False
        return True

if __name__ == "__main__":
    groups = [[1,-1,-1],[3,-2,0]]
    nums = [1,-1,0,1,-1,-1,3,-2,0]
    result = Solution().canChoose(groups, nums)
    print(result)