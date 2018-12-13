# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        val_list = []
        if not root:
            return val_list
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
        return val_list


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution()
print(s.levelOrder(root))
