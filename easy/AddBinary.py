"""
    编程思路：
        由于a, b是二进制的字符串，将a, b转化为十进制的整数
        再将它们相加，转化为字符串，最后需切片获得结果
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]