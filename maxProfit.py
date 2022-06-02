class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [(0,0)]*len(prices)
        # dp[0] = (prices[0], 0)
        # for i in range(1, len(prices)):
        #     dp[i] = (min(dp[i-1][0], prices[i]), max(prices[i]-dp[i-1][0], dp[i-1][1]))
        # return dp[len(prices)-1][1]
        
        dp = [0]*len(prices)
        curr_max = -1 
        for i in range(len(prices)-2, -1, -1):
            curr = prices[i]
            curr_max = max(curr_max, prices[i+1])
            temp = curr_max - curr 
            dp[i] = temp 
        
        return max(dp)
        
