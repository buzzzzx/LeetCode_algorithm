"""
    编程思路：
        利用字典，循环遍历，用（target - 列表的值）作为字典中的key
        当判断下一个列表中的值 == 这个key时，表示找到了符合target的两个值
        再利用value和i值找到他们的下标
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i