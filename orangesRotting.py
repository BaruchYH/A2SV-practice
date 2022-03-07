   def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rottenOranges = {(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2}
        freshOranges = {(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
         
        count = 0        
        while freshOranges:
            if not rottenOranges:
                return -1
            rottenOranges = {(i+r, j+n) for i,j in rottenOranges for r,n in [(1,0),(-1,0),(0,-1),(0,1)] if (i+r,j+n)  in freshOranges}
            freshOranges -= rottenOranges
            count += 1
        return count
            
