# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路: 定义奇数指针和偶数指针，奇数指针遍历奇数序号的链表结点，偶数指针遍历偶数结点，遍历完后，在奇数链表尾部添加偶数链表
        """
        if not head or head.next is None:
            return head
        right_head = head.next
        odd, even = head, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            if even.next.next:
                even.next = even.next.next
                even = even.next
            else:
                even.next = None
        odd.next = right_head
        return head
