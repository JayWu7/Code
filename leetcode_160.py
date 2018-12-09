# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        head_set = set()
        while headA:
            head_set.add(headA)
            headA = headA.next
        while headB and headB not in head_set:
            headB = headB.next
        return headB