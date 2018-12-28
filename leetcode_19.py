# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        思路： 先遍历一遍算出链表结点数，通过结点数计算出 倒数第n个结点是整数第几个结点
        然后再遍历一次，找到这个结点
        """
        cur, amount = head, 0
        while cur:  # 当前结点不为None
            amount += 1
            cur = cur.next
        cur, pre = head, None
        sequence = amount - n  # 正数第几个元素 下标
        for _ in range(sequence):  # 找到要删除的那个结点
            pre, cur = cur, cur.next
        if pre:  # 删除的不是第一个结点
            pre.next = cur.next
        else:
            head = cur.next
        return head


# method 2    只扫描一次
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        思路：  遍历一次，利用list来存储所有的结点
        如果要删除的结点是最后一个结点，直接把最后一个结点设为None
        否则，把要删除结点的下一个结点的next和val赋给要删除的结点
        """
        node_list = []  # 用来存储所有的结点
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next
        if not len(node_list) - 1:
            return None
        if n == 1:  # 要删除的是倒数第一个结点
            node_list[-2].next = None
        else:
            node_list[-n].val = node_list[-n].next.val  # 注意要先交换值
            node_list[-n].next = node_list[-n].next.next
        return head


# method 3   只扫描一次， 且不需用列表储存结点
class Solution:
    def removeNthFromEnd(self, head, n):
        '''
        思路：
            使用快慢指针
            快指针先走n次，
            然后快慢指针同时走，快指针永远在慢指针前n个位置
            这样当快指针走到最后一个结点的next，为None时
            慢指针刚好走在快指针的n个位置前，即为倒数第n个结点
        '''
        fast, slow, pre = head, head, None   #pre作为slow的前一个结点
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next
        if pre:   #要删除的不为第一个结点
            pre.next = slow.next
        else:
            head = head.next
        return head
