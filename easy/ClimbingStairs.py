"""
    问题描述：
        You are climbing a stair case. It takes n steps to reach to the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Note: Given n will be a positive integer.
"""
"""
    编程思路：
        fibonacci
        到达n的路个数就是到达 n-1的路个数 加上 到达 n-2 的路个数
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1

        for _ in range(n):
            a, b = b, a + b
        return a