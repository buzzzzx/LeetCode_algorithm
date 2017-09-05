"""
    编程思路：
        巧妙地利用了字典和堆的特性
        如果是'(', '[', '{'就一直添加进堆中
        当出现一个')', ']','}'就与堆中的最后一个比较（pop()）
        最后s遍历完了，若stack还有数据就返回False
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in dict.values():
              stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []