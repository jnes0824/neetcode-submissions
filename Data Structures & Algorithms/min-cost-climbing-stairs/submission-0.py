class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [n+1] * 101 #record the min cost to each stairs
        min_cost[0], min_cost[1] = 0, 0
        for i in range(2, n+1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] +cost[i-2])
        return min_cost[n]
[1,2,1,2,1,1,1]
[0,0,1,2,2,3,3,4]