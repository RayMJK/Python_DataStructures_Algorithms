def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur

    return prev
