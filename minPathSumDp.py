class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp = {}
        
        return self.solve(0, 0, grid)
        
    def solve(self, row, col, grid):
        no_row = len(grid)
        no_col = len(grid[0])
        
        if row >= no_row or col >= no_col:
            return float('inf')
        elif (row, col) in self.dp:
            return self.dp[(row, col)]
        elif (row, col) == (no_row - 1, no_col - 1):
            return grid[row][col]
        self.dp[(row, col)] = grid[row][col] + min(self.solve(row + 1, col, grid), self.solve(row, col + 1, grid))
        
        return self.dp[(row, col)]
