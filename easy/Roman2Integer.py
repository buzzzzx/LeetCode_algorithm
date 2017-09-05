"""
    编程思路：
        把罗马数字关键的几个字母创建一个字典
        根据输入字符的长度写一个循环
        然后根据罗马数字的规则进行判断
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romanNum_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = romanNum_dict[s[0]]
        i = 1

        while i < len(s):
            if romanNum_dict[s[i]] > romanNum_dict[s[i-1]]:
                result += romanNum_dict[s[i]] - 2 * romanNum_dict[s[i - 1]]
            else:
                result += romanNum_dict[s[i]]
            i = i + 1

        return result


if __name__ == '__main__':
    sl = Solution()
    result = sl.romanToInt("XLVIII")
    print(result)