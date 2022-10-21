from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        i_back = head
        i_front = head.next
        future = i_front.next
        i_front.next = i_back
        i_back.next = future
        head = i_front
        i_anchor = i_back
        if future is None:
            return head
        i_front = future.next
        i_back = future

        while future is not None and future.next is not None:
            future = i_front.next
            i_front.next = i_back
            i_back.next = future
            i_anchor.next = i_front
            if future is None:
                break
            i_anchor = i_back
            i_front = future.next
            i_back = future
        return head
sol = Solution()
n4 = ListNode(4)
# n3 = ListNode(3, n4)
# n2 = ListNode(2, n3)
# n1 = ListNode(1, n2)

solution = sol.swapPairs(None)
print(solution.val)
# print(solution.next.val, solution.next.next.val, solution.next.next.next.val)
