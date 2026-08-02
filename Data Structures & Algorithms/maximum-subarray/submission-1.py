class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = nums[0]
        best_sum = nums[0]
        l = 0
        r = 1
        while r < n:
            if curr_sum < 0:
                l = r
                curr_sum = nums[r]
            else:
                curr_sum += nums[r]
            if curr_sum > best_sum:
                best_sum = curr_sum
            r += 1

            
        return best_sum
                
        
