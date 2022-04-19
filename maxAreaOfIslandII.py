class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [-1]*(m*n)
        
        def find(x):
            i = x
            while parent[i] >= 0:
                i = parent[i]
                parent[x] = i
                
            return i 
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            
            if rootx != rooty:
                if rootx > rooty:
                    rootx, rooty = rooty, rootx
                parent[rootx] += parent[rooty]
                parent[rooty] = rootx
        
        flag  = False 
        dxn = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag = True 
                    for r, c in dxn:
                        row = i + r
                        col = j + c 

                        if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                            union(i*n + j, row*n + col)
                            
        if not flag:
            return 0
        else:
            return -min(parent)
                            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
  
