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

#### 2.1 0455分发饼干

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

#### 2.2 0376摆动序列

摆动序列，相邻两个数字的差是正负交替出现的，返回值是这段子序列的长度

```python
# 2022/8/4  author:WH
# 此解有问题，preC的处理有问题
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        preC = curC = 0
        for i in range(1, len(nums)-1):
            preC = nums[i] - nums[i-1]
            curC = nums[i+1] - nums[i]
            if preC * curC < 0:
                preC = curC
                ans += 1
        return ans
    
# 正确解
class Solution:
    def wiggleMaxLength(self, nums):
        ans = 1
        preC = curC = 0
        for i in range(1, len(nums)):
            if preC * curC <= 0 and curC != 0:
                ans += 1
                preC = curC
        return ans
if __name__ == "__main__":
    nums = [1,7,4,9,2,5]
    result = Solution().wiggleMaxLength(nums)
    print(result)
```

#### 2.3 0053最大子序和

连续数组和，没想出来。。。

```python
# 2022/8/7  author:WH
class Solution:
    def maxSubArray(self, nums):
        minSum = sum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            # sum求和是从头到当前位置的所有数值之和
            sum += nums[i]
            # 最大和是当前最大和与总和减掉前面的最小和之后的结果中的较大者
            maxSum = max(maxSum, sum-minSum)
            # 最小值是当前最小值和总和中的较小者
            minSum = min(minSum, sum)
        return maxSum
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = Solution().maxSubArray(nums)
    print(result)
```

#### 2.4 0122买卖股票的最佳时机II

只计算利润值正值之和，所有利润值正值之和即为最大利润。求利润的公式转换，举栗子：加入第0天买入，第3天卖出，则利润为：prices[3]-prices[0]，相当于：
$$
prices[3]-prices[2]+prices[2]-prices[1]+prices[1]-prices[0]
$$

```python
# 2022/8/12  author:WH
class Solution:
    def maxProfits(self, prices):
        res = 0
        for i in range(len(prices)-1):
            # 统计利润，正值即加入到结果中
            res += max(0, prices[i+1] - prices[i])
        return res
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4,10,8,9,1,9]
    result = Solution().maxProfits(prices)
    print(result)
```

#### 2.5 0055跳跃游戏

贪心的关键点在于，每次取最大步数，查看其最大覆盖范围能不能包含终点

```python
# 2022/8/17  author:WH
class Solution:
    def canJump(self, nums):
        cover = 0
        if i > cover:
            return False
        for i, num in enumerate(nums):
            cover = max(cover, i+num)
        return True
    
if __name__ == "__main__":
    nums = [3, 2, 1, 0, 4]
    result = Solution().canJump(nums)
    print(result)
```

#### 2.6 0045跳跃游戏II

两个条件：第一个要达到最后一位，第二个步数最少。核心还是要看最大覆盖范围，但是还要要求跳跃的步数最少

```python
# 2022/8/19  author:代码随想录
# 没有弄明白
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        ans = 0
        curDistance = nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i+nums[i], nextDistance)
            if i == curDistance:
                if curDistance != len(nums)-1:
                    ans += 1
                    curDistance = nexDistance
                    if nextDistance >= len(nums)-1:
                        break
            return ans
```

#### 2.7 1005 K次取反后最大化的数组和

贪心：只修改最小值，若都为正值，怎每次仅将最小正值的符号进行改变，累计至K次；如果有负值，那就先让赋值变正值，然后再按照前述逻辑进行运算

```python
# 2022/8/22  author:WH
class Solution:
    def largestSumAfterNegations(self, nums, k):
        nums.sort()
        flag = 0
        if flag < k:
            nums[0] = -nums[0]
            flag += 1
            self.largestSumAfterNegations(nums, k)
        return sum(nums)
    
# 2022/8/22  author:代码随想录
class Solution:
    def largestSumAfterNegations(self, nums, k):
        # 以绝对值进行从大到小的排序，倒序
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
            if k > 0:
                nums[-1] *= (-1)**k
            return sum(nums)
    
if __name__ == "__main__":
    nums = [2, -3, -1, 5, -4]
    k = 1
    result = Solution().largestSumAfterNegations(nums, k)
    print(result)
```

