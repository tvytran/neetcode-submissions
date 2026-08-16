class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+2], cost[i+1])
        
        return min(cost[0], cost[1])


        