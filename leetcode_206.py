# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        pre_head = ListNode(0)
        pre = pre_head

        def recursion(node):
            nonlocal pre_head
            if node.next:  # next结点不为空
                recursion(node.next)
            pre_head.next = node
            pre_head = pre_head.next

        recursion(head)
        pre_head.next = None
        return pre.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

s = Solution()
l = s.reverseList(l1)
print(1)
print(1)

#excellent code, Awesome

# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         cur, prev = head, None
#         while cur:
#             cur.next, prev, cur = prev, cur, cur.next
#         return prev
