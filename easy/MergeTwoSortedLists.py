"""
    待做
    7/28号终于完成，之前没看懂题就一直放着，直到在后面看到一道类似的题目
    题目的意思是：将两个已排序的列表组合成一个新列表，新列表是根据节点合成而来，同样有序

    编程思路：
        先声明一个头结点值为0的节点cur，并且也赋值给另外一个变量result（用于返回结果,因为最终返回的是列表的头结点）
        根据l1和l2的节点的值的比较，将值小的节点赋值给cur的下一节点，不断地比较
        直到有一个列表的节点比较完毕，将未比较完的节点直接赋值给cur.next
        最后返回cur这个列表的头节点的下一节点，也就是result.next，但是cur的头结点是0
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    # iteratively
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return result.next

    # recursively
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
