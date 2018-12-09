# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_node, cur = [], head
        while cur:
            list_node.append(cur.val)
            cur = cur.next
        list_node.sort()
        cur = head
        for val in list_node:
            cur.val = val
            cur = cur.next
        return head



l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
s = Solution()
s.sortList(l1)
