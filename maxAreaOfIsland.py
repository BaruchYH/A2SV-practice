class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = max(area , self.dfs(grid,i,j,m,n))
        return area 
    
    def dfs(self,grid,i,j,m,n):
        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == 1:
            grid[i][j] = 0
            up = self.dfs(grid,i-1,j,m,n)
            down = self.dfs(grid,i+1,j,m,n)
            left = self.dfs(grid,i,j-1,m,n)
            right = self.dfs(grid,i,j+1,m,n)
        else:
            return 0

        return up + down + left + right + 1
