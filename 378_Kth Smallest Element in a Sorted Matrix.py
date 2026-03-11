class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        import heapq
        heap = []
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i,0))
        t = 0
        for t in range(k):
            v,l,ei = heapq.heappop(heap)
            t += 1
            if ei + 1 < n:
                heapq.heappush(heap,(matrix[l][ei+1],l,ei+1))
        return v
        
