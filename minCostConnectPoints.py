class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.rank[rootx] += 1
                self.parent[rooty] = rootx
                
    def isConnected(self, p1, p2):
        return self.find(p1) == self.find(p2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        uf = UnionFind(len(points))
        heap = []
        heapify(heap)
        for p1 in range(len(points)-1):
            for p2 in range(p1+1, len(points)):
                heappush(heap, (abs(points[p1][0]-points[p2][0]) + abs(points[p1][1]-points[p2][1]), p1, p2))
        
        cnt = 0
        res = 0                 
        while heap and cnt < len(points)-1:
            cost, p1, p2 = heappop(heap)
            if not uf.isConnected(p1, p2):
               cnt += 1
               res += cost
               uf.union(p1, p2)
        return res 
             
                
        
        
