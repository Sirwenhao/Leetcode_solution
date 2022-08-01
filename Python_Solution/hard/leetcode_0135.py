"""
    1、分发糖果
    2、在保证满足条件的情况下，需要糖果数量尽量少
"""
# 2022/8/1  author:代码随想录
class Solution:
    def candy(self, ratings):
        # 创建等长默认长度的糖果序列，默认用最小值1
        candyVec = [1] * len(ratings)
        # 先左到右遍历，满足分发条件
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candyVec[i] = candyVec[i-1]+1
        print('candyVec:', candyVec)

        # 再从右到左遍历，满足分发条件
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candyVec[j] = max(candyVec[j], candyVec[j+1]+1)
        print('candyVec:', candyVec)
        return sum(candyVec)

if __name__ == "__main__":
    ratings = [1,2,2,5,4,3,2]
    result = Solution().candy(ratings)
    print(result)
