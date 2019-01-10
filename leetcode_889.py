# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return

        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        len_left = post.index(pre[1]) + 1

        left_pre = pre[1:1 + len_left]
        right_pre = pre[1 + len_left:]

        if left_pre:
            left_post = post[:len_left]
            root.left = self.constructFromPrePost(left_pre, left_post)
        if right_pre:
            right_post = post[len_left: -1]
            root.right = self.constructFromPrePost(right_pre, right_post)

        return root

#method2  使用闭包函数递归   (速度更快)

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def construct(pre,post):
            if not pre:
                return

            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root

            len_left = post.index(pre[1]) + 1

            left_pre = pre[1:1 + len_left]
            right_pre = pre[1 + len_left:]

            if left_pre:
                left_post = post[:len_left]
                root.left = construct(left_pre, left_post)
            if right_pre:
                right_post = post[len_left: -1]
                root.right = construct(right_pre, right_post)

            return root
        return construct(pre,post)