'''
    1、python中的链表操作还是不熟悉
    2、不熟悉的是具体的表示方法以及链表相应的语法
'''

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def removeElements(head:ListNode, val:int):
    prev = ListNode(0)
    prev.next = head
    cur = prev
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return prev.next


head = ListNode(1,0)
val = 6
result = removeElements(head, val)