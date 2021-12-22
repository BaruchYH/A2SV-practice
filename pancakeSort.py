class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        li = []
        length = len(arr)
        while True :
            maxindex = arr.index(max(arr[:length]))  
            if maxindex != length-1 :
                if maxindex != 0:
                    li.append(maxindex + 1 )
                    arr[:maxindex+1] = arr[:maxindex+1][::-1]
                li.append(length)   
                arr[:length] = arr[:length][::-1]
            length -= 1 
            
            if length == 0:
                return li
                
            
                
