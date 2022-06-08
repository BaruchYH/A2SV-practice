class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        #@lru_cache(maxsize = None)
        
        def profit(idx, buy_bool):
            
            if idx >= len(prices):
                return 0
            if (idx, buy_bool) in dp:
                return dp[(idx, buy_bool)]
            
            res = 0
            if buy_bool:
                res = max(res, -prices[idx] + profit(idx+1, not(buy_bool)))
            else:
                res = max(res, prices[idx] + profit(idx+2, not(buy_bool)))
                
            res = max(res, profit(idx+1, buy_bool))
            
            dp[(idx, buy_bool)] = res
            
            return res
        
        return profit(0, True)
            
            
