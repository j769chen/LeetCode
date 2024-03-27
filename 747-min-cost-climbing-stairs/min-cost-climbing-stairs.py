class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # since at each step you can either climb one or two steps,
        # the min cost to reach any given step is the minimum of the cost from the step 
        # directly below, or the one two steps below
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])

        for i in range(2, len(cost)):
            dp.append(min(cost[i] + dp[i-1], cost[i] + dp[i-2]))
        
        return min(dp[-1], dp[-2])