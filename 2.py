# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        ans = ListNode()
        tmp = ans
        while l1 or l2 or add:
            if l1 and l2:
                if l1.val + l2.val + add < 10:
                    tmp.val = l1.val + l2.val + add
                    add = 0
                else:
                    tmp.val = l1.val + l2.val + add - 10
                    add = 1
                l1 = l1.next
                l2 = l2.next
                if l1 or l2 or add:
                    tmp.next = ListNode()
                    tmp = tmp.next
                continue


            if l1 and l2 is None:
                if l1.val  + add < 10:
                    tmp.val = l1.val   + add
                    add = 0
                else:
                    tmp.val = l1.val  + add - 10
                    add = 1
                l1 = l1.next
                if l1 or l2 or add:
                    tmp.next = ListNode()
                    tmp = tmp.next
                continue

            if l1 is None and l2:
                if l2.val  + add < 10:
                    tmp.val = l2.val   + add
                    add = 0
                else:
                    tmp.val = l2.val  + add - 10
                    add = 1
                l2 = l2.next

                if l1 or l2 or add:
                    tmp.next = ListNode()
                    tmp = tmp.next
                continue

            if l1 is None and l2 is None:
                tmp.val = add
                add = 0
                continue
        return ans