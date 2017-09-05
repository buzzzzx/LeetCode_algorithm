"""
    编程思路：
        注意：列表是已排序的！！！
        先判断这个nums是否为None，是就返回0
        用第一个数与列表中的其他数比较，若相同，就跳过，若不相同，r就加一
        然后用剩下还没遍历完的数依次再与这个数做比较
        最后返回的是r+1,r的作用相当于记录多少个不同的数
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        r = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[r]:
                r += 1
                nums[r] = nums[i]

        return r + 1