class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        count = 0 
        
        for i in range(len(citations),0,-1 ) :
            
            for j in range(0,len(citations)) :
                
                if citations[j] >= i :
                    
                    count += 1
                    
            if count >= i :
                
                return i
            
            else :
                
                count = 0
                
        return count 
                    
                
                
        
        
