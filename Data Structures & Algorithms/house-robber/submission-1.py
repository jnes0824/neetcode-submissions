class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_value = [-1] * n # 走到 i 為止，最多多少？
        max_value[0] = nums[0]
        max_value[1] = max(nums[1], max_value[0])

        for i in range(2, n):
            max_value[i] = max(nums[i] + max_value[i-2], max_value[i-1]) # rob the ith house or not
        return max_value[n-1]
# 1, 2, 3, 4, 5, 6