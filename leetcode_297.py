# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        思路： 前序遍历
        """
        res = []

        def helper(ro):  # 递归遍历tree
            if ro:
                res.append(str(ro.val))
                helper(ro.left)
                helper(ro.right)
            else:
                res.append('#')

        helper(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#':  # 空树
            return None

        trees_val = data.split(',')
        root = TreeNode(int(trees_val[0]))
        length, index = len(trees_val), 1
        cur, root_stack = root, []
        while index < length - 1:  # 保证判断index+1数组不越界
            if trees_val[index] != '#':
                cur.left = TreeNode(int(trees_val[index]))
                root_stack.append(cur)
                cur = cur.left
            elif trees_val[index + 1] != '#':
                cur.right = TreeNode(int(trees_val[index + 1]))
                cur = cur.right
                index += 1
            elif root_stack:  #非空
                cur = root_stack.pop()
            index += 1
        #判断trees_val最后一个元素
        if trees_val[-1] != '#':
            if root_stack:
                root_stack[-1].right = TreeNode(int(trees_val[-1]))
            else:
                cur.left = TreeNode(int(trees_val[-1]))

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
