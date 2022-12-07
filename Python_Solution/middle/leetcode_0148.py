# 2022/12/07 author:WH
# 链表排序：使用双循环遍历比较应该可以解决，但是时间复杂度O(N^2)太高
# 直接开辟一个新的链表，取出原链表的所有值，进行排序，将排序后的值按从小到大传入新的链表中
# 少有的一次就可以AC的题
# class Solution:
#     def sortList(self, head):
#         # 创建空的list存储链表中的元素值
#         ans = []
#         # 创建空表
#         dummyNode = ListNode(0)
#         while head:
#             ans.append(head.val)
#             head = head.next
#         ans.sort()
#         idx = 0
#         cur = dummyNode
#         while idx < len(ans):
#             cur.next = ListNode(ans[idx])
#             cur = cur.next
#             idx += 1
#         return dummyNode.next

# github
# 先用快慢指针找到链表中点，分成左右两个子链表，递归排序两个子链表，最后将两个链表合并
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        t = slow.next
        slow.next = None
        l1, l2 = self.sortList(head), self.sortList(t)
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    head = [4,2,1,3]
    result = Solution().sortList(head)
    print(result)