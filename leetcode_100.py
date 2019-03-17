# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val == q.val:
                is_same_left = self.isSameTree(p.left, q.left)
                is_same_right = self.isSameTree(p.right, q.right)
                return is_same_left and is_same_right
            else:
                return False
        elif p is None and q is None:
            return True
        else:
            return False
