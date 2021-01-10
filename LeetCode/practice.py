# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    head.sort()
    return head
