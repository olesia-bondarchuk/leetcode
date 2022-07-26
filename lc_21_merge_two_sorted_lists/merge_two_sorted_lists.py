from typing import Optional
from helpers.list_node import ListNode

class Solution:
    def mergeTwoLists(self,
    list1: Optional[ListNode],
    list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2
        if list2 is None:
            return list1


        current1 = list1
        current2 = list2
        head = ListNode()
        current = head

        while not (current1 is None and current2 is None):
            if (current2 is None or (current1 is not None and current1.val < current2.val)):
                current.next = ListNode(current1.val, None)
                current = current.next
                current1 = current1.next
            else:
                current.next = ListNode(current2.val, None)
                current = current.next
                current2 = current2.next

        return head.next
