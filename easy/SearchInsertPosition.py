"""
    编程思路：
        有个人用了一行代码！！！
        解释他的思路：
            遍历nums（已排序），小于target的都放在列表内
            返回列表的长度
"""

"""
    牛逼：return len([x for x in nums if x<target])
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                continue
            else:
                return i
        return len(nums)
