import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [] #要找第k大，代表要紀錄k個中的最小值，有新進的比較再popy位小值，剩下的就會是第K大
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]