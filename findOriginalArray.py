 from collections import Counter 
    def findOriginalArray(self, changed: List[int]) -> List[int]: 
        li = [] 
        if len(changed)%2 == 1 :
            return []
        else :
            changed.sort()
            repOfItem = Counter(changed)
            for x in repOfItem :
                while x*2 in repOfItem and repOfItem[x] > 0 :
                        if repOfItem[x*2] > 0:
                            repOfItem[x] -= 1
                            repOfItem[x*2] -= 1
                            li.append(x)
                        else :
                            break 
            for x in repOfItem :
                if repOfItem[x] != 0 :
                    return []
            else :
                return li 
                            
                      
             
