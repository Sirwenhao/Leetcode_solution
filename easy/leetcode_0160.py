"""
    1、相交链表
"""

class Solution:
    def getIntersectionNode(headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha