class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        if goal == 0:
            return True
        for i in range(n-2, -1, -1):
            if goal - i <= nums[i]:
                goal = i #只要能到i就一定能到最後一格，所以把goal設成到i

        return goal == 0 #檢查有沒有連到第一格