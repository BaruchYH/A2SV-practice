class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        
        friq = [0]*26
        
        for task in tasks:
            friq[ord(task)-ord('A')] += 1
            
        friq.sort(reverse = True)
        
        blocksofideal = friq[0] - 1
        statesofideal = blocksofideal*n 
        
        for i in range(1,26):
            statesofideal -= min(friq[i], blocksofideal)
            
        return len(tasks) + max(0,statesofideal)
