class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.dp = {}
        
        return self.solve(0, 0, triangle)
        
    def solve(self, row, idx, triangle):
        len_tri = len(triangle)
        
        if row == len_tri:
            return 0
        elif (row, idx) in self.dp:
            return self.dp[(row, idx)]
        
        self.dp[(row, idx)] = triangle[row][idx] + min(self.solve(row + 1, idx, triangle), self.solve(row + 1, idx + 1, triangle)) 
        
        return self.dp[(row, idx)]
        
        
