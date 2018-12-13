# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node_list = []
        def recursive(node):
            if node:
                recursive(node.left)
                node_list.append(node.val)
                recursive(node.right)
        recursive(root)
        return node_list


#迭代，利用list构造栈
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         ret = []
#         if not root:
#             return ret
#         stk = []
#         curr = root
#
#         while stk or curr:
#             while curr:
#                 stk.append(curr)
#                 curr = curr.left
#             curr = stk.pop()
#             ret.append(curr.val)
#             curr = curr.right
#
#         return ret
