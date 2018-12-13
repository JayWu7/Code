# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node_list = []
        def recursive(node):
            if node:
                recursive(node.left)
                recursive(node.right)
                node_list.append(node.val)
        recursive(root)
        return node_list
