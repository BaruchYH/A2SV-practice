class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)[2:]               
        n = '%32s' %n       
        n = n.replace(' ', '0')[:]  
        
        return int(n[::-1], 2)
