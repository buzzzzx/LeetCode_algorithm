"""
    编程思路：
        head是一个ListNode类型
        如果该节点的值 == 下一个节点的值，就让该节点指向下下个节点
        如果 != 就让下一个节点和下下个节点的值比较
        一直到最后一个节点
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head

        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head