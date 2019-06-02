# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode 
        """
        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)

        left_ino = inorder[:index]
        right_ino = inorder[index + 1:]

        if left_ino:
            left_post = postorder[:len(left_ino)]
            root.left = self.buildTree(left_ino, left_post)
        if right_ino:
            right_post = postorder[-len(right_ino) - 1: -1]
            root.right = self.buildTree(right_ino, right_post)
        return root

