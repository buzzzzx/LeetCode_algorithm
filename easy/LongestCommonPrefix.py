"""
    编程思路：
        先判断strs是否为None，是就返回"" (还有其他两种写法为：if strs is None, if not x is None)
        然后取strs中最短的数，依次与strs中的值比较
        若有不同的值，就返回之前已经比较过的字符
        最后全都遍历完成后，返回shortest
        关键函数：enumerate
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, v in enumerate(shortest):
            for str in strs:
                if str[i] != v:
                    return str[:i]

        return shortest


if __name__ == '__main__':
    sl = Solution()
    res = sl.longestCommonPrefix(['hello', 'he', 'hell'])
    print(res)