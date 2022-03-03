class Solution:
    def binarysearchfornegatives(self,l,r,row):
        while l < r :
            mid = (l+r)//2
            if row[mid] > -1:
                l = mid+1
            else:
                r = mid
        return r
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        l = 0
        r = n = len(grid[0])
        countneg = 0
        for row in grid:
            r = self.binarysearchfornegatives(l,r,row)
            countneg += n-r
        return countneg
                
