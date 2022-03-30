'''
    1、力扣链表系列习题，反转链表
'''



def reverseList(head):
    if not head: return None
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev