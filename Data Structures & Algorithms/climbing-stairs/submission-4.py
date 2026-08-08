
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {} #dp[i] = 走到第i階，有幾種走法
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]