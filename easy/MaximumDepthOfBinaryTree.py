"""
    编程思路：
        把root的子节点划分成左边和右边，最终那边的结果大，就是最大深度
        递归就是把每一个节点（假如这是个左节点）的子节点都分成左边和右边，那边的结果大就取那边的值然后继续和右边的结果比较
        假如这个左节点（右节点）已经没有子节点了，左节点（右节点）的值为1（这里为1是因为两个都是0但是要加1），然后再与右节点（左节点）的值比较，
            若左节点的值更大（因为右节点其实为None），他们的父节点(假如是一个左节点)的值就是左节点的值1再加1为2，
            这个父节点（也是个左节点）再与兄弟节点（右节点）的值比较，更大的值加1（每一次左右比较都要加1）再赋值给他们的父节点，
            一直到root的左边或者右边比较完毕
        最后root的左边会得到一个最大的值，同理右边也会得到一个最大的值，他们之间再比较得到最大深度
"""

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
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0