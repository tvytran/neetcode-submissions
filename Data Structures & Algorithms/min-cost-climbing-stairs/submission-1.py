class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = len(cost) +1
        dp = [0] * (total)

        for i in range(len(cost)-1, -1, -1):
            if i + 2 < total:
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])
            else:
                dp[i] = cost[i] + dp[i+1]
        
        return min(dp[0], dp[1])


        