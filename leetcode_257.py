# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        思路： 递归，dns
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []

        def recursive(node, path):
            if not node.left and not node.right:
                res.append(path + str(node.val))
            else:
                path = path + '{}->'.format(node.val)
                if node.left:
                    recursive(node.left, path)
                if node.right:
                    recursive(node.right, path)

        recursive(root, '')
        return res 
