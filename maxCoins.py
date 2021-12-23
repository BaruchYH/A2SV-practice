class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        maxCoin = 0 
        piles.sort() 
        
        for i in range(1, int((len(piles)/3))+1):
             maxCoin += piles[len(piles)-2*i]
        
        return maxCoin
