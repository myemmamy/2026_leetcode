# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1000)
        cur = dummy
        cur.next = head
        dup = 0
        while cur.next:
            if cur.val != cur.next.val:
                if dup:
                    pre.next = cur.next
                    cur = cur.next
                    dup = 0
                else:
                    pre = cur
                    cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
                dup = 1
        if dup:
            pre.next = cur.next
        return dummy.next
                
        
