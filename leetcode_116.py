# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def helper(root):
            if not root or not root.left:
                return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            helper(root.left)
            helper(root.right)

        helper(root) 
