# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)  # 0头节点
        currentNode = head
        valueOrCarry = 0  # 相加数字之和或进位
        while l1 != None or l2 != None or valueOrCarry != 0:
            if l1 != None:
                valueOrCarry += l1.val
                l1 = l1.next
            if l2 != None:
                valueOrCarry += l2.val
                l2 = l2.next
            node = ListNode(valueOrCarry % 10)  # 创建节点
            valueOrCarry = int(valueOrCarry / 10)  # 是否需要进位
            currentNode.next = node
            currentNode = node
        return head.next
