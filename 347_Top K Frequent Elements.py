import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        heap = []
        ans = []
        for n in nums:
            d[n] += 1
        for v,c in d.items():
            heapq.heappush(heap,(c,v))
            if len(heap) > k:
                heapq.heappop(heap)
        return [v for c, v in heap]
        
