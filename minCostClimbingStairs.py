class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*n
        
        def minCost(pos):
            if pos >= len(cost):
                return 0
            
            if dp[pos] != -1:
                return dp[pos]
            
            near = minCost(pos+1)
            far = minCost(pos+2)
            
            dp[pos] = min(near,far) + cost[pos]
            
            return dp[pos]
        
        
        
        return min(minCost(0), minCost(1))
        
        
    
            
            
        
        
        
        
            
        
