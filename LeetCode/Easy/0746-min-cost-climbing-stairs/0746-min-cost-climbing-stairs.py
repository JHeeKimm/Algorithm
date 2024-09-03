class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]
        
        for i in range(2, len(cost)):
            current = min(prev2, prev1) + cost[i]
            prev2 = prev1
            prev1 = current
            
        return min(prev2, prev1)