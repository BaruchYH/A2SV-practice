class Solution:
    def minNonZeroProduct(self, p: int) -> int:
         
    def myPow(self, x: float, n: int) -> float:

    if n < 0 :
        return 1/ self.myPow2(x, -n)

    elif n == 0 :
        return 1 

    else :
        return self.myPow2(x , n )

        
        
    def myPow2(self, x: float, n:int) :
        
        if n == 0:
            return 1
        
        elif n%2 == 0 :
            curr= self.myPow2(x , n//2)
            
            return curr*curr
        
        else : 
            curr= self.myPow2(x , n//2)
            return x*curr*curr
        
