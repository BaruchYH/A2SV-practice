class Solution(object):
    def findTheWinner(self, n, k):
         
        arr = list(range(1, n + 1))
        
        i = 0
        
        while len(arr) > 1:
            nex = (i + k - 1) % len(arr) # get the next element to pop out
            arr.pop(nex)
            i = nex % len(arr) # move start index 
        
        
        return arr[0]
