"""
    编程思路：
        先判断nums是否为空
        遍历nums中的值与val比较，相等就将r+1
        最后把nums中的val remove掉，一共r次
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0
        r = 0
        for num in nums:
            if num == val:
                r += 1

        while r:
            nums.remove(val)
            r -= 1
        return len(nums)
