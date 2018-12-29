# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        思路:层次遍历二叉树
        """
        if not root:
            return 0
        max_depth = 0
        node_list = [root]
        while node_list:
            max_depth += 1  # 加一层
            cur_nodes = node_list
            node_list = []
            for node in cur_nodes:
                if node.left:  # 有左儿子
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
        return max_depth


# method 2   递归
class Solution(object):
    def maxDepth(self, root):
        '''
        递归遍历二叉树，从左至右，每到一个节点，比较当前深度和最深深度
        '''
        if not root:
            return 0

        def dfs(node, depth):
            if depth > max_depth[0]:
                max_depth[0] = depth
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        max_depth = [1]
        dfs(root, 1)
        return max_depth[0]


# method 3  Excellent code  递归
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
