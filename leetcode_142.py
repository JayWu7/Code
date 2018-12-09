# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  #有环
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None



# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         node_set, cur = set(), head
#         while cur:
#             if cur in node_set:
#                 return cur
#             else:
#                 node_set.add(cur)
#             cur = cur.next
#         return cur


