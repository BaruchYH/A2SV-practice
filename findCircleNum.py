class Union_find():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    
    def union(self, x, y):
        if x == y:
            return 
        rootx, rooty = self.find(x), self.find(y) 
        if rootx < rooty:
            self.parents[rooty] = rootx
        else:
            self.parents[rootx] = rooty
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        uf = Union_find(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
                    
        for i in range(n):
            uf.find(i)
            
        return len(collections.Counter(uf.parents))
         
         
