# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         val_list = []
#         reverse = False
#         if not root:
#             return val_list
#         node_list = [root]
#         while node_list:
#             cur_nodes = node_list
#             node_list = []
#             vals = []
#             for node in cur_nodes:
#                 if node:
#                     vals.append(node.val)
#                     node_list.extend(filter(lambda x: x, [node.left, node.right]))
#             if reverse:
#                 val_list.append(vals[::-1])
#             else:
#                 val_list.append(vals)
#             reverse = not reverse
#         return val_list


# 列表生成式版本 ,28ms 击败99%
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        val_list = []
        reverse = False
        if not root:
            return val_list
        node_list = [root]
        while node_list:
            cur_list = []
            if reverse:
                val_list.append([node.val for node in node_list][::-1])
            else:
                val_list.append([node.val for node in node_list])
            for node in node_list:
                if node.left:
                    cur_list.append(node.left)
                if node.right:
                    cur_list.append(node.right)
            node_list = cur_list
            reverse = not reverse
        return val_list
