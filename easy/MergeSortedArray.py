"""
    编程思路;
        这道题题目不是很明白，查了一下大概是，nums1和nums2都是有序数组，因为nums1的空间更大，所以将nums2的值放到nums1中，但是要有序
        m和n分别是nums1中nums2中已经初始化的元素个数
        如果从前面插入，nums1中的每个元素都要向后移，所以干脆从后面插入
        将nums1和nums2中最后一个数比较，大的就放在nums1[m+n-1]，次大的就放在nums1[m+n-2]中依次类推，直到n不大于0了
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1