class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        if len(nums) == 0:
            return False
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        for val in d.values():
            if val != 1:
                return True
        return False
