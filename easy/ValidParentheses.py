"""
    这个无法判断"()[]{}"这种类型
    只能判断"{(([]))}"这种类型
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']

        l_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        r_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        if len(s) % 2 != 0:
            return False

        half = len(s) // 2
        for i in range(half):
            if s[i] in l_dict and s[len(s)-1-i] in r_dict:
                if s[i] != r_dict[s[len(s)-1-i]]:
                    return False
            else:
                return False

        return True
if __name__ == '__main__':
    sl = Solution()
    print(sl.isValid("([()])"))