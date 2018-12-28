# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路：  遍历，将链表的值储存在列表，再做处理
        """
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# method 2

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路： 双指针，快指针每次走两步，则当快指针走完后，慢指针在链表中心
            重点： 使用一个pre节点，用来修改链表，将慢指针走过的节点的指向性由向右转为向左
        """
        pre = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, pre, slow = pre, slow, slow.next
        if fast:  # 表示链表个数为奇数
            slow = slow.next  # slow为中心节点，  从slow.next节点开始从中心向两边比较
        while pre and pre.val == slow.val:
            pre = pre.next
            slow = slow.next

        return not pre  # 如果是回文数，则pre最后值为None
