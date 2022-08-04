## Leetcode刷题总结——贪心

------

2022/8/4  author:WH

### 1、相关题目编号

- 0455分发饼干
- 0376摆动序列
- 0053最大子序和
- 0122买卖股票的最佳时机II
- 0055跳跃游戏
- 0045跳跃游戏II
- 1005K次取反后最大化的数组和
- 0134加油站
- 0135分发糖果
- 0860柠檬水找零
- 0406根据身高重建队列
- 0452用最少的箭引爆气球
- 0435无重叠区间
- 0763划分字母区间
- 0056合并区间
- 0738单调递增的数字
- 0714买卖股票的最佳时机含手续费

放弃篇~：

- 0968监控二叉树

### 2、代码实现

#### 0455分发饼干

两种思路：一种是以胃口为准，满足胃口大小；另一种是以饼干为准，满足饼干分发

解法一：以饼干为准，其中if判断语句处，处理的有问题

```python
# 2022/8/4  author:WH
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        # 此处的start表示从排好序的第几个小孩开始
        ans = start = 0
        # 以饼干为准
        for i in range(len(s)):
            # 此处if语句的判断，一定要把start < len(g)的判断写在前面否则会报错
            if start < len(g) and s[i] >= g[start]:
                start += 1
                ans += 1
        return ans
    
# 上述代码的优化，其中的start和ans有异曲同工之妙
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        ans = 0
        for i in range(len(s)):
            if ans < len(g) and s[i] >= g[ans]:
                ans += 1
        return ans
    
if __name__ == "__main__":
    g = [1,4,3,5,3]
    s = [1,2,2]
    result = Solution().findContentChildren(g, s)
    print(result)
```

解法二：以胃口为准，大饼干要优先满足大胃口

```python
# 2022/8/4  author:WH
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        ans = 0
        # 饼干中的起始位置
        start = len(s)-1
        for i in range(len(g)-1, -1, -1):
            # 此处start终点是索引为0
            if start >= 0 and g[i] <= s[start]:
                ans += 1
                start -= 1
        return ans
    
if __name__ == "__main__":
    g = [1,4,3,5,3]
    s = [1,2,2]
    result = Solution().findContentChildren(g, s)
    print(result)
```

