class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        dic = { }
        monoStack = []
        
        for i in range(0, len(speed)) :
            dic[position[i]] = (target - position[i])/speed[i]
            
        position.sort()
            
        for i in position :
            
            while len(monoStack) != 0 and monoStack[-1] <= dic[i] :
                  monoStack.pop()
                
            monoStack.append(dic[i])
            
        return len(monoStack)
