class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        emptystack =  [ ]
        
        for i in pushed :
            emptystack.append(i)
            
            while (emptystack and emptystack[-1] == popped[0]) :
                    emptystack.pop()
                    popped.pop(0)
                    
        return not emptystack 
