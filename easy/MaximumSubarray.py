"""
    编程思路：
        定义cur用来进行比较下一次单独的num和num+cur的大小，大的赋值给cur
        maxNum用来存储每一次的结果，maxNum和cur谁大赋值给maxNum，永远保存最大的结果
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur = maxNum = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            maxNum = max(cur, maxNum)

        return maxNum

