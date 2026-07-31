class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = nums[0]
        best_sum = nums[0]
        l = 0
        r = 0
        while r < n:
            if l == r:
                curr_sum = nums[r]
            else:
                curr_sum += nums[r]
            if curr_sum > best_sum:
                best_sum = curr_sum

            if nums[r] > curr_sum:
                l = r
                continue
            r += 1
        return best_sum
                
        
