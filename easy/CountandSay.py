"""
    编程思路：
        利用正则表达式的re.sub()函数
        我也不是完全看明白了，先写下一些
        re.sub()函数接收三个必选参数，pattern, repl, string，repl是要替换的值
        group（0）就是匹配正则表达式整体结果，group(1) 列出第一个括号匹配部分
        (.)\1*表示匹配重复的字段
"""

import re

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

        return s
