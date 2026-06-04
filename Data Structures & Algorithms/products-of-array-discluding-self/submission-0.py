class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_counts = 1, 0
        for num in nums:
            if num != 0:
                prod = prod * num
            else:
                zero_counts = zero_counts + 1
        
        if zero_counts > 1:
            return [0] * len(nums)

        res = [0] * len(nums)           
        for i in range(len(nums)):
            if zero_counts != 0:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // nums[i]
        return res
            
