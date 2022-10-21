import copy
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        global result
        global p
        p1 = list1
        p2 = list2
        flag = 0

        if p1 is None and p2 is None:
            return None

        while p1 is not None or p2 is not None:
            if p1 is None:
                if flag == 1:
                    p.next = ListNode(p2.val)
                    p = p.next
                else:
                    result = ListNode(p2.val)
                    p = result
                    flag = 1
                p2 = p2.next
                continue

            if p2 is None:
                if flag == 1:
                    p.next = ListNode(p1.val)
                    p = p.next
                else:
                    result = ListNode(p1.val)
                    p = result
                    flag = 1
                p1 = p1.next
                continue

            if p1.val < p2.val:
                if flag == 1:
                    p.next = ListNode(p1.val)
                    p = p.next
                else:
                    result = ListNode(p1.val)
                    p = result
                    flag = 1
                p1 = p1.next


            else:
                if flag == 1:
                    p.next = ListNode(p2.val)
                    p = p.next
                else:
                    result = ListNode(p2.val)
                    p = result
                    flag = 1
                p2 = p2.next

        return result

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

s = Solution().mergeTwoLists(list1, list2)
print(s.next.next.val)