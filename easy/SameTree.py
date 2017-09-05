"""
    编程思路：
        用递归, is是看两个标识符是不是引用自一个对象,利用id()就明白,id可以理解为内存地址,引用地址
        ex:如果p和q都没有左节点就 return p is q，None is None为True
        ex:如果p有左节点q没有，return p is q,就是False
        递归速度较慢
        更牛逼的写法，一句话：
            return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) or p is q

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q