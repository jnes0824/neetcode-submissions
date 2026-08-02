class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        flag = False

        if goal == 0:
            return True
        for i in range(n-2, -1, -1):
            if goal - i <= nums[i]:
                flag = self.canJump(nums[:i+1])
                if flag:
                    break
        return flag