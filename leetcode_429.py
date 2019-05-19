
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        思路： bfs，使用栈
        time： 10min
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            res.append([])
            cur_level = stack
            stack = []
            for node in cur_level:
                res[-1].append(node.val)
                if node.children:
                    stack.extend(node.children)
        return res

