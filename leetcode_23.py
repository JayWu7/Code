# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        index = 0
        while True:
            if len(lists) == 1:
                return lists[0]
            if index in {len(lists), len(lists) - 1}:
                index = 0
            new_head = self.mergeTwoLists(lists[index], lists[index + 1])
            lists[index:index + 2] = [new_head]  # 列表部分替换
            index = index + 1


l1 = None
l2 = ListNode(-1)
l2.next = ListNode(5)
l2.next.next = ListNode(11)
l3 = None
l4 = ListNode(6)
l4.next = ListNode(10)
llist = [l1, l2, l3, l4]
s = Solution()
s.mergeKLists(llist)

#转list方法
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         if not lists:
#             return None
#         # dic = {}
#         stack = []
#         for i in range(len(lists)):
#             head = lists[i]
#             # dic[i] = []
#             while head:
#                 stack.append(head)
#                 head = head.next
#         sorts = sorted(stack,key = lambda x:x.val)
#         if not sorts:
#             return None
#         for i in range(len(sorts)-1):
#             sorts[i].next = sorts[i+1]
#         return sorts[0]
