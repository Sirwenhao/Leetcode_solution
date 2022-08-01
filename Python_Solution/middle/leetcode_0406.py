"""
    1、根据身高重建队列
    2、贪心的关键点在于分两个维度考虑，优先对身高高的进行处理
    3、Python的lambda语句
"""
# 2022/8/1  author:代码随想录
class Solution:
    def reconstructQueue(self, people):
        # 使用lambda语句进行排序
        # -x[0]是为了实现从大到校的排序，默认是从小到大
        # lambda语句可以实现首先按照-x[0]排序，当-x[0]相同时，按照x[1]从小到大排序
        people.sort(key=lambda x:(-x[0], x[1]))
        que = []
        # 根据每个元素的第二维度k，贪心算法，进行插入
        # 此时的people已经排序，同一身高条件下，k值小的排前面
        for p in people:
            que.insert(p[1], p)
        return que

if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    result = Solution().reconstructQueue(people)
    print(result)