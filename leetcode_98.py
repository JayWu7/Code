# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        中序遍历,使用cur_node[0]来储存上一个值
        """
        cur_node = [None]

        def middle_sequence(node):
            if node is None:
                return True
            left_valid = middle_sequence(node.left)
            if cur_node[0] != None and cur_node[0] >= node.val:
                return False
            cur_node[0] = node.val
            right_valid = middle_sequence(node.right)
            return left_valid and right_valid

        return middle_sequence(root)

