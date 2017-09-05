"""
    编程思路：
        此题不能使用字符的方法，所以就在数字上进行判断
        先判断第一位和最后一位是否相等，第二位和倒数第二位是否相等，以此类推
        若不相等就 return False
        最后while循环结束 return True
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div = 1
        while x // 10 >= div:
            div *= 10

        while x > 0:
            l = x % 10
            f = x // div
            if l != f:
                return False
            x = x % div // 10
            div /= 100
        return True