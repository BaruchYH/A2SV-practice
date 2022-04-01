class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        timer = 0
        n = len(grid)
        visited = set()
        visited.add((0,0))
        
        while heap:
            val, row, col = heapq.heappop(heap)
            timer = max(val, timer) 
            for dx, dy in [(1,0), (0, 1), (0, -1), (-1, 0)]:
                x = row + dx 
                y = col + dy 
                if (x, y) == (n-1, n-1):
                    timer = max(timer, grid[x][y])
                    return timer       
                if x in range(n) and y in range(n) and (x, y) not in visited:
                    heapq.heappush(heap, (grid[x][y], x, y))
                    visited.add((x, y))
                    
        return timer 
                    
        
