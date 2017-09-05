"""
    编程思路：
        利用自建函数reduce(), 两个参数，一个函数，一个列表
        函数用lambda匿名函数，每次携带一对（先前的结果以及下一个序列的元素）
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x, y: x * 10 + y, digits) + 1
        return [int(i) for i in str(num)]