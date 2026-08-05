import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        max_heap = stones
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)
            if s1 < s2:
                s2 = s2 - s1
                heapq.heappush(max_heap, -s2)
            elif s2 < s1:
                s1 = s1 - s2
                heapq.heappush(max_heap, -s1)
            
        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]
        