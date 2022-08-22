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

只计算利润值正值之和，所有利润值正值之和即为最大利润

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

