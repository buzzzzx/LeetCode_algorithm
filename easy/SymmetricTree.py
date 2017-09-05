"""
    编程思路：
        其实就是在内部再写一个函数用于递归
        其他的就跟Same Tree那道题差不多啦
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def isSym(L, R):
            return L and R and L.val == R.val and isSym(L.left, R.right)and isSym(L.right, R.left) or L is R

        return isSym(root.left, root.right)

