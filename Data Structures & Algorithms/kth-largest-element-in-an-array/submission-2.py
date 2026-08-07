import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(l, r):
            pivot_index = random.randint(l, r)

            # 把隨機選到的 pivot 搬到最右邊
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            pivot = nums[r]

            p = l

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            # 把 pivot 放到正確位置
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p > k:
                return quick_select(l, p - 1)
            else:
                return quick_select(p + 1, r)

        k = len(nums) - k
        return quick_select(0, len(nums) - 1)