#### 2.8 0134 加油站

贪心算法的关键点：从开始节点出发到当前节点如果rest[i]之和小于0那么肯定不能实现遍历过程，只能往i之后进行查找

```python
# 2022/8/23  author:WH
class Solution:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        curSum = totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0:
            return -1
        return start
    
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = Solution().canCompleteCircuits(gas, cost)
    print(result)
```

github:使用$i$和$j$分表标记起始点，$rest$用于表示当前剩余的汽油量，$cnt$表示当前行驶过的加油站数量，可以从任意起点开始判断位置。如在最后一个位置$i=n-1$处进行判断，起始时移动$j$，当$s$小于0时表示当前起始位置不满足要求，循环左移进行更新

```python
# 2022/8/23  author:github
class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        i = j = n - 1
        cnt = rest = 0
        while cnt < n:
            rest += gas[i] - cost[i]
            cnt += 1
            j = (j+1) % n # 循环移位
            while rest < 0 and cnt < n:
                i -= 1
                rest += gas[i] - cost[i]
                cnt += 1
        return -1 if rest < 0 else i
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = Solution().canCompleteCircuits(gas, cost)
    print(result)
```

#### 2.9 0135分发糖果

每个孩子至少分到一个糖果，评分高的孩子需要多分配糖果。两边遍历，第一遍从左到右；第二遍从右到左。从右到左遍历时，需要考虑第i个小孩的糖果数量要大于左边的也大于右边的。

```python
# 2022/8/28  author:WH
class Solution:
    def candy(self, ratings):
        # 每个孩子至少要一个分一个糖果，因此有如下命令
        candyList = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candyList[i] = candyList[i-1] + 1
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                # 此条命令
                candyList[j] = max(candyList[j], candyList[j+1]+1)
        return sum(candyList)
    
if __name__ == "__main__":
    ratings = [1, 0, 2]
    result = Solution().candy(ratings)
    print(result)
```

#### 2.10 0860柠檬水找零

贪心关键点：遇到20的面额优先使用10的面额去解决找零。想到了分三种情况去解决，但是没有想到对应到面额为10和20的情况里面要减掉消耗掉的5面额和10面额。

```python
# 2022/8/28  author:WH
class Solution:
    def lemonadeChange(self, bills):
        five = ten = twenty = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True
    
if __name__ == "__main__":
    bills = [5,5,5,10,20]
    result = Solution().lemonadeChange(bills)
    print(result)
```

#### 2.11 0406根据身高重建队列

本题难点在于：每一个元素都对应于两个维度。一般遇到两个维度进行权衡的问题，需要先确定一个维度，再确定另一个。两种维度先确定那个也需要考虑，此题目中，按照身高进行排列的话，一定可以确定一个顺序就是身高是从大到小进行排列的

```python
# 2022/8/29  author:WH
class Solution:
    def reconstructQueue(self, people):
        # sort命令默认从小到大进行排序，lambda语句首先按照第一维度进行排序
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
    
if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    result = Solution().reconstructQueue(people)
    print(result)
```

#### 2.12 0452用最少的箭引爆气球

最少的箭意味着如果存在重叠情况，则重叠情况最好用一只箭解决掉尽量多的气球。

```python
# 2022/8/29  author:WH
class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[0])
        ans = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                ans += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])
        return ans
    
# 2022/8/29  author:github
class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        ans = 1
        x = points[0][1]
        for a,b in points:
            if a > x:
                ans += 1
                x = b
        return ans
    
if __name__ == "__main__":
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    result = Solution().findMinArrayShots(points)
    print(result)
```

#### 2.13 0435无重叠区间

完全没有想法。。。要知道的是需要移除的区间的个数，可以反过来考虑不需要移除的区间个数，用总数减掉就行。四个难点：

- 难点一：排序的顺序，是按照左边边界排序还是按照右边边界排序
- 难点二：排序后的遍历，从左遍历还是从右遍历
- 难点三：直接求重复区间较为复杂，转而求非重复区间的个数
- 难点四：求最大非重复区间的个数时，需要一个分割点来做标记

