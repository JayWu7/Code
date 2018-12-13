class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#Excellent code
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

#quickest code
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         def isParent(p, node):
#             if not p:
#                 return False
#             if p == node:
#                 return True
#             return isParent(p.left, node) or isParent(p.right, node)
#         if root in [None, p, q]:
#             return root
#         if isParent(p, q):
#             return p
#         if isParent(q, p):
#             return q
#         while root:
#             if isParent(root.left, p) and isParent(root.left, q):
#                 root = root.left
#             elif isParent(root.right, p) and isParent(root.right, q):
#                 root = root.right
#             else:
#                 return root
#         return None
root = TreeNode(1)
root.left = TreeNode(2)

s = Solution()
s.lowestCommonAncestor(root,root,root.left)
