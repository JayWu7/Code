# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# method 1   思路繁杂 需要改进或者换一个思路
class Solution(object):
    def isSymmetric(self, root):
        """ 
        :type root: TreeNode
        :rtype: bool
        思路: 层次遍历二叉树，判断每一层是不是镜像对称
        重点：  要对称，则除根节点外，其他每层的节点数必须是偶数
        """
        if not root:
            return True
        node_stack = [root.left, root.right]
        valid = 0  # 每层所带的有效节点数
        while True:
            for node in node_stack:
                if node:
                    valid += 1
            if valid == 0:
                return True
            elif valid % 2 != 0:
                return False
            cur_nodes = node_stack
            left_stack, right_stack = [], []
            i, j = 0, len(cur_nodes) - 1
            while i < j:
                if cur_nodes[i] != cur_nodes[j]:  # 对称的位置不相等
                    if cur_nodes[i] and cur_nodes[j] and cur_nodes[i].val == cur_nodes[j].val:
                        pass
                    else:
                        return False
                left_stack = left_stack + ([None, None] if cur_nodes[i] is None else [cur_nodes[i].left,
                                                                                      cur_nodes[i].right])
                right_stack = ([None, None] if cur_nodes[j] is None else [cur_nodes[j].left,
                                                                          cur_nodes[j].right]) + right_stack
                i += 1
                j -= 1
            node_stack, valid = left_stack + right_stack, 0


# method 2

class Solution(object):
    '''
    递归，一个树为的左子树与右子树镜像对称，那么这个数是对称的
    因此，该问题可以转换为：两个树在什么情况下互为镜像？
    如果同时满足下面两个条件，则互为镜像：
            1.它们的两个根节点具有相同的值
            2.每个树的右子树都与另一个树的左子树镜像对称
    '''

    def isSymmetric(self, root):
        def isSym(t1, t2):
            if t1 is None  and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            else:
                return t1.val == t2.val and isSym(t1.right, t2.left) and isSym(t1.left,t2.right)
        return isSym(root,root)


#boreas
