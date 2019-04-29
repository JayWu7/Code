# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    #思路： 后序遍历，将遍历的结点加入栈
    #time: 10min


    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root
        self.dfs(self.root)

    def dfs(self,node):
        if node:
            self.dfs(node.right)
            self.stack.append(node.val)
            self.dfs(node.left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop()


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()