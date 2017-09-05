"""
    编程思路：
        参考答案：https://discuss.leetcode.com/topic/21276/python-solutions-dfs-recursively-dfs-stack-bfs-queue
        我参考了其中的递归写法（主要是自己写不出来！！！）
        定义一个深度优先寻找的方法dfs，这个方法接受三个参数节点node，级数level，最终要返回的res
        判断当前节点若不为None，就把他的val存到res的第一个位置（每次都是第一个位置），这样到最后最下面的节点的值就在前面
        当一个节点判断完了就判断他的子节点（左右都要），level要加1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            self.dfs(node.left, level+1, res)
            self.dfs(node.right, level+1, res)