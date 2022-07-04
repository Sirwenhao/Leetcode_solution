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
        temp = []
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
        while(cur != None):
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

![image-20220703201600230](https://gitee.com/sirwenhao/images/raw/master/image-20220703201600230.png)

几个关键问题：

- 使用双指针：快慢指针解决此问题
- fast指针每次移动两步，slow指针每次移动一步。即相当于slow以相对速度每一次一个指针不断靠近fast指针，最终相遇
- 快慢指针的相遇一定是在环内，fast指针至少要多走一圈才能个slow指针相遇
- 具体入环的位置分析，代码随想录的版本就很清晰。注意最重要返回的是开始入环的第一个节点。

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
                while 
        
```

