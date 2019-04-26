# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # dfs, 递归，分别计算左、右子树的深度，然后根据深度差，判断左右子树是否是平衡二叉树,利用val来存储深度值
        def helper(node, depth):
            if node:
                depth += 1
                depth_left = helper(node.left, depth)
                depth_right = helper(node.right, depth)
                if depth_left is False or depth_right is False or abs(depth_left - depth_right) > 1:
                    return False
                else:
                    return max(depth_right,depth_left)
            else:
                return depth

        return helper(root,0) is not False