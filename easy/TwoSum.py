"""
    编程思路：
        用了两个循环，o(n的平方)，淘汰这种方法
"""

class Solution:
    def __init__(self):
        self.nums = []
        self.target = 0
        self.result = []

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        start = 0
        for i in range(start, len(self.nums)):
            for j in range(i+1, len(self.nums)):
                a = self.nums[i] + self.nums[j]
                if a == self.target:
                    self.result.append(i)
                    self.result.append(j)
        return self.result


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sl = Solution()
    result = sl.twoSum(nums, target)
    print(result)
