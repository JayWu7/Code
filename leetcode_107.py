# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        思路： 层次遍历，然后反转list后再返回
        """
        if not root: 
            return []
        val_list = []
        node_list = [root]
        while node_list:
            cur_nodes = node_list
            node_list = []
            vals = []
            for node in cur_nodes:
                if node:
                    vals.append(node.val)
                    node_list.extend(filter(lambda x: x, [node.left, node.right]))
            val_list.append(vals)
        return val_list[::-1]
