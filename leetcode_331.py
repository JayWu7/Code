class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 思路： 把 空结点 理解成 叶子结点
        #        根据二叉树性质，叶子结点的数量一定比非叶子结点多1
        # time:30min
        num = 1
        for node in preorder.split(','):
            if num == 0:
                return False
            if node == '#': #叶子结点
                num -= 1
            else:
                num += 1

        return num == 0

