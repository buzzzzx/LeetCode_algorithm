"""
    编程思路：
        可能是最简单的题了
        用到math模块的sqrt方法，最后转化为整数即可
"""

import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        return int(math.sqrt(x))