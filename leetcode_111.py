# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 层次遍历,队列
        if not root:
            return 0
        cur_level = [root]
        depth = 1

        while cur_level:
            cur = cur_level
            cur_level = []
            for node in cur:
                if node.left is None and node.right is None:
                    return depth
                else:
                    if node.left: cur_level.append(node.left)
                    if node.right: cur_level.append(node.right)
            depth += 1
