# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         addr = []
#         head_start = head
#         while head is not None:
#             addr.append(head)
#             head = head.next
#         length = len(addr)
#         if length == 1:
#             return None
#         if n < length:
#             node_tmp = addr[- n - 1]
#             node_tmp.next = addr[- n].next
#         if n == length:
#             head_start = addr[1]
#         return head_start

# use fast and slow pointer to get slow to the last n node
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head