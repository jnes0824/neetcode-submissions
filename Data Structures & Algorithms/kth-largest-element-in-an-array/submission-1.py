import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p > k:
                return quick_select(l, p-1)
            else:
                return quick_select(p+1, r)
        k = len(nums) - k #從第k大(1 based index)，變成找第k小(0 based index)
        return quick_select(0, len(nums) - 1)