# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first, second = head, head.next
        previous = ListNode(0)
        head = second
        while first and first.next:
            second = first.next
            first.next = second.next
            second.next = first
            previous.next = second
            previous, first = first, first.next
        return head
