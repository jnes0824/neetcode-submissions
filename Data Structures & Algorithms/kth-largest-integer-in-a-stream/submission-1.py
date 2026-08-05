import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_heap = nums
        heapq.heapify(self.k_heap)
        while len(self.k_heap) > k:
            heapq.heappop(self.k_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_heap, val)
        if len(self.k_heap) > self.k:
            heapq.heappop(self.k_heap)
        return self.k_heap[0]
