# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        思路：中序遍历二叉树
        """
        n = 0
        if not root:
            return
        stk = []
        curr = root
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right


# method2   递归解法
class Solution(object):
    def __init__(self):
        self.__n = 0

    def kthSmallest(self, root, k):
        if root:
            left = self.kthSmallest(root.left, k)
            if left is not None:
                return left
            self.__n += 1
            if self.__n == k:
                return root.val
            right = self.kthSmallest(root.right, k)
            if right is not None:
                return right
