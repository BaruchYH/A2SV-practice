class Solution:
    def countGoodNumbers(self, n: int) -> int: 
        
        ans = pow(20,n//2,10**9+7)
        if n%2 == 1:
            return (ans*5)%(10**9+7)
        else:
            return ans%(10**9+7)
