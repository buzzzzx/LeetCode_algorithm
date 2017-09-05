"""
    编程思路：
        利用Python的字符切片很容易找到方法
        需注意的是 (r < 2**31) * r这种写法表示括号里面的情况为真就是1 * r, 为假就是0 * r
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            r = int(str(x)[::-1])
            return (r < 2**31) * r
        else:
            fuhao = str(x)[0]
            r2 = int(fuhao + str(x)[1::][::-1])
            return (r2 > -2**31) * r2

if __name__ == '__main__':
    sl = Solution()
    result = sl.reverse(231983183616371263726371263712637126372163721627431)
    print(result)
