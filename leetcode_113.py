# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res = []

        def helper(stack, root, sum):
            if root:
                stack.append(root.val)
                if root.left or root.right:
                    sum = sum - root.val
                    helper(stack.copy(), root.left, sum)
                    helper(stack.copy(), root.right, sum)
                elif sum == root.val:
                    res.append(stack)


        helper([], root, sum)
        return res
