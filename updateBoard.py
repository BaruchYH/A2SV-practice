class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.dxn = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        self.dfs(click[0], click[1], board, self.dxn)
        
        return board 
        
    def solve(self, x, y, board, dxn):
        total = 0
        for dr in dxn:
            if 0 <= x + dr[0] and x + dr[0] < len(board) and 0 <= y+ dr[1] and y+ dr[1] < len(board[0]):
                if board[x + dr[0]][y+dr[1]] == "M":
                    total += 1
                    
        return total 
    
    
    def dfs(self, x, y, board, dxn):
        
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return 
        
        if board[x][y] == "M":
            board[x][y] = "X"
            return
        
        if board[x][y] != "E":
            return 
        
        temp = self.solve(x, y, board, dxn)
        if temp :
            board[x][y] = str(temp)
            return 
        
        board[x][y] = "B"
        for dr in dxn:
            self.dfs(x + dr[0], y + dr[1], board, dxn)
        

        
        
        
        
