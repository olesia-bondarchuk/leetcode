from typing import Optional
from helpers.list_node import ListNode
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        current = head
        prev = ListNode(0, head)
        result = prev
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return result.next
