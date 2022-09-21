## Leetcode刷题总结——双指针

双指针题型专题，常用双指针一般包含左右指针和快慢指针。双指针的使用可以提高算法效率，一般把复杂度从$O(N^2)$降低至$O(N)$，此外还有一些题型（如链表）必须使用双指针解决。相关题型以及解法具体如下：

#### 第一类：数组类

1. 0027移除元素

#### 第二类：字符串类

1. 0344反转字符串
2. 剑指offer05替换空格
3. 0151反转字符串里的单词

#### 第三类：链表类

1. 0206反转链表
2. 0019删除链表的倒数第N个节点
3. 面试题02.07链表相交
4. 0142环形链表II

#### 第四类：N数之和

1. 0015三数之和
2. 0018四数之和

#### 具体解法：

##### 1.1 0027移除元素

```python
# 2022/7/2  author:WH
# 双指针：快慢指针
# 版本一：有问题，不能解决val连续出现的情况
class Solution:
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(len(nums)-1):
            if nums[fast] == val:
                slow = fast
                nums[fast], nums[fast+1] = nums[fast+1], nums[fast]
        return slow

# 版本二：参考了代码随想录
class Solution:
    def removeElement(self, nums, val):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow       
    
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = Solution().removeElement(nums, val)
    print(result)
```

##### 2.1 反转字符串

```python
# 2022/7/2  authoe:WH
# 双指针：左右指针
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    result = Solution().reverseString(s)
    print(result)
```

##### 2.2 剑指0ffer05替换空格

```python
# 2022/7/2  author:WH
class Solution:
    def replaceSpace(self, s):
        return '%20'.join(s.split(' '))
    
# 2022/7/2  author:WH
# 双指针法：
class Solution:
    def replaceSpace(self, s):
        spaceNum = s.count(" ")
        # 转换为字符串类型，str是不可变类型
        ans = list(s + spaceNum * 2 * " ")
         # 利用双指针：左右指针
        # left指向原字符串末端，right指向新字符串末端
        left, right = len(s)-1, len(ans)-1
        while left >= 0:
            if ans[left] != " ":
                ans[right] = ans[left]
                right -= 1
            else:
                ans[right-2:right+1] = "%20"
                right -= 3
            left -= 1
        return ''.join(ans)
    
if __name__ == "__main__":
    s = "We are the world!"
    result = Solution().replaceString(s)
    print(result)
```

##### 2.3 0151反转字符串里面的单词

```python
# 2022/7/2  author:WH
# 不使用双指针
class Solution:
    def reverseWord(self, s):
        return ''.join(i[::-1] for i in s.split(" ") len(i) > 0)
    
# 使用双指针：左右指针，快慢指针
class Solution:
    # 左右指针
    def removeExtraSpace(self, s):
        left, right = 0, len(s)-1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1
        temp = []
        while left <= right:
            if s[left] != " ":
                temp.append(s[left])
            elif temp[-1] != " ":
                temp.append(s[left])
            left += 1
    # 左右指针
    def reverseString(self, s, l, r):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return None
    
    # 快慢指针
    def reverseEachWord(self, s):
        slow = fast = 0
        while slow < len(s):
            while fast < len(s) and s[fast] != " ":
                fast += 1
            self.reverseString(s, slow, fast-1)
            slow = fast+1
            fast += 1
        return None
    
    def reverseWords(self, s):
        l = self.removeExtraSpace(s)
        self.reverseString(l)
        self.reverseEachWord(l)
        return ''.join(l)
        
if __name__ == "__main__":
    s = "  the   sky is    blue  "
    result = Solution().reverseWords(s)
    print(resule)
```

##### 3.1 0206反转链表

```python
# 2022/7/2  author:WH
# 双指针：快慢指针
class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            # 把cur.next用temp保存
            temp = cur.next
            # 把当前节点的下一个指向改为指向前一个节点
            cur.next = pre
            # 把前一个节点改为指向当前节点
            pre = cur
            cur = temp
        return pre    
```

##### 3.2 0019删除链表的倒数第N个节点

```python
# 2022/7/2  author:WH
# 双指针：快慢指针
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode()
        dummyNode.next = head
        cur = head
        while n != 0:
            cur = cur.next
            n -= 1
        while cur != None:
            dummyNode = dumyNode.next
            cur = cur.next
        dummyNode.next = dumyNode.next.next
        return dummyNode.next
```

##### <font color=red>3.3 0142环形链表</font>

- 难点一：判断是否有环（使用快慢指针，如果有环，快指针一定会赶上慢指针）
- 难点二：判断何处相遇（难点）

几个关键问题：

- 使用双指针：快慢指针解决此问题
- fast指针每次移动两步，slow指针每次移动一步。即相当于slow以相对速度每一次一个指针不断靠近fast指针，最终相遇
- 快慢指针的相遇一定是在环内，fast指针至少要多走一圈才能和slow指针相遇
- 具体入环的位置分析，代码随想录的版本就很清晰。注意最终要返回的是开始入环的第一个节点。

示意图：

<img src="https://gitee.com/sirwenhao/typora-illustration/raw/master/image-20220920171429770.png" style="zoom:50%;" />

数学推导：

- 快指针所走路径总长度：$x+n\cdot(y+z)+y$
- 慢指针所走路径总长度：$x+y$
- $n$表示快慢指针相遇时，快指针已经在环内转了多少圈
- 快指针每次走两步，慢指针每次走一步，出发点相同，因此相遇时：$x+n\cdot(y+z)+y=2\cdot(x+y)$
- 化简可得：$x=(n-1)\cdot(y+z)+z$，$n\geq 1$

```python
# 2022/7/3  author:代码随想录
class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
```

##### 4.1 0015三数之和

```python
# 2022/7/3  author:WH
class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return list(map(list, ans))
    
# 方法二：重点在于去重的逻辑
class Solution:
    def threeSum(self, nums):
    nums.sort()
    ans = []
    for i in range(len(nums)-2):
        left, right = i+1, len(num)-1
        if ans != [] and ans[-1][0] == nums[i]: continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                ans.append([nums[i], nums[left], nums[right]])
                while l < r+1 and nums[l] == nums[l+1]:
                    l += 1
                while r > l and nums[r] == nums[r-1]:
                    r -= 1
            if total < 0:
                left += 1
            else:
                right -= 1         
        return ans
    
# 方法三：去重操作是对三个元素都要进行
class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            if nums[i] > 0:
                break
            # 对a去重
            if i > 1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 对b和c去重
                    while left != right and nums[left] == nums[left+1]: left += 1
                    while left != right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
        return ans
  
if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(nums)
    print(result)
```

##### 4.2 0018四数之和

相比于三数之和，实际上多了一层循环。先通过两侧循环固定两个数字，然后使用左右指针计算对应的四个数字之和。相比于三数之和，此例中的target是不固定的，因此剪枝的情况更应该仔细考虑下。还有个关键点在于如何去重，去重的逻辑要搞清楚。

```python
# 2022/7/4 author:WH
class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        nums.sort()
        ans = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left, right = j+1, len(nums)-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right] 
                    if total == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                    if total < target:
                        left += 1
                    else:
                        right -= 1
        return list(map(list, ans))
    
if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = Solution().fourSum(nums, target)
    print(result)
```

总结：双指针部分习题主要使用的指针类型基本为：左右指针、快慢指针两种类型。左右指针需确定好指针的更新规律，快慢指针要特别注意慢指针的更新逻辑。此外xx之和问题中，使用哈希表去重的思想以及map()函数的用法值得注意。
