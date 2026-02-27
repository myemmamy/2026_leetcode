# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        i = 0
        while i < left - 1:
            pre = pre.next
            i += 1
        start = pre.next
        if start.next:
            then = start.next
        for i in range(right - left):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next