```python
# 2022/8/30  author:WH
class Solution:
    def eraseOverlapIntervals(self, intervals):
        # 按照右侧边界排序，从左到右遍历
        intervals.sort(key=lambda x:x[1])
        ans = 1
        currentEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= currentEnd:
                ans += 1
                # 更新终点，为下一次判断做准备
                currentEnd = intervals[i][1]
        return len(intervals) - ans
    
    
if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    result = Solution().eraseOverlapInterval(self, intervals)
    print(result)
```

#### 2.14 0763划分字母区间

关键点：统计每个元素最后一次的出现位置，然后从头遍历字符，更新当前字符的最远下标，若最远下标等于当前下标，则就表示找到了分割点

```python
# 2022/9/1  author:WH
class Solution:
    def partitionLabels(self, s):
        # 统计字符串s中每个字符出现的最远位置
        lastPosition = [0] * 26
        for i,j in enumerate(s):
            # 记录并更新对应元素出现的最远位置
            lastPosition[ord(j) - ord('a')] = i
        ans = []
        # 设置两个变量记录当前分割字符串的左右位置
        left = right = 0
        for i,j in enumerate(s):
            # 计算并更新左右边界
            right = max(right, lastPosition[ord(j) - ord('a')])
            # 当当前元素位置等于其最远位置时，找到分割位置
            if right == i:
                ans.append(right - left + 1)
                left = right + 1
         return ans
    
if __name__ == "__main__":
    s = 'abcabcbacadefegdehijhklij'
    result = Solution().partitionLabesls(s)
    print(result)
```

#### 2.15 0056合并区间

先按照一个维度（如左侧）进行排序，再根据右侧是否重叠变更右边界值。贪心：先按照左边界排序，每次合并都取最大的右边界

```python
# 2022/9/1  author:WH
class Solution:
    def merge(self, intervals):
        # 先按照左边区间排序
        intervals.sort(key=lambda x:x[0])
        ans = []
        # 维持两个变量left和right记录区间左右边界
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                ans.append([left, right])
                # 需要更新左右边界
                left, right = intervals[i][0], intervals[i][1]
            else:
                right = max(right, intervals[i][1])
        ans.append([left, right])
        return ans
    
if __name__ == "__main__":
    intervals = [[1,6],[8,10],[2,6],[15,18]]
    result = Solution().merge(intervals)
    print(result)
```

合并区间问题的模板

```python
# 区间合并的模板
def merge(intervals):
    ans = []
    intervals.sort()
    st, ed = intervals[0]
    for s, e in intervals[1:]:
        if ed < s:
            ans.append([st, ed])
            st, ed = s, e
        else:
            ed = max(ed, e)
    ans.append([st, ed])
    return ans
```

#### 2.16 0738单调递增的数字

贪心：局部最优解遇到nums[i-1]>nums[i]，让nums[i-1]--，同时nums[i]==9。

```python
# 2022/9/4  author:WH
class Solution:
    def monotoneIncreasingDigits(self, n):
        a = list(str(n))
        for i in range(len(a), 0, -1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1])-1)
                a[i:] = '9' * (len(a)-i)
        return int("".join(a))
if __name__ == "__main__":
    n = 3324
    result = Solution().monotonIncreasingDigits(n)
    print(result)
```

#### 2.17 0714买卖股票的最佳时机含手续费

不同于0122买卖股票的最佳时机II，此时需要考虑卖出的时机（需要考虑买卖的利润能否满足手续费的问题）。贪心策略：最低值买，最高值卖。分三种情况：

- 可以收获利润，但不是能够收获利润的区间中的最后一天，相当于持有股票
- 前一天是收获利润的区间中的最后一天，卖出之后就要重新记录最小价格
- 不做操作，保持原有状态

```python
# 2022/9/5 author:WH
class Solution:
    def maxProfits(self, prices, fee):
        ans = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            # 记录最低价格
            if prices[i] < minPrice:
                minPrice = prices[i]
            # 保持原有状态，不能卖掉，不够弥补手续费
            elif prices[i] >= minPrice and prices[i] <= minPrice + fee:
                continue
            else:
                ans += prices[i] - minPrice - fee
                minPrice = prices[i] - fee
        return ans

if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2
    result = Solution().maxProfits(prices, fee)
    print(result)
```

