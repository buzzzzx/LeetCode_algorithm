"""
    编程思路：
        这道题很简单，利用python的split()函数就可以了
        然后返回最后一个的长度
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1]) if s.split() else 0