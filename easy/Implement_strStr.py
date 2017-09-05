"""
    编程思路：
        遍历haystack，从最开始切片
        切片长度于我们要找的needle相等
        若切片内容==needle，就返回下标
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "" and needle == "":
            return 0
        if needle not in haystack:
            return -1

        for i in range(0, len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                return i

if __name__ == '__main__':
    sl = Solution()
    r = sl.strStr("abbds", "bd")
    print(r)