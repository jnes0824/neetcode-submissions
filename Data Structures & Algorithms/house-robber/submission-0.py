class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_value = [-1] * n # max money you get when robbing the ith(1~i) house
        max_value[0], max_value[1] = nums[0], nums[1]
        ans = max(nums[0], nums[1])
        for i in range(2, n):
            if i == 2:
                max_value[i] = max_value[i - 2] + nums[i]
            else:
                max_value[i] = max(max_value[i - 2] + nums[i], max_value[i - 3] + nums[i])
            if max_value[i] > ans:
                ans = max_value[i]
        return ans
# 100, 1, 1, 1, 1, 100