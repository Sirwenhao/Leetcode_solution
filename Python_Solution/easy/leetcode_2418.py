# 2023/4/25  author:WH

# # 创建二元数组，按照身高排序，返回排序后的人名.时间复杂度：O(nlongn)，空间复杂度O(n)
# class Solution:
#     def sortPeople(self, names, heights):
#         return [value for _,value in sorted(zip(heights, names), reverse=True)]

class Solution:
    def sortPeople(self, names, heights):
        idx = list(range(len(heights)))
        # print(idx)
        idx.sort(key=lambda i: -heights[i])
        return [names[i] for i in idx]
    
if __name__ == "__main__":
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    result = Solution().sortPeople(names, heights)
    print(result)
