# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路快慢指针法，快指针每次走一步，慢指针每次走两步，如果有环，快慢指针一定会相遇，否则无环
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# method 2
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路： 遍历一遍，对遍历过的节点做标记,将下一个节点指向头节点
        """
        cur = head
        while cur and cur.next:
            if cur.next is head:
                return True
            cur.next, cur = head, cur.next
        return False
