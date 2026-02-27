# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        k = len(lists)
        heap = []
        dummy = ListNode()
        cur = dummy
        counter = 0
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, counter,lists[i]))
                counter += 1
        while heap:    
            _, j, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap,(node.next.val,counter, node.next))
                counter += 1
            cur.next = node
            cur = cur.next

        return dummy.next
