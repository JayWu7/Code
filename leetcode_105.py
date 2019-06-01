# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution: 
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        思路： 根据前序遍历确定根节点，然后根据根节点在中序遍历的位置，确定左右子树
        """
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        left_ino = inorder[:index]
        right_ino = inorder[index + 1:]
        length_left = len(left_ino)
        left_pre = preorder[1:1 + length_left]
        right_pre = preorder[1+length_left:]
        root.left = self.buildTree(left_pre,left_ino)
        root.right = self.buildTree(right_pre, right_ino)
        return root
