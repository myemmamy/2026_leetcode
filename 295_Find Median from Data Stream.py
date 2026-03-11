import heapq
class MedianFinder:
    def __init__(self):
        self._h1 = []
        self._h2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self._h1,-num)
        heapq.heappush(self._h2,-heapq.heappop(self._h1))
        if len(self._h2) > len(self._h1):
            heapq.heappush(self._h1, -heapq.heappop(self._h2))

    def findMedian(self) -> float:
        if len(self._h1) > len(self._h2):
            return -self._h1[0]
        else:
            return (-self._h1[0]+self._h2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
