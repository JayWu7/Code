# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2:
            return l1
        new_listnode = ListNode(0)
        node = new_listnode  # 指针
        while True:
            if l1.val < l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            if not l1:
                node.next = l2
                return new_listnode
            elif not l2:
                node.next = l1
                return new_listnode
            else:
                node.next = ListNode(0)
                node = node.next

#Excellent code
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         思路：
#             注意返回的也是一个有序列表
#             比较当前l1 与 l2 大小 最后拼接剩余部分
#         """
#         head = temp = ListNode(0)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 temp.next = l1
#                 l1 = l1.next
#             else:
#                 temp.next = l2
#                 l2 = l2.next
#             temp = temp.next
#         temp.next = l1 or l2
#         return head.